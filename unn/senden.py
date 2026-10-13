import json, os, time, urllib.request
from datetime import datetime, timezone
TOKEN = os.environ["TELEGRAM_TOKEN"]; KANAL = "@unabhaengig_neutral"; MAX_MIN = 180
liste = json.load(open("unn/warteschlange.json", encoding="utf-8"))
pfad = "unn/gesendet.json"
gesendet = set(json.load(open(pfad)) if os.path.exists(pfad) else [])
def tg(methode, daten):
    req = urllib.request.Request(f"https://api.telegram.org/bot{TOKEN}/{methode}", json.dumps(daten).encode(), {"Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=30))
    except urllib.error.HTTPError as e:
        return json.load(e)
jetzt = datetime.now(timezone.utc)
for p in liste:
    if p["id"] in gesendet: continue
    alter = (jetzt - datetime.fromisoformat(p["zeit"].replace("Z", "+00:00"))).total_seconds() / 60
    if alter > MAX_MIN: gesendet.add(p["id"]); continue
    text = p["text"] + "\n\n@unabhaengig_neutral"
    bilder = p.get("bilder") or ([p["bild"]] if p.get("bild") else [])
    if len(bilder) > 1:
        media = [{"type": "photo", "media": u} for u in bilder[:10]]
        media[0].update({"caption": text, "parse_mode": "HTML"})
        r = tg("sendMediaGroup", {"chat_id": KANAL, "media": media})
        if not r.get("ok"): r = tg("sendPhoto", {"chat_id": KANAL, "photo": bilder[0], "caption": text, "parse_mode": "HTML"})
    elif bilder:
        r = tg("sendPhoto", {"chat_id": KANAL, "photo": bilder[0], "caption": text, "parse_mode": "HTML"})
        if not r.get("ok"): r = tg("sendMessage", {"chat_id": KANAL, "text": text, "parse_mode": "HTML", "link_preview_options": {"is_disabled": True}})
    else:
        r = tg("sendMessage", {"chat_id": KANAL, "text": text, "parse_mode": "HTML", "link_preview_options": {"is_disabled": True}})
    print(p["id"], "gesendet" if r.get("ok") else r)
    if r.get("ok"): gesendet.add(p["id"])
    time.sleep(4)
json.dump(sorted(gesendet)[-1000:], open(pfad, "w"))
