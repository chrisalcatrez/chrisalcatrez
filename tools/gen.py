# Generator fuer Instagram-Beitraege im Design System "chrisalcatrez"
# Vorlagen: s_hook, s_point, s_proof (Beleg: Zahl, Screenshot, Zitat), s_memo (Merkzettel zum Speichern), s_vs, s_bingo,
# s_question, s_story, s_mail, s_chat, s_list. Jede Inhaltsfolie nimmt cue=... als Sog-Zeile zur naechsten Folie.
# Nutzung: im Arbeitsordner 'npm i @fontsource/montserrat @fontsource/libre-baskerville playwright',
# dann in Python: sys.path.insert(0, '<repo>/tools'); from gen import *; build('beitrag-N', [s_hook(...), s_point(...), ...])
# Schriften: Montserrat (Ueberschriften, Labels) + Libre Baskerville (Fliesstext) nach Anchus Schriftarten-1x1
import html, json, os, re, subprocess, sys, base64, unicodedata

NM = os.environ.get('NM', os.path.join(os.getcwd(), 'node_modules'))
OUT = os.environ.get('OUT', os.path.join(os.getcwd(), 'build'))
os.makedirs(OUT, exist_ok=True)
HANDLE = '@_chrisalcatrez_'

def ff():
    m = NM + '/@fontsource/montserrat/files/montserrat-latin-%s-normal.woff2'
    b = NM + '/@fontsource/libre-baskerville/files/libre-baskerville-latin-%s-%s.woff2'
    s = ''.join("@font-face{font-family:'Montserrat';font-weight:%s;src:url(file://%s)}" % (w, m % w) for w in ('400', '500', '600', '700', '800'))
    s += "@font-face{font-family:'Libre Baskerville';font-weight:400;font-style:normal;src:url(file://%s)}" % (b % ('400', 'normal'))
    s += "@font-face{font-family:'Libre Baskerville';font-weight:700;font-style:normal;src:url(file://%s)}" % (b % ('700', 'normal'))
    s += "@font-face{font-family:'Libre Baskerville';font-weight:400;font-style:italic;src:url(file://%s)}" % (b % ('400', 'italic'))
    return s

