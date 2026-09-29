# Bild-Werbeanzeige (Meta, 1:1, 1080x1080) nach Anchu Kögls Vorlage fuer Bild-Ads:
# Foto mit Blick in die Kamera, freigestellt und gross im Bild, kontrastreich und leicht uebersaettigt,
# strukturierter dunkler Hintergrund, eine Akzentfarbe plus Schwarz/Weiss, wenig Text (Hook als Text auf dem Bild).
# Nutzung: NM=<node_modules mit @fontsource und playwright> python3 tools/anzeige.py foto.jpg ausgabe.png ['{"S":1.7}']
# Die Ankerwerte (Kopfoberkante, Kinn, Kopfmitte) gelten fuer das Lobby-Foto im blauen Hemd (880x1184);
# fuer ein anderes Foto neu messen. Die Uhr am Handgelenk liegt unterhalb der Leinwand bzw. im Schwarz-Verlauf.
import json, os, subprocess, sys, tempfile
import numpy as np, cv2
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen

W = H = 1080
P = dict(S=1.62, head_top_o=129, chin_o=375, head_cx_o=413,    # Anker im Original
         head_top_c=130, head_cx_c=860,                            # Anker auf der Leinwand
         fade_b0=800, fade_b1=1075,                                # Verlauf nach unten in Schwarz
         fade_l0=445, fade_l1=695,                                 # Verlauf nach links in Schwarz (Textspalte)
         bg_gain=0.34, bg_sat=0.40, bg_blur=3.0,
         glow=0.22, glow_r=260,
         contrast=1.10, sat=1.18, sharpen=0.25, grain=0.010, denoise=3, burn=0.15,
         kick='Kostenfreies Online-Training', kick_size=24,
         head='Die 3&nbsp;Fehlgriffe,<br>an denen<br>Krypto-Anfänger<br><span class="acc">ihr Geld verlieren.</span>',
         h1_size=62, h1_lh='1.08', text_top=245, col_w=600,
         proof='Mich hat eine einzige App <b>70.000&nbsp;$</b> gekostet.', proof_size=32,
         meta='', meta_size=24)

def smooth(a, b, x):
    t = np.clip((x - a) / (b - a), 0, 1)
    return t * t * (3 - 2 * t)

def maske(foto):
    from rembg import new_session, remove
    return np.asarray(remove(Image.open(foto).convert('RGB'), session=new_session('isnet-general-use'), only_mask=True)).astype(np.float32) / 255

