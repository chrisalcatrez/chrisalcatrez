# Bildvorlagen fuer Pinterest im Design System "chrisalcatrez": 1000x1500 (2:3, Pinterest-Standard).
# Grundsatz (Vorgabe des Nutzers): visuell statt Textwueste. Ein Badge oben, eine kurze Ueberschrift (in 1 bis 2 Sekunden
# erfassbar), darunter ein visueller Block (Icons, Schritte mit Pfeilen, Gegenueberstellung, Chat im Handy-Rahmen,
# Balken- oder Kurvenchart), unten ein dezenter Hinweis statt Verkaufs-Button, dazu Domain und Wasserzeichen.
# Im Bild steht nur das Was (Anchu Koegl: Appetizer-Prinzip). Die Geschichte und das Wie gehoeren in die Pin-Beschreibung.
# Nutzung: sys.path.insert(0, '<repo>/tools'); from pin_gen import *; build_pin('p-N', [pin_check(...)])
# Vorlagen: pin_check (Checkliste mit Icons oder Nummern), pin_flow (Schritte mit Pfeilen), pin_vs (Mythos gegen
# Wirklichkeit), pin_chat (Chat im Handy-Rahmen), pin_term (Begriff erklaert mit 12 Woerter-Kacheln), pin_faq (Frage,
# kurze Antwort, Pills), pin_bars (Balkenchart im Handy-Rahmen), pin_compare_chart (zwei Kurven-Karten), pin_hero
# (grosse Zahl), pin_photo (Person unten aus pinterest/foto-ebene.png). Farben: theme='' (schwarz), 'light' (hell),
# 'acc' (Akzentfarbe als Grund). build_pin() rendert und prueft (over, overlap, bad, gestrichene Woerter).
#
# Stil 2 (Vorgabe des Nutzers vom 07.10.2026, gilt fuer alle neuen Pins): pro Pin eine dominante Aussage, ein visuelles
# Element, hoechstens 3 bis 5 Informationseinheiten; keine Badges, keine kleinen Icons, keine Mini-Labels, keine
# gestapelten Boxen. Hierarchie: grosse Headline oben -> grosses zentrales Visual -> 3 deutliche Punkte -> kurzer CTA unten.
# Vorlage pin2(theme, title, visual, points, cta, size, marks, photo): visual aus vz_num (grosse Zahl), vz_bubble (ein
# Beispielsatz in einer grossen Sprechblase), vz_bars (2 bis 3 dicke Balken mit grossen Zahlen), vz_curve (eine grosse
# Kurve mit Punkten in festem Abstand), vz_card (ein grosses Wort oder ein Begriff auf einer Karte) oder photo=True
# (Person unten aus pinterest/foto-ebene.png, Punkte stehen ueber dem Foto). Punkte mit grossen Ziffern (marks='num')
# oder grossen Haken (marks='check'). CTA-Zeile als Balken innerhalb der Raender, Wasserzeichen darin.
import os
import gen
from gen import check_text, HANDLE, sheet

PW, PH = 1000, 1500
DOMAIN = 'chrisalcatrez.de'