CSS = """
*{box-sizing:border-box}
html,body{margin:0;background:#000}
:root{--bg:#000;--fg:#F5F5F0;--fg2:#C9C9C2;--meta:#9C9C96;--acc:#ffab00;--line:#2A2A28}
.s{width:1080px;height:1350px;padding:96px;display:flex;flex-direction:column;justify-content:space-between;background:#000;color:var(--fg);font-family:'Montserrat',sans-serif;overflow:hidden;position:relative}
.s.story{height:1920px;padding:260px 96px 360px}
.hd{font-weight:700;font-size:26px;line-height:1.2;letter-spacing:4px;text-transform:uppercase;color:var(--acc)}
.hd.meta{color:var(--meta)}
.mid{display:flex;flex-direction:column;gap:44px}
h1{margin:0;font-weight:800;font-size:80px;line-height:1.1;letter-spacing:-0.5px}
h1.hook{font-size:96px;line-height:1.06}
h1.m{font-size:72px;line-height:1.1}
h2{margin:0;font-weight:800;font-size:60px;line-height:1.1;letter-spacing:-0.3px}
.p{display:flex;flex-direction:column;gap:28px;font-family:'Libre Baskerville',serif;font-size:35px;line-height:1.5;color:var(--fg)}
.p p{margin:0}
.p .dim{color:var(--fg2)}
.src{font-size:22px;line-height:1.35;color:var(--meta)}
.swipe{font-weight:700;font-size:32px;color:var(--fg2)}
.ft{display:flex;justify-content:space-between;font-size:24px;color:var(--meta)}
.acc{color:var(--acc)}
.cta{font-weight:700;font-size:36px;line-height:1.3;color:var(--fg)}
/* Gegenueberstellung */
.vsw{display:flex;flex-direction:column;gap:56px}
.cols{display:grid;grid-template-columns:1fr 2px 1fr;column-gap:40px}
.col{display:flex;flex-direction:column;gap:30px}
.vline{background:var(--line)}
.pill{align-self:flex-start;font-weight:800;font-size:30px;letter-spacing:1px;padding:10px 24px;border-radius:8px}
.pill.a{background:#262624;color:var(--fg2)}
.pill.b{background:var(--acc);color:#000}
.row{display:grid;grid-template-columns:44px 1fr;column-gap:18px;align-items:start;font-family:'Libre Baskerville',serif;font-size:31px;line-height:1.36}
.row svg{margin-top:2px}
.row.a{color:var(--fg2)}
/* Bingo */
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.cell{border:2px solid var(--line);border-radius:14px;height:228px;padding:20px;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:600;font-size:30px;line-height:1.28;color:var(--fg)}
.cell.c{border-color:var(--acc);color:var(--acc)}
.sub{font-family:'Libre Baskerville',serif;font-size:32px;line-height:1.45;color:var(--fg2);margin:0}
/* Frage */
.q{align-items:stretch}
.qmid{display:flex;flex-direction:column;gap:48px;text-align:center;align-items:center}
.kick{font-weight:800;font-size:44px;letter-spacing:2px;text-transform:uppercase;color:var(--acc)}
.me{font-family:'Libre Baskerville',serif;font-style:italic;font-size:40px;color:var(--fg2)}
.pcta{align-self:flex-start;background:var(--acc);color:#000;font-weight:800;font-size:40px;line-height:1.2;padding:24px 36px;border-radius:14px}
h1.sm{font-size:60px;line-height:1.12}
/* Mail-Karten (echte Betrugsmails, anonymisiert) */
.mails{display:flex;flex-direction:column;gap:22px}
.mail{border:2px solid var(--line);border-radius:16px;padding:24px 30px;display:flex;flex-direction:column;gap:10px}
.mfrom{font-weight:700;font-size:24px;line-height:1.3;color:var(--meta)}
.mfrom b{color:var(--acc);font-weight:700}
.mtext{font-family:'Libre Baskerville',serif;font-size:30px;line-height:1.42;color:var(--fg)}
/* Chat-Blasen mit Einordnung */
.chat{display:flex;flex-direction:column;gap:50px}
.cblock{display:flex;flex-direction:column;gap:18px}
.bub{align-self:flex-start;max-width:92%;background:#1C1C1A;border-radius:30px 30px 30px 8px;padding:26px 32px}
.bfrom{font-weight:700;font-size:22px;color:var(--meta);margin-bottom:10px}
.btext{font-family:'Libre Baskerville',serif;font-size:34px;line-height:1.42;color:var(--fg)}
.tag{align-self:flex-start;background:var(--acc);color:#000;font-weight:800;font-size:24px;letter-spacing:2px;text-transform:uppercase;padding:8px 16px;border-radius:8px}
.tnote{font-family:'Libre Baskerville',serif;font-size:30px;line-height:1.4;color:var(--fg2)}
/* Nummerierte Liste */
.list{display:flex;flex-direction:column;gap:24px}
.li{display:grid;grid-template-columns:52px 1fr;column-gap:20px;align-items:baseline}
.num{font-weight:800;font-size:52px;line-height:1;color:var(--acc)}
.lt{font-family:'Libre Baskerville',serif;font-size:30px;line-height:1.38;color:var(--fg)}
/* Beleg-Folie: grosse Zahl oder Screenshot-Karte, Zitat als Karte */
.big{font-weight:800;font-size:150px;line-height:0.95;letter-spacing:-3px;color:var(--acc)}
.big.sm{font-size:112px}
.bigsub{font-family:'Libre Baskerville',serif;font-size:36px;line-height:1.4;color:var(--fg2)}
.shot{border-radius:24px;overflow:hidden;box-shadow:0 24px 70px rgba(0,0,0,.7),0 0 0 1px rgba(255,255,255,.08)}
.shot img{display:block;width:100%}
.quote{background:#F5F5F0;color:#141412;border-radius:26px;padding:36px 42px;display:flex;flex-direction:column;gap:18px}
.quote .qf{font-weight:700;font-size:22px;letter-spacing:2px;text-transform:uppercase;color:#6B6B66}
.quote .qt{font-family:'Libre Baskerville',serif;font-size:36px;line-height:1.42}
.quote .qt mark{background:#FFD26A;color:inherit;padding:0 4px;margin:0 -4px}
/* Merkzettel: Checkliste zum Speichern */
.memo{border:2px solid var(--acc);border-radius:20px;padding:30px 34px;display:flex;flex-direction:column;gap:20px}
.memo .mh{font-weight:800;font-size:26px;letter-spacing:3px;text-transform:uppercase;color:var(--acc)}
.memo .mi{display:grid;grid-template-columns:44px 1fr;column-gap:16px;align-items:start;font-family:'Libre Baskerville',serif;font-size:30px;line-height:1.36;color:var(--fg)}
.memo .mi svg{margin-top:4px}
"""

def esc(t):
    return t  # Texte werden bewusst als HTML-Fragmente gepflegt (fuer <span class=acc>)

