# Titelbild fuer X (Twitter), 1500x500, im Design System "chrisalcatrez".
# Aufbau: schwarzer, leicht strukturierter Hintergrund, freigestelltes Foto rechts (Blick nach links zum Text),
# Wortmarke und Positionierung mittig-links. Die linke untere Ecke bleibt frei, dort liegt das Profilbild.
# Nutzung: NM=<node_modules mit @fontsource und playwright> python3 tools/banner_x.py foto.jpg maske.png ausgabe.png ['{"S":0.9}']
import json, os, subprocess, sys, tempfile
import numpy as np, cv2
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen

W, H = 1500, 500
P = dict(S=0.92, head_top_o=93, chin_o=320, head_cx_o=410,     # Anker im Original (Anzug-Foto 880x1184)
         head_top_c=38, head_cx_c=1280,                            # Anker auf der Leinwand
         fade_b0=380, fade_b1=500,                                 # Verlauf nach unten
         fade_l0=1000, fade_l1=1130,                                # Verlauf nach links (Textbereich)
         glow=0.16, glow_r=330, contrast=1.08, sharpen=0.25, grain=0.012, denoise=3, burn=0.18,
         kick='Krypto aus dem echten Leben', brand='Chris Alcatrez',
         proof='<b>70.000&nbsp;$</b> Lehrgeld <i>·</i> <b>250+</b> Kunden <i>·</i> Alltag in Venezuela',
         cta='Kostenloses Krypto-Training: Link im Profil',
         text_left=430, text_top=96, text_w=560, h1_size=76)

def smooth(a, b, x):
    t = np.clip((x - a) / (b - a), 0, 1)
    return t * t * (3 - 2 * t)