P_CSS = """
.pin{--pbg:#000;--pfg:#F5F5F0;--pfg2:#C9C9C2;--pmeta:#9C9C96;--pline:#2A2A28;--ptile:#141413;--pbub:#262624;--pacc:#ffab00;--pacc-fg:#000;--pico:#ffab00;
 width:1000px;height:1500px;padding:88px 96px 78px;display:flex;flex-direction:column;justify-content:flex-start;background:var(--pbg);color:var(--pfg);font-family:'Montserrat',sans-serif;overflow:hidden;position:relative}
.pin.light{--pbg:#F5F5F0;--pfg:#0B0B0B;--pfg2:#3A3A36;--pmeta:#6B6B66;--pline:#D9D9D0;--ptile:#FFFFFF;--pbub:#E9E9E1;--pico:#0B0B0B}
.pin.acc{--pbg:#ffab00;--pfg:#000;--pfg2:#2A1E00;--pmeta:#4A3500;--pline:rgba(0,0,0,.22);--ptile:rgba(0,0,0,.07);--pbub:rgba(0,0,0,.10);--pacc:#000;--pacc-fg:#ffab00;--pico:#000}
.pin.dots{background-image:radial-gradient(var(--pline) 1.6px,transparent 1.7px);background-size:38px 38px;background-position:19px 19px}
.pin .top{display:flex;flex-direction:column;align-items:flex-start;gap:30px}
.pin .badge{display:inline-flex;align-items:center;gap:12px;padding:12px 22px 12px 18px;border-radius:999px;background:var(--pacc);color:var(--pacc-fg);font-weight:800;font-size:22px;letter-spacing:3px;text-transform:uppercase;line-height:1}
.pin .badge svg{display:block}
.pin h1{font-size:86px;line-height:1.04;letter-spacing:-2px;margin:0;font-weight:800;max-width:808px}
.pin h1.big{font-size:104px;line-height:1.0;letter-spacing:-3px}
.pin h1.sm{font-size:74px;line-height:1.06;letter-spacing:-1.5px}
.pin h1.xs{font-size:64px;line-height:1.1;letter-spacing:-1px}
.pin .lead{font-family:'Libre Baskerville',serif;font-size:33px;line-height:1.42;color:var(--pfg2);margin:0;max-width:780px}
.pin .lead b{color:var(--pfg);font-weight:700}
.pin .vis{flex:1;display:flex;flex-direction:column;justify-content:center;margin:40px 0 28px}
.pin .bot{display:flex;flex-direction:column;gap:22px}
.pin .cta{display:flex;align-items:center;gap:12px;font-weight:600;font-size:26px;color:var(--pmeta)}
.pin .cta svg{display:block;color:var(--pacc)}
.pin.light .cta svg{color:var(--pfg)}
.pin .pft{display:flex;justify-content:space-between;align-items:center;font-size:24px;color:var(--pmeta);border-top:2px solid var(--pline);padding-top:24px;min-height:58px}
.pin .pft b{color:var(--pacc);font-weight:700;font-size:28px;letter-spacing:0.5px}
.pin.light .pft b{color:var(--pfg)}
/* Checkliste */
.pin .checks{display:flex;flex-direction:column;gap:26px}
.pin .ck{display:grid;grid-template-columns:96px 1fr;column-gap:26px;align-items:center}
.pin .tile{width:96px;height:96px;border-radius:26px;background:var(--ptile);border:2px solid var(--pline);display:flex;align-items:center;justify-content:center;color:var(--pico)}
.pin .tile.num{font-weight:800;font-size:44px;background:var(--pacc);color:var(--pacc-fg);border-color:transparent}
.pin .cl{font-weight:600;font-size:36px;line-height:1.22}
.pin .cl.q{font-family:'Libre Baskerville',serif;font-weight:400;font-size:35px;line-height:1.34}
.pin .checks.dense{gap:20px}
.pin .checks.dense .tile{width:84px;height:84px;border-radius:22px}
.pin .checks.dense .ck{grid-template-columns:84px 1fr}
.pin .checks.dense .cl{font-size:33px}
/* Schritte */
.pin .flow{display:flex;flex-direction:column;gap:8px}
.pin .step{display:grid;grid-template-columns:90px 1fr;column-gap:26px;align-items:center;background:var(--ptile);border:2px solid var(--pline);border-radius:28px;padding:24px 28px 24px 20px}
.pin .sn{width:90px;height:90px;border-radius:50%;background:var(--pacc);color:var(--pacc-fg);font-weight:800;font-size:46px;display:flex;align-items:center;justify-content:center}
.pin .sl{font-weight:600;font-size:36px;line-height:1.22}
.pin .conn{height:46px;display:flex;align-items:center;justify-content:center;color:var(--pacc)}
.pin.light .conn{color:var(--pfg)}
/* Gegenueberstellung */
.pin .vs{display:flex;flex-direction:column;gap:22px}
.pin .vb{border:2px solid var(--pline);border-radius:30px;padding:30px 34px 32px;display:flex;flex-direction:column;gap:22px;background:var(--ptile)}
.pin .vb.hl{border-color:var(--pacc)}
.pin .vh{align-self:flex-start;font-weight:800;font-size:22px;letter-spacing:3px;text-transform:uppercase;padding:9px 16px;border-radius:8px;background:var(--pline);color:var(--pfg)}
.pin .vb.hl .vh{background:var(--pacc);color:var(--pacc-fg)}
.pin .vr{display:grid;grid-template-columns:52px 1fr;column-gap:18px;align-items:center;font-weight:600;font-size:34px;line-height:1.25}
.pin .vi{width:52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.pin .vi.x{background:var(--pline);color:var(--pfg2)}
.pin .vi.ok{background:var(--pacc);color:var(--pacc-fg)}
/* Handy-Rahmen, Chat, Balken */
.pin .phone{width:700px;margin:0 auto;border:4px solid var(--pline);border-radius:60px;padding:62px 32px 44px;background:var(--ptile);display:flex;flex-direction:column;gap:20px;position:relative}
.pin .phone:before{content:'';position:absolute;top:18px;left:50%;transform:translateX(-50%);width:150px;height:12px;border-radius:6px;background:var(--pline)}
.pin .phone.wide{width:780px}
.pin .bub{align-self:flex-start;max-width:88%;background:var(--pbub);border-radius:28px 28px 28px 6px;padding:20px 26px}
.pin .bub.mine{align-self:flex-end;background:var(--pacc);color:var(--pacc-fg);border-radius:26px 26px 6px 26px}
.pin .bfrom{font-weight:700;font-size:19px;color:var(--pmeta);margin-bottom:6px}
.pin .bub.mine .bfrom{color:inherit;opacity:.7}
.pin .btext{font-family:'Libre Baskerville',serif;font-size:31px;line-height:1.38}
.pin .bars{display:flex;flex-direction:column;gap:38px;padding:12px 10px 8px}
.pin .bl{display:flex;justify-content:space-between;align-items:baseline;font-weight:600;font-size:30px;color:var(--pfg2);margin-bottom:14px;gap:16px}
.pin .bl b{font-weight:800;font-size:40px;color:var(--pfg);white-space:nowrap}
.pin .bt{height:40px;border-radius:20px;background:var(--pline);overflow:hidden}
.pin .bf{height:100%;background:var(--pacc);border-radius:20px;min-width:20px}
.pin .bhead{font-weight:800;font-size:22px;letter-spacing:3px;text-transform:uppercase;color:var(--pmeta);margin-bottom:-6px}
.pin .bnote{font-family:'Libre Baskerville',serif;font-size:30px;line-height:1.4;color:var(--pfg2);padding:18px 10px 0}
/* Begriff */
.pin .def{font-family:'Libre Baskerville',serif;font-size:36px;line-height:1.4;color:var(--pfg2);margin:0}
.pin .wgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.pin .wt{background:var(--ptile);border:2px solid var(--pline);border-radius:16px;padding:16px 16px;font-weight:700;font-size:26px;letter-spacing:2px;color:var(--pfg2);display:flex;gap:10px;align-items:center}
.pin .wt span{color:var(--pacc);font-size:20px;font-weight:800}
.pin.light .wt span{color:var(--pfg)}
.pin .termv{display:flex;flex-direction:column;gap:44px}
/* FAQ */
.pin .faq{display:flex;flex-direction:column;gap:34px}
.pin .ans{font-family:'Libre Baskerville',serif;font-size:42px;line-height:1.42;margin:0}
.pin .pills{display:flex;flex-wrap:wrap;gap:14px}
.pin .pill{align-self:auto;font-weight:700;font-size:27px;letter-spacing:0;padding:14px 22px;border-radius:999px;background:var(--ptile);border:2px solid var(--pline);color:var(--pfg)}
.pin .pill.hl{background:var(--pacc);color:var(--pacc-fg);border-color:transparent}
/* Kurven-Karten */
.pin .cmp{display:grid;grid-template-columns:1fr;gap:22px}
.pin .cc{background:var(--ptile);border:2px solid var(--pline);border-radius:28px;padding:22px 30px 20px;display:flex;flex-direction:column;gap:8px;align-items:stretch}
.pin .cc.hl{border-color:var(--pacc)}
.pin .cch{display:flex;align-items:center;gap:14px;font-weight:800;font-size:24px;letter-spacing:3px;text-transform:uppercase}
.pin .cch .vi{width:40px;height:40px}
.pin .cc svg.chart{width:100%;height:auto;display:block;margin:0 auto}
.pin .ccs{font-weight:600;font-size:29px;line-height:1.25;color:var(--pfg2)}
/* Hero */
.pin .bignum{font-weight:800;font-size:170px;line-height:0.95;letter-spacing:-7px;color:var(--pacc)}
.pin.light .bignum{color:var(--pfg)}
.pin .hero{display:flex;flex-direction:column;gap:30px}
/* Foto-Pin */
.pin.photo{background-color:#000;background-repeat:no-repeat;background-size:1000px 1500px;background-position:0 0}
.pin.photo .vis{flex:1}
.pin.photo .pft{border-top-color:rgba(255,255,255,0.14)}

/* Stil 2: Headline, ein Visual, drei Punkte, CTA-Balken */
.pin.v2{padding:92px 96px 40px;justify-content:flex-start}
.pin.v2 h1{font-size:100px;line-height:1.02;letter-spacing:-3px;max-width:808px}
.pin.v2 h1.sm{font-size:88px;line-height:1.04;letter-spacing:-2.5px}
.pin.v2 h1.xs{font-size:78px;line-height:1.06;letter-spacing:-2px}
.pin.v2 h1 em{font-style:normal;color:var(--pacc)}
.pin.light.v2 h1 em,.pin.acc.v2 h1 em{color:var(--pfg);text-decoration:underline;text-decoration-thickness:8px;text-underline-offset:10px;text-decoration-color:var(--pacc)}
.pin.light.v2 h1 em{text-decoration-color:#ffab00}
.pin.v2 .viz{flex:1 0 auto;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;gap:22px;margin:42px 0 34px}
.pin.v2 .viz.center{align-items:center;text-align:center}
.pin.v2 .vz-num{font-weight:800;font-size:190px;line-height:.95;letter-spacing:-8px;color:var(--pacc)}
.pin.light.v2 .vz-num{color:var(--pfg)}
.pin.v2 .vz-sub{font-family:'Libre Baskerville',serif;font-size:36px;line-height:1.38;color:var(--pfg2);max-width:800px}
.pin.v2 .vz-bub{background:var(--ptile);border:2px solid var(--pline);border-radius:46px 46px 46px 10px;padding:40px 46px;font-family:'Libre Baskerville',serif;font-size:46px;line-height:1.3;max-width:808px}
.pin.v2 .vz-note{font-weight:600;font-size:27px;color:var(--pmeta);letter-spacing:.5px}
.pin.v2 .vz-bars{display:flex;flex-direction:column;gap:30px;width:808px}
.pin.v2 .vzb .l{display:flex;justify-content:space-between;align-items:baseline;gap:20px;font-weight:600;font-size:36px;color:var(--pfg2);margin-bottom:12px}
.pin.v2 .vzb .l b{font-weight:800;font-size:58px;color:var(--pfg);letter-spacing:-2px;white-space:nowrap}
.pin.v2 .vzb .t{height:54px;border-radius:27px;background:var(--pline);overflow:hidden}
.pin.v2 .vzb .f{height:100%;background:var(--pacc);border-radius:27px;min-width:54px}
.pin.light.v2 .vzb .f{background:#0B0B0B}
.pin.v2 svg.vz-curve{width:808px;height:auto;display:block}
.pin.v2 .vz-card{background:var(--ptile);border:3px solid var(--pacc);border-radius:40px;padding:44px 52px;font-weight:800;font-size:96px;line-height:1;letter-spacing:-3px;color:var(--pfg)}
.pin.light.v2 .vz-card{border-color:#0B0B0B}
.pin.v2 .pts{display:flex;flex-direction:column;gap:26px;margin-bottom:42px}
.pin.v2 .pt{display:grid;grid-template-columns:92px 1fr;column-gap:18px;align-items:center}
.pin.v2 .pn{font-weight:800;font-size:72px;line-height:1;letter-spacing:-3px;color:var(--pacc)}
.pin.light.v2 .pn{color:var(--pfg)}
.pin.v2 .pn svg{display:block;color:var(--pacc)}
.pin.light.v2 .pn svg{color:var(--pfg)}
.pin.v2 .pl{font-weight:600;font-size:44px;line-height:1.18}
.pin.v2 .pl.q{font-family:'Libre Baskerville',serif;font-weight:400;font-size:41px;line-height:1.28}
.pin.v2 .ctabar{display:flex;justify-content:space-between;align-items:center;gap:24px;background:var(--pacc);color:#000;border-radius:24px;padding:28px 36px;font-weight:800;font-size:31px;line-height:1.15}
.pin.v2 .ctabar .h{font-weight:600;font-size:25px;opacity:.75;white-space:nowrap}
.pin.light.v2 .ctabar{background:#0B0B0B;color:#F5F5F0}
.pin.acc.v2 .ctabar{background:#000;color:#ffab00}
.pin.photo.v2 .viz{flex:1 1 auto;min-height:0;margin:12px 0 12px}
.pin.photo.v2 .pts{margin:34px 0 0}
.pin.v2 .pts.dense{gap:18px}
.pin.v2 .pts.dense .pl{font-size:40px}
.pin.v2 .pts.dense .pn{font-size:64px}
.pin.v2 .pts.dense .pt{grid-template-columns:80px 1fr}
"""
if P_CSS not in gen.CSS:
    gen.CSS += P_CSS

