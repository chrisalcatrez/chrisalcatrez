# B-Roll-Reel (1080x1920) aus eigenen Clips und Fotos: schneiden, leicht entrauschen, Farben angleichen,
# Texte im Markenlook (Montserrat, Akzent #ffab00, schwarze Textbox) einblenden, ruhige Tonspur darunterlegen.
# Nutzung: NM=<node_modules mit @fontsource/montserrat und playwright> python3 tools/reel_broll.py plan.json ausgabe.mp4
# plan.json: {"segments": [{"src": "...", "start": 0, "dur": 2, "text": "…", "pos": "center|top|bottom", "cropx": null,
#              "photo": false, "zoom": [1.0, 1.12], "focus": [0.5, 0.6], "crop_rel": [x0, y0, x1, y1]}], "audio": "wellen|stumm"}
# Texte duerfen <b>…</b> fuer die Akzentfarbe enthalten. Sichere Zone: oben 250 px, unten 420 px, rechts 150 px frei.
import json, os, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen

W, H, FPS = 1080, 1920, 30
POS_Y = {'top': 470, 'center': 860, 'bottom': 1330}

def probe(src):
    j = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-print_format', 'json', '-show_streams', src],
                                  capture_output=True, text=True).stdout)
    v = next(s for s in j['streams'] if s['codec_type'] == 'video')
    w, h = v['width'], v['height']
    rot = 0
    for sd in v.get('side_data_list', []) or []:
        rot = sd.get('rotation', rot)
    if abs(int(rot)) in (90, 270):
        w, h = h, w
    return w, h

def text_png(html_text, pos, out, tmp):
    m = gen.NM + '/@fontsource/montserrat/files/montserrat-latin-%s-normal.woff2'
    fonts = ''.join("@font-face{font-family:'Montserrat';font-weight:%s;src:url(file://%s)}" % (w, m % w) for w in ('800', '900'))
    page = """<!doctype html><html><head><meta charset="utf-8"><style>%s
html,body{margin:0;background:transparent}
.s{position:relative;width:1080px;height:1920px}
.t{position:absolute;left:80px;width:850px;top:%dpx;transform:translateY(-50%%);text-align:center;font-family:'Montserrat';font-weight:800;font-size:62px;line-height:1.52;color:#F5F5F0}
.t span{background:rgba(0,0,0,.74);padding:8px 20px;border-radius:14px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.t b{color:#ffab00;font-weight:800}
</style></head><body><div class="s"><div class="t"><span>%s</span></div></div></body></html>""" % (fonts, POS_Y[pos], html_text)
    hp = os.path.join(tmp, os.path.basename(out) + '.html')
    open(hp, 'w', encoding='utf-8').write(page)
    js = os.path.join(tmp, 'txt.js')
    open(js, 'w').write("""const {chromium}=require('%s/playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.argv[2]);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(100);
const r=await p.evaluate(()=>{const q=document.querySelector('.t span').getBoundingClientRect();return [Math.round(q.top),Math.round(q.bottom),Math.round(q.left),Math.round(q.right),document.fonts.check('800 62px Montserrat')]});
console.log(JSON.stringify(r));await p.screenshot({path:process.argv[3],omitBackground:true});await b.close()})();""" % gen.NM)
    r = subprocess.run(['node', js, hp, out], capture_output=True, text=True)
    return json.loads(r.stdout.strip() or '[]')

