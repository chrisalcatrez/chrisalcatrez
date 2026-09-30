# Fotoebene fuer Pinterest-Pins (1000x1500): freigestellte Person unten, warmes Licht hinter dem Kopf,
# Uebergang in Schwarz nach unten (Fussbereich bleibt schwarz, die Uhr liegt ausserhalb der Leinwand).
import sys, json
import numpy as np, cv2
from PIL import Image
W, H = 1000, 1500
P = dict(S=1.32, head_top_o=93, chin_o=320, head_cx_o=410,
         head_top_c=850, head_cx_c=580,
         fade_b0=1235, fade_b1=1400,
         glow=0.17, glow_r=330, contrast=1.08, sharpen=0.25, grain=0.012, denoise=3, burn=0.16)
if len(sys.argv) > 2: P.update(json.loads(sys.argv[2]))
out = sys.argv[1]
def smooth(a, b, x):
    t = np.clip((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t)
# Quelle: Foto (880x1184) und Maske (rembg) liegen ausserhalb des Repositorys; Pfad als Umgebungsvariable FOTO_DIR
import os
SC=os.environ.get('FOTO_DIR', '.').rstrip('/') + '/'
im8 = np.asarray(Image.open(SC+'foto.jpg').convert('RGB'))
im8 = cv2.fastNlMeansDenoisingColored(im8, None, P['denoise'], P['denoise'], 7, 21)
im = im8.astype(np.float32) / 255
mk = np.asarray(Image.open(SC+'mask.png').convert('L')).astype(np.float32) / 255
S = P['S']
M = np.float32([[S, 0, P['head_cx_c'] - P['head_cx_o'] * S], [0, S, P['head_top_c'] - P['head_top_o'] * S]])
warp = lambda a, f=cv2.INTER_LANCZOS4: cv2.warpAffine(a, M, (W, H), flags=f, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
photo = np.clip(warp(im), 0, 1)
valid = np.clip(warp(np.ones(mk.shape, np.float32), cv2.INTER_LINEAR), 0, 1)
mask = cv2.GaussianBlur(np.clip(warp(mk, cv2.INTER_LINEAR), 0, 1), (0, 0), 0.9)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
hy = P['head_top_c'] + (P['chin_o'] - P['head_top_o']) * S * 0.55
d = np.sqrt((xx - P['head_cx_c']) ** 2 + ((yy - hy) * 1.1) ** 2)
glow = np.exp(-(d / P['glow_r']) ** 2) * P['glow']
bg = np.zeros((H, W, 3), np.float32) + glow[..., None] * np.float32([1.0, 0.67, 0.0])
stripes = (np.sin((xx + yy) * 0.35) * 0.5 + 0.5) * 0.012
bg += stripes[..., None]
bg += np.random.default_rng(3).normal(0, P['grain'], (H, W, 1)).astype(np.float32)
# Glow oben (Textbereich) daempfen, damit der Text auf Schwarz steht
bg *= (1 - 0.85 * (1 - smooth(720, 900, yy)))[..., None]
bg = np.clip(bg, 0, 1)
sj = np.clip((photo - 0.5) * P['contrast'] + 0.5 + 0.01, 0, 1)
sj = np.clip(sj + P['sharpen'] * (sj - cv2.GaussianBlur(sj, (0, 0), 1.6)), 0, 1)
chin = P['head_top_c'] + (P['chin_o'] - P['head_top_o']) * S
sj *= (1 - P['burn'] * smooth(chin + 20, chin + 260, yy))[..., None]
f = (1 - smooth(P['fade_b0'], P['fade_b1'], yy)) ** 1.2
a = (mask * valid * f)[..., None]
o = bg * (1 - a) + sj * a
Image.fromarray((np.clip(o, 0, 1) * 255 + 0.5).astype(np.uint8)).save(out)
uhr = P['head_top_c'] + (700 - P['head_top_o']) * S
print(json.dumps({'kinn_y': round(chin), 'uhr_y': round(uhr), 'kopf_ab_y': P['head_top_c'], 'schwarz_ab_y': P['fade_b1']}))