# ---------------- Icons (Linien, 24er Raster, Farbe folgt currentColor) ----------------
ICONS = {
 'link': '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
 'globe': '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
 'user': '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
 'users': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 'star': '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
 'key': '<path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"/>',
 'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
 'shield-check': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>',
 'phone': '<rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/>',
 'chat': '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
 'wallet': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M3 9V5a2 2 0 0 1 2-2h11"/><circle cx="16.5" cy="13.5" r="1.4"/>',
 'bank': '<path d="M3 22h18"/><path d="M5 22V10M9.5 22V10M14.5 22V10M19 22V10"/><path d="M2 10l10-6 10 6z"/>',
 'dollar': '<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
 'trend-up': '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
 'trend-down': '<polyline points="23 18 13.5 8.5 8.5 13.5 1 6"/><polyline points="17 18 23 18 23 12"/>',
 'bars': '<line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/>',
 'calendar': '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
 'alert': '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
 'x': '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
 'check': '<polyline points="20 6 9 17 4 12"/>',
 'pin': '<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>',
 'arrow-right': '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>',
 'arrow-down': '<line x1="12" y1="5" x2="12" y2="19"/><polyline points="19 12 12 19 5 12"/>',
 'lock': '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 'mail': '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>',
 'help': '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
 'download': '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>',
 'file': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
 'camera': '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
 'cloud': '<path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/>',
 'percent': '<line x1="19" y1="5" x2="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
 'repeat': '<polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>',
 'call': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
 'tag': '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>',
 'map-pin': '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
 'eye': '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
 'clock': '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
 'card': '<rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="23" y2="10"/>',
 'zap': '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
 'coins': '<circle cx="9" cy="9" r="7"/><path d="M15.9 7.2A7 7 0 1 1 7.2 15.9"/>',
 'search': '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
 'home': '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
 'cart': '<circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>',
}

