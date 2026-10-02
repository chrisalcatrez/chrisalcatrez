# Anzeigen mit Teilnehmer-Stimmen (Meta, 1:1, 1080x1080) im Design System "chrisalcatrez".
# Zwei Bausteine:
#   1. stimme_bild(): Einzelbild. Hook oben, echter Chat-Ausschnitt als Karte in der Mitte (Kernsatz mit Marker),
#      unten die Zeile zum kostenfreien Online-Training. Vorbild: Anchus Teilnehmer-Ads, Text auf dem Bild scannbar.
#   2. k_hook(), k_stimme(), k_cta(): Folien fuer eine Karussell-Anzeige (Hook, Einwand plus Stimme, CTA mit Foto).
# Regeln: Stimmen nur mit Einverstaendnis, Auszuege woertlich (Auslassung als " … "), Vorname plus Initial,
# nie Mailadressen oder Nachnamen. Die Anzeige pitcht nur den naechsten Schritt (kostenfreies Training).
# Nutzung: NM=<node_modules mit @fontsource und playwright> OUT=<Ausgabeordner>, dann
#   sys.path.insert(0, '<repo>/tools'); from anzeige_stimme import *
import json, os, subprocess, sys
from PIL import Image, ImageChops, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen

W = H = 1080
ACC = (255, 171, 0)

def karte(shot, crop, marks, out, breite=952, marker=0.62):
    """Schneidet einen Chat-Screenshot zu, legt einen Marker (Multiplizieren) ueber die Kernzeilen und skaliert.
    crop und marks in Pixeln des Originals: (x0, y0, x1, y1)."""
    im = Image.open(shot).convert('RGB')
    lay = Image.new('RGB', im.size, (255, 255, 255))
    d = ImageDraw.Draw(lay)
    tint = tuple(int(255 - (255 - c) * marker) for c in ACC)
    for x0, y0, x1, y1 in marks:
        d.rounded_rectangle((x0, y0, x1, y1), radius=7, fill=tint)
    im = ImageChops.multiply(im, lay).crop(crop)
    s = breite / im.width
    im = im.resize((breite, round(im.height * s)), Image.LANCZOS)
    im.save(out)
    return out, im.size

def fonts():
    m = gen.NM + '/@fontsource/montserrat/files/montserrat-latin-%s-normal.woff2'
    b = gen.NM + '/@fontsource/libre-baskerville/files/libre-baskerville-latin-%s-%s.woff2'
    f = ''.join("@font-face{font-family:'Montserrat';font-weight:%s;src:url(file://%s)}" % (w, m % w) for w in ('500', '600', '700', '800', '900'))
    f += "@font-face{font-family:'Libre Baskerville';font-weight:400;font-style:normal;src:url(file://%s)}" % (b % ('400', 'normal'))
    f += "@font-face{font-family:'Libre Baskerville';font-weight:400;font-style:italic;src:url(file://%s)}" % (b % ('400', 'italic'))
    f += "@font-face{font-family:'Libre Baskerville';font-weight:700;font-style:normal;src:url(file://%s)}" % (b % ('700', 'normal'))
    return f