def photo_frames(seg, tmp, idx):
    from PIL import Image, ImageOps
    try:
        from pillow_heif import register_heif_opener
        register_heif_opener()
    except ImportError:
        pass
    im = ImageOps.exif_transpose(Image.open(seg['src']).convert('RGB'))
    if seg.get('crop_rel'):
        x0, y0, x1, y1 = seg['crop_rel']
        im = im.crop((int(im.width * x0), int(im.height * y0), int(im.width * x1), int(im.height * y1)))
    # auf 9:16 zuschneiden
    tw = min(im.width, int(im.height * 9 / 16)); th = int(tw * 16 / 9)
    fx, fy = seg.get('focus', [0.5, 0.5])
    cx = min(max(int(im.width * fx), tw // 2), im.width - tw // 2); cy = min(max(int(im.height * fy), th // 2), im.height - th // 2)
    base = im.crop((cx - tw // 2, cy - th // 2, cx + tw // 2, cy + th // 2)).resize((W * 2, H * 2), Image.LANCZOS)
    z0, z1 = seg.get('zoom', [1.0, 1.1])
    n = int(round(seg['dur'] * FPS)); d = os.path.join(tmp, 'ph%02d' % idx); os.makedirs(d, exist_ok=True)
    for i in range(n):
        t = i / max(n - 1, 1); t = t * t * (3 - 2 * t)
        z = z0 + (z1 - z0) * t
        cw, ch = int(W * 2 / z), int(H * 2 / z)
        l = int((W * 2 - cw) * fx); tp = int((H * 2 - ch) * fy)
        base.crop((l, tp, l + cw, tp + ch)).resize((W, H), Image.LANCZOS).save(os.path.join(d, 'f%04d.png' % i))
    return os.path.join(d, 'f%04d.png'), n

def build_segment(seg, idx, tmp):
    out = os.path.join(tmp, 'seg%02d.mp4' % idx)
    grade = 'eq=contrast=1.04:saturation=1.08'
    txt = None
    if seg.get('text'):
        txt = os.path.join(tmp, 'txt%02d.png' % idx)
        seg['_box'] = text_png(seg['text'], seg.get('pos', 'center'), txt, tmp)
    if seg.get('photo'):
        pattern, n = photo_frames(seg, tmp, idx)
        inp = ['-framerate', str(FPS), '-i', pattern]
        vf = '[0:v]%s,format=yuv420p,setsar=1[v0]' % grade
    else:
        w, h = probe(seg['src'])
        s = H / h
        sw = int(round(w * s / 2) * 2)
        chain = []
        den = 'hqdn3d=3:2.5:6:5' if h < 1500 else 'hqdn3d=1.6:1.3:4:3'
        chain.append(den)
        chain.append('scale=%d:%d:flags=lanczos' % (sw, H))
        if sw > W:
            cx = seg.get('cropx')
            cx = (sw - W) // 2 if cx is None else int(cx * s)
            chain.append('crop=%d:%d:%d:0' % (W, H, max(0, min(cx, sw - W))))
        elif sw < W:
            chain.append('scale=%d:%d:flags=lanczos,crop=%d:%d' % (W, int(round(H * W / sw / 2) * 2), W, H))
        if h < 1500:
            chain.append('unsharp=5:5:0.35')
        chain += ['fps=%d' % FPS, grade, 'format=yuv420p', 'setsar=1']
        inp = ['-ss', str(seg['start']), '-t', str(seg['dur']), '-i', seg['src']]
        vf = '[0:v]%s[v0]' % ','.join(chain)
    if txt:
        inp += ['-loop', '1', '-t', str(seg['dur']), '-i', txt]
        vf += ';[1:v]format=rgba,fade=in:st=0:d=0.15:alpha=1[t];[v0][t]overlay=0:0:format=auto[v]'
    else:
        vf += ';[v0]null[v]'
    cmd = ['ffmpeg', '-v', 'error', '-y'] + inp + ['-filter_complex', vf, '-map', '[v]', '-t', str(seg['dur']), '-an',
                                                  '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', str(FPS), out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit('Segment %d: %s' % (idx, r.stderr[-800:]))
    return out

def audio_bed(total, out):
    # ruhiges Meeresrauschen aus gefiltertem Rauschen, langsame Wellen, weich ein- und ausgeblendet
    af = ("anoisesrc=color=pink:amplitude=0.6:seed=7:d=%.2f,lowpass=f=950,highpass=f=70,"
          "volume='0.30+0.22*sin(2*PI*t/6.3)+0.10*sin(2*PI*t/2.7+1.3)':eval=frame,"
          "afade=t=in:st=0:d=1.2,afade=t=out:st=%.2f:d=1.6,aformat=sample_rates=48000:channel_layouts=stereo,"
          "loudnorm=I=-22:TP=-2:LRA=11") % (total, max(0, total - 1.6))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', af, '-c:a', 'aac', '-b:a', '128k', out], check=True)

def main():
    plan = json.load(open(sys.argv[1], encoding='utf-8')); out = sys.argv[2]
    for s in plan['segments']:
        if s.get('text'):
            gen.check_text('Reel-Text', s['text'])
    tmp = tempfile.mkdtemp()
    segs = [build_segment(s, i, tmp) for i, s in enumerate(plan['segments'])]
    lst = os.path.join(tmp, 'list.txt')
    open(lst, 'w').write(''.join("file '%s'\n" % p for p in segs))
    total = sum(float(s['dur']) for s in plan['segments'])
    video = os.path.join(tmp, 'video.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c:v', 'libx264', '-preset', 'slow', '-crf', str(plan.get('crf', 20)),
                    '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an', video], check=True)
    if plan.get('audio', 'wellen') == 'wellen':
        a = os.path.join(tmp, 'bed.m4a'); audio_bed(total, a)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', video, '-i', a, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'copy',
                        '-shortest', '-map_metadata', '-1', '-movflags', '+faststart', out], check=True)
    else:
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', video, '-c', 'copy', '-map_metadata', '-1', '-movflags', '+faststart', out], check=True)
    print(json.dumps({'ausgabe': out, 'dauer_s': round(total, 2), 'segmente': len(segs),
                      'textboxen': [s.get('_box') for s in plan['segments']]}, ensure_ascii=False))

if __name__ == '__main__':
    main()