def ico(name, size=36, cls=''):
    return ('<svg class="ic %s" width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
            % (cls, size, size, ICONS[name]))

# ---------------- Bausteine ----------------
def badge(label, icon=None):
    return '<div class="badge">%s<span>%s</span></div>' % (ico(icon, 26) if icon else '', label)

def top(label, icon, title, size='', lead=None):
    l = ('<p class="lead">%s</p>' % lead) if lead else ''
    return '<div class="top">%s<h1 class="%s">%s</h1>%s</div>' % (badge(label, icon), size, title, l)

CTAS = {
 'save': ('pin', 'Für später speichern'),
 'more': ('arrow-right', 'Mehr dazu auf ' + DOMAIN),
 'read': ('arrow-right', 'Die ganze Geschichte auf ' + DOMAIN),
}

def bot(cta='save'):
    ctah = ''
    left = '<b>%s</b>' % DOMAIN
    if cta:
        ic, t = CTAS[cta]
        ctah = '<div class="cta">%s<span>%s</span></div>' % (ico(ic, 26), t)
        if DOMAIN in t:
            left = '<div>Chris Alcatrez</div>'
    return '<div class="bot">%s<div class="pft">%s<div>%s</div></div></div>' % (ctah, left, HANDLE)

def wrap(theme, inner, style='', dots=True):
    cls = ' '.join(c for c in ('s', 'pin', theme, 'dots' if dots and theme != 'photo' else '') if c)
    return '<section class="%s" style="%s">%s</section>' % (cls, style, inner)

