# Bildvorlagen fuer X (Twitter) im Design System "chrisalcatrez": 1600x900 (16:9), schwarz, eine Akzentfarbe.
# Nutzung: sys.path.insert(0, '<repo>/tools'); from x_gen import *; build_x('x-N', [x_card(...), x_vs(...)])
# Vorlagen: x_card (Aussage gross), x_vs (zwei Spalten), x_chat (Betrueger-Saetze als Chat), x_meme (zwei Felder),
# x_list (nummerierte Liste). check_text() aus gen prueft gestrichene Woerter, build_x() rendert und prueft Lage.
import gen
from gen import check_text, HANDLE, ICON_X, ICON_OK, sheet

XW, XH = 1600, 900
X_CSS = """
.x{width:1600px;height:900px;padding:80px 96px;display:flex;flex-direction:column;justify-content:space-between;background:#000;color:var(--fg);font-family:'Montserrat',sans-serif;overflow:hidden;position:relative}
.x .hd{font-size:24px;letter-spacing:4px}
.x .xft{display:flex;justify-content:space-between;font-size:24px;color:var(--meta)}
.x h1{font-size:82px;line-height:1.1;letter-spacing:-1px;margin:0;font-weight:800;max-width:1300px}
.x h1.big{font-size:96px;line-height:1.06}
.x h1.sm{font-size:64px;line-height:1.14}
.x .sub{font-family:'Libre Baskerville',serif;font-size:34px;line-height:1.45;color:var(--fg2);max-width:1250px}
.x .mid{display:flex;flex-direction:column;gap:34px;justify-content:center;flex:1;margin:24px 0}
/* zwei Spalten */
.x .cols{display:grid;grid-template-columns:1fr 2px 1fr;column-gap:56px;align-items:start}
.x .col{display:flex;flex-direction:column;gap:22px}
.x .pill{font-size:28px;padding:10px 22px}
.x .row{grid-template-columns:40px 1fr;font-size:30px;line-height:1.35}
/* Chat */
.x .chat{display:flex;flex-direction:column;gap:20px;max-width:940px}
.x .bub{align-self:flex-start;max-width:100%;background:#1C1C1A;border-radius:26px 26px 26px 6px;padding:20px 28px}
.x .bub.me{align-self:flex-end;background:#2A2A28;border-radius:26px 26px 6px 26px}
.x .bfrom{font-weight:700;font-size:20px;color:var(--meta);margin-bottom:6px}
.x .btext{font-family:'Libre Baskerville',serif;font-size:27px;line-height:1.4;color:var(--fg)}
.x .side{display:grid;grid-template-columns:940px 1fr;column-gap:56px;align-items:center;flex:1;margin:24px 0}
.x .side h2{font-size:42px;line-height:1.16;margin:0;font-weight:800;overflow-wrap:anywhere}
/* Meme: zwei Felder */
.x .meme{display:grid;grid-template-columns:1fr 1fr;column-gap:40px;flex:1;grid-template-rows:1fr;align-items:stretch;min-height:440px}
.x .cell{border:2px solid var(--line);border-radius:20px;padding:40px 44px;display:flex;flex-direction:column;gap:22px;justify-content:center;height:auto;text-align:left;align-items:flex-start}
.x .cell.acc{border-color:var(--acc)}
.x .clabel{font-weight:800;font-size:26px;letter-spacing:3px;text-transform:uppercase;color:var(--meta)}
.x .cell.acc .clabel{color:var(--acc)}
.x .ctext{font-family:'Libre Baskerville',serif;font-size:36px;line-height:1.4;color:var(--fg)}
/* Liste */
.x .list{display:flex;flex-direction:column;gap:18px;max-width:1300px}
.x .li{display:grid;grid-template-columns:64px 1fr;column-gap:20px;align-items:baseline}
.x .num{font-weight:800;font-size:48px;line-height:1;color:var(--acc)}
.x .lt{font-family:'Libre Baskerville',serif;font-size:32px;line-height:1.35;color:var(--fg)}
"""
if X_CSS not in gen.CSS:
    gen.CSS += X_CSS

def xfoot(label=''):
    return '<div class="xft"><div>%s</div><div>%s</div></div>' % (label, HANDLE)

def x_card(label, title, sub=None, size=''):
    s = ('<div class="sub">%s</div>' % sub) if sub else ''
    return lambda n, N: ('<section class="s x"><div class="hd">%s</div><div class="mid"><h1 class="%s">%s</h1>%s</div>%s</section>'
                         % (label, size, title, s, xfoot()))

def x_vs(label, title, left_head, left, right_head, right):
    lrows = ''.join('<div class="row a">%s<div>%s</div></div>' % (ICON_X, t) for t in left)
    rrows = ''.join('<div class="row b">%s<div>%s</div></div>' % (ICON_OK, t) for t in right)
    return lambda n, N: ('<section class="s x"><div class="hd meta">%s</div><div class="mid"><h1 class="sm">%s</h1><div class="cols"><div class="col"><div class="pill a">%s</div>%s</div><div class="vline"></div><div class="col"><div class="pill b">%s</div>%s</div></div></div>%s</section>'
                         % (label, title, left_head, lrows, right_head, rrows, xfoot()))

def x_chat(label, headline, bubbles):
    # bubbles: [(Absender, Text, ist_ich)]
    b = ''.join('<div class="bub%s"><div class="bfrom">%s</div><div class="btext">%s</div></div>' % (' me' if me else '', frm, t) for frm, t, me in bubbles)
    return lambda n, N: ('<section class="s x"><div class="hd meta">%s</div><div class="side"><div class="chat">%s</div><h2>%s</h2></div>%s</section>'
                         % (label, b, headline, xfoot()))

def x_meme(label, title, left_label, left_text, right_label, right_text):
    return lambda n, N: ('<section class="s x"><div class="hd meta">%s</div><div class="mid"><h1 class="sm">%s</h1><div class="meme"><div class="cell"><div class="clabel">%s</div><div class="ctext">%s</div></div><div class="cell acc"><div class="clabel">%s</div><div class="ctext">%s</div></div></div></div>%s</section>'
                         % (label, title, left_label, left_text, right_label, right_text, xfoot()))

def x_list(label, title, items):
    li = ''.join('<div class="li"><div class="num">%d</div><div class="lt">%s</div></div>' % (i + 1, t) for i, t in enumerate(items))
    return lambda n, N: ('<section class="s x"><div class="hd meta">%s</div><div class="mid"><h1 class="sm">%s</h1><div class="list">%s</div></div>%s</section>'
                         % (label, title, li, xfoot()))

def build_x(name, slides):
    return gen.build(name, slides, XW, XH)
