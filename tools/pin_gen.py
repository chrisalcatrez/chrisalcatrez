# Bildvorlagen fuer Pinterest im Design System "chrisalcatrez": 1000x1500 (2:3, Pinterest-Standard), schwarz, eine Akzentfarbe.
# Nutzung: sys.path.insert(0, '<repo>/tools'); from pin_gen import *; build_pin('p-N', [pin_list(...)])
# Vorlagen: pin_hero (grosse Aussage), pin_list (nummerierte Checkliste), pin_vs (Mythos oben, Wirklichkeit unten),
# pin_chat (nachgestellter Chat), pin_steps (Schritte, nur das Was), pin_term (Begriff erklaert), pin_faq (Frage und Antwort),
# pin_photo (Person unten, Aussage oben). Jede Vorlage kennt theme='acc' (Akzentfarbe als Grund, Formattest).
# Jede Vorlage traegt unten die Domain (chrisalcatrez.de) und das Wasserzeichen; Text bleibt im sicheren Bereich (96 px seitlich).
import gen
from gen import check_text, HANDLE, ICON_X, ICON_OK, sheet

PW, PH = 1000, 1500
DOMAIN = 'chrisalcatrez.de'
P_CSS = """
.pin{width:1000px;height:1500px;padding:88px 96px;display:flex;flex-direction:column;justify-content:space-between;background:#000;color:var(--fg);font-family:'Montserrat',sans-serif;overflow:hidden;position:relative}
.pin .hd{font-size:24px;letter-spacing:4px;line-height:1.3;color:var(--acc);font-weight:700;text-transform:uppercase}
.pin .hd.meta{color:var(--meta)}
.pin .mid{display:flex;flex-direction:column;gap:40px;justify-content:center;flex:1;margin:28px 0}
.pin h1{font-size:90px;line-height:1.06;letter-spacing:-1.5px;margin:0;font-weight:800}
.pin h1.big{font-size:106px;line-height:1.02;letter-spacing:-2px}
.pin h1.sm{font-size:78px;line-height:1.08;letter-spacing:-1.2px}
.pin h1.xs{font-size:64px;line-height:1.1;letter-spacing:-0.8px}
.pin .sub{font-family:'Libre Baskerville',serif;font-size:36px;line-height:1.45;color:var(--fg2);margin:0}
.pin .sub b{color:var(--fg);font-weight:700}
.pin .pft{display:flex;justify-content:space-between;align-items:center;font-size:24px;color:var(--meta);border-top:2px solid var(--line);padding-top:26px}
.pin .pft b{color:var(--acc);font-weight:700;font-size:28px;letter-spacing:0.5px}
.pin .pcta{align-self:flex-start;background:var(--acc);color:#000;font-weight:800;font-size:32px;line-height:1.2;padding:20px 30px;border-radius:14px}
.pin .bignum{font-weight:800;font-size:150px;line-height:0.95;letter-spacing:-5px;color:var(--acc)}
/* Liste */
.pin .list{display:flex;flex-direction:column;gap:30px}
.pin .li{display:grid;grid-template-columns:78px 1fr;column-gap:18px;align-items:baseline}
.pin .num{font-weight:800;font-size:64px;line-height:1;color:var(--acc)}
.pin .lt{font-family:'Libre Baskerville',serif;font-size:36px;line-height:1.38;color:var(--fg)}
.pin .list.dense{gap:24px}
.pin .list.dense .lt{font-size:32px}
.pin .list.dense .num{font-size:56px}
/* Mythos gestapelt */
.pin .vsw{display:flex;flex-direction:column;gap:44px}
.pin .blk{display:flex;flex-direction:column;gap:24px}
.pin .pill{align-self:flex-start;font-weight:800;font-size:27px;letter-spacing:1px;padding:10px 22px;border-radius:8px}
.pin .row{grid-template-columns:48px 1fr;column-gap:20px;font-size:34px;line-height:1.36}
.pin .row.b{color:var(--fg)}
/* Chat */
.pin .chat{display:flex;flex-direction:column;gap:20px}
.pin .bub{align-self:flex-start;max-width:90%;background:#1C1C1A;border-radius:28px 28px 28px 6px;padding:22px 30px}
.pin .bub.me{align-self:flex-end;background:#2A2A28;border-radius:28px 28px 6px 28px}
.pin .bfrom{font-weight:700;font-size:22px;color:var(--meta);margin-bottom:6px}
.pin .btext{font-family:'Libre Baskerville',serif;font-size:34px;line-height:1.4;color:var(--fg)}
.pin .tag{align-self:flex-start;background:var(--acc);color:#000;font-weight:800;font-size:22px;letter-spacing:2px;text-transform:uppercase;padding:8px 14px;border-radius:8px}
/* Schritte */
.pin .steps{display:flex;flex-direction:column;gap:32px}
.pin .st{display:grid;grid-template-columns:92px 1fr;column-gap:20px;align-items:start}
.pin .sn{width:74px;height:74px;border-radius:50%;background:var(--acc);color:#000;font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center;margin-top:2px}
.pin .stt{font-weight:700;font-size:38px;line-height:1.2;margin-bottom:8px}
.pin .stx{font-family:'Libre Baskerville',serif;font-size:31px;line-height:1.4;color:var(--fg2)}
/* Begriff */
.pin .term{font-weight:800;font-size:120px;line-height:1;letter-spacing:-4px;margin:0}
.pin .def{font-family:'Libre Baskerville',serif;font-size:40px;line-height:1.45;color:var(--fg);margin:0}
.pin .rules{display:flex;flex-direction:column;gap:24px}
.pin .rules .row{color:var(--fg2)}
/* FAQ */
.pin .ans{font-family:'Libre Baskerville',serif;font-size:38px;line-height:1.45;color:var(--fg);margin:0}
.pin .pts{display:flex;flex-direction:column;gap:22px}
/* Foto-Pin: Person unten (Ebene pinterest/foto-ebene.png), Text oben auf Schwarz */
.pin.photo{background-color:#000;background-repeat:no-repeat;background-size:1000px 1500px;background-position:0 0;justify-content:flex-start}
.pin.photo .mid{flex:0 0 auto;justify-content:flex-start;margin:44px 0 0;gap:34px}
.pin.photo .pft{margin-top:auto}
.pin.photo .pft{border-top-color:rgba(255,255,255,0.14)}
.pin.photo .sub{max-width:760px}
/* Akzent-Thema: Akzentfarbe als Grund, Schrift schwarz (Formattest) */
.pin.acc{background:var(--acc);color:#000}
.pin.acc .hd{color:#000}
.pin.acc .hd.meta{color:#3a2a00}
.pin.acc .sub,.pin.acc .lt,.pin.acc .stx,.pin.acc .ans,.pin.acc .def,.pin.acc .btext{color:#000}
.pin.acc .sub b{color:#000}
.pin.acc .num,.pin.acc .bignum,.pin.acc .term{color:#000}
.pin.acc .pft{border-top-color:rgba(0,0,0,0.25);color:#3a2a00}
.pin.acc .pft b{color:#000}
.pin.acc .pcta{background:#000;color:var(--acc)}
.pin.acc .pill.b{background:#000;color:var(--acc)}
.pin.acc .pill.a{background:rgba(0,0,0,0.12);color:#000}
.pin.acc .sn{background:#000;color:var(--acc)}
.pin.acc .tag{background:#000;color:var(--acc)}
.pin.acc .bub{background:rgba(0,0,0,0.10)}
.pin.acc .bub.me{background:rgba(0,0,0,0.20)}
.pin.acc .bfrom{color:#3a2a00}
.pin.acc .row.a{color:#3a2a00}
.pin.acc .row.b{color:#000}
"""
if P_CSS not in gen.CSS:
    gen.CSS += P_CSS

