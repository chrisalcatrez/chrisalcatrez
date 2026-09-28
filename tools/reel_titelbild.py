# Titelbild fuer das Vorstellungs-Reel (1080x1920) im Design System "chrisalcatrez".
# Aufbau: freigestellte Person (rembg, isnet-general-use), abgedunkelter Originalhintergrund mit Struktur,
# warmes Licht hinter dem Kopf, Oberkoerper laeuft ab der Brust in Schwarz aus (Haende und Uhr verschwinden),
# Text mittig im Bereich, den Profilraster (3:4) und 4:5 zeigen, nie ueber dem Gesicht.
# Nutzung: NM=<node_modules mit @fontsource/montserrat und playwright> python3 tools/reel_titelbild.py foto.jpg ausgabe.png ['{"S":2.0}']
# Die Ankerwerte (Kopfoberkante, Kinn, Kopfmitte) gelten fuer das Originalfoto 880x1184 vom 28.09.2026;
# fuer ein anderes Foto neu messen (Maske: oberste Zeile ueber 50 %, Kinn am Bart-Ende).
import json, os, subprocess, sys, tempfile
import numpy as np, cv2
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen

W, H = 1080, 1920
P = dict(S=2.05, head_top_o=93, chin_o=320, ax_o=430,          # Massstab, Anker im Original
         head_top_c=330, ax_c=525,                               # Anker auf der Leinwand
         fade0=935, fade1=1200,                                  # Uebergang in Schwarz
         bg_gain=0.30, bg_sat=0.45, bg_blur=4.0,                 # Hintergrund
         glow=0.20, glow_r=300, glow_x=476, glow_y=560,          # warmes Licht hinter dem Kopf
         contrast=1.08, sharpen=0.25, grain=0.012, denoise=3, burn=0.18,
         top=1190, kick='Neu hier?', kick_size=64, kick_ls=9, gap1=20,
         head='Das bin<br>ich<span class="acc">.</span>', h1_size=184, h1_lh='0.93', h1_ls=-2,
         proof='<b>250+</b> Kunden<i>·</i><b>70.000&nbsp;$</b> Lehrgeld', proof_size=40, proof_top=1712, handle_top=1830)

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
    oy = P['head_top_c'] - P['head_top_o'] * S
    M = np.float32([[S, 0, P['ax_c'] - P['ax_o'] * S], [0, S, oy]])
    warp = lambda a, f=cv2.INTER_LANCZOS4: cv2.warpAffine(a, M, (W, H), flags=f, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    photo = np.clip(warp(im), 0, 1)
    valid = np.clip(warp(np.ones(mk.shape, np.float32), cv2.INTER_LINEAR), 0, 1)
    mask = cv2.GaussianBlur(np.clip(warp(mk, cv2.INTER_LINEAR), 0, 1), (0, 0), 0.9)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    g = photo @ np.float32([0.299, 0.587, 0.114])
    bg = g[..., None] * (1 - P['bg_sat']) + photo * P['bg_sat']
    bg = cv2.GaussianBlur(bg, (0, 0), P['bg_blur']) * P['bg_gain']
    d = np.sqrt((xx - 540) ** 2 + ((yy - 640) * 0.8) ** 2)
    bg *= (0.30 + 0.70 * (1 - smooth(260, 980, d)))[..., None]
    tf = smooth(oy, oy + 260, yy)
    bg *= tf[..., None]
    glow = np.exp(-(np.sqrt((xx - P['glow_x']) ** 2 + (yy - P['glow_y']) ** 2) / P['glow_r']) ** 2) * P['glow']
    bg = np.clip(bg + glow[..., None] * np.float32([1.0, 0.67, 0.0]) * (valid * tf)[..., None], 0, 1)
    sj = np.clip((photo - 0.5) * P['contrast'] + 0.5 + 0.01, 0, 1)
    sj = np.clip(sj + P['sharpen'] * (sj - cv2.GaussianBlur(sj, (0, 0), 2.0)), 0, 1)
    chin = P['head_top_c'] + (P['chin_o'] - P['head_top_o']) * S
    sj *= (1 - P['burn'] * smooth(chin + 20, chin + 300, yy))[..., None]
    o = (bg * (1 - mask[..., None]) + sj * mask[..., None]) * valid[..., None]
    f = (1 - smooth(P['fade0'], P['fade1'], yy)) ** 1.4
    o *= f[..., None]
    o += np.random.default_rng(7).normal(0, P['grain'], (H, W, 1)).astype(np.float32) * (f * valid * np.maximum(tf, mask))[..., None]
    Image.fromarray((np.clip(o, 0, 1) * 255 + 0.5).astype(np.uint8)).save(out)
    return out

def seite(bg):
    m = gen.NM + '/@fontsource/montserrat/files/montserrat-latin-%s-normal.woff2'
    fonts = ''.join("@font-face{font-family:'Montserrat';font-weight:%s;src:url(file://%s)}" % (w, m % w) for w in ('600', '800', '900'))
    return """<!doctype html><html><head><meta charset="utf-8"><style>%s
*{box-sizing:border-box}html,body{margin:0;background:#000}
:root{--fg:#F5F5F0;--fg2:#C9C9C2;--meta:#9C9C96;--acc:#ffab00}
.s{position:relative;width:1080px;height:1920px;overflow:hidden;background:#000 url('file://%s') no-repeat 0 0/1080px 1920px;font-family:'Montserrat',sans-serif;color:var(--fg)}
.txt{position:absolute;left:95px;right:95px;top:%dpx;display:flex;flex-direction:column;align-items:center;text-align:center}
.kick{font-weight:800;font-size:%dpx;line-height:1;letter-spacing:%dpx;padding-left:%dpx;text-transform:uppercase;color:var(--acc)}
h1{margin:%dpx 0 0;font-weight:900;font-size:%dpx;line-height:%s;letter-spacing:%dpx;text-transform:uppercase}
.acc{color:var(--acc)}
.proof{position:absolute;left:0;right:0;top:%dpx;text-align:center;font-weight:600;font-size:%dpx;line-height:1.2;letter-spacing:0.5px;color:var(--fg2)}
.proof b{font-weight:800;color:var(--fg)}.proof i{font-style:normal;color:var(--acc);padding:0 14px}
.hdl{position:absolute;left:0;right:0;top:%dpx;text-align:center;font-weight:600;font-size:26px;letter-spacing:1px;color:var(--meta)}
</style></head><body><section class="s"><div class="txt"><div class="kick">%s</div><h1>%s</h1></div><div class="proof">%s</div><div class="hdl">%s</div></section></body></html>""" % (
        fonts, bg, P['top'], P['kick_size'], P['kick_ls'], P['kick_ls'], P['gap1'], P['h1_size'], P['h1_lh'], P['h1_ls'],
        P['proof_top'], P['proof_size'], P['handle_top'], P['kick'], P['head'], P['proof'], gen.HANDLE)

JS = r"""const {chromium}=require('%s/playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.argv[2]);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
console.log(JSON.stringify({f900:await p.evaluate(()=>document.fonts.check('900 100px Montserrat'))}));
await p.screenshot({path:process.argv[3]});await b.close()})();"""

def pruefen(png, bgpng):
    c = np.asarray(Image.open(png).convert('RGB')).astype(int)
    b = np.asarray(Image.open(bgpng).convert('RGB')).astype(int)
    rows = np.where((np.abs(c - b).max(axis=2) > 60).any(axis=1))[0]
    blocks, s, p = [], rows[0], rows[0]
    for r in rows[1:]:
        if r > p + 6:
            blocks.append((int(s), int(p))); s = r
        p = r
    blocks.append((int(s), int(p)))
    fotoende = int(np.where((b.max(axis=2) > 5).any(axis=1))[0].max())
    uhr = P['head_top_c'] + (700 - P['head_top_o']) * P['S']
    return {'textzeilen_y': blocks, 'titel_im_raster_3x4': all(240 <= a and z <= 1680 for a, z in blocks[:3]),
            'titel_in_4x5': all(285 <= a and z <= 1635 for a, z in blocks[:3]), 'foto_endet_bei_y': fotoende, 'uhr_laege_bei_y': round(uhr),
            'uhr_unsichtbar': fotoende < uhr - 150, 'kopf_ab_y': P['head_top_c'], 'text_ab_y': blocks[0][0],
            'kinn_y': round(P['head_top_c'] + (P['chin_o'] - P['head_top_o']) * P['S'])}

def main():
    foto, out = sys.argv[1], sys.argv[2]
    if len(sys.argv) > 3:
        P.update(json.loads(sys.argv[3]))
    d = tempfile.mkdtemp()
    bg = fotoebene(foto, os.path.join(d, 'foto.png'))
    hp = os.path.join(d, 'titel.html')
    open(hp, 'w', encoding='utf-8').write(seite(bg))
    gen.check_text('Reel-Titelbild', seite(bg).split('<body>')[1])
    js = os.path.join(d, 'r.js'); open(js, 'w').write(JS % gen.NM)
    r = subprocess.run(['node', js, hp, os.path.abspath(out)], capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr[-1500:])
    print(json.dumps(pruefen(out, bg), ensure_ascii=False))

if __name__ == '__main__':
    main()