CSS = """
*{box-sizing:border-box}html,body{margin:0;background:#000}
:root{--fg:#F5F5F0;--fg2:#C9C9C2;--meta:#9C9C96;--acc:#ffab00;--line:#2A2A28;--paper:#F5F5F0;--ink:#141412}
.s{position:relative;width:1080px;height:1080px;overflow:hidden;background:#000;font-family:'Montserrat',sans-serif;color:var(--fg);display:flex;flex-direction:column}
.acc{color:var(--acc)}
.tag{align-self:flex-start;background:var(--acc);color:#000;font-weight:800;font-size:24px;letter-spacing:2px;text-transform:uppercase;padding:10px 18px;border-radius:8px;line-height:1}
h1{margin:0;font-weight:800;letter-spacing:-0.5px}
/* Einzelbild */
.b{padding:50px 64px 46px}
.b .top{display:flex;flex-direction:column;gap:20px}
.b h1{font-size:56px;line-height:1.1}
.b .sub{font-family:'Libre Baskerville',serif;font-style:italic;font-size:31px;line-height:1.35;color:var(--fg2)}
.b .glow{position:absolute;left:140px;top:330px;width:800px;height:620px;background:radial-gradient(closest-side,rgba(255,171,0,.20),rgba(255,171,0,0));filter:blur(30px)}
.b .card{position:relative;margin-top:26px;border-radius:26px;overflow:hidden;box-shadow:0 24px 70px rgba(0,0,0,.75),0 0 0 1px rgba(255,255,255,.10)}
.b .card img{display:block;width:952px}
.b .card:after{content:'';position:absolute;left:0;right:0;bottom:0;height:34px;background:linear-gradient(rgba(0,0,0,0),rgba(0,0,0,.22))}
.b .foot{margin-top:auto;font-weight:700;font-size:27px;line-height:1.32;color:var(--fg);white-space:nowrap}
/* Karussell */
.k{padding:68px 72px 54px;justify-content:space-between}
.k .lab{font-weight:700;font-size:25px;letter-spacing:4px;text-transform:uppercase;color:var(--acc)}
.k .ft{display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:26px;color:var(--fg2)}
.k .ft .n{font-weight:600;color:var(--meta)}
.k h1{font-size:74px;line-height:1.08}
.k h2{margin:0;font-weight:800;font-size:58px;line-height:1.1;letter-spacing:-0.3px}
.k .head{display:flex;flex-direction:column;gap:22px}
.k .msg{background:var(--paper);color:var(--ink);border-radius:28px;padding:40px 46px 36px;display:flex;flex-direction:column;gap:24px;box-shadow:0 24px 70px rgba(0,0,0,.75)}
.k .chip{align-self:flex-start;font-weight:800;font-size:20px;letter-spacing:2.5px;text-transform:uppercase;color:#6B6B66;border:2px solid #CFCFC8;border-radius:999px;padding:7px 16px;line-height:1}
.k .q{font-family:'Libre Baskerville',serif;font-size:37px;line-height:1.44;margin:0}
.k .q .nb{white-space:nowrap}
.k .q.g{font-size:45px;line-height:1.4}
.k .q p{margin:0 0 18px}.k .q p:last-child{margin:0}
.k mark{background:linear-gradient(transparent 12%,#FFD26A 12%,#FFD26A 92%,transparent 92%);color:inherit;padding:0 4px;margin:0 -4px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.k .who{display:flex;align-items:baseline;gap:14px;border-top:2px solid #DCDCD5;padding-top:18px}
.k .who b{font-weight:800;font-size:29px}
.k .who span{font-weight:600;font-size:24px;color:#6B6B66}
/* Hook-Folie: Karte ragt von unten ins Bild */
.k.hook{justify-content:flex-start;gap:34px}
.k.hook .peek{position:absolute;left:72px;right:72px;top:__PEEK_TOP__px}
.k.hook .fade{position:absolute;left:0;right:0;bottom:0;height:270px;background:linear-gradient(rgba(0,0,0,0),#000 62%)}
.k.hook .ft{position:absolute;left:72px;right:72px;bottom:54px}
/* CTA-Folie mit Foto */
.k.cta{background:#000 url('file://__FOTO__') no-repeat 0 0/1080px 1080px;justify-content:flex-start;padding:0}
.k.cta .col{position:absolute;left:64px;top:__CTA_TOP__px;width:610px;display:flex;flex-direction:column;gap:30px}
.k.cta h1{font-size:60px;line-height:1.08;text-shadow:0 2px 14px rgba(0,0,0,.55)}
.k.cta .sub{font-family:'Libre Baskerville',serif;font-style:italic;font-size:31px;line-height:1.42;color:var(--fg2);max-width:520px;text-shadow:0 2px 12px rgba(0,0,0,.6)}
.k.cta .go{display:flex;align-items:center;gap:16px;font-weight:800;font-size:32px;color:var(--fg)}
.k.cta .go svg{flex:0 0 auto}
"""

ARROW = '<svg width="46" height="46" viewBox="0 0 46 46"><circle cx="23" cy="23" r="23" fill="#ffab00"/><path d="M13 23 H32 M24 15 L32 23 L24 31" stroke="#000" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def page(sec, **kw):
    v = dict(peek_top=560, foto='', cta_top=220)
    v.update(kw)
    css = CSS.replace('__PEEK_TOP__', str(v['peek_top'])).replace('__FOTO__', v['foto']).replace('__CTA_TOP__', str(v['cta_top']))
    return '<!doctype html><html><head><meta charset="utf-8"><style>%s%s</style></head><body>%s</body></html>' % (fonts(), css, sec)

def stimme_bild(tag, head, karte_png, fuss, sub=None):
    s = ('<div class="sub">%s</div>' % sub) if sub else ''
    return ('<section class="s b"><div class="glow"></div><div class="top"><div class="tag">%s</div><h1>%s</h1>%s</div>'
            '<div class="card"><img src="file://%s"></div><div class="foot">%s</div></section>' % (tag, head, s, karte_png, fuss))

