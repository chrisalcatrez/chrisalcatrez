# Beispiele nach Abschnitt 3a (Hook -> Retain -> Reward, Vorgabe vom 07.10.2026): Beitraege 17 bis 19.
# Aufbau je Karussell: Hook mit Zahl plus Konsequenz plus Luecke -> Beleg auf Folie 2 -> ein Punkt je Folie mit Sog-Zeile
# -> Merkzettel zum Speichern -> ein CTA. Aufruf wie beispiele.py; NM und OUT als Umgebungsvariablen setzen.
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen import *

A = lambda t: '<span class="acc">%s</span>' % t
D = lambda t: (t, 'dim')
TAGS = '#krypto #kryptowährung #kryptowährungen #bitcoindeutschland #bitcoinkaufen #bitcoinfüranfänger #kryptofüranfänger #kryptobetrug #anlagebetrug #onlinebetrug #betrugsmasche #kryptosicherheit #kryptowallet #finanzbildung #geldanlage #vermögensaufbau'
TRAINING = 'Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich dir im %s' % A('kostenlosen Training.')

POSTS = {}

# ---------- Beitrag 17: Schritt-fuer-Schritt (4 Fragen vor jedem Coin-Kauf) ----------
POSTS['beitrag-17'] = dict(
    date='2026-10-12', fmt='Schritt-für-Schritt-Anleitung', topic='Mein Vorgehen vor jedem Coin-Kauf: 4 Fragen (Influencer-Coin, 5.000 $, Rug Pull)',
    slides=[
        s_hook('SCHRITT FÜR SCHRITT', '5.000 $ für einen Coin, den ich keinem erklären konnte. %s stelle ich seitdem vor jedem Kauf.' % A('4 Fragen'),
               sub='Mein Vorgehen, bevor Geld fließt. Grob, der Rest im Training.', cue='Zuerst, was mich 5.000 $ gekostet hat &#8594;', size=''),
        s_proof('MEIN LEHRGELD', 'Ein Influencer-Coin. Bekanntes Gesicht, unbekanntes Team.',
                big='5.000 $', big_sub='weg, als die Macher ihre Coins auf einmal verkauften. Rug Pull.',
                cue='Die erste Frage hätte das verhindert &#8594;'),
        s_point('FRAGE 1', 'Wer hat den Coin gemacht?',
                ['Ein Name, ein Gesicht, ein Team, das antwortet.', D('Kein Team, kein Kauf. Ein Gesicht mit Reichweite zählt dafür null.')],
                cue='Frage 2 trennt Hype von Substanz &#8594;'),
        s_point('FRAGE 2', 'Wie viel halten die Macher selbst?',
                ['Halten sie den Großteil, gehört der Coin ihnen. Sie entscheiden, wann der Kurs fällt.', D('Beim Rug Pull verkaufen sie alles auf einmal. Die Käufer halten den Rest.')],
                cue='Frage 3 kostet dich 30 Sekunden &#8594;'),
        s_point('FRAGE 3', 'Welche Börse handelt ihn?',
                ['Eine Börse mit Namen, die ihn auch wieder zurücknimmt.', D('Ein Token, den keine Börse handelt, ist nur ein Name im Wallet-Bildschirm.')],
                cue='Die letzte Frage stelle ich mir selbst &#8594;'),
        s_point('FRAGE 4', 'Kann ich ihn in zwei Sätzen erklären?',
                ['Was er tut und warum ihn jemand braucht.', D('Bleibe ich stecken, bleibt das Geld, wo es ist.')],
                cue='Dein Merkzettel für den nächsten Kauf &#8594;'),
        s_memo('ZUM SPEICHERN', 'Die 4 Fragen, %s' % A('bevor Geld fließt.'), 'Dein Merkzettel', [
            'Wer hat den Coin gemacht? Name, Gesicht, Team.',
            'Wie viel halten die Macher selbst?',
            'Welche Börse handelt ihn?',
            'Kann ich ihn in zwei Sätzen erklären?',
        ], 'Speichere dir das für den nächsten Coin, den dir jemand empfiehlt.'),
        s_point('KOSTENLOSES TRAINING', TRAINING, ['Link in meiner Bio.'], meta=True, size='m'),
    ],
    alts=['Schritt für Schritt: 5.000 $ für einen Coin, den ich keinem erklären konnte. 4 Fragen stelle ich seitdem vor jedem Kauf',
          'Mein Lehrgeld: 5.000 $ weg, als die Macher eines Influencer-Coins ihre Coins auf einmal verkauften, Rug Pull',
          'Frage 1: Wer hat den Coin gemacht? Ein Name, ein Gesicht, ein Team, das antwortet. Kein Team, kein Kauf',
          'Frage 2: Wie viel halten die Macher selbst? Halten sie den Großteil, gehört der Coin ihnen',
          'Frage 3: Welche Börse handelt ihn? Ein Token ohne Börse ist nur ein Name im Wallet-Bildschirm',
          'Frage 4: Kann ich ihn in zwei Sätzen erklären? Bleibe ich stecken, bleibt das Geld, wo es ist',
          'Merkzettel, die 4 Fragen, bevor Geld fließt: Wer hat den Coin gemacht, wie viel halten die Macher, welche Börse handelt ihn, kann ich ihn erklären. Speichere dir das',
          'Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich dir im kostenlosen Training, Link in meiner Bio'],
    caption='''Ein bekanntes Gesicht hat mich 5.000 $ gekostet. Heute stelle ich vier Fragen, bevor ich einen Coin kaufe.

Der Coin kam von einem Influencer. Ich hab gekauft, ohne zu wissen, wer dahintersteht und wie viel die Macher selbst halten. Dann verkauften sie alles auf einmal, der Kurs fiel senkrecht, die Käufer hielten den Rest. Rug Pull heißt das.

Mein Vorgehen seitdem, grob:
1. Wer hat den Coin gemacht? Name, Gesicht, ein Team, das antwortet. Kein Team, kein Kauf.
2. Wie viel halten die Macher selbst? Halten sie den Großteil, gehört der Coin ihnen.
3. Welche Börse handelt ihn? Ein Token ohne Börse ist nur ein Name im Wallet-Bildschirm.
4. Kann ich ihn in zwei Sätzen erklären? Bleibe ich stecken, bleibt das Geld, wo es ist.

Vier Fragen, 5.000 $ billiger als meine Version. Wie das in mein System aus vier Schritten passt, zeige ich im Training.

Für alle, die mit Krypto und Bitcoin anfangen und gerade einen Coin empfohlen bekommen haben.

Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich dir im kostenlosen Training. Link in meiner Bio.''')