def page(section, w=1080, h=1350):
    return ('<!doctype html><html lang="de"><head><meta charset="utf-8"><style>%s%s</style></head><body>%s</body></html>'
            % (ff(), CSS, section))

def foot(n=None, N=None):
    left = '%d / %d' % (n, N) if n else ''
    return '<div class="ft"><div>%s</div><div>%s</div></div>' % (left, HANDLE)

def paras(ps):
    out = []
    for p in ps or []:
        if isinstance(p, (list, tuple)):
            out.append('<p class="%s">%s</p>' % (p[1], p[0]))
        else:
            out.append('<p>%s</p>' % p)
    return '<div class="p">%s</div>' % ''.join(out) if out else ''

def s_hook(label, title, cue='Weiterwischen &#8594;', sub=None, size='hook'):
    subh = '<div class="p"><p class="dim">%s</p></div>' % sub if sub else ''
    return lambda n, N: ('<section class="s"><div class="hd meta">%s</div><div class="mid"><h1 class="%s">%s</h1>%s<div class="swipe">%s</div></div>%s</section>'
                         % (label, size, title, subh, cue, foot(n, N)))

def cue_div(cue):
    # Sog-Zeile ans Folienende: nennt konkret, was die naechste Folie bringt (nie generisch "Weiterwischen")
    return '<div class="swipe">%s</div>' % cue if cue else ''

def s_point(label, title, ps=None, src=None, meta=False, size='', cue=None):
    srch = '<div class="src">%s</div>' % src if src else ''
    return lambda n, N: ('<section class="s"><div class="hd%s">%s</div><div class="mid"><h1 class="%s">%s</h1>%s%s%s</div>%s</section>'
                         % (' meta' if meta else '', label, size, title, paras(ps), srch, cue_div(cue), foot(n, N)))

def s_proof(label, title, big=None, big_sub=None, img=None, quote=None, quote_from=None, ps=None, src=None, cue=None, size='m'):
    # Beleg-Folie (Proof vor Promise): eine grosse Zahl (big + big_sub), ein Screenshot (img, Dateipfad, nur mit
    # Einverstaendnis und anonymisiert) oder ein woertliches Zitat als Karte (quote, quote_from). Nachgestelltes
    # immer als solches kennzeichnen (quote_from='Nachgestellt').
    parts = []
    if big:
        parts.append('<div><div class="big%s">%s</div><div class="bigsub">%s</div></div>' % (' sm' if len(strip_tags(big)) > 9 else '', big, big_sub or ''))
    if img:
        parts.append('<div class="shot"><img src="file://%s"></div>' % img)
    if quote:
        parts.append('<div class="quote"><div class="qf">%s</div><div class="qt">%s</div></div>' % (quote_from or '', quote))
    srch = '<div class="src">%s</div>' % src if src else ''
    return lambda n, N: ('<section class="s"><div class="hd">%s</div><div class="mid"><h1 class="%s">%s</h1>%s%s%s%s</div>%s</section>'
                         % (label, size, title, ''.join(parts), paras(ps), srch, cue_div(cue), foot(n, N)))

def s_memo(label, title, head, items, cta, sub=None):
    # Merkzettel-Folie zum Speichern: Checkliste in einem Bild, darunter genau ein CTA
    li = ''.join('<div class="mi">%s<div>%s</div></div>' % (ICON_OK, t) for t in items)
    subh = '<p class="sub">%s</p>' % sub if sub else ''
    ctah = '<div class="cta">%s</div>' % cta if cta else ''
    return lambda n, N: ('<section class="s"><div class="hd meta">%s</div><div style="display:flex;flex-direction:column;gap:30px"><h2>%s</h2>%s<div class="memo"><div class="mh">%s</div>%s</div></div><div style="display:flex;flex-direction:column;gap:36px">%s%s</div></section>'
                         % (label, title, subh, head, li, ctah, foot(n, N)))

ICON_X = '<svg width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#3A3A37"/><path d="M15 15 L29 29 M29 15 L15 29" stroke="#C9C9C2" stroke-width="3.5" stroke-linecap="round"/></svg>'
ICON_OK = '<svg width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#ffab00"/><path d="M13 22.5 L19.5 29 L31 16" stroke="#000" stroke-width="3.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def s_vs(label, title, left_head, left, right_head, right, cta):
    lrows = ''.join('<div class="row a">%s<div>%s</div></div>' % (ICON_X, t) for t in left)
    rrows = ''.join('<div class="row b">%s<div>%s</div></div>' % (ICON_OK, t) for t in right)
    return lambda n, N: ('<section class="s"><div class="hd meta">%s</div><div class="vsw"><h2>%s</h2><div class="cols"><div class="col"><div class="pill a">%s</div>%s</div><div class="vline"></div><div class="col"><div class="pill b">%s</div>%s</div></div></div><div style="display:flex;flex-direction:column;gap:40px"><div class="cta">%s</div>%s</div></section>'
                         % (label, title, left_head, lrows, right_head, rrows, cta, foot(n, N)))