def vis(inner):
    return '<div class="vis">%s</div>' % inner

# ---------------- Visuelle Bloecke ----------------
def v_check(items, numbered=False, dense=False, quote=False):
    # items: [label] oder [(icon, label)]
    rows = ''
    for i, it in enumerate(items, 1):
        icon, label = (None, it) if isinstance(it, str) else it
        tile = ('<div class="tile num">%d</div>' % i) if (numbered or not icon) else ('<div class="tile">%s</div>' % ico(icon, 38))
        rows += '<div class="ck">%s<div class="cl%s">%s</div></div>' % (tile, ' q' if quote else '', label)
    return '<div class="checks%s">%s</div>' % (' dense' if dense else '', rows)

def v_flow(steps):
    h = ''
    for i, s in enumerate(steps, 1):
        if i > 1:
            h += '<div class="conn">%s</div>' % ico('arrow-down', 30)
        h += '<div class="step"><div class="sn">%d</div><div class="sl">%s</div></div>' % (i, s)
    return '<div class="flow">%s</div>' % h

def v_vs(top_head, top_rows, bottom_head, bottom_rows):
    a = ''.join('<div class="vr"><span class="vi x">%s</span><div>%s</div></div>' % (ico('x', 24), t) for t in top_rows)
    b = ''.join('<div class="vr"><span class="vi ok">%s</span><div>%s</div></div>' % (ico('check', 24), t) for t in bottom_rows)
    return '<div class="vs"><div class="vb"><div class="vh">%s</div>%s</div><div class="vb hl"><div class="vh">%s</div>%s</div></div>' % (top_head, a, bottom_head, b)