# ---------- Beitrag 18: FAQ (zu spaet fuer Bitcoin?) ----------
POSTS['beitrag-18'] = dict(
    date='2026-10-13', fmt='FAQ beantworten', topic='FAQ: „Zu spät für Bitcoin?“ (Panikverkauf Ende 2024, Sparplan statt Timing)',
    slides=[
        s_hook('FAQ', '„Zu spät für Bitcoin?“ Die Frage hat mich Ende 2024 %s' % A('alle Bitcoin gekostet.'),
               sub='Was ich Anfängern heute darauf antworte.', cue='Zuerst, was damals passierte &#8594;', size=''),
        s_proof('WAS PASSIERTE', 'Ich wollte den perfekten Moment treffen und traf den schlechtesten.',
                big='Ende 2024', big_sub='alle Bitcoin verkauft. In Panik, auf der Suche nach dem richtigen Zeitpunkt.',
                cue='Der Haken an der Frage &#8594;'),
        s_point('DER HAKEN', 'Zu spät war ich nie. %s' % A('Zu hastig schon.'),
                ['Die Frage „zu spät?“ sucht einen Moment. Der Markt kennt keinen.', D('Wer auf den richtigen Tag wartet, kauft oder verkauft in Panik. Bei mir war es der Verkauf.')],
                size='m', cue='Was ich stattdessen mache &#8594;'),
        s_point('MEINE ANTWORT', 'Sparplan statt Timing.',
                ['Ein fester Tag, eine feste Summe. Der Kurs entscheidet nie.', D('Keine Kursprognose, keine Gewinnzusage. Meine Erfahrung nach 70.000 $ Lehrgeld.')],
                cue='Dazu zwei Regeln für den Anfang &#8594;'),
        s_point('ZWEI REGELN', 'Klein anfangen. %s' % A('Verstehen, was du kaufst.'),
                ['Mit 100 € siehst du denselben Kurs wie mit 10.000 €. Nur billiger.', D('Jeder Kauf, den du erklären kannst, hält Panik aus.')],
                size='m', cue='Dein Merkzettel &#8594;'),
        s_memo('ZUM SPEICHERN', 'Die Antwort auf „zu spät?“ %s' % A('in 4 Zeilen.'), 'Dein Merkzettel', [
            'Es gibt keinen richtigen Tag. Nur einen festen.',
            'Fester Tag, feste Summe, egal wo der Kurs steht.',
            'Klein anfangen, bis du verstehst, was du kaufst.',
            'Panik verkauft immer zum schlechtesten Zeitpunkt.',
        ], 'Speichere dir das, bevor der nächste Kurs-Alarm kommt.'),
        s_point('KOSTENLOSES TRAINING', TRAINING, ['Link in meiner Bio.'], meta=True, size='m'),
    ],
    alts=['FAQ: Zu spät für Bitcoin? Die Frage hat mich Ende 2024 alle Bitcoin gekostet. Was ich Anfängern heute darauf antworte',
          'Was passierte: Ende 2024 alle Bitcoin verkauft, in Panik, auf der Suche nach dem richtigen Zeitpunkt',
          'Der Haken: Zu spät war ich nie, zu hastig schon. Die Frage sucht einen Moment, der Markt kennt keinen',
          'Meine Antwort: Sparplan statt Timing. Ein fester Tag, eine feste Summe, der Kurs entscheidet nie. Keine Kursprognose, keine Gewinnzusage',
          'Zwei Regeln: Klein anfangen, verstehen, was du kaufst. Mit 100 Euro siehst du denselben Kurs wie mit 10.000 Euro',
          'Merkzettel, die Antwort auf zu spät in vier Zeilen: kein richtiger Tag, nur ein fester; fester Tag, feste Summe; klein anfangen; Panik verkauft zum schlechtesten Zeitpunkt',
          'Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich dir im kostenlosen Training, Link in meiner Bio'],
    caption='''„Ist es zu spät für Bitcoin?“ Die Frage bekomme ich am häufigsten. Ich hab sie mir selbst gestellt, und sie hat mich Ende 2024 alle Bitcoin gekostet.

Ich wollte den perfekten Moment treffen. Stattdessen hab ich in Panik verkauft, zum schlechtesten Zeitpunkt, den ich mir hätte aussuchen können.

Zu spät war ich nie. Zu hastig schon. Die Frage „zu spät?“ sucht einen Moment, den der Markt gar kennt. Wer auf den richtigen Tag wartet, handelt irgendwann aus dem Bauch.

Was ich heute anders mache:
– Sparplan statt Timing: ein fester Tag, eine feste Summe. Der Kurs entscheidet nie.
– Klein anfangen: Mit 100 € siehst du denselben Kurs wie mit 10.000 €. Nur billiger.
– Verstehen, was du kaufst: Jeder Kauf, den du erklären kannst, hält Panik aus.

Keine Kursprognose, keine Gewinnzusage. Meine Erfahrung nach 70.000 $ Lehrgeld.

Für alle, die mit Bitcoin anfangen wollen und seit Monaten auf den richtigen Moment warten.

Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich dir im kostenlosen Training. Link in meiner Bio.''')