def s_bingo(label, title, sub, cells, center_idx, cta):
    cs = ''.join('<div class="cell%s">%s</div>' % (' c' if i == center_idx else '', t) for i, t in enumerate(cells))
    return lambda n, N: ('<section class="s"><div class="hd meta">%s</div><div style="display:flex;flex-direction:column;gap:32px"><h2>%s</h2><p class="sub">%s</p><div class="grid">%s</div></div><div style="display:flex;flex-direction:column;gap:36px"><div class="cta">%s</div>%s</div></section>'
                         % (label, title, sub, cs, cta, foot()))

def s_question(label, kick, question, me, cta):
    return lambda n, N: ('<section class="s q"><div class="hd meta">%s</div><div class="qmid"><div class="kick">%s</div><h1 class="m">%s</h1><div class="me">%s</div><div class="cta" style="color:var(--fg2)">%s</div></div>%s</section>'
                         % (label, kick, question, me, cta, foot()))

def s_story(label, title, ps, cta):
    return lambda n, N: ('<section class="s story"><div class="hd">%s</div><div class="mid"><h1>%s</h1>%s</div><div class="pcta">%s &#8594;</div></section>'
                         % (label, title, paras(ps), cta))

def s_mail(label, title, mails, src=None, cue=None):
    # mails: [(Absenderzeile, Kernsatz)] - Klarnamen und Adressen von Betroffenen nie zeigen
    ms = ''.join('<div class="mail"><div class="mfrom">%s</div><div class="mtext">%s</div></div>' % (f, t) for f, t in mails)
    srch = '<div class="src">%s</div>' % src if src else ''
    return lambda n, N: ('<section class="s"><div class="hd">%s</div><div style="display:flex;flex-direction:column;gap:34px"><h2>%s</h2><div class="mails">%s</div>%s%s</div>%s</section>'
                         % (label, title, ms, srch, cue_div(cue), foot(n, N)))

def s_chat(label, title, blocks, sender='Support', cue=None):
    # blocks: [(Zitat des Betruegers, Schlagwort, Einordnung)]
    bs = ''.join('<div class="cblock"><div class="bub"><div class="bfrom">%s</div><div class="btext">%s</div></div><div class="tag">%s</div><div class="tnote">%s</div></div>'
                 % (sender, q, tg, nt) for q, tg, nt in blocks)
    return lambda n, N: ('<section class="s"><div class="hd">%s</div><div style="display:flex;flex-direction:column;gap:40px"><h2>%s</h2><div class="chat">%s</div>%s</div>%s</section>'
                         % (label, title, bs, cue_div(cue), foot(n, N)))

def s_list(label, title, items, cta, sub=None):
    li = ''.join('<div class="li"><div class="num">%d</div><div class="lt">%s</div></div>' % (i, t) for i, t in enumerate(items, 1))
    subh = '<p class="sub">%s</p>' % sub if sub else ''
    return lambda n, N: ('<section class="s"><div class="hd meta">%s</div><div style="display:flex;flex-direction:column;gap:34px"><h2>%s</h2>%s<div class="list">%s</div></div><div style="display:flex;flex-direction:column;gap:36px"><div class="cta">%s</div>%s</div></section>'
                         % (label, title, subh, li, cta, foot(n, N)))

# ---------------- Pruefungen ----------------
_B = 'WyJhYmVyIiwgImplZG9jaCIsICJub2NoIiwgIm5pY2h0IiwgImFsbGVyZGluZyIsICJkYW5lYmVuIiwgInZvcnd1cmYiLCAiZWhybGljaCIsICJkaXJla3QiLCAia2xhciIsICJmZWluanVzdCIsICJmZWluc2NobGlmZiIsICJkZW5rZmVobGVyIiwgImZlaGxlciIsICJwcm9ibGVtIiwgImxlcm4iLCAibGVpZGVyIiwgInRoZXJhcGkiLCAicHJvZmVzc2lvbmVsbGUgaGlsZmUiLCAia2FsaWJyIiwgInByw6R6aXMiLCAiamFqYSIsICJvZmZlbiBnZXNhZ3QiLCAidGlwcCIsICJleHBlcnRlIiwgImV4cGVydGluIiwgInByb2ZpIiwgImNvYWNoIiwgIm1lbnRvciJd'
def banned():
    return json.loads(base64.b64decode(_B).decode('utf-8'))