def v_phone(inner, wide=False):
    return '<div class="phone%s">%s</div>' % (' wide' if wide else '', inner)

def v_chat(bubbles):
    # bubbles: [(Absender, Text, ist_ich)]
    return ''.join('<div class="bub%s"><div class="bfrom">%s</div><div class="btext">%s</div></div>' % (' mine' if me else '', frm, t) for frm, t, me in bubbles)

def v_bars(rows, note=None, head=None):
    # rows: [(Beschriftung, Wert als Text, Prozent der Balkenbreite)]
    hd = ('<div class="bhead">%s</div>' % head) if head else ''
    h = hd + ''.join('<div class="bar"><div class="bl"><span>%s</span><b>%s</b></div><div class="bt"><div class="bf" style="width:%d%%"></div></div></div>' % (l, v, p) for l, v, p in rows)
    n = ('<div class="bnote">%s</div>' % note) if note else ''
    return '<div class="bars">%s</div>%s' % (h, n)

def v_term(rules):
    tiles = ''.join('<div class="wt"><span>%d</span>····</div>' % i for i in range(1, 13))
    return '<div class="termv"><div class="wgrid">%s</div>%s</div>' % (tiles, v_check(rules, dense=True))

def v_faq(answer, points):
    # points: [(icon, kurzer Punkt)] oder [Text] (dann Pills)
    if points and not isinstance(points[0], str):
        return '<div class="faq"><p class="ans">%s</p>%s</div>' % (answer, v_check(points))
    p = ''.join('<div class="pill%s">%s</div>' % (' hl' if i == 0 else '', t) for i, t in enumerate(points))
    return '<div class="faq"><p class="ans">%s</p><div class="pills">%s</div></div>' % (answer, p)

LINE = '14,118 86,58 158,96 230,30 302,112 374,70 446,132 518,46 590,100 662,66'
def _pts():
    return [tuple(map(int, p.split(','))) for p in LINE.split()]

def _y_at(x):
    pts = _pts()
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return pts[-1][1]