def fotoebene(foto, maske, out):
    im8 = np.asarray(Image.open(foto).convert('RGB'))
    if P['denoise'] > 0:
        im8 = cv2.fastNlMeansDenoisingColored(im8, None, P['denoise'], P['denoise'], 7, 21)
    im = im8.astype(np.float32) / 255
    mk = np.asarray(Image.open(maske).convert('L')).astype(np.float32) / 255
    S = P['S']
    ox = P['head_cx_c'] - P['head_cx_o'] * S
    oy = P['head_top_c'] - P['head_top_o'] * S
    M = np.float32([[S, 0, ox], [0, S, oy]])
    warp = lambda a, f=cv2.INTER_AREA: cv2.warpAffine(a, M, (W, H), flags=f, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    photo = np.clip(warp(im), 0, 1)
    valid = np.clip(warp(np.ones(mk.shape, np.float32), cv2.INTER_LINEAR), 0, 1)
    mask = cv2.GaussianBlur(np.clip(warp(mk, cv2.INTER_LINEAR), 0, 1), (0, 0), 0.8)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    # Hintergrund: sehr dunkel, mit weichem warmem Licht hinter dem Kopf und feiner Struktur
    hy = P['head_top_c'] + (P['chin_o'] - P['head_top_o']) * S * 0.55
    d = np.sqrt((xx - P['head_cx_c']) ** 2 + ((yy - hy) * 1.1) ** 2)
    glow = np.exp(-(d / P['glow_r']) ** 2) * P['glow']
    bg = np.zeros((H, W, 3), np.float32) + glow[..., None] * np.float32([1.0, 0.67, 0.0])
    # feine diagonale Struktur, kaum sichtbar
    stripes = (np.sin((xx + yy) * 0.35) * 0.5 + 0.5) * 0.012
    bg += stripes[..., None]
    rng = np.random.default_rng(3)
    bg += rng.normal(0, P['grain'], (H, W, 1)).astype(np.float32)
    bg = np.clip(bg, 0, 1)
    # Person
    sj = np.clip((photo - 0.5) * P['contrast'] + 0.5 + 0.01, 0, 1)
    sj = np.clip(sj + P['sharpen'] * (sj - cv2.GaussianBlur(sj, (0, 0), 1.6)), 0, 1)
    chin = P['head_top_c'] + (P['chin_o'] - P['head_top_o']) * S
    sj *= (1 - P['burn'] * smooth(chin + 20, chin + 260, yy))[..., None]
    f = (1 - smooth(P['fade_b0'], P['fade_b1'], yy)) ** 1.2 * smooth(P['fade_l0'], P['fade_l1'], xx)
    person = sj * (mask * valid * f)[..., None]
    o = bg * (1 - (mask * valid * f)[..., None]) + person
    Image.fromarray((np.clip(o, 0, 1) * 255 + 0.5).astype(np.uint8)).save(out)
    return out

def seite(bg):
    m = gen.NM + '/@fontsource/montserrat/files/montserrat-latin-%s-normal.woff2'
    b = gen.NM + '/@fontsource/libre-baskerville/files/libre-baskerville-latin-%s-%s.woff2'
    fonts = ''.join("@font-face{font-family:'Montserrat';font-weight:%s;src:url(file://%s)}" % (w, m % w) for w in ('600', '700', '800', '900'))
    fonts += "@font-face{font-family:'Libre Baskerville';font-weight:400;font-style:italic;src:url(file://%s)}" % (b % ('400', 'italic'))
    return """<!doctype html><html><head><meta charset="utf-8"><style>%s
*{box-sizing:border-box}html,body{margin:0;background:#000}
:root{--fg:#F5F5F0;--fg2:#C9C9C2;--meta:#9C9C96;--acc:#ffab00}
.s{position:relative;width:1500px;height:500px;overflow:hidden;background:#000 url('file://%s') no-repeat 0 0/1500px 500px;font-family:'Montserrat',sans-serif;color:var(--fg)}
.col{position:absolute;left:%dpx;top:%dpx;width:%dpx;display:flex;flex-direction:column;gap:22px}
.kick{font-weight:700;font-size:22px;line-height:1;letter-spacing:5px;text-transform:uppercase;color:var(--acc)}
h1{margin:0;font-weight:900;font-size:%dpx;line-height:0.98;letter-spacing:-2px;text-transform:uppercase;white-space:nowrap}
h1 span{color:var(--acc)}
.proof{font-weight:600;font-size:23px;line-height:1.3;letter-spacing:0.3px;color:var(--fg2);white-space:nowrap}
.proof b{font-weight:800;color:var(--fg)}
.proof i{font-style:normal;color:var(--acc);padding:0 4px}
.cta{display:flex;align-items:center;gap:14px;margin-top:6px;font-family:'Libre Baskerville',serif;font-style:italic;font-size:22px;color:var(--meta);white-space:nowrap}
.cta:before{content:'';display:block;width:34px;height:2px;background:var(--acc)}
</style></head><body><section class="s"><div class="col"><div class="kick">%s</div><h1>%s<span>.</span></h1><div class="proof">%s</div><div class="cta">%s</div></div></section></body></html>""" % (
        fonts, bg, P['text_left'], P['text_top'], P['text_w'], P['h1_size'], P['kick'], P['brand'], P['proof'], P['cta'])

JS = r"""const {chromium}=require('%s/playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1500,height:500}});
await p.goto('file://'+process.argv[2]);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
const r=await p.evaluate(()=>{const box=s=>{const e=document.querySelector(s);if(!e)return null;const q=e.getBoundingClientRect();return [Math.round(q.left),Math.round(q.top),Math.round(q.right),Math.round(q.bottom)]};
 return {fonts:document.fonts.check('900 76px Montserrat')&&document.fonts.check('italic 23px "Libre Baskerville"'),kick:box('.kick'),h1:box('h1'),proof:box('.proof'),cta:box('.cta'),col:box('.col')}});
console.log(JSON.stringify(r));
await p.screenshot({path:process.argv[3]});await b.close()})();"""

def main():
    foto, maske, out = sys.argv[1], sys.argv[2], sys.argv[3]
    if len(sys.argv) > 4:
        P.update(json.loads(sys.argv[4]))
    d = tempfile.mkdtemp()
    bg = fotoebene(foto, maske, os.path.join(d, 'foto.png'))
    html = seite(bg)
    gen.check_text('X-Banner', html.split('<body>')[1])
    hp = os.path.join(d, 'banner.html'); open(hp, 'w', encoding='utf-8').write(html)
    js = os.path.join(d, 'r.js'); open(js, 'w').write(JS % gen.NM)
    r = subprocess.run(['node', js, hp, os.path.abspath(out)], capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr[-1500:])
    S = P['S']
    fl = lambda yo: round(P['head_top_c'] + (yo - P['head_top_o']) * S)
    fx = lambda xo: round(P['head_cx_c'] + (xo - P['head_cx_o']) * S)
    lay = np.asarray(Image.open(bg).convert('RGB'))
    reg = lay[min(fl(695), H):H, max(fx(215), 0):min(fx(295), W)]
    avatar = lay[300:500, 40:400]   # Bereich hinter dem Profilbild (Desktop)
    print(json.dumps({'kopf_y': [P['head_top_c'], fl(P['chin_o'])], 'kopf_x': [fx(322), fx(491)], 'uhr_ab_y': fl(695),
                      'uhr_unsichtbar': fl(695) >= H or (reg.size and int(reg.max()) <= 8),
                      'hinter_profilbild_max_helligkeit': int(avatar.max())}))

if __name__ == '__main__':
    main()