def _msg(kanal, absaetze, name, rolle):
    # ein einzelner kurzer Absatz wird groesser gesetzt
    q = ''.join('<p>%s</p>' % a for a in absaetze)
    g = ' g' if len(absaetze) == 1 and len(gen.strip_tags(absaetze[0])) < 130 else ''
    return ('<div class="msg"><div class="chip">%s</div><div class="q%s">%s</div><div class="who"><b>%s</b><span>%s</span></div></div>'
            % (kanal, g, q, name, rolle))

def k_hook(tag, head, kanal, absaetze, name, rolle, n, N, weiter='Weiterwischen &#8594;'):
    return ('<section class="s k hook"><div class="tag">%s</div><h1>%s</h1><div class="peek">%s</div><div class="fade"></div>'
            '<div class="ft"><div>%s</div><div class="n">%d/%d</div></div></section>' % (tag, head, _msg(kanal, absaetze, name, rolle), weiter, n, N))

def k_stimme(label, gedanke, kanal, absaetze, name, rolle, n, N, weiter='Weiterwischen &#8594;'):
    return ('<section class="s k"><div class="head"><div class="lab">%s</div><h2>%s</h2></div>%s'
            '<div class="ft"><div>%s</div><div class="n">%d/%d</div></div></section>' % (label, gedanke, _msg(kanal, absaetze, name, rolle), weiter, n, N))

def k_cta(tag, head, sub, go):
    return ('<section class="s k cta"><div class="col"><div class="tag">%s</div><h1>%s</h1><div class="sub">%s</div>'
            '<div class="go">%s<div>%s</div></div></div></section>' % (tag, head, sub, ARROW, go))

RENDER = r"""const {chromium}=require('%s/playwright');const jobs=require(process.argv[2]);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const j of jobs){const p=await b.newPage({viewport:{width:1080,height:1080}});
await p.goto('file://'+j.html);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);
const r=await p.evaluate(()=>{const s=document.querySelector('.s');const out=[];
 for(const e of s.querySelectorAll('.tag,h1,h2,.sub,.card,.foot,.lab,.msg,.ft,.go,.col')){if(e.closest('.peek'))continue;const q=e.getBoundingClientRect();
  if(q.left<56||q.right>1024||q.top<40||q.bottom>1040)out.push(e.className+':'+[q.left,q.top,q.right,q.bottom].map(Math.round).join(','));}
 const kids=[...s.children].filter(e=>getComputedStyle(e).position!=='absolute');let overlap=false;
 for(let i=0;i<kids.length-1;i++){if(kids[i].getBoundingClientRect().bottom>kids[i+1].getBoundingClientRect().top-10)overlap=true;}
 const box=q=>{const e=s.querySelector(q);if(!e)return null;const r=e.getBoundingClientRect();return [r.left,r.top,r.right,r.bottom].map(Math.round)};
 const used=new Set([...s.querySelectorAll('*')].map(e=>getComputedStyle(e).fontFamily.split(',')[0].replace(/["']/g,'').trim()));
 const loaded=new Set([...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family.replace(/["']/g,'')));
 return {fonts:[...used].every(f=>loaded.has(f)),
  over:s.scrollHeight>s.clientHeight||s.scrollWidth>s.clientWidth,overlap,rand:out,h1:box('h1'),card:box('.card'),msg:box('.msg'),foot:box('.foot')}});
console.log(JSON.stringify({png:j.png.split('/').pop(),...r}));
await p.screenshot({path:j.png});await p.close();}
await b.close()})();"""

def build(name, secs, **kw):
    """secs: Liste fertiger <section>-Strings. Prueft gestrichene Woerter, rendert, meldet Lage."""
    d = os.path.join(gen.OUT, name)
    os.makedirs(d, exist_ok=True)
    jobs = []
    ok = True
    for i, sec in enumerate(secs, 1):
        ok = gen.check_text('%s Bild %d' % (name, i), sec) and ok
        hp = os.path.join(d, '%s-%02d.html' % (name, i))
        open(hp, 'w', encoding='utf-8').write(page(sec, **kw))
        jobs.append({'html': hp, 'png': os.path.join(d, '%s-%02d.png' % (name, i))})
    jf = os.path.join(d, 'jobs.json')
    json.dump(jobs, open(jf, 'w'))
    rj = os.path.join(d, 'render.js')
    open(rj, 'w').write(RENDER % gen.NM)
    r = subprocess.run(['node', rj, jf], capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr[-2000:])
    return [j['png'] for j in jobs], ok