def _chart(kind):
    # Gleiche Kurve in beiden Karten: links Fragezeichen (raten, wann), rechts Punkte in festem Abstand (fester Tag,
    # egal wo der Kurs steht)
    base = '<polyline points="%s" fill="none" stroke="var(--pmeta)" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>' % LINE
    if kind == 'timing':
        marks = ''.join('<text x="%d" y="%d" font-family="Montserrat" font-weight="800" font-size="36" text-anchor="middle" fill="var(--pfg)">?</text>' % (x, y) for x, y in ((230, -2), (446, 174), (518, 32)))
        return '<svg class="chart" viewBox="0 -36 676 216" style="max-height:230px">%s%s</svg>' % (base, marks)
    dots = ''.join('<circle cx="%d" cy="%.1f" r="13" fill="var(--pacc)"/>' % (x, _y_at(x)) for x in (60, 180, 300, 420, 540, 660))
    return '<svg class="chart" viewBox="0 -36 676 216" style="max-height:230px">%s%s</svg>' % (base, dots)

def v_compare_chart(left_head, left_sub, right_head, right_sub):
    l = '<div class="cc"><div class="cch"><span class="vi x">%s</span>%s</div>%s<div class="ccs">%s</div></div>' % (ico('x', 22), left_head, _chart('timing'), left_sub)
    r = '<div class="cc hl"><div class="cch"><span class="vi ok">%s</span>%s</div>%s<div class="ccs">%s</div></div>' % (ico('check', 22), right_head, _chart('plan'), right_sub)
    return '<div class="cmp">%s%s</div>' % (l, r)

# ---------------- Vorlagen ----------------
def pin_check(label, icon, title, items, lead=None, numbered=False, dense=False, quote=False, cta='save', size='', theme=''):
    return lambda n, N: wrap(theme, top(label, icon, title, size, lead) + vis(v_check(items, numbered, dense, quote)) + bot(cta))

def pin_flow(label, icon, title, steps, lead=None, cta='more', size='', theme=''):
    return lambda n, N: wrap(theme, top(label, icon, title, size, lead) + vis(v_flow(steps)) + bot(cta))

def pin_vs(label, icon, title, top_head, top_rows, bottom_head, bottom_rows, lead=None, cta='save', size='sm', theme=''):
    return lambda n, N: wrap(theme, top(label, icon, title, size, lead) + vis(v_vs(top_head, top_rows, bottom_head, bottom_rows)) + bot(cta))

def pin_chat(label, icon, title, bubbles, lead=None, cta='save', size='sm', theme=''):
    return lambda n, N: wrap(theme, top(label, icon, title, size, lead) + vis(v_phone(v_chat(bubbles))) + bot(cta))

def pin_term(label, icon, term, definition, rules, cta='save', theme=''):
    return lambda n, N: wrap(theme, top(label, icon, term, 'big', definition) + vis(v_term(rules)) + bot(cta))

def pin_faq(label, icon, question, answer, pills, cta='save', size='big', theme=''):
    return lambda n, N: wrap(theme, top(label, icon, question, size) + vis(v_faq(answer, pills)) + bot(cta))

def pin_bars(label, icon, title, rows, note=None, lead=None, head=None, cta='more', size='', theme=''):
    return lambda n, N: wrap(theme, top(label, icon, title, size, lead) + vis(v_phone(v_bars(rows, note, head), wide=True)) + bot(cta))

def pin_compare_chart(label, icon, title, left_head, left_sub, right_head, right_sub, lead=None, cta='save', size='', theme=''):
    return lambda n, N: wrap(theme, top(label, icon, title, size, lead) + vis(v_compare_chart(left_head, left_sub, right_head, right_sub)) + bot(cta))

def pin_hero(label, icon, title, bignum=None, lead=None, cta='more', size='', theme=''):
    b = ('<div class="bignum">%s</div>' % bignum) if bignum else ''
    l = ('<p class="lead">%s</p>' % lead) if lead else ''
    return lambda n, N: wrap(theme, '<div class="top">%s</div>' % badge(label, icon) + vis('<div class="hero">%s<h1 class="%s">%s</h1>%s</div>' % (b, size, title, l)) + bot(cta))

def pin_photo(label, icon, title, lead=None, cta='more', size='', ebene=None):
    # Person unten aus der Fotoebene (Standard: pinterest/foto-ebene.png im Repository), Text oben; die Ebene endet in
    # Schwarz, bevor die Fusszeile beginnt. Hoechstens ein Foto-Pin pro Woche.
    eb = ebene or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'pinterest', 'foto-ebene.png')
    st = 'background-image:url(file://%s)' % eb
    return lambda n, N: wrap('photo', top(label, icon, title, size, lead) + vis('') + bot(cta), style=st, dots=False)