def fotoebene(foto, out):
    im8 = np.asarray(Image.open(foto).convert('RGB'))
    if P['denoise'] > 0:
        im8 = cv2.fastNlMeansDenoisingColored(im8, None, P['denoise'], P['denoise'], 7, 21)
    im = im8.astype(np.float32) / 255
    mk = maske(foto)
    S = P['S']
    ox = P['head_cx_c'] - P['head_cx_o'] * S
    oy = P['head_top_c'] - P['head_top_o'] * S
    M = np.float32([[S, 0, ox], [0, S, oy]])
    warp = lambda a, f=cv2.INTER_LANCZOS4: cv2.warpAffine(a, M, (W, H), flags=f, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    photo = np.clip(warp(im), 0, 1)
    valid = np.clip(warp(np.ones(mk.shape, np.float32), cv2.INTER_LINEAR), 0, 1)
    mask = cv2.GaussianBlur(np.clip(warp(mk, cv2.INTER_LINEAR), 0, 1), (0, 0), 0.9)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    lum = photo @ np.float32([0.299, 0.587, 0.114])
    # Hintergrund: abgedunkelt, entsaettigt, weich; Struktur bleibt sichtbar
    bg = lum[..., None] * (1 - P['bg_sat']) + photo * P['bg_sat']
    bg = cv2.GaussianBlur(bg, (0, 0), P['bg_blur']) * P['bg_gain']
    hy = P['head_top_c'] + (P['chin_o'] - P['head_top_o']) * S * 0.5
    d = np.sqrt((xx - P['head_cx_c']) ** 2 + ((yy - hy) * 0.9) ** 2)
    bg *= (0.35 + 0.65 * (1 - smooth(200, 900, d)))[..., None]
    glow = np.exp(-(d / P['glow_r']) ** 2) * P['glow']
    bg = np.clip(bg + glow[..., None] * np.float32([1.0, 0.67, 0.0]) * valid[..., None], 0, 1)
    # Person: Kontrast, Saettigung (bewusst etwas kraeftiger), Schaerfe, Oberkoerper leicht abgedunkelt
    sj = np.clip((photo - 0.5) * P['contrast'] + 0.5 + 0.01, 0, 1)
    l2 = sj @ np.float32([0.299, 0.587, 0.114])
    sj = np.clip(l2[..., None] + (sj - l2[..., None]) * P['sat'], 0, 1)
    sj = np.clip(sj + P['sharpen'] * (sj - cv2.GaussianBlur(sj, (0, 0), 2.0)), 0, 1)
    chin = P['head_top_c'] + (P['chin_o'] - P['head_top_o']) * S
    sj *= (1 - P['burn'] * smooth(chin + 20, chin + 300, yy))[..., None]
    o = (bg * (1 - mask[..., None]) + sj * mask[..., None]) * valid[..., None]
    f = (1 - smooth(P['fade_b0'], P['fade_b1'], yy)) ** 1.3 * smooth(P['fade_l0'], P['fade_l1'], xx)
    o *= f[..., None]
    o += np.random.default_rng(7).normal(0, P['grain'], (H, W, 1)).astype(np.float32) * (f * valid)[..., None]
    Image.fromarray((np.clip(o, 0, 1) * 255 + 0.5).astype(np.uint8)).save(out)
    return out

def seite(bg):
    m = gen.NM + '/@fontsource/montserrat/files/montserrat-latin-%s-normal.woff2'
    b = gen.NM + '/@fontsource/libre-baskerville/files/libre-baskerville-latin-%s-%s.woff2'
    fonts = ''.join("@font-face{font-family:'Montserrat';font-weight:%s;src:url(file://%s)}" % (w, m % w) for w in ('600', '700', '800', '900'))
    fonts += "@font-face{font-family:'Libre Baskerville';font-weight:400;font-style:italic;src:url(file://%s)}" % (b % ('400', 'italic'))
    fonts += "@font-face{font-family:'Libre Baskerville';font-weight:700;font-style:normal;src:url(file://%s)}" % (b % ('700', 'normal'))
    meta = ('<div class="meta">%s</div>' % P['meta']) if P.get('meta') else ''
    return """<!doctype html><html><head><meta charset="utf-8"><style>%s
*{box-sizing:border-box}html,body{margin:0;background:#000}
:root{--fg:#F5F5F0;--fg2:#C9C9C2;--meta:#9C9C96;--acc:#ffab00}
.s{position:relative;width:1080px;height:1080px;overflow:hidden;background:#000 url('file://%s') no-repeat 0 0/1080px 1080px;font-family:'Montserrat',sans-serif;color:var(--fg)}
.col{position:absolute;left:64px;top:%dpx;width:%dpx;display:flex;flex-direction:column;gap:34px}
.tag{align-self:flex-start;background:var(--acc);color:#000;font-weight:800;font-size:%dpx;letter-spacing:2px;text-transform:uppercase;padding:10px 18px;border-radius:8px;line-height:1}
h1{margin:0;font-weight:800;font-size:%dpx;line-height:%s;letter-spacing:-0.5px;text-shadow:0 2px 14px rgba(0,0,0,.55)}
.acc{color:var(--acc)}
.proof{font-family:'Libre Baskerville',serif;font-style:italic;font-size:%dpx;line-height:1.42;color:var(--fg2);max-width:500px;text-shadow:0 2px 12px rgba(0,0,0,.6)}
.proof b{font-family:'Montserrat',sans-serif;font-style:normal;font-weight:800;color:var(--fg)}
.meta{position:absolute;left:64px;bottom:60px;font-weight:600;font-size:%dpx;letter-spacing:1px;color:var(--meta)}
</style></head><body><section class="s"><div class="col"><div class="tag">%s</div><h1>%s</h1><div class="proof">%s</div></div>%s</section></body></html>""" % (
        fonts, bg, P['text_top'], P['col_w'], P['kick_size'], P['h1_size'], P['h1_lh'], P['proof_size'], P['meta_size'],
        P['kick'], P['head'], P['proof'], meta)

JS = r"""const {chromium}=require('%s/playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1080}});
await p.goto('file://'+process.argv[2]);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
const r=await p.evaluate(()=>{const box=s=>{const e=document.querySelector(s);if(!e)return null;const q=e.getBoundingClientRect();return [Math.round(q.left),Math.round(q.top),Math.round(q.right),Math.round(q.bottom)]};
 const h=document.querySelector('h1');return {fonts:document.fonts.check('800 66px Montserrat')&&document.fonts.check('italic 31px "Libre Baskerville"'),tag:box('.tag'),h1:box('h1'),proof:box('.proof'),meta:box('.meta'),h1_overflow:h.scrollWidth>h.clientWidth}});
console.log(JSON.stringify(r));
await p.screenshot({path:process.argv[3]});await b.close()})();"""

def main():
    foto, out = sys.argv[1], sys.argv[2]
    if len(sys.argv) > 3:
        P.update(json.loads(sys.argv[3]))
    d = tempfile.mkdtemp()
    bg = fotoebene(foto, os.path.join(d, 'foto.png'))
    html = seite(bg)
    gen.check_text('Bild-Anzeige', html.split('<body>')[1])
    hp = os.path.join(d, 'anzeige.html'); open(hp, 'w', encoding='utf-8').write(html)
    js = os.path.join(d, 'r.js'); open(js, 'w').write(JS % gen.NM)
    r = subprocess.run(['node', js, hp, os.path.abspath(out)], capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr[-1500:])
    S = P['S']
    fl = lambda yo: round(P['head_top_c'] + (yo - P['head_top_o']) * S)
    fx = lambda xo: round(P['head_cx_c'] + (xo - P['head_cx_o']) * S)
    lay = np.asarray(Image.open(bg).convert('RGB'))
    reg = lay[min(fl(695), H):H, max(fx(215), 0):min(fx(295), W)]   # Uhr im Original bei x 225-285, y 705-770
    print(json.dumps({'kopf_y': [P['head_top_c'], fl(P['chin_o'])], 'kopf_x': [fx(327), fx(503)],
                      'uhr_bereich_max_helligkeit': int(reg.max()) if reg.size else 0,
                      'uhr_unsichtbar': (int(reg.max()) if reg.size else 0) <= 8}))
    Image.open(bg).save(os.path.splitext(out)[0] + '-foto.png') if os.environ.get('KEEP_BG') else None

if __name__ == '__main__':
    main()