def strip_tags(t):
    return re.sub(r'<[^>]+>', ' ', html.unescape(t))

def check_text(label, text):
    t = strip_tags(text).lower()
    hits = []
    for w in banned():
        if w == 'klar':
            if re.search(r'\bklar', t):
                hits.append(w)
        elif w in ('profi', 'jaja'):
            if re.search(r'\b' + w + r'(s)?\b', t):
                hits.append(w)
        elif w in ('noch', 'aber'):
            if re.search(r'\b' + w + r'\b', t) or (w == 'noch' and re.search(r'noch', t)):
                hits.append(w)
        elif w in t:
            hits.append(w)
    emo = [c for c in text if unicodedata.category(c) == 'So' and ord(c) > 0x2100 and c not in '→↑←↓']
    if emo:
        hits.append('EMOJI:' + ''.join(emo))
    if hits:
        print('!! VERBOTEN in %s: %s' % (label, sorted(set(hits))))
    return not hits

# ---------------- Rendern ----------------
RENDER_JS = r"""
const {chromium}=require('%s/playwright');
const jobs=require(process.argv[2]);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const j of jobs){const p=await b.newPage({viewport:{width:j.w,height:j.h}});
await p.goto('file://'+j.html);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(120);
const r=await p.evaluate(()=>{const s=document.querySelector('.s');const R=s.getBoundingClientRect();
 const bad=[];for(const e of s.querySelectorAll('*')){const q=e.getBoundingClientRect();if(q.width===0)continue;
  if(q.left<R.left+95||q.right>R.right-95||q.top<R.top+40||q.bottom>R.bottom-40)bad.push(e.tagName+'.'+e.className+':'+Math.round(q.left)+','+Math.round(q.right)+','+Math.round(q.top)+','+Math.round(q.bottom));}
 const ft=s.querySelector('.ft');const kids=[...s.children];let overlap=false;
 for(let i=0;i<kids.length-1;i++){if(kids[i].getBoundingClientRect().bottom>kids[i+1].getBoundingClientRect().top-8)overlap=true;}
 return {m:document.fonts.check('800 80px Montserrat'),b:document.fonts.check('400 35px "Libre Baskerville"'),over:s.scrollHeight>s.clientHeight||s.scrollWidth>s.clientWidth,overlap,bad:bad.slice(0,5)}});
console.log(JSON.stringify({png:j.png.split('/').pop(),...r}));
await p.screenshot({path:j.png});await p.close();}
await b.close()})();
""" % NM

def build(name, slides, w=1080, h=1350):
    d = os.path.join(OUT, name)
    os.makedirs(d, exist_ok=True)
    jobs = []
    N = len(slides)
    for i, sl in enumerate(slides, 1):
        sec = sl(i if N > 1 else None, N if N > 1 else None)
        sec = re.sub(r'(\d) (\$|%|€|BTC|Uhr|Wörter|Bitcoin|Tage|Schritte|Fehlgriffe|Teilnehmer|Wallets)', lambda m: m.group(1) + '&nbsp;' + m.group(2), sec)
        check_text('%s Bild %d' % (name, i), sec)
        hp = os.path.join(d, '%s-%02d.html' % (name, i))
        open(hp, 'w', encoding='utf-8').write(page(sec, w, h))
        jobs.append({'html': hp, 'png': os.path.join(d, '%s-%02d.png' % (name, i)), 'w': w, 'h': h})
    jf = os.path.join(d, 'jobs.json')
    json.dump(jobs, open(jf, 'w'))
    rj = os.path.join(OUT, 'render.js')
    open(rj, 'w').write(RENDER_JS)
    res = subprocess.run(['node', rj, jf], capture_output=True, text=True)
    print(res.stdout.strip() or res.stderr[-2000:])
    return [j['png'] for j in jobs]

def sheet(pngs, out, cols=4, tw=360):
    from PIL import Image
    ims = [Image.open(p) for p in pngs]
    th = int(ims[0].size[1] * tw / ims[0].size[0])
    rows = (len(ims) + cols - 1) // cols
    c = Image.new('RGB', (tw * min(cols, len(ims)), th * rows), (40, 40, 40))
    for i, im in enumerate(ims):
        c.paste(im.resize((tw, th)), ((i % cols) * tw, (i // cols) * th))
    c.save(out)
    return out