# ---------------- Stil 2 (ab 07.10.2026): eine Aussage, ein Visual, drei Punkte, ein CTA ----------------
def vz_num(big, sub=None):
    s = ('<div class="vz-sub">%s</div>' % sub) if sub else ''
    return '<div class="vz-num">%s</div>%s' % (big, s)

def vz_bubble(text, note=None):
    n = ('<div class="vz-note">%s</div>' % note) if note else ''
    return '<div class="vz-bub">%s</div>%s' % (text, n)

def vz_bars(rows, note=None):
    # rows: [(Beschriftung, Wert als Text, Prozent der Balkenbreite)]
    h = ''.join('<div class="vzb"><div class="l"><span>%s</span><b>%s</b></div><div class="t"><div class="f" style="width:%d%%"></div></div></div>' % (l, v, p) for l, v, p in rows)
    n = ('<div class="vz-note">%s</div>' % note) if note else ''
    return '<div class="vz-bars">%s</div>%s' % (h, n)

def vz_curve(sub=None, marks='dots'):
    # Eine grosse Kurve; marks='dots': Punkte in festem Abstand (Sparplan), 'x': ein Kreuz am Tiefpunkt (Panikverkauf)
    base = '<polyline points="%s" fill="none" stroke="var(--pfg2)" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>' % LINE
    if marks == 'dots':
        m = ''.join('<circle cx="%d" cy="%.1f" r="17" fill="var(--pacc)"/>' % (x, _y_at(x)) for x in (50, 170, 290, 410, 530, 650))
    else:
        x, y = 446, _y_at(446)
        m = '<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="var(--pacc)" stroke-width="9" stroke-linecap="round"/><line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="var(--pacc)" stroke-width="9" stroke-linecap="round"/>' % (x-22, y-22, x+22, y+22, x-22, y+22, x+22, y-22)
    s = ('<div class="vz-sub">%s</div>' % sub) if sub else ''
    return '<svg class="vz-curve" viewBox="0 -30 676 200">%s%s</svg>%s' % (base, m, s)

def vz_card(text, sub=None):
    s = ('<div class="vz-sub">%s</div>' % sub) if sub else ''
    return '<div class="vz-card">%s</div>%s' % (text, s)

def v2_points(points, marks='num', quote=False, start=1, dense=False):
    rows = ''
    for i, label in enumerate(points, start):
        if marks == 'check':
            mk = ico('check', 60, 'big')
        elif marks == 'x':
            mk = ico('x', 56, 'big')
        else:
            mk = str(i)
        rows += '<div class="pt"><div class="pn">%s</div><div class="pl%s">%s</div></div>' % (mk, ' q' if quote else '', label)
    return '<div class="pts%s">%s</div>' % (' dense' if dense else '', rows)

def v2_cta(text):
    return '<div class="ctabar"><span>%s</span><span class="h">%s</span></div>' % (text, HANDLE)

def pin2(theme, title, visual=None, points=(), cta='Für später speichern', size='', marks='num', quote=False, photo=False, center=False, start=1, dense=False):
    # Reihenfolge: Headline -> Visual -> Punkte -> CTA. Beim Foto-Pin: Headline -> Punkte -> Foto (unten) -> CTA.
    head = '<h1 class="%s">%s</h1>' % (size, title)
    pts = v2_points(points, marks, quote, start, dense) if points else ''
    if photo:
        eb = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'pinterest', 'foto-ebene.png')
        inner = head + pts + '<div class="viz"></div>' + v2_cta(cta)
        return lambda n, N: '<section class="s pin photo v2" style="background-image:url(file://%s)">%s</section>' % (eb, inner)
    inner = head + '<div class="viz%s">%s</div>' % (' center' if center else '', visual or '') + pts + v2_cta(cta)
    cls = ' '.join(c for c in ('s', 'pin', theme, 'v2') if c)
    return lambda n, N: '<section class="%s">%s</section>' % (cls, inner)

def build_pin(name, slides):
    return gen.build(name, slides, PW, PH)