# ---------- Beitrag 19: Aufzaehlung (4 echte Gebuehren, eine falsche) ----------
POSTS['beitrag-19'] = dict(
    date='2026-10-14', fmt='Aufzählung', topic='4 Gebühren sind echt, die 5. ist immer Betrug (Netzwerkgebühr vor der Auszahlung)',
    slides=[
        s_hook('AUFZÄHLUNG', 'Eine „Netzwerkgebühr“ hat mich meine Auszahlung gekostet. 4 Gebühren sind echt, %s' % A('die 5. ist immer Betrug.'),
               sub='So unterscheidest du sie in 10 Sekunden.', cue='Zuerst die Nachricht, die mich erwischt hat &#8594;', size=''),
        s_proof('MEIN FALL', 'Über Instagram, kurz vor der „Auszahlung“.',
                quote='„Ihre Auszahlung ist freigegeben. Es fehlt nur die Netzwerkgebühr.“', quote_from='Nachgestellt, so kam es bei mir',
                ps=[D('Ich hab gezahlt. Die Auszahlung kam nie.')], cue='Echte Gebühren sehen anders aus &#8594;'),
        s_point('ECHT: 1 UND 2', 'Handelsgebühr und Spread.',
                ['Die Börse nimmt bei jedem Kauf einen kleinen Anteil. Er wird vom Betrag abgezogen.', D('Der Spread ist der Abstand zwischen Kauf- und Verkaufskurs. Auch der wird nie vorab verlangt.')],
                size='m', cue='Jetzt die zwei, die Betrüger nachbauen &#8594;'),
        s_point('ECHT: 3 UND 4', 'Netzwerkgebühr beim Versand. Auszahlungsgebühr.',
                ['Beide gibt es wirklich. Beide werden vom Betrag abgezogen, den du schickst.', D('Du überweist sie nie an eine Person. Genau das nutzt die Masche aus.')],
                size='m', cue='Und genau diesen Fehlgriff machen fast alle &#8594;'),
        s_point('BETRUG: 5', 'Eine Gebühr, %s' % A('bevor du dein Geld bekommst.'),
                ['Vorkasse auf die eigene Auszahlung gibt es bei keiner echten Börse.', D('Wer sie verlangt, hat nie vor zu zahlen. Egal, wie das Wort heißt.')],
                size='m', cue='Dein 10-Sekunden-Test &#8594;'),
        s_memo('ZUM SPEICHERN', 'Der Gebühren-Test, %s' % A('bevor du überweist.'), 'Dein Merkzettel', [
            'Echte Gebühr: wird vom Betrag abgezogen.',
            'Falsche Gebühr: du sollst sie vorab überweisen.',
            'Eine Gebühr, die zweimal fällig wird, ist keine Gebühr.',
            'Steht „Netzwerkgebühr“ im Chat statt in der App: Betrug.',
        ], 'Speichere dir das, bevor die nächste „Auszahlung“ auf dich wartet.'),
    ],
    alts=['Aufzählung: Eine Netzwerkgebühr hat mich meine Auszahlung gekostet. 4 Gebühren sind echt, die 5. ist immer Betrug',
          'Mein Fall, nachgestellt: Ihre Auszahlung ist freigegeben, es fehlt nur die Netzwerkgebühr. Ich hab gezahlt, die Auszahlung kam nie',
          'Echt 1 und 2: Handelsgebühr und Spread, beide werden vom Betrag abgezogen, nie vorab verlangt',
          'Echt 3 und 4: Netzwerkgebühr beim Versand und Auszahlungsgebühr, beide werden vom Betrag abgezogen, nie an eine Person überwiesen',
          'Betrug 5: Eine Gebühr, bevor du dein Geld bekommst. Vorkasse auf die eigene Auszahlung gibt es bei keiner echten Börse',
          'Merkzettel, der Gebühren-Test: echte Gebühr wird abgezogen, falsche Gebühr sollst du vorab überweisen, eine Gebühr, die zweimal fällig wird, ist keine Gebühr. Speichere dir das'],
    caption='''Vier Gebühren sind bei Krypto normal. Die fünfte hat mich meine Auszahlung gekostet.

Die Nachricht kam damals über Instagram: „Ihre Auszahlung ist freigegeben. Es fehlt nur die Netzwerkgebühr.“ Ich hab gezahlt. Die Auszahlung kam nie. Das Wort war echt, die Gebühr war erfunden.

Die vier echten Gebühren, die jeder Krypto-Anfänger kennt:
1. Handelsgebühr: Die Börse nimmt bei jedem Kauf einen kleinen Anteil, abgezogen vom Betrag.
2. Spread: der Abstand zwischen Kauf- und Verkaufskurs.
3. Netzwerkgebühr beim Versand: wird vom Betrag abgezogen, den du schickst.
4. Auszahlungsgebühr: zieht die Börse ab, bevor das Geld bei dir landet.

Die fünfte, immer Betrug:
5. Eine Gebühr, die du vorab überweisen sollst, damit du dein Geld bekommst. Vorkasse auf die eigene Auszahlung gibt es bei keiner echten Börse.

Der Test in 10 Sekunden: Wird die Gebühr abgezogen, ist sie echt. Sollst du sie vorab an jemanden überweisen, ist es Betrug. Egal, wie das Wort heißt.

Welche Gebühr wurde dir schon mal vorab abverlangt? Schreib es in die Kommentare.

Für alle, die mit Krypto und Bitcoin anfangen und die erste Auszahlung vor sich haben.

Speichere dir das, bevor die nächste „Auszahlung“ auf dich wartet.''')

if __name__ == '__main__':
    which = sys.argv[1:] or list(POSTS)
    allpng = {}
    ok_all = True
    for name in which:
        p = POSTS[name]
        ok = check_text(name + ' Caption', p['caption']) and all(check_text(name + ' Alt', a) for a in p['alts'])
        ok_all = ok_all and ok
        assert len(p['alts']) == len(p['slides']), name + ': Zahl der Alt-Texte weicht ab'
        allpng[name] = build(name, p['slides'])
    json.dump(allpng, open(os.path.join(OUT, 'pngs.json'), 'w'), indent=1)
    print('Texte sauber:', ok_all)