def pcls(theme=''):
    return 'acc' if theme == 'acc' else ''

def pfoot():
    return '<div class="pft"><b>%s</b><div>%s</div></div>' % (DOMAIN, HANDLE)

def _cta(cta):
    return ('<div class="pcta">%s &#8594;</div>' % cta) if cta else ''

def pin_hero(label, title, sub=None, bignum=None, cta=None, size='', theme=''):
    s = ('<p class="sub">%s</p>' % sub) if sub else ''
    b = ('<div class="bignum">%s</div>' % bignum) if bignum else ''
    return lambda n, N: ('<section class="s pin %s"><div class="hd">%s</div><div class="mid">%s<h1 class="%s">%s</h1>%s%s</div>%s</section>'
                         % (pcls(theme), label, b, size, title, s, _cta(cta), pfoot()))

def pin_list(label, title, items, sub=None, cta=None, size='sm', dense=False, theme=''):
    li = ''.join('<div class="li"><div class="num">%d</div><div class="lt">%s</div></div>' % (i, t) for i, t in enumerate(items, 1))
    s = ('<p class="sub">%s</p>' % sub) if sub else ''
    return lambda n, N: ('<section class="s pin %s"><div class="hd">%s</div><div class="mid"><h1 class="%s">%s</h1>%s<div class="list%s">%s</div>%s</div>%s</section>'
                         % (pcls(theme), label, size, title, s, ' dense' if dense else '', li, _cta(cta), pfoot()))

def pin_vs(label, title, top_head, top, bottom_head, bottom, cta=None, size='sm', theme=''):
    a = ''.join('<div class="row a">%s<div>%s</div></div>' % (ICON_X, t) for t in top)
    b = ''.join('<div class="row b">%s<div>%s</div></div>' % (ICON_OK, t) for t in bottom)
    return lambda n, N: ('<section class="s pin %s"><div class="hd meta">%s</div><div class="mid"><h1 class="%s">%s</h1><div class="vsw"><div class="blk"><div class="pill a">%s</div>%s</div><div class="blk"><div class="pill b">%s</div>%s</div></div>%s</div>%s</section>'
                         % (pcls(theme), label, size, title, top_head, a, bottom_head, b, _cta(cta), pfoot()))

def pin_chat(label, headline, bubbles, tag='Nachgestellt', cta=None, size='xs', theme=''):
    # bubbles: [(Absender, Text, ist_ich)]
    b = ''.join('<div class="bub%s"><div class="bfrom">%s</div><div class="btext">%s</div></div>' % (' me' if me else '', frm, t) for frm, t, me in bubbles)
    return lambda n, N: ('<section class="s pin %s"><div class="hd meta">%s</div><div class="mid"><div class="tag">%s</div><div class="chat">%s</div><h1 class="%s">%s</h1>%s</div>%s</section>'
                         % (pcls(theme), label, tag, b, size, headline, _cta(cta), pfoot()))

def pin_steps(label, title, steps, sub=None, cta=None, size='sm', theme=''):
    # steps: [(Titel, ein Satz)]
    st = ''.join('<div class="st"><div class="sn">%d</div><div><div class="stt">%s</div><div class="stx">%s</div></div></div>' % (i, t, x) for i, (t, x) in enumerate(steps, 1))
    s = ('<p class="sub">%s</p>' % sub) if sub else ''
    return lambda n, N: ('<section class="s pin %s"><div class="hd">%s</div><div class="mid"><h1 class="%s">%s</h1>%s<div class="steps">%s</div>%s</div>%s</section>'
                         % (pcls(theme), label, size, title, s, st, _cta(cta), pfoot()))

def pin_term(label, term, definition, rules, rules_head='Drei Regeln', cta=None, theme=''):
    r = ''.join('<div class="row">%s<div>%s</div></div>' % (ICON_OK, t) for t in rules)
    return lambda n, N: ('<section class="s pin %s"><div class="hd meta">%s</div><div class="mid"><h1 class="term">%s</h1><p class="def">%s</p><div class="pill b" style="align-self:flex-start">%s</div><div class="rules">%s</div>%s</div>%s</section>'
                         % (pcls(theme), label, term, definition, rules_head, r, _cta(cta), pfoot()))

def pin_faq(label, question, answer, points=None, cta=None, size='', theme=''):
    p = ''.join('<div class="row b">%s<div>%s</div></div>' % (ICON_OK, t) for t in (points or []))
    pts = ('<div class="pts">%s</div>' % p) if p else ''
    return lambda n, N: ('<section class="s pin %s"><div class="hd meta">%s</div><div class="mid"><h1 class="%s">%s</h1><p class="ans">%s</p>%s%s</div>%s</section>'
                         % (pcls(theme), label, size, question, answer, pts, _cta(cta), pfoot()))

def pin_photo(label, title, sub=None, cta=None, size='big', ebene=None):
    # Person unten aus der Fotoebene (Standard: pinterest/foto-ebene.png im Repository), Text oben; die Ebene endet
    # in Schwarz, bevor die Fusszeile beginnt. Hoechstens ein Foto-Pin pro Woche, damit jeder Pin frisch bleibt.
    import os
    eb = ebene or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'pinterest', 'foto-ebene.png')
    st = 'background-image:url(file://%s)' % eb
    s = ('<p class="sub">%s</p>' % sub) if sub else ''
    return lambda n, N: ('<section class="s pin photo" style="%s"><div class="hd">%s</div><div class="mid"><h1 class="%s">%s</h1>%s%s</div>%s</section>'
                         % (st, label, size, title, s, _cta(cta), pfoot()))

def build_pin(name, slides):
    return gen.build(name, slides, PW, PH)
