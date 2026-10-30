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

Zu spät war ich nie. Zu hastig schon. Die Frage „zu spät?“ sucht einen Moment. Der Markt kennt keinen. Wer auf den richtigen Tag wartet, handelt irgendwann aus dem Bauch.

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

# ---------- Beitrag 20: Statement-Karussell (Geldentwertung: Sparkonto verliert ohne Kurssturz) ----------
Q_DESTATIS = 'Quelle: Statistisches Bundesamt, Verbraucherpreisindex 2020 = 100, Jahresdurchschnitt 2025'
Q_IWF = 'Quelle: IWF, World Economic Outlook, Oktober 2026'
POSTS['beitrag-20'] = dict(
    date='2026-10-17', fmt='Statement-Karussell', topic='Geldentwertung: 100 € von 2020 kaufen heute für 82 €, das Sparkonto verliert ohne Kurssturz (Blick aus Venezuela)',
    slides=[
        s_hook('STATEMENT', '100 € von 2020 kaufen heute Waren für 82 €. %s' % A('Ohne einen einzigen Kurssturz.'),
               sub='Das Sparkonto ist die einzige Anlage, bei der der Verlust feststeht. Meine Sicht aus Venezuela.',
               cue='Was ich hier jeden Tag sehe &#8594;', size=''),
        s_proof('WO ICH LEBE', 'Ich lebe in Venezuela.',
                big='468 %', big_sub='Inflation rechnet der IWF hier für 2026. Die höchste in Lateinamerika.',
                src=Q_IWF, cue='Was das mit Erspartem macht &#8594;'),
        s_point('WAS ICH HIER SEHE', 'Die Zahl auf dem Konto bleibt. Was sie kauft, geht.',
                ['Keiner hat beschlossen, dass Erspartes weniger wert wird. Es kam Preis für Preis.',
                 D('Krypto ist hier Alltag. Aus Not, aus keinem Hype.')],
                cue='Deutschland in Zeitlupe &#8594;'),
        s_point('DEUTSCHLAND IN ZEITLUPE', 'Rund 22 % teurer seit 2020.',
                ['Der Verbraucherpreisindex stieg von 100 im Jahr 2020 auf rund 122 im Jahr 2025.',
                 D('Für 100 € von damals bekommst du heute Waren für rund 82 €. Ohne Kurssturz, ohne Betrug, ohne Schlagzeile.')],
                src=Q_DESTATIS, cue='Heißt das: alles in Krypto? &#8594;'),
        s_point('HEISST DAS: ALLES IN KRYPTO?', 'Nein. Es heißt: %s' % A('Stillstand ist auch eine Entscheidung.'),
                ['Krypto schwankt, jeden Tag. Wer das aushält, braucht einen Plan, Verständnis und kleine Beträge.',
                 D('Das Sparkonto schwankt nie. Es verliert nur leise. Welche Seite du wählst, entscheidest du.')],
                size='m', cue='Dein Merkzettel &#8594;'),
        s_memo('ZUM SPEICHERN', 'Vier Sätze %s' % A('über Erspartes.'), 'Dein Merkzettel', [
            'Null Schwankung heißt null Risiko? Nein. Es heißt Verlust ohne Kurve.',
            'Rund 22 % teurer seit 2020: 100 € von damals kaufen heute für 82 €.',
            'Niemand beschließt Geldentwertung. Sie kommt Preis für Preis.',
            'Krypto schwankt. Wer einsteigt, braucht Plan, Verständnis und kleine Beträge.',
        ], 'Schick das jemandem, der sein Erspartes seit Jahren auf dem Sparkonto parkt.'),
    ],
    alts=['Statement: 100 Euro von 2020 kaufen heute Waren für 82 Euro, ohne einen einzigen Kurssturz. Das Sparkonto ist die einzige Anlage, bei der der Verlust feststeht. Meine Sicht aus Venezuela',
          'Wo ich lebe: Ich lebe in Venezuela. 468 Prozent Inflation rechnet der IWF hier für 2026, die höchste in Lateinamerika. Quelle: IWF, World Economic Outlook, Oktober 2026',
          'Was ich hier sehe: Die Zahl auf dem Konto bleibt, was sie kauft, geht. Keiner hat beschlossen, dass Erspartes weniger wert wird, es kam Preis für Preis. Krypto ist hier Alltag, aus Not',
          'Deutschland in Zeitlupe: Rund 22 Prozent teurer seit 2020. Der Verbraucherpreisindex stieg von 100 im Jahr 2020 auf rund 122 im Jahr 2025. Für 100 Euro von damals bekommst du heute Waren für rund 82 Euro. Quelle: Statistisches Bundesamt',
          'Heißt das, alles in Krypto? Nein. Es heißt: Stillstand ist auch eine Entscheidung. Krypto schwankt, wer das aushält, braucht Plan, Verständnis und kleine Beträge. Das Sparkonto schwankt nie, es verliert nur leise',
          'Merkzettel, vier Sätze über Erspartes: Null Schwankung heißt Verlust ohne Kurve; rund 22 Prozent teurer seit 2020; niemand beschließt Geldentwertung, sie kommt Preis für Preis; Krypto schwankt, wer einsteigt, braucht Plan und kleine Beträge. Schick das jemandem, der sein Erspartes seit Jahren auf dem Sparkonto parkt'],
    caption='''Ich wohne in dem Land mit der höchsten Inflation Lateinamerikas. Dein Sparkonto macht dasselbe, nur leiser.

Der IWF rechnet für Venezuela 2026 mit rund 468 % Inflation (Quelle: IWF, World Economic Outlook, Oktober 2026). Ich lebe hier. Was ich jeden Tag sehe: Die Zahl auf dem Konto bleibt gleich. Was sie kauft, wird weniger. Keiner hat das beschlossen. Es kam Preis für Preis. Krypto ist hier Alltag, aus Not, aus keinem Hype.

Deutschland läuft dieselbe Strecke, nur in Zeitlupe:
– Der Verbraucherpreisindex stieg von 100 im Jahr 2020 auf rund 122 im Jahr 2025 (Quelle: Statistisches Bundesamt, Jahresdurchschnitt 2025).
– Für 100 € von 2020 bekommst du heute Waren für rund 82 €.
– Ohne Kurssturz, ohne Betrug, ohne Schlagzeile.

Heißt das, alles in Krypto? Nein. Krypto schwankt, jeden Tag. Wer das aushält, braucht einen Plan, Verständnis für das, was er kauft, und kleine Beträge. Das Sparkonto schwankt nie. Es verliert nur leise. Welche Seite du wählst, entscheidest du. Keine Kursprognose, keine Gewinnzusage, nur das, was ich hier sehe.

Für alle, die als Anfänger über Bitcoin und Krypto nachdenken und sich um ihr Erspartes sorgen.

Wie viele Jahre liegt dein Erspartes schon auf dem Sparkonto? Schreib die Zahl in die Kommentare.

Schick das jemandem, der sein Erspartes seit Jahren auf dem Sparkonto parkt.''')

# ---------- Beitrag 21: Gegenueberstellung (Vorurteil vs. Wahrheit: Bezahlen mit Bitcoin im Alltag) ----------
POSTS['beitrag-21'] = dict(
    date='2026-10-18', fmt='Gegenüberstellung', topic='Vorurteil vs. Wahrheit: „Bitcoin kannst du nirgends ausgeben“ (BTC Map, Krypto-Karte, Alltag in Venezuela)',
    slides=[
        s_vs('VORURTEIL VS. WAHRHEIT', '„Bitcoin kannst du nirgends ausgeben.“ %s' % A('Über 26.000 Läden sagen Nein.'),
             'VORURTEIL', ['Nur zum Spekulieren da', 'Kein Laden nimmt ihn an', 'Bezahlen braucht Technik-Wissen', 'Spielgeld für Nerds'],
             'WAHRHEIT', ['Über 26.000 Händler nehmen ihn an', 'BTC Map zeigt sie dir in deiner Nähe', 'Krypto-Karte zahlt überall mit Kartenzahlung', 'In Venezuela, wo ich lebe, ist Krypto Alltag'],
             'Schick das jemandem, der sagt, mit Bitcoin kann man nirgends bezahlen.', src='Quelle: BTC Map, Stand August 2026'),
    ],
    alts=['Gegenüberstellung Vorurteil und Wahrheit: Bitcoin kannst du nirgends ausgeben, über 26.000 Läden sagen Nein. Vorurteil: nur zum Spekulieren da, kein Laden nimmt ihn an, Bezahlen braucht Technik-Wissen, Spielgeld für Nerds. Wahrheit: Über 26.000 Händler nehmen ihn an, BTC Map zeigt sie dir in deiner Nähe, Krypto-Karte zahlt überall mit Kartenzahlung, in Venezuela, wo ich lebe, ist Krypto Alltag. Quelle: BTC Map, Stand August 2026. Schick das jemandem, der sagt, mit Bitcoin kann man nirgends bezahlen'],
    caption='''Ich wohne in einem Land, in dem Krypto Alltag ist. In Deutschland höre ich: Damit kann man nirgends bezahlen.

Das Vorurteil:
– Bitcoin ist nur zum Spekulieren da.
– Kein Laden nimmt ihn an.
– Zum Bezahlen brauchst du Technik-Wissen.
– Krypto ist Spielgeld für Nerds.

Die Wahrheit:
– Über 26.000 Händler weltweit nehmen Bitcoin an, Tendenz steigend (Quelle: BTC Map, Stand August 2026).
– BTC Map ist eine kostenlose Karte. Sie zeigt dir jeden Laden in deiner Nähe, der Bitcoin nimmt: Café, Friseur, Werkstatt.
– Mit einer Krypto-Karte zahlst du überall, wo Kartenzahlung geht. Die Karte wechselt im Hintergrund in Euro, der Laden sieht nur eine Kartenzahlung.
– Wo ich lebe, in Venezuela, ist Krypto Alltag. Aus Not, aus keinem Hype.

Keine Coin-Empfehlung, keine Kursprognose. Nur die Antwort auf einen Satz, den jeder Krypto-Anfänger zu hören bekommt.

Hast du schon mal mit Bitcoin oder einer Krypto-Karte bezahlt? Schreib Ja oder Nein in die Kommentare.

Schick das jemandem, der sagt, mit Bitcoin kann man nirgends bezahlen.''')

# ---------- Beitrag 22: Nischenmythos (feste Rendite ist sicherer als Schwankung, Cloud-Mining) ----------
Q_ESMA = 'Quelle: ESMA, Faktenblatt zu Krypto-Betrug, Januar 2026'
POSTS['beitrag-22'] = dict(
    date='2026-10-19', fmt='Nischenmythos entlarven', topic='Mythos: Eine feste Rendite ist sicherer als Schwankung (Cloud-Mining, 4.000 bis 5.000 $, ESMA-Warnzeichen)',
    slides=[
        s_hook('MYTHOS', '„Eine feste Rendite ist sicherer als %s“' % A('Schwankung.'),
               sub='Dieser Glaube hat mich 4.000 bis 5.000 $ gekostet. Woran du ihn in 5 Sekunden erkennst.',
               cue='Zuerst das Angebot, auf das ich reingefallen bin &#8594;', size=''),
        s_proof('MEIN FALL', 'Cloud-Mining mit festem Ertrag, jeden Monat.',
                big='4.000 $', big_sub='und mehr: 4.000 bis 5.000 $ hab ich eingezahlt. Wiedergesehen hab ich das Geld nie.',
                cue='Warum die Zahl nie stimmen konnte &#8594;'),
        s_point('DIE WAHRHEIT', 'Aus schwankenden Kursen gibt es keinen festen Ertrag.',
                ['Mining bringt Bitcoin. Was der wert ist, entscheidet der Kurs, jeden Tag neu.',
                 D('Eine feste Zahl kann dir nur versprechen, wer sie aus dem Geld der nächsten Einzahler nimmt. Oder aus gar keinem.')],
                cue='Die Aufsicht sagt dasselbe &#8594;'),
        s_point('WAS DIE AUFSICHT SAGT', '„Garantiert schnelle und hohe Rendite“ steht auf der Warnliste.',
                ['Die EU-Wertpapieraufsicht ESMA nennt das als Warnzeichen für Krypto-Betrug. Dazu: unaufgefordertes Angebot, Zeitdruck, Zahlung nur in Krypto.',
                 D('Bei meinem Angebot war die feste Rendite das Verkaufsargument.')],
                src=Q_ESMA, size='m', cue='Dein Test in 5 Sekunden &#8594;'),
        s_point('DER 5-SEKUNDEN-TEST', 'Steht eine Zahl pro Monat im Angebot, %s' % A('ist es keins.'),
                ['Echtes Mining und echte Börsen nennen dir Gebühren. Erträge nennt dir keiner im Voraus.',
                 D('Frag nach der Quelle des Ertrags. Kommt ein Prozentsatz statt einer Erklärung, bleibt dein Geld, wo es ist.')],
                size='m', cue='Dein Merkzettel &#8594;'),
        s_memo('ZUM SPEICHERN', 'Feste Rendite: %s' % A('die 4 Warnzeichen.'), 'Dein Merkzettel', [
            'Eine feste Zahl pro Monat aus schwankenden Kursen gibt es nie.',
            '„Garantiert“ steht bei der ESMA auf der Warnliste.',
            'Der Ertrag kommt aus dem Geld der Nächsten oder aus keinem.',
            'Frag nach der Quelle des Ertrags. Prozent statt Erklärung: raus.',
        ], 'Speichere dir das, bevor dir das nächste Angebot eine feste Rendite verspricht.'),
    ],
    alts=['Mythos: Eine feste Rendite ist sicherer als Schwankung. Dieser Glaube hat mich 4.000 bis 5.000 Dollar gekostet. Woran du ihn in 5 Sekunden erkennst',
          'Mein Fall: Cloud-Mining mit festem Ertrag jeden Monat. 4.000 bis 5.000 Dollar eingezahlt, wiedergesehen hab ich das Geld nie',
          'Die Wahrheit: Aus schwankenden Kursen gibt es keinen festen Ertrag. Mining bringt Bitcoin, was der wert ist, entscheidet der Kurs jeden Tag neu. Eine feste Zahl kann nur versprechen, wer sie aus dem Geld der nächsten Einzahler nimmt',
          'Was die Aufsicht sagt: Garantiert schnelle und hohe Rendite steht auf der Warnliste. Die ESMA nennt das als Warnzeichen für Krypto-Betrug, dazu unaufgefordertes Angebot, Zeitdruck, Zahlung nur in Krypto. Quelle: ESMA, Faktenblatt zu Krypto-Betrug, Januar 2026',
          'Der 5-Sekunden-Test: Steht eine Zahl pro Monat im Angebot, ist es keins. Echte Börsen nennen Gebühren, Erträge nennt keiner im Voraus. Frag nach der Quelle des Ertrags',
          'Merkzettel, feste Rendite, die vier Warnzeichen: eine feste Zahl pro Monat aus schwankenden Kursen gibt es nie; garantiert steht bei der ESMA auf der Warnliste; der Ertrag kommt aus dem Geld der Nächsten oder aus keinem; frag nach der Quelle des Ertrags. Speichere dir das, bevor dir das nächste Angebot eine feste Rendite verspricht'],
    caption='''Die sicherste Zahl in meinem Mining-Vertrag war die gefährlichste. Sie hat mich 4.000 bis 5.000 $ gekostet.

Der Mythos: „Eine feste Rendite ist sicherer als Schwankung.“ Genau das wollte ich damals als Krypto-Anfänger hören. Ein Cloud-Mining-Anbieter versprach einen festen Ertrag jeden Monat. Ich hab 4.000 bis 5.000 $ eingezahlt. Wiedergesehen hab ich das Geld nie.

Die Wahrheit:
– Mining bringt Bitcoin. Was der wert ist, entscheidet der Kurs, jeden Tag neu. Aus schwankenden Kursen gibt es keinen festen Ertrag.
– Eine feste Zahl kann dir nur versprechen, wer sie aus dem Geld der nächsten Einzahler nimmt. Oder aus gar keinem.
– Die EU-Wertpapieraufsicht ESMA führt „garantiert schnelle und hohe Rendite“ als Warnzeichen für Krypto-Betrug, dazu unaufgeforderte Angebote, Zeitdruck und Zahlung nur in Krypto (Quelle: ESMA, Faktenblatt zu Krypto-Betrug, Januar 2026).

Der 5-Sekunden-Test: Steht eine Zahl pro Monat im Angebot, ist es keins. Echtes Mining und echte Börsen nennen dir Gebühren. Erträge nennt dir keiner im Voraus. Frag nach der Quelle des Ertrags. Kommt ein Prozentsatz statt einer Erklärung, bleibt dein Geld, wo es ist.

Keine Kursprognose, keine Anbieter-Empfehlung. Nur mein Lehrgeld und die Warnliste der Aufsicht.

Welche feste Rendite wurde dir schon mal versprochen? Schreib die Zahl in Prozent in die Kommentare.

Speichere dir das, bevor dir das nächste Angebot eine feste Rendite verspricht.''')

# ---------- Beitrag 23: Erfolgsgeschichte (Bestaetigung von Fremden gesucht, heute ein System) ----------
POSTS['beitrag-23'] = dict(
    date='2026-10-20', fmt='Erfolgsgeschichte', topic='Damals Bestätigung von Fremden gesucht, heute über 250 Kunden (selbst verstehen, einfaches System)',
    slides=[
        s_hook('ERFOLGSGESCHICHTE', 'Früher hab ich Fremde gefragt, ob mein Kauf richtig ist. Heute fragen mich %s' % A('über 250 Kunden.'),
               sub='Was sich dazwischen geändert hat. Eine Episode aus meiner Geschichte.', cue='Zuerst die Zahl, um die es geht &#8594;', size=''),
        s_proof('HEUTE', 'Meine Zahl, kein Versprechen für dich.',
                big='5-stellig', big_sub='Krypto-Gewinn, jedes Jahr. Dazu über 250 Kunden.',
                cue='Und so sah es davor aus &#8594;'),
        s_point('DAMALS', 'Ich hab Bestätigung gesucht. %s' % A('Lange.'),
                ['Ich wollte, dass mir jemand anderes sagt: So ist es richtig.', D('Jedes Ja von anderen fühlte sich sicher an. Verstanden hatte ich dadurch null.')],
                cue='Der Moment, an dem sich das drehte &#8594;'),
        s_point('DER WENDEPUNKT', 'Ich hab angefangen, selbst zu verstehen, was ich kaufe.',
                ['Schritt für Schritt. Eine Frage nach der anderen, bis ich sie selbst beantworten konnte.', D('Kein weiteres Ja von Fremden. Nur meine eigene Antwort.')],
                size='m', cue='Was daraus geworden ist &#8594;'),
        s_point('HEUTE', 'Ein einfaches System. %s' % A('Langfristig.'),
                ['Ich kaufe nach Plan, statt auf eine Meinung zu warten.', D('Jeder Schritt darin ist einer, den ich selbst erklären kann.')],
                cue='Was das für dich heißt &#8594;'),
        s_point('FÜR DICH', 'Ich bin kein Genie.',
                ['Wenn ich das nach 70.000 $ Verlust geschafft habe, schaffst du den sicheren Einstieg auch.', D('Dafür brauchst du kein Ja von anderen. Du brauchst Verständnis für das, was du kaufst.')],
                cue='Dein Merkzettel für den nächsten Kauf &#8594;'),
        s_memo('ZUM SPEICHERN', 'Bevor du wieder %s' % A('nach einem Ja fragst.'), 'Dein Merkzettel', [
            'Ein Ja von Fremden ersetzt kein eigenes Verstehen.',
            'Kannst du den Kauf in zwei Sätzen erklären? Erst dann kaufen.',
            'Eine Meinung ist kein Plan.',
            'Du entscheidest. Auch dann, wenn du andere fragst.',
        ], 'Speichere dir das für den Moment, in dem du wieder fragen willst.'),
        s_point('KOSTENLOSES TRAINING', 'Das kostenlose Training findest du %s' % A('im Link in meiner Bio.'), meta=True, size='m'),
    ],
    alts=['Erfolgsgeschichte: Früher hab ich Fremde gefragt, ob mein Kauf richtig ist. Heute fragen mich über 250 Kunden',
          'Heute: jedes Jahr ein fünfstelliger Krypto-Gewinn, dazu über 250 Kunden. Meine Zahl, kein Versprechen für dich',
          'Damals: Ich hab lange Bestätigung gesucht. Jedes Ja von anderen fühlte sich sicher an, verstanden hatte ich dadurch null',
          'Der Wendepunkt: Ich hab angefangen, selbst zu verstehen, was ich kaufe. Schritt für Schritt',
          'Heute: ein einfaches, langfristiges System. Ich kaufe nach Plan, statt auf eine Meinung zu warten',
          'Für dich: Ich bin kein Genie. Wenn ich das nach 70.000 Dollar Verlust geschafft habe, schaffst du den sicheren Einstieg auch',
          'Merkzettel, bevor du wieder nach einem Ja fragst: Ein Ja von Fremden ersetzt kein eigenes Verstehen; erst kaufen, wenn du es in zwei Sätzen erklären kannst; eine Meinung ist kein Plan; du entscheidest. Speichere dir das',
          'Das kostenlose Training findest du im Link in meiner Bio'],
    caption='''Lange hab ich andere gefragt, ob mein Kauf passt. Heute hab ich über 250 Kunden.

Am Anfang wollte ich vor jedem Schritt ein Ja hören. Von Fremden, von anderen, die angeblich mehr wussten. Jedes Ja fühlte sich sicher an. Verstanden hatte ich dadurch null.

Der Wendepunkt:
– Ich hab angefangen, selbst zu verstehen, was ich kaufe. Schritt für Schritt.
– Daraus wurde ein einfaches, langfristiges System.
– Heute mache ich laut meiner eigenen Rechnung jedes Jahr einen fünfstelligen Krypto-Gewinn. Meine Zahl, kein Versprechen für dich.

Ich bin kein Genie. Wenn ich das nach 70.000 $ Verlust geschafft habe, schaffst du den sicheren Einstieg auch. Dafür brauchst du kein Ja von anderen. Du brauchst Verständnis für das, was du kaufst.

Für alle Krypto-Anfänger, die vor dem ersten Bitcoin-Kauf erst ein Ja von anderen hören wollen.

Das kostenlose Training findest du im Link in meiner Bio.''')

# ---------- Beitrag 24: Visueller Post (Raster: 3 Orte fuer deine Bitcoin, wer den Schluessel haelt) ----------
Q_BAFIN = 'Quelle: BaFin, Verbraucherinformation zu Kryptowerten (Einlagensicherung, Private Key)'
POSTS['beitrag-24'] = dict(
    date='2026-10-21', fmt='Visueller Post', topic='Raster: 3 Orte für deine Bitcoin, wer den Schlüssel hält und wo die Falle liegt (Börse, Wallet-App, Hardware-Wallet; gefälschte App 70.000 $)',
    slides=[
        s_raster('WO DEINE BITCOIN LIEGEN', '3 Orte für deine Bitcoin. %s' % A('3 Arten, sie zu verlieren.'), [
            ('1 &nbsp;Börse', [('Schlüssel', 'hat die Börse'), ('Falle', 'Hack: keine Einlagensicherung wie beim Sparkonto')]),
            ('2 &nbsp;Wallet-App auf dem Handy', [('Schlüssel', 'hast du, auf dem Handy'), ('Falle', 'gefälschte App, die echt aussieht. Meine 70.000 $')]),
            ('3 &nbsp;Hardware-Wallet', [('Schlüssel', 'hast du, auf einem eigenen Gerät'), ('Falle', 'Wörter herausgegeben, oder Gerät und Wörter weg')]),
        ], 'Speichere dir das für den Tag, an dem du entscheidest, wo deine Bitcoin liegen.',
            src=Q_BAFIN, hi=1),
    ],
    alts=['Raster, 3 Orte für deine Bitcoin, 3 Arten, sie zu verlieren. 1 Börse: den Schlüssel hat die Börse, Falle: Hack, keine Einlagensicherung wie beim Sparkonto. 2 Wallet-App auf dem Handy: den Schlüssel hast du, Falle: gefälschte App, die echt aussieht, so verlor ich 70.000 Dollar. 3 Hardware-Wallet: den Schlüssel hast du auf einem eigenen Gerät, Falle: Wörter herausgegeben, oder Gerät und Wörter weg. Quelle: BaFin. Speichere dir das für den Tag, an dem du entscheidest, wo deine Bitcoin liegen'],
    caption='''Jeder Ort für deine Bitcoin hat seine eigene Falle. Meine war eine App, die echt aussah.

Wo Krypto liegen kann und wer den Schlüssel hält:

1. Börse: Den Schlüssel hat die Börse. Wird sie gehackt, gibt es keine Einlagensicherung wie beim Sparkonto (Quelle: BaFin).

2. Wallet-App auf dem Handy: Den Schlüssel hast du. Die Falle ist eine gefälschte App, die aussieht wie das Original. Genau so hab ich 70.000 $ verloren.

3. Hardware-Wallet: Den Schlüssel hast du, auf einem eigenen Gerät. Gibst du deine Wörter heraus, ist das Guthaben weg. Sind Gerät und Wörter weg, stellt es keiner wieder her (Quelle: BaFin).

Kein Ort ist ohne Risiko. Wer weiß, welches Risiko er trägt, wird seltener überrascht.

Keine Anbieter-Empfehlung, keine Kursprognose. Nur die drei Orte und meine teuerste Erfahrung als Krypto-Anfänger.

Wo liegen deine Bitcoin gerade? Schreib 1, 2 oder 3 in die Kommentare.

Speichere dir das für den Tag, an dem du entscheidest, wo deine Bitcoin liegen.''')

# ---------- Beitrag 25: Frage an die Zielgruppe (Memecoin-Verlust, Chainalysis-Zahlen) ----------
POSTS['beitrag-25'] = dict(
    date='2026-10-22', fmt='Frage an die Zielgruppe', topic='Hand aufs Herz: Geld mit einem Memecoin verloren? (764.000 Wallets im Minus laut Chainalysis, eigener Memecoin-Verlust)',
    slides=[
        s_question('FRAGE AN DICH', 'Hand aufs Herz', 'Hast du schon mal Geld mit einem %s verloren?' % A('Memecoin'), 'Ich fange an: Ja.',
                   'Schreib Ja oder Nein in die Kommentare.',
                   pre='764.000 Wallets im Minus. 58 mit je über 10 Mio. $ Gewinn. Ein einziger Memecoin.',
                   src='Quelle: Chainalysis via CNBC, 06.05.2025'),
    ],
    alts=['Hand aufs Herz: 764.000 Wallets im Minus, 58 mit je über 10 Millionen Dollar Gewinn, ein einziger Memecoin. Hast du schon mal Geld mit einem Memecoin verloren? Ich fange an: Ja. Schreib Ja oder Nein in die Kommentare. Quelle: Chainalysis via CNBC, 06.05.2025'],
    caption='''58 Wallets haben mit einem Memecoin Millionen gemacht. Rund 764.000 haben Geld verloren.

Die Zahlen stammen von Chainalysis zu einem der bekanntesten Memecoins 2025:
– Rund 2 Millionen Wallets haben gekauft.
– 58 davon machten je über 10 Mio. $ Gewinn, zusammen rund 1,1 Mrd. $.
– Rund 764.000 lagen im Minus, die meisten mit kleinen Beträgen.
(Quelle: Chainalysis via CNBC, 06.05.2025)

Ich fange an: Ja. Ich hab selbst Geld mit einem Memecoin verloren.

Jetzt du:
– Hast du schon mal einen Memecoin gekauft?
– Lag er am Ende im Plus oder im Minus?

Keine Coin-Empfehlung, keine Kursprognose. Ich will wissen, wie es Krypto-Anfängern hier mit Memecoins geht.

Schreib Ja oder Nein in die Kommentare.''')

# ---------- Beitrag 26: Schritt-fuer-Schritt (rote Tage: Plan statt Panik) ----------
Q_KURS = 'Quelle: Schwäbische Zeitung, Kursverlauf Oktober 2025 bis Februar 2026'
POSTS['beitrag-26'] = dict(
    date='2026-10-23', fmt='Schritt-für-Schritt-Anleitung', topic='Rote Tage: Ende 2024 alle Bitcoin in Panik verkauft, heute 3 Schritte, bevor der Kurs fällt (Schwankungen aushalten, Plan statt Puls)',
    slides=[
        s_hook('SCHRITT FÜR SCHRITT', 'Ende 2024 hab ich %s meiner Bitcoin in Panik verkauft. Heute gehen rote Tage nach 3 Schritten.' % A('100 %'),
               sub='Mein Vorgehen, wenn der Kurs fällt. Grob, die Tiefe im Training.', cue='Zuerst, wie es damals lief &#8594;', size=''),
        s_proof('MEIN LEHRGELD', 'Der Kurs fiel. Ich hatte keinen Plan, nur Puls.',
                big='100 %', big_sub='meiner Bitcoin verkauft, Ende 2024. In Panik, an einem einzigen Tag der Angst.',
                cue='Schritt 1 hätte das verhindert &#8594;'),
        s_point('SCHRITT 1 VON 3', 'Verstehen, %s' % A('bevor ich kaufe.'),
                ['Ich kaufe nur, was ich in zwei Sätzen erklären kann.', D('Wer weiß, was er hält, verkauft seltener aus Angst.')],
                cue='Schritt 2 passiert Wochen vor dem roten Tag &#8594;'),
        s_point('SCHRITT 2 VON 3', 'Der Plan steht, %s' % A('bevor der Kurs fällt.'),
                ['Fester Tag, feste Summe. Festgelegt an einem ruhigen Tag.', D('Am roten Tag gibt es keine neue Entscheidung. Der Plan hat sie schon getroffen.')],
                cue='Schritt 3 nimmt dem Absturz den Schreck &#8594;'),
        s_point('SCHRITT 3 VON 3', 'Kursrutsche %s statt fürchten.' % A('einplanen'),
                ['Anfang Oktober 2025 zeitweise über 126.000 $. Anfang Februar 2026 unter 63.000 $.', D('Halbiert in vier Monaten. Wer so etwas vorher einplant, erschrickt seltener.')],
                src=Q_KURS + '. Rückblick, keine Kursprognose.', cue='Dein Merkzettel für den nächsten roten Tag &#8594;'),
        s_memo('ZUM SPEICHERN', 'Rote Tage, %s' % A('in 4 Zeilen.'), 'Dein Merkzettel', [
            'Nur kaufen, was du in zwei Sätzen erklären kannst.',
            'Den Plan an einem ruhigen Tag festlegen.',
            'Kursrutsche vorher einplanen statt fürchten.',
            'Panik verkauft zum schlechtesten Zeitpunkt.',
        ], 'Speichere dir das für den nächsten roten Tag.'),
        s_point('KOSTENLOSES TRAINING', 'Das kostenlose Training findest du %s' % A('im Link in meiner Bio.'), meta=True, size='m'),
    ],
    alts=['Schritt für Schritt: Ende 2024 hab ich 100 Prozent meiner Bitcoin in Panik verkauft. Heute gehen rote Tage nach 3 Schritten',
          'Mein Lehrgeld: 100 Prozent meiner Bitcoin verkauft, Ende 2024, in Panik. Der Kurs fiel, ich hatte keinen Plan, nur Puls',
          'Schritt 1 von 3: Verstehen, bevor ich kaufe. Ich kaufe nur, was ich in zwei Sätzen erklären kann',
          'Schritt 2 von 3: Der Plan steht, bevor der Kurs fällt. Fester Tag, feste Summe, festgelegt an einem ruhigen Tag',
          'Schritt 3 von 3: Kursrutsche einplanen statt fürchten. Anfang Oktober 2025 zeitweise über 126.000 Dollar, Anfang Februar 2026 unter 63.000 Dollar. Quelle: Schwäbische Zeitung',
          'Merkzettel, rote Tage in 4 Zeilen: nur kaufen, was du erklären kannst; den Plan an einem ruhigen Tag festlegen; Kursrutsche einplanen; Panik verkauft zum schlechtesten Zeitpunkt. Speichere dir das für den nächsten roten Tag',
          'Das kostenlose Training findest du im Link in meiner Bio'],
    caption='''Mein teuerster Verkauf hatte keinen Grund. Nur Angst.

Ende 2024 hab ich alle meine Bitcoin verkauft. In Panik. Der Kurs fiel, und ich hatte keinen Plan, nur Puls.

Heute laufen rote Tage bei mir nach drei groben Schritten:
1. Verstehen, bevor ich kaufe: Ich kaufe nur, was ich in zwei Sätzen erklären kann. Wer weiß, was er hält, verkauft seltener aus Angst.
2. Der Plan steht, bevor der Kurs fällt: fester Tag, feste Summe, festgelegt an einem ruhigen Tag. Am roten Tag gibt es keine neue Entscheidung.
3. Kursrutsche einplanen statt fürchten: Anfang Oktober 2025 kostete ein Bitcoin zeitweise über 126.000 $, Anfang Februar 2026 unter 63.000 $ (Quelle: Schwäbische Zeitung). Halbiert in vier Monaten. Wer so etwas vorher einplant, erschrickt seltener.

Keine Kursprognose, keine Gewinnzusage. Nur mein Lehrgeld als Krypto-Anfänger und der Blick zurück.

Für alle, die Bitcoin halten und bei jedem roten Tag aufs Handy starren.

Das kostenlose Training findest du im Link in meiner Bio.''')

# ---------- Beitrag 27: FAQ (Wie viel Geld brauche ich fuer den Einstieg?) ----------
Q_SAT = 'Quelle: BTC-Echo Academy, Stichwort Satoshi'
POSTS['beitrag-27'] = dict(
    date='2026-10-24', fmt='FAQ beantworten', topic='FAQ: „Wie viel Geld brauche ich für den Einstieg?“ (100 Millionen Satoshi, 70.000 $ Verlust trotz großem Betrag)',
    slides=[
        s_hook('FAQ', '„Wie viel Geld brauche ich?“ Ein Bitcoin hat %s Die Antwort ist kleiner, als du denkst.' % A('100 Millionen Teile.'),
               sub='Was ich Anfängern darauf antworte.', cue='Zuerst die Zahl, die alles ändert &#8594;', size=''),
        s_proof('DER BELEG', 'Du musst nie einen ganzen Bitcoin kaufen.',
                big='100 Mio.', big_sub='Satoshi stecken in einem Bitcoin. Börsen verkaufen dir Bruchteile, schon für kleine Beträge.',
                src=Q_SAT, cue='Warum der Betrag am Anfang zweitrangig ist &#8594;'),
        s_point('MEIN FALL', '70.000 $ waren kein kleiner Betrag. %s' % A('Weg waren sie trotzdem.'),
                ['Ich hab eine gefälschte Wallet-App geladen, weil sie echt aussah.', D('Mehr Geld hat mich nie sicherer gemacht. Verstehen schon.')],
                size='m', cue='Was am Anfang wirklich zählt &#8594;'),
        s_point('MEINE ANTWORT', 'Fang mit einem Betrag an, %s' % A('dessen Verlust du aushältst.'),
                ['Damit siehst du denselben Kurs, dieselbe App, dieselben Schwankungen.', D('Nur billiger, falls du dich vertust.')],
                size='m', cue='Und so wächst er danach &#8594;'),
        s_point('DANACH', 'Fester Tag, feste Summe.',
                ['Ein Sparplan kauft eine Summe, kein Stück. Der Kurs entscheidet nie.', D('Keine Gewinnzusage, keine Kursprognose. Mein Weg nach 70.000 $ Lehrgeld.')],
                cue='Die Antwort in 4 Zeilen zum Speichern &#8594;'),
        s_memo('ZUM SPEICHERN', 'Wie viel Geld? %s' % A('Die Antwort in 4 Zeilen.'), 'Dein Merkzettel', [
            'Ein Bitcoin hat 100 Millionen Teile. Du kaufst Bruchteile.',
            'Mehr Geld macht dich nie sicherer. Verstehen schon.',
            'Starte mit einem Betrag, dessen Verlust du aushältst.',
            'Fester Tag, feste Summe. Der Kurs entscheidet nie.',
        ], 'Speichere dir das für deinen ersten Kauf.'),
        s_point('KOSTENLOSES TRAINING', 'Das kostenlose Training findest du %s' % A('im Link in meiner Bio.'), meta=True, size='m'),
    ],
    alts=['FAQ: Wie viel Geld brauche ich? Ein Bitcoin hat 100 Millionen Teile. Die Antwort ist kleiner, als du denkst',
          'Der Beleg: 100 Millionen Satoshi stecken in einem Bitcoin. Börsen verkaufen Bruchteile, schon für kleine Beträge. Quelle: BTC-Echo Academy',
          'Mein Fall: 70.000 Dollar waren kein kleiner Betrag, weg waren sie trotzdem. Eine gefälschte Wallet-App, die echt aussah',
          'Meine Antwort: Fang mit einem Betrag an, dessen Verlust du aushältst. Derselbe Kurs, dieselbe App, nur billiger',
          'Danach: fester Tag, feste Summe. Ein Sparplan kauft eine Summe, kein Stück. Keine Gewinnzusage, keine Kursprognose',
          'Merkzettel, wie viel Geld in 4 Zeilen: Bruchteile kaufen; mehr Geld macht dich nie sicherer; mit einem Betrag starten, dessen Verlust du aushältst; fester Tag, feste Summe. Speichere dir das für deinen ersten Kauf',
          'Das kostenlose Training findest du im Link in meiner Bio'],
    caption='''Die häufigste Frage von Krypto-Anfängern: Wie viel Geld brauche ich für den Einstieg? Meine Antwort beginnt mit 70.000 $, die trotzdem weg waren.

Zuerst die Zahl: Ein Bitcoin hat 100 Millionen Teile. Die kleinste Einheit heißt Satoshi (Quelle: BTC-Echo Academy). Du musst nie einen ganzen Bitcoin kaufen. Börsen verkaufen dir Bruchteile, schon für kleine Beträge.

Dann mein Fall: 70.000 $ waren kein kleiner Betrag. Ich hab eine gefälschte Wallet-App geladen, weil sie echt aussah. Das Geld war weg. Mehr Geld hat mich nie sicherer gemacht. Verstehen schon.

Was ich heute darauf antworte:
– Fang mit einem Betrag an, dessen Verlust du aushältst. Du siehst denselben Kurs, dieselbe App, dieselben Schwankungen. Nur billiger, falls du dich vertust.
– Danach: fester Tag, feste Summe. Ein Sparplan kauft eine Summe, kein Stück. Der Kurs entscheidet nie.

Keine Gewinnzusage, keine Kursprognose, keine Anbieter-Empfehlung. Mein Weg nach 70.000 $ Lehrgeld.

Für alle, die Bitcoin kaufen wollen und glauben, dafür fehle ihnen das Geld.

Das kostenlose Training findest du im Link in meiner Bio.''')

# ---------- Beitrag 28: Aufzaehlung (7 Saetze, die du sofort als Warnsignal erkennst) ----------
Q_ESAS = 'Quelle: ESMA, EBA, EIOPA, Faktenblatt zu Krypto-Betrug (Dezember 2025)'
NACH = 'Nachgestellt'
POSTS['beitrag-28'] = dict(
    date='2026-10-25', fmt='Aufzählung', topic='7 Sätze, die du sofort als Warnsignal erkennst (12 Wörter am Telefon, Warnzeichen der EU-Aufsicht, 5-Sekunden-Test)',
    slides=[
        s_hook('AUFZÄHLUNG', '„Nenn mir deine 12 Wörter.“ Ein Satz, und deine Wallet ist leer. %s' % A('Diese 7 Sätze erkennst du sofort.'),
               sub='Typische Sätze von Betrügern, dazu die Einordnung der EU-Aufsicht.', cue='Satz 1 hab ich selbst am Telefon gehört &#8594;', size=''),
        s_proof('SATZ 1', 'Am Telefon, in der Community eines Mining-Anbieters.',
                quote='„Nenn mir kurz deine 12 Wörter, dann synchronisiere ich deine Wallet.“', quote_from='Nachgestellt, so lief es bei mir',
                ps=[D('Ich hab ihm ausgedachte Wörter gegeben. Er ist ausgerastet.')], cue='Satz 2 und 3 kommen meist zuerst &#8594;'),
        s_chat('SATZ 2 UND 3', 'Der Einstieg.', [
            ('„Hey, ich hab dein Profil gesehen. Ich hätte da was für dich.“', 'Unaufgefordert', 'Ein Angebot, um das du nie gebeten hast.'),
            ('„Garantiert 3 % im Monat, ganz ohne Risiko.“', 'Garantierte Rendite', 'Bei Krypto garantiert dir keiner einen Ertrag.'),
        ], sender=NACH, cue='Satz 4 und 5 machen Druck &#8594;'),
        s_chat('SATZ 4 UND 5', 'Der Druck.', [
            ('„Das geht nur bis heute Abend, danach ist der Platz weg.“', 'Zeitdruck', 'Du sollst handeln, bevor du nachdenkst.'),
            ('„Am schnellsten zahlst du in Krypto oder mit einer Geschenkkarte.“', 'Zahlungsweg', 'Wege, die sich kaum zurückverfolgen lassen.'),
        ], sender=NACH, cue='Die letzten zwei führen in deine Wallet &#8594;'),
        s_chat('SATZ 6 UND 7', 'Der Zugriff.', [
            ('„Klick kurz auf den Link und bestätige deine Wallet.“', 'Link oder QR-Code', 'Ein Klick, und du landest auf einer nachgebauten Seite.'),
            ('„Lade dir diese App, dann kann ich dir helfen.“', 'App von Fremden', 'Hilfe, die eine App braucht, will Zugang.'),
        ], sender=NACH, src=Q_ESAS, cue='Dein 5-Sekunden-Test zum Speichern &#8594;'),
        s_memo('ZUM SPEICHERN', 'Der 5-Sekunden-Test, %s' % A('bevor du antwortest.'), 'Dein Merkzettel', [
            'Hat er zuerst geschrieben? Warnsignal.',
            'Garantiert, nur heute, deine 12 Wörter? Gespräch beenden.',
            'Klicken, scannen, App laden? Nein.',
            'Zahlung nur in Krypto oder per Geschenkkarte? Nein.',
        ], 'Schick das jemandem, der in Krypto-Gruppen unterwegs ist.'),
    ],
    alts=['Aufzählung: Nenn mir deine 12 Wörter. Ein Satz, und deine Wallet ist leer. Diese 7 Sätze erkennst du sofort',
          'Satz 1, nachgestellt, so lief es bei mir am Telefon: Nenn mir kurz deine 12 Wörter, dann synchronisiere ich deine Wallet. Ich hab ihm ausgedachte Wörter gegeben, er ist ausgerastet',
          'Satz 2 und 3, nachgestellt: Hey, ich hab dein Profil gesehen, ich hätte da was für dich, unaufgefordert. Garantiert 3 Prozent im Monat, ganz ohne Risiko, garantierte Rendite',
          'Satz 4 und 5, nachgestellt: Das geht nur bis heute Abend, Zeitdruck. Am schnellsten zahlst du in Krypto oder mit einer Geschenkkarte, Zahlungsweg',
          'Satz 6 und 7, nachgestellt: Klick kurz auf den Link und bestätige deine Wallet. Lade dir diese App, dann kann ich dir helfen. Quelle: ESMA, EBA, EIOPA, Faktenblatt zu Krypto-Betrug',
          'Merkzettel, der 5-Sekunden-Test, bevor du antwortest: Hat er zuerst geschrieben; garantiert, nur heute, 12 Wörter; klicken, scannen, App laden; Zahlung nur in Krypto oder Geschenkkarte. Schick das jemandem, der in Krypto-Gruppen unterwegs ist'],
    caption='''Ein Anrufer wollte meine 12 Wörter. Er bekam ausgedachte und ist ausgerastet.

Das war in der Community eines Mining-Anbieters. Am Telefon hieß es, er müsse meine Wallet „synchronisieren“. Dafür bräuchte er nur meine Seed-Phrase. Mit den echten Wörtern wäre meine Wallet leer gewesen.

Diese 7 Sätze erkennst du ab heute sofort als Warnsignal für Krypto-Betrug (nachgestellt):
1. „Nenn mir kurz deine 12 Wörter.“ Seed-Phrase: Die verlangt kein echter Support.
2. „Ich hab dein Profil gesehen, ich hätte da was für dich.“ Unaufgefordert.
3. „Garantiert 3 % im Monat.“ Garantierte Rendite.
4. „Das geht nur bis heute Abend.“ Zeitdruck.
5. „Zahl in Krypto oder mit einer Geschenkkarte.“ Ein Weg, der sich kaum zurückverfolgen lässt.
6. „Klick auf den Link und bestätige deine Wallet.“ Link oder QR-Code.
7. „Lade dir diese App, dann helfe ich dir.“ App von Fremden.

Genau diese Warnzeichen nennen die EU-Aufsichtsbehörden ESMA, EBA und EIOPA in ihrem Faktenblatt zu Krypto-Betrug (Dezember 2025).

Der 5-Sekunden-Test, bevor du antwortest:
– Hat er zuerst geschrieben? Warnsignal.
– Fallen Wörter wie garantiert, nur heute oder 12 Wörter? Gespräch beenden.
– Sollst du klicken, scannen oder eine App laden? Nein.
– Zahlung nur in Krypto oder per Geschenkkarte? Nein.

Welchen dieser 7 Sätze hast du schon gehört? Schreib die Zahl in die Kommentare.

Schick das jemandem, der in Krypto-Gruppen unterwegs ist.''')

# ---------- Beitrag 29: Statement-Karussell (Der Kurs ist dein kleinstes Risiko: gefaelschte Wallet-Apps) ----------
Q_KASP = 'Quelle: Kaspersky, Pressemitteilung vom 20.04.2026'
POSTS['beitrag-29'] = dict(
    date='2026-10-26', fmt='Statement-Karussell', topic='Der Kurs ist dein kleinstes Risiko: 70.000 $ durch eine gefälschte Wallet-App, 26 Fake-Wallets im App Store (Kaspersky), 3 Prüfungen vor dem Download',
    slides=[
        s_hook('STATEMENT', 'Der Kurs ist dein kleinstes Risiko. %s' % A('Mich hat ein Download 70.000 $ gekostet.'),
               sub='Alle starren auf den Chart. Mein teuerster Verlust kam von woanders.',
               cue='Wie das passiert ist &#8594;', size=''),
        s_proof('MEIN BELEG', 'Ich hab eine Wallet-App geladen, weil sie echt aussah.',
                big='70.000 $', big_sub='waren danach weg. Ohne Kurssturz, ohne Crash, ohne Warnung.',
                cue='Und genau das läuft gerade wieder &#8594;'),
        s_proof('KEIN EINZELFALL', 'Echt aussehen ist ihr Geschäft.',
                big='26', big_sub='gefälschte Wallet-Apps fand Kaspersky im App Store von Apple. Mit Namen und Logos bekannter Wallets.',
                src=Q_KASP, cue='Warum der Chart dich davon ablenkt &#8594;'),
        s_point('UND DER KURS?', 'Der Kurs schwankt. Das stimmt.',
                ['Das siehst du jeden Tag. Mit Plan und kleinen Beträgen hältst du das aus.',
                 D('Eine gefälschte App siehst du erst, wenn das Guthaben weg ist. Dann holt es dir keiner zurück.')],
                cue='Prüfung 1 vor jedem Download &#8594;'),
        s_point('PRÜFUNG 1', 'Der Link kommt vom Anbieter. %s' % A('Von sonst keinem.'),
                ['Ich lade eine Wallet-App nur über den Link auf der offiziellen Seite des Anbieters.',
                 D('Nie über Werbung, Suchtreffer oder einen Link aus einem Chat.')],
                cue='Prüfung 2 dauert 5 Sekunden &#8594;'),
        s_point('PRÜFUNG 2', 'Schau, wer die App gemacht hat.',
                ['Im Store steht unter dem Namen der Entwickler. Passt er zum Anbieter?',
                 D('Die Fälschungen bei Kaspersky tarnten sich als Spiel oder Taschenrechner. Öffnet so eine App eine Seite, die wie der App Store aussieht: sofort schließen.')],
                cue='Prüfung 3 rettet deine Wallet &#8594;'),
        s_point('PRÜFUNG 3', 'Fragt die App nach deinen 12 Wörtern? %s' % A('Stopp.'),
                ['Laut Kaspersky fragt die echte Ledger-App nie nach den Wörtern. Die gefälschte schon.',
                 D('Wer deine Wörter hat, hat deine Bitcoin.')],
                src=Q_KASP, cue='Dein Merkzettel zum Speichern &#8594;'),
        s_memo('ZUM SPEICHERN', 'Vor jedem Download, %s' % A('in 4 Zeilen.'), 'Dein Merkzettel', [
            'Wallet-App nur über den Link auf der Seite des Anbieters.',
            'Entwickler im Store prüfen, bevor du lädst.',
            'Spiel oder Rechner öffnet einen Store? Schließen.',
            'Eine App fragt nach deinen 12 Wörtern? Stopp.',
        ], 'Speichere dir das, bevor du deine nächste Wallet-App lädst.'),
    ],
    alts=['Statement: Der Kurs ist dein kleinstes Risiko. Mich hat ein Download 70.000 Dollar gekostet. Alle starren auf den Chart, mein teuerster Verlust kam von woanders',
          'Mein Beleg: Ich hab eine Wallet-App geladen, weil sie echt aussah. 70.000 Dollar waren danach weg, ohne Kurssturz, ohne Crash, ohne Warnung',
          'Kein Einzelfall: 26 gefälschte Wallet-Apps fand Kaspersky im App Store von Apple, mit Namen und Logos bekannter Wallets. Quelle: Kaspersky, Pressemitteilung vom 20.04.2026',
          'Und der Kurs? Der Kurs schwankt, das stimmt. Mit Plan und kleinen Beträgen hältst du das aus. Eine gefälschte App siehst du erst, wenn das Guthaben weg ist',
          'Prüfung 1: Der Link kommt vom Anbieter. Wallet-App nur über den Link auf der offiziellen Seite des Anbieters laden, nie über Werbung, Suchtreffer oder Links aus Chats',
          'Prüfung 2: Schau, wer die App gemacht hat. Passt der Entwickler im Store zum Anbieter? Öffnet ein Spiel oder Taschenrechner eine Seite, die wie der App Store aussieht, sofort schließen',
          'Prüfung 3: Fragt die App nach deinen 12 Wörtern? Stopp. Laut Kaspersky fragt die echte Ledger-App nie nach den Wörtern, die gefälschte schon. Wer deine Wörter hat, hat deine Bitcoin',
          'Merkzettel vor jedem Download: Wallet-App nur über den Link des Anbieters; Entwickler im Store prüfen; Spiel oder Rechner öffnet einen Store, schließen; App fragt nach 12 Wörtern, Stopp. Speichere dir das, bevor du deine nächste Wallet-App lädst'],
    caption='''Mein teuerster Verlust hatte mit dem Bitcoin-Kurs null zu tun.

Als Krypto-Anfänger hab ich jeden Tag auf den Chart geschaut. Verloren hab ich mein Geld woanders: Ich hab eine Wallet-App geladen, weil sie echt aussah. Danach waren 70.000 $ weg. Ohne Kurssturz, ohne Crash, ohne Warnung.

Das ist kein Einzelfall:
– Kaspersky fand 26 gefälschte Wallet-Apps im App Store von Apple, mit Namen und Logos bekannter Wallets (Quelle: Kaspersky, Pressemitteilung vom 20.04.2026).
– Viele tarnten sich als Spiel oder Taschenrechner und öffneten dann eine Seite, die wie der App Store aussah.
– Laut Kaspersky fragt die echte Ledger-App nie nach den Wörtern der Wallet. Die gefälschte schon.

Der Kurs schwankt, das stimmt. Das siehst du jeden Tag und hältst es mit Plan und kleinen Beträgen aus. Eine gefälschte App siehst du erst, wenn das Guthaben weg ist.

Meine 3 Prüfungen vor jedem Download:
1. Die Wallet-App nur über den Link auf der offiziellen Seite des Anbieters. Nie über Werbung, Suchtreffer oder Links aus Chats.
2. Den Entwickler im Store prüfen. Passt er zum Anbieter?
3. Fragt eine App nach deinen 12 Wörtern: Stopp. Wer deine Wörter hat, hat deine Bitcoin.

Keine Anbieter-Empfehlung, keine Kursprognose. Nur mein Lehrgeld gegen Betrug mit Wallet-Apps, für alle, die gerade ihre erste Wallet oder Börse einrichten.

Hast du deine Wallet-App über den Link auf der Seite des Anbieters geladen? Schreib Ja oder Nein in die Kommentare.

Speichere dir das, bevor du deine nächste Wallet-App lädst.''')

# ---------- Beitrag 30: Gegenueberstellung (Fall Thomas: Rueckhol-Mails nach dem Verlust, Falsch vs. so pruefe ich) ----------
Q_BAFIN_NAME = 'Quelle: BaFin, „Betrug mit dem Namen der BaFin“'
POSTS['beitrag-30'] = dict(
    date='2026-10-27', fmt='Gegenüberstellung', topic='Fall Thomas: 40.000 $ verloren, dann kamen die Rückhol-Mails („BaFin Team“, Kanzlei, 2,08 BTC); die Mail vs. so prüfe ich (Absender @bafin.de)',
    slides=[
        s_vs('ECHTER FALL · NAME GEÄNDERT', 'Thomas verlor 40.000 $. Dann schrieb das „BaFin Team“. %s' % A('Echt?'),
             'DIE MAILS', ['Kanzlei „im Auftrag der Finanzaufsicht“', '„BaFin Team“ mit echtem BaFin-Link', '2,08 BTC ausgesetzt, Ausweis bitte', '„Coinbase Wallet“ von fremder Adresse'],
             'SO PRÜFE ICH', ['Wer zuerst schreibt, will etwas', 'BaFin schreibt nur von @bafin.de', 'Ausweis nie per Mail', 'Echter Link, falsche Mail'],
             'Schick das jemandem, der schon Geld an Betrüger verloren hat.', src=Q_BAFIN_NAME),
    ],
    alts=['Gegenüberstellung, echter Fall, Name geändert: Thomas verlor 40.000 Dollar, dann schrieb das BaFin Team. Echt? Die Mails: eine Kanzlei im Auftrag der Finanzaufsicht; ein BaFin Team mit echtem BaFin-Link; 2,08 BTC ausgesetzt, Ausweis bitte; eine Coinbase Wallet von fremder Adresse. So prüfe ich: Wer zuerst schreibt, will etwas; die BaFin schreibt nur von @bafin.de; Ausweis nie per Mail; echter Link, falsche Mail. Quelle: BaFin, Betrug mit dem Namen der BaFin. Schick das jemandem, der schon Geld an Betrüger verloren hat'],
    caption='''Nach dem ersten Betrug kommt die zweite Welle. Sie verspricht, das Geld zurückzuholen.

Echter Fall, Name geändert, veröffentlicht mit Zustimmung: Thomas hat beim Online-Trading nach eigener Aussage rund 40.000 $ verloren. Seitdem bekommt er Mails. Jede leitet er mir weiter und fragt: echt?

Die Mails an Thomas:
– Eine angebliche Londoner Kanzlei schreibt „im Auftrag der britischen Finanzaufsicht“. Zahlung nur bei Erfolg.
– Ein „BaFin Team“ schreibt, die BaFin sei ein „legitimes und seriöses Unternehmen“, und verlinkt die echte BaFin-Seite.
– Ein „Blockchain Support“ meldet 2,08 BTC, die angeblich ausgesetzt sind. Dafür will er Ausweis und Stromrechnung.
– Eine „Coinbase Wallet“ schreibt von einer fremden Adresse.

So prüfe ich jede dieser Mails:
– Wer nach einem Verlust zuerst schreibt, will etwas von dir. Geld, Daten oder beides.
– Die BaFin verwendet nur E-Mail-Adressen mit @bafin.de, einzige Ausnahme ist ihr Newsletter (Quelle: BaFin, „Betrug mit dem Namen der BaFin“).
– Ausweis und Stromrechnung schicke ich auf keine Mail hin. Prüfungen laufen bei mir nur im eigenen Konto der Börse, nie über einen Link aus einer Mail.
– Ein echter Link in einer Mail macht die Mail nie echt. Kopieren kann ihn jeder.

Keine Anbieter-Empfehlung, keine Rückhol-Versprechen. Nur das, was ich bei Betrug mit Krypto, Bitcoin und Börsen-Namen immer wieder sehe, für jeden Anfänger, der schon einmal Geld verloren hat.

Hast du nach einem Verlust schon mal so eine Mail bekommen? Schreib Ja oder Nein in die Kommentare.

Schick das jemandem, der schon Geld an Betrüger verloren hat.''')

# ---------- Beitrag 31: Nischenmythos (Krypto ist nur Betrug; 70.000 $ verloren, Betrug sass vor Bitcoin, TRM Labs 1,2 %) ----------
Q_TRM = 'Quelle: TRM Labs, Crypto Crime Report 2026'
POSTS['beitrag-31'] = dict(
    date='2026-10-28', fmt='Nischenmythos entlarven', topic='Mythos: „Krypto ist nur Betrug“ (70.000 $ an eine gefälschte Wallet-App, der Betrug saß vor Bitcoin, 1,2 % laut TRM Labs)',
    slides=[
        s_hook('MYTHOS', '„Krypto ist %s“' % A('nur Betrug.'),
               sub='Ich hab 70.000 $ an Betrüger verloren. Bitcoin selbst hat mir keinen Cent davon genommen. Wo der Betrug wirklich saß.',
               cue='Zuerst, wohin meine 70.000 $ gingen &#8594;'),
        s_proof('MEIN FALL', 'Mein teuerster Betrug sah aus wie eine echte App.',
                big='70.000 $', big_sub='weg durch eine gefälschte Wallet-App. Geladen, weil sie echt aussah.',
                cue='Das Muster hinter jedem meiner Verluste &#8594;'),
        s_point('DIE WAHRHEIT', 'Der Betrug saß nie in Bitcoin. %s' % A('Er saß davor.'),
                ['Eine falsche App. Eine „Netzwerkgebühr“ vor der Auszahlung. Ein Coin mit bekanntem Gesicht. Ein Anrufer, der meine 12 Wörter wollte.',
                 D('Jedes Mal ein Mensch mit einer Geschichte. Kein einziges Mal Bitcoin selbst.')],
                size='m', cue='Was die Zahlen dazu sagen &#8594;'),
        s_proof('DIE ZAHLEN', 'Der Betrug ist echt. Er ist nur %s' % A('ein kleiner Teil.'),
                big='1,2 %', big_sub='des zugeordneten Krypto-Volumens floss 2025 an Kriminelle. In Summe 158 Mrd. $.',
                src=Q_TRM, cue='Der Unterschied, den du in Sekunden siehst &#8594;'),
        s_point('DER UNTERSCHIED', 'Betrug will dein Geld. %s' % A('Bitcoin fragt nie danach.'),
                ['Bitcoin schreibt dir nie. Ruft nie an. Verspricht nie eine Rendite.',
                 D('Wer schreibt, verspricht oder drängt, ist ein Mensch. Den prüfst du, bevor Geld fließt.')],
                size='m', cue='Dein Merkzettel &#8594;'),
        s_memo('ZUM SPEICHERN', 'Krypto oder Betrug: %s' % A('der Unterschied.'), 'Dein Merkzettel', [
            'Bitcoin schreibt dir nie. Wer schreibt, ist ein Mensch.',
            'Bitcoin verspricht keine Rendite. Wer verspricht, will Geld.',
            'Eine App will deine 12 Wörter? Löschen.',
            'Gebühr vor der Auszahlung? Betrug, jedes Mal.',
        ], 'Schick das jemandem, der sagt, Krypto sei nur Betrug.'),
    ],
    alts=['Mythos: Krypto ist nur Betrug. Ich hab 70.000 Dollar an Betrüger verloren. Bitcoin selbst hat mir keinen Cent davon genommen. Wo der Betrug wirklich saß',
          'Mein Fall: Mein teuerster Betrug sah aus wie eine echte App. 70.000 Dollar weg durch eine gefälschte Wallet-App, geladen, weil sie echt aussah',
          'Die Wahrheit: Der Betrug saß nie in Bitcoin, er saß davor. Eine falsche App, eine Netzwerkgebühr vor der Auszahlung, ein Coin mit bekanntem Gesicht, ein Anrufer, der meine 12 Wörter wollte. Jedes Mal ein Mensch mit einer Geschichte',
          'Die Zahlen: Der Betrug ist echt, er ist nur ein kleiner Teil. 1,2 Prozent des zugeordneten Krypto-Volumens floss 2025 an Kriminelle, in Summe 158 Milliarden Dollar. Quelle: TRM Labs, Crypto Crime Report 2026',
          'Der Unterschied: Betrug will dein Geld, Bitcoin fragt nie danach. Bitcoin schreibt dir nie, ruft nie an, verspricht nie eine Rendite. Wer schreibt, verspricht oder drängt, ist ein Mensch',
          'Merkzettel, Krypto oder Betrug: Bitcoin schreibt dir nie; Bitcoin verspricht keine Rendite; eine App will deine 12 Wörter, löschen; Gebühr vor der Auszahlung, Betrug, jedes Mal. Schick das jemandem, der sagt, Krypto sei nur Betrug'],
    caption='''Ich hab 70.000 $ an Betrüger verloren. Krypto ist heute trotzdem Teil meines Systems.

Der Mythos: „Krypto ist nur Betrug.“ Den Satz hören Krypto-Anfänger ständig. Ich verstehe ihn. Nach meinen Verlusten hätte ich ihn selbst sagen können.

Mein Fall: Ich hab eine Wallet-App geladen, weil sie echt aussah. Sie war gefälscht. Danach waren 70.000 $ weg.

Wo der Betrug bei mir saß:
– Eine gefälschte Wallet-App.
– Eine „Netzwerkgebühr“, die ein Instagram-Kontakt vor der Auszahlung wollte. Die Auszahlung kam nie.
– Ein Influencer-Coin mit bekanntem Gesicht.
– Ein Anrufer, der meine 12 Wörter wollte, um meine Wallet zu „synchronisieren“.
Jedes Mal ein Mensch mit einer Geschichte. Kein einziges Mal Bitcoin selbst.

Die Zahlen: Der Betrug ist echt. 2025 flossen 158 Mrd. $ an Kriminelle, rund 1,2 % des zugeordneten Krypto-Volumens (Quelle: TRM Labs, Crypto Crime Report 2026). Viel Geld. Und trotzdem ein kleiner Teil.

Der Unterschied, den du in Sekunden siehst:
– Bitcoin schreibt dir nie. Wer schreibt, ist ein Mensch.
– Bitcoin verspricht keine Rendite. Wer verspricht, will Geld.
– Eine App will deine 12 Wörter? Löschen.
– Gebühr vor der Auszahlung? Betrug, jedes Mal.

Keine Kursprognose, keine Coin-Empfehlung. Nur mein Lehrgeld gegen Betrug rund um Krypto, Wallet und Börse.

Hältst du Krypto für Betrug? Schreib Ja oder Nein in die Kommentare.

Schick das jemandem, der sagt, Krypto sei nur Betrug.''')

# ---------- Beitrag 32: Erfolgsgeschichte (70.000 $ an eine App, die echt aussah; damals vertraut, heute verstanden) ----------
POSTS['beitrag-32'] = dict(
    date='2026-10-29', fmt='Erfolgsgeschichte', topic='Damals 70.000 $ an eine App verloren, die echt aussah, heute jedes Jahr fünfstellig (vertrauen statt verstehen, Wendepunkt)',
    slides=[
        s_hook('ERFOLGSGESCHICHTE', '70.000 $ an eine App verloren, die echt aussah. Heute bringt mir Krypto %s' % A('jedes Jahr fünfstellig.'),
               sub='Was dazwischen lag. Eine Episode aus meiner Geschichte.', cue='Zuerst, wie die 70.000 $ verschwanden &#8594;', size=''),
        s_proof('DAMALS', 'Ich hab eine Wallet-App geladen, weil sie echt aussah.',
                big='70.000 $', big_sub='weg. Kein Kurssturz, kein Crash. Eine gefälschte App.',
                cue='Warum mich das so viel gekostet hat &#8594;'),
        s_point('DIE ERKENNTNIS', 'Ich hab vertraut, %s' % A('statt zu verstehen.'),
                ['Mein einziger Grund für den Download: Sie sah echt aus.', D('Aussehen ist kein Beleg. Ein Logo kann jeder kopieren.')],
                size='m', cue='Was ich danach anders gemacht habe &#8594;'),
        s_point('DER WENDEPUNKT', 'Ich hab angefangen, selbst zu verstehen, was ich kaufe.',
                ['Wo liegen meine Bitcoin? Wer hält den Schlüssel? Woher kommt die App?', D('Eine Frage nach der anderen, bis ich sie selbst beantworten konnte.')],
                size='m', cue='Was daraus geworden ist &#8594;'),
        s_point('HEUTE', 'Ein einfaches System. %s' % A('Langfristig.'),
                ['Jedes Jahr ein fünfstelliger Krypto-Gewinn. Dazu über 250 Kunden.', D('Meine Zahl, kein Versprechen für dich.')],
                cue='Was das für dich heißt &#8594;'),
        s_point('FÜR DICH', 'Ich bin kein Genie.',
                ['Wenn ich das nach 70.000 $ Verlust geschafft habe, schaffst du den sicheren Einstieg auch.', D('Und du musst dafür nie so viel Lehrgeld zahlen wie ich.')],
                cue='Dein Merkzettel für deine erste Wallet &#8594;'),
        s_memo('ZUM SPEICHERN', 'Damals vertraut. %s' % A('Heute verstanden.'), 'Dein Merkzettel', [
            '„Sieht echt aus“ ist kein Beleg.',
            'Wallet-App nur über die Seite des Anbieters laden.',
            'Wer deine 12 Wörter hat, hat deine Bitcoin.',
            'Kauf nur, was du selbst erklären kannst.',
        ], 'Speichere dir das, bevor du deine erste Wallet einrichtest.'),
        s_point('KOSTENLOSES TRAINING', 'Das kostenlose Training findest du %s' % A('im Link in meiner Bio.'), meta=True, size='m'),
    ],
    alts=['Erfolgsgeschichte: 70.000 Dollar an eine App verloren, die echt aussah. Heute bringt mir Krypto jedes Jahr einen fünfstelligen Gewinn. Was dazwischen lag',
          'Damals: Ich hab eine Wallet-App geladen, weil sie echt aussah. 70.000 Dollar weg, ohne Kurssturz, ohne Crash, durch eine gefälschte App',
          'Die Erkenntnis: Ich hab vertraut, statt zu verstehen. Mein einziger Grund für den Download: Sie sah echt aus. Aussehen ist kein Beleg',
          'Der Wendepunkt: Ich hab angefangen, selbst zu verstehen, was ich kaufe. Wo liegen meine Bitcoin, wer hält den Schlüssel, woher kommt die App',
          'Heute: ein einfaches, langfristiges System. Jedes Jahr ein fünfstelliger Krypto-Gewinn, dazu über 250 Kunden. Meine Zahl, kein Versprechen für dich',
          'Für dich: Ich bin kein Genie. Wenn ich das nach 70.000 Dollar Verlust geschafft habe, schaffst du den sicheren Einstieg auch',
          'Merkzettel, damals vertraut, heute verstanden: Sieht echt aus ist kein Beleg; Wallet-App nur über die Seite des Anbieters laden; wer deine 12 Wörter hat, hat deine Bitcoin; kauf nur, was du selbst erklären kannst. Speichere dir das',
          'Das kostenlose Training findest du im Link in meiner Bio'],
    caption='''Mein teuerster Download war eine Wallet-App. Preis: 70.000 $.

Damals hab ich eine Wallet-App geladen, weil sie echt aussah. Sie war gefälscht. Danach waren 70.000 $ weg. Kein Kurssturz, kein Crash. Nur eine App.

Die Erkenntnis danach:
– Ich hab vertraut, statt zu verstehen. Mein einziger Grund für den Download: Sie sah echt aus.
– Aussehen ist kein Beleg. Ein Logo kann jeder kopieren.

Der Wendepunkt:
– Ich hab angefangen, Schritt für Schritt selbst zu verstehen, was ich kaufe.
– Wo liegen meine Bitcoin? Wer hält den Schlüssel? Woher kommt die App?
– Daraus wurde ein einfaches, langfristiges System.

Heute mache ich laut meiner eigenen Rechnung jedes Jahr einen fünfstelligen Krypto-Gewinn. Dazu über 250 Kunden. Meine Zahl, kein Versprechen für dich.

Ich bin kein Genie. Wenn ich das nach 70.000 $ Verlust geschafft habe, schaffst du den sicheren Einstieg auch.

Keine Kursprognose, keine Anbieter-Empfehlung. Für alle Krypto-Anfänger, die gerade ihre erste Wallet oder Börse einrichten und Betrug vermeiden wollen.

Das kostenlose Training findest du im Link in meiner Bio.''')

# ---------- Beitrag 33: Visueller Post (Ablauf mit Pfeilen, Fall Peter) ----------
POSTS['beitrag-33'] = dict(
    date='2026-10-30', fmt='Visueller Post', topic='Ablauf mit Pfeilen, Fall Peter: 250 € Einstieg, 62.000 € Schaden, 7 Stufen von der Instagram-Werbung bis zur falschen EZB',
    slides=[
        s_flow('ECHTER FALL · NAME GEÄNDERT', '250 € Einstieg. %s' % A('62.000 € Schaden.'), [
            ('Werbung auf Instagram', 'Gute Gewinne, Nebeneinkommen.'),
            ('250 € zum Start', 'Dafür wird sein Handelskonto „aktiviert“.'),
            ('„Laura“ ruft an', 'Mehrmals täglich. Sie handelt für ihn.'),
            ('5.000 € in bar', 'Von der Kreditkarte. „Laura“ will 5.000 € privat dazulegen.'),
            ('83.000 € auf dem Konto', 'Ausgezahlt: 5 €.'),
            ('Fremdes Geld auf seinem Girokonto', 'Weiterleiten an ein „Sicherheitskonto“. 3 Konten geschlossen.'),
            ('Mails einer falschen „EZB“', 'Mit Frist und Geldwäsche-Paragrafen.'),
        ], 'Speichere dir das, bevor dich die nächste Trading-Werbung anspricht.',
            sub='Peters Schaden laut seiner Anzeige. So lief es, Stufe für Stufe.', hi=4),
    ],
    alts=['Ablauf mit Pfeilen, echter Fall, Name geändert: 250 Euro Einstieg, 62.000 Euro Schaden. Peters Schaden laut seiner Anzeige, so lief es Stufe für Stufe. 1 Werbung auf Instagram: gute Gewinne, Nebeneinkommen. 2 250 Euro zum Start, dafür wird sein Handelskonto aktiviert. 3 Laura ruft an, mehrmals täglich, sie handelt für ihn. 4 5.000 Euro in bar von der Kreditkarte, Laura will 5.000 Euro privat dazulegen. 5 83.000 Euro auf dem Konto, ausgezahlt 5 Euro. 6 Fremdes Geld auf seinem Girokonto, weiterleiten an ein Sicherheitskonto, 3 Konten geschlossen. 7 Mails einer falschen EZB mit Frist und Geldwäsche-Paragrafen. Speichere dir das, bevor dich die nächste Trading-Werbung anspricht'],
    caption='''Es fing mit 250 € an. Am Ende standen rund 62.000 € Schaden in der Anzeige.

Echter Fall aus meiner Community, Name geändert, veröffentlicht mit Zustimmung. Peter kam über eine Werbung auf Instagram zu einem Trading-Angebot. Keine Stufe sah für sich allein nach Betrug aus. Zusammen schon.

Die 7 Stufen:
1. Werbung auf Instagram: gute Gewinne, Nebeneinkommen.
2. Für gut 250 € wird sein Handelskonto „aktiviert“.
3. „Laura“, angeblich Abteilungsleiterin mit zehn Jahren Erfahrung, ruft mehrmals täglich an und handelt für ihn.
4. Für ein Sechs-Monats-Angebot über 10.000 € will sie 5.000 € privat dazulegen. Peter holt 5.000 € als Bargeld von der Kreditkarte.
5. Sein Handelskonto zeigt 83.000 €. Ausgezahlt werden 5 €.
6. Statt Auszahlung landet Geld von Fremden auf seinem Girokonto. Er soll es über eine Krypto-Börse an ein „Sicherheitskonto“ weiterschicken. Vor jeder Überweisung ein Videoanruf mit geteiltem Bildschirm. Drei seiner Girokonten werden geschlossen.
7. Am Ende ein angeblicher Vorgesetzter und Mails einer falschen „Europäischen Zentralbank“ mit Frist und Geldwäsche-Paragrafen.

Schaden laut seiner Anzeige: rund 62.000 €, einschließlich Forderungen aus zurückgebuchten Zahlungen.

Was ich in diesem Ablauf sehe:
– Eine Zahl auf dem Bildschirm ist kein Geld. Geld ist, was auf deinem Konto ankommt.
– Wer für dich handelt und dafür Geld will, will dein Geld.
– Fremdes Geld weiterschicken ist nie eine Auszahlung.
– Frist und Paragrafen in einer Mail machen sie nie zu einer Behörde.

Keine Anbieter-Empfehlung, keine Gewinnzusage. Nur ein echter Fall, damit du die Stufen erkennst, bevor du selbst auf einer stehst.

An welcher Stufe wärst du ausgestiegen? Schreib die Zahl in die Kommentare.

Speichere dir das, bevor dich die nächste Trading-Werbung anspricht.''')

# ---------- Beitrag 34: Frage an die Zielgruppe (Fake-Account mit meinem Namen in der Telegram-Gruppe) ----------
POSTS['beitrag-34'] = dict(
    date='2026-10-31', fmt='Frage an die Zielgruppe', topic='Hand aufs Herz: In einer Krypto-Gruppe zuerst privat angeschrieben worden? (Fake-Account mit meinem Namen, geschätzt 4.000 bis 5.000 € aus fremden Wallets)',
    slides=[
        s_question('FRAGE AN DICH', 'Hand aufs Herz', 'Hat dich in einer Krypto-Gruppe schon mal jemand %s angeschrieben?' % A('zuerst privat'),
                   'Ich fange an: In meiner eigenen Gruppe ist es passiert.',
                   'Schick das jemandem, der in Krypto-Gruppen unterwegs ist.',
                   pre='Ein Fake-Account mit meinem Namen. Geschätzt 4.000 bis 5.000 € aus fremden Wallets.'),
    ],
    alts=['Hand aufs Herz: Ein Fake-Account mit meinem Namen, geschätzt 4.000 bis 5.000 Euro aus fremden Wallets. Hat dich in einer Krypto-Gruppe schon mal jemand zuerst privat angeschrieben? Ich fange an: In meiner eigenen Gruppe ist es passiert. Schick das jemandem, der in Krypto-Gruppen unterwegs ist'],
    caption='''Ich war Admin der Gruppe. Der Betrüger hat sich trotzdem als ich ausgegeben.

Das war in der Telegram-Gruppe eines Coin-Projekts. Ein Fake-Account mit meinem Namen hat Mitglieder privat angeschrieben. Danach waren Wallets leer. Geschätzt 4.000 bis 5.000 €.

Meine Fragen nach dem Entwicklerteam hat damals keiner beantwortet.

Was ich daraus mitgenommen habe:
– Ein Name im Profil ist kein Beweis. Kopieren kann ihn jeder.
– Wer dich in einer Krypto-Gruppe zuerst privat anschreibt, will etwas von dir.
– Fragt jemand nach Wallet, Wörtern oder Geld: Gespräch beenden und in der Gruppe selbst nachfragen.
– Ein Team, das auf Fragen schweigt, ist eine Antwort.

Keine Coin-Empfehlung, keine Kursprognose. Nur ein Erlebnis aus meiner Zeit als Admin, damit du Betrug in Krypto-Gruppen erkennst, bevor deine Wallet leer ist. Für jeden Anfänger, der Bitcoin oder eine Börse gerade erst entdeckt.

Hat dich in einer Krypto-Gruppe schon mal jemand zuerst privat angeschrieben? Schreib Ja oder Nein in die Kommentare.

Schick das jemandem, der in Krypto-Gruppen unterwegs ist.''')

# ---------- Beitrag 35: Schritt-fuer-Schritt (Phishing-Mail mit Frist, 3 Schritte ohne Klick) ----------
Q_VZ = 'Quelle: Verbraucherzentrale, „Phishing-Mails: Woran Sie sie erkennen“'
POSTS['beitrag-35'] = dict(
    date='2026-11-01', fmt='Schritt-für-Schritt-Anleitung', topic='Phishing: „Ihre Wallet wird in 24 Stunden gesperrt“, mein Check in 3 Schritten ohne Klick (Netzwerkgebühr an Instagram-Kontakt, Verbraucherzentrale)',
    slides=[
        s_hook('SCHRITT FÜR SCHRITT', '„Ihre Wallet wird in %s gesperrt.“ Ein Klick, und deine Bitcoin sind weg. %s' % ('24 Stunden', A('Der Check in 3 Schritten.')),
               sub='Nachgestellte Mail. Drei Schritte, bevor du klickst. Grob, die Tiefe im Training.', cue='Zuerst mein eigenes Lehrgeld &#8594;', size=''),
        s_proof('MEIN LEHRGELD', 'Ich hab selbst schon auf eine Nachricht hin gezahlt.',
                big='0 $', big_sub='ausgezahlt. Ein Instagram-Kontakt wollte vorher eine „Netzwerkgebühr“. Ich hab gezahlt, die Auszahlung kam nie.',
                cue='Schritt 1 dauert 5 Sekunden &#8594;'),
        s_point('SCHRITT 1 VON 3', 'Der Link in der Mail %s' % A('bleibt zu.'),
                ['Öffne die App oder die Seite selbst. Nie über den Link aus der Mail.', D('Ist am Konto wirklich etwas, siehst du es dort auch.')],
                cue='Schritt 2 entlarvt die Frist &#8594;'),
        s_point('SCHRITT 2 VON 3', 'Je kürzer die Frist, %s' % A('desto langsamer du.'),
                ['Druck mit Frist und Sperre ist ein Warnzeichen für Phishing.', D('Die Frist soll dich schneller machen als dein Kopf.')],
                src=Q_VZ, cue='Schritt 3 beendet jede Diskussion &#8594;'),
        s_point('SCHRITT 3 VON 3', 'Will ein Feld deine 12 Wörter? %s' % A('Stopp.'),
                ['Wer deine Wörter hat, hat deine Bitcoin. Ohne Handy, ohne PIN, ohne dich.', D('Kein echter Anbieter fragt per Mail danach. Egal, wie echt das Logo aussieht.')],
                cue='Dein Merkzettel für die nächste Sperr-Mail &#8594;'),
        s_memo('ZUM SPEICHERN', 'Sperr-Mail, %s' % A('in 4 Zeilen.'), 'Dein Merkzettel', [
            'Den Link in der Mail nie öffnen.',
            'App oder Seite selbst aufrufen und dort nachsehen.',
            'Frist und Sperre heißen: langsamer werden.',
            'Ein Feld will deine 12 Wörter? Stopp.',
        ], 'Speichere dir das, bevor die nächste Sperr-Mail kommt.'),
        s_point('KOSTENLOSES TRAINING', 'Das kostenlose Training findest du %s' % A('im Link in meiner Bio.'), meta=True, size='m'),
    ],
    alts=['Schritt für Schritt, nachgestellte Mail: Ihre Wallet wird in 24 Stunden gesperrt. Ein Klick, und deine Bitcoin sind weg. Der Check in 3 Schritten',
          'Mein Lehrgeld: 0 Dollar ausgezahlt. Ein Instagram-Kontakt wollte vorher eine Netzwerkgebühr, ich hab gezahlt, die Auszahlung kam nie',
          'Schritt 1 von 3: Der Link in der Mail bleibt zu. Öffne die App oder die Seite selbst, nie über den Link aus der Mail',
          'Schritt 2 von 3: Je kürzer die Frist, desto langsamer du. Druck mit Frist und Sperre ist ein Warnzeichen für Phishing. Quelle: Verbraucherzentrale',
          'Schritt 3 von 3: Will ein Feld deine 12 Wörter? Stopp. Wer deine Wörter hat, hat deine Bitcoin. Kein echter Anbieter fragt per Mail danach',
          'Merkzettel, Sperr-Mail in 4 Zeilen: den Link nie öffnen; App oder Seite selbst aufrufen; Frist und Sperre heißen langsamer werden; ein Feld will deine 12 Wörter, Stopp. Speichere dir das, bevor die nächste Sperr-Mail kommt',
          'Das kostenlose Training findest du im Link in meiner Bio'],
    caption='''Die gefährlichste Mail in deinem Postfach droht mit einer Sperre.

„Ihre Wallet wird in 24 Stunden gesperrt.“ So oder so ähnlich beginnen Phishing-Mails rund um Krypto (nachgestellt). Darunter ein Link. Dahinter eine Seite, die wie deine Börse oder Wallet aussieht.

Ich weiß, wie sich so eine Mail anfühlt. Ich hab selbst schon auf eine Nachricht hin gezahlt: Ein Instagram-Kontakt wollte vor meiner Auszahlung eine „Netzwerkgebühr“. Ich hab gezahlt. Die Auszahlung kam nie.

Seitdem weiß ich: Eine Nachricht, die Geld, einen Klick oder deine Wörter will, verdient Misstrauen. Drei grobe Schritte bei jeder Sperr-Mail:
1. Der Link bleibt zu: Öffne die App oder die Seite selbst, nie über den Link aus der Mail. Ist am Konto wirklich etwas, siehst du es dort auch.
2. Je kürzer die Frist, desto langsamer du: Druck mit kurzer Frist, dazu die Drohung mit einer Sperre, ist ein Warnzeichen für Phishing (Quelle: Verbraucherzentrale, „Phishing-Mails: Woran Sie sie erkennen“).
3. Will ein Feld deine 12 Wörter, ist Schluss: Wer deine Wörter hat, hat deine Bitcoin. Kein echter Anbieter fragt per Mail danach.

Keine Anbieter-Empfehlung. Nur mein Lehrgeld gegen Betrug mit Mails, für jeden Anfänger mit Wallet oder Konto bei einer Börse.

Wie viele Sperr-Mails hast du dieses Jahr bekommen? Schreib die Zahl in die Kommentare.

Das kostenlose Training findest du im Link in meiner Bio.''')

# ---------- Beitrag 36: FAQ (Kann ich mit wenig Zeit einsteigen?) ----------
Q_BO = 'Quelle: Barber & Odean, „Trading Is Hazardous to Your Wealth“, Journal of Finance 2000'
POSTS['beitrag-36'] = dict(
    date='2026-11-02', fmt='FAQ beantworten', topic='FAQ: „Kann ich mit wenig Zeit einsteigen?“ (aktivste Anleger 11,4 % statt 17,9 % laut Barber & Odean, lange Bestätigungssuche, Zeit einmal zum Verstehen)',
    slides=[
        s_hook('FAQ', '„Ich hab kaum Zeit für Krypto.“ Wer am meisten handelte, bekam %s Warum wenig Zeit dich schützen kann.' % A('11,4 % statt 17,9 %.'),
               sub='Was ich Anfängern darauf antworte.', cue='Zuerst die Studie hinter der Zahl &#8594;', size=''),
        s_proof('DER BELEG', 'Die fleißigsten Anleger bekamen am wenigsten.',
                big='11,4 %', big_sub='im Jahr für die Haushalte, die am meisten handelten. Der Markt brachte 17,9 %. Untersucht: 66.465 Haushalte mit Aktien, 1991 bis 1996.',
                src=Q_BO, cue='Mir ging es genauso, nur mit Krypto &#8594;'),
        s_point('MEIN FALL', 'Ich hab viel Zeit investiert. %s' % A('In Fragen an Fremde.'),
                ['Lange hab ich vor jedem Kauf andere gefragt, ob er richtig ist.', D('Viel Zeit, wenig Verstehen. Das Minus blieb bei mir.')],
                size='m', cue='Wofür du Zeit wirklich brauchst &#8594;'),
        s_point('MEINE ANTWORT', 'Zeit brauchst du einmal: %s' % A('zum Verstehen.'),
                ['Was kaufe ich? Wo liegt es? Wer hält den Schlüssel?', D('Das klärst du einmal am Anfang, statt jeden Tag aufs Neue.')],
                size='m', cue='Und danach läuft es fast ohne dich &#8594;'),
        s_point('DANACH', 'Fester Tag, feste Summe. %s' % A('Kein tägliches Kurs-Gucken.'),
                ['Mein System ist einfach und langfristig gebaut. Es braucht keinen Bildschirm am Abend.', D('Keine Gewinnzusage, keine Kursprognose. Meine Erfahrung, kein Versprechen für dich.')],
                size='m', cue='Der eine Moment, in dem du Zeit brauchst &#8594;'),
        s_point('DIE AUSNAHME', 'Zeit nimmst du dir immer dann, %s' % A('wenn jemand drängt.'),
                ['Eine Frist, ein Anruf, eine Gebühr vor der Auszahlung.', D('Wer dir keine Zeit lässt, will dein Geld.')],
                size='m', cue='Die Antwort in 4 Zeilen zum Speichern &#8594;'),
        s_memo('ZUM SPEICHERN', 'Wenig Zeit? %s' % A('Die Antwort in 4 Zeilen.'), 'Dein Merkzettel', [
            'Die aktivsten Anleger bekamen am wenigsten: 11,4 % statt 17,9 %.',
            'Zeit brauchst du einmal: zum Verstehen.',
            'Fester Tag, feste Summe. Kein tägliches Kurs-Gucken.',
            'Wer drängt, bekommt deine Zeit, nie dein Geld.',
        ], 'Speichere dir das für deinen ersten Kauf.'),
        s_point('KOSTENLOSES TRAINING', 'Das kostenlose Training findest du %s' % A('im Link in meiner Bio.'), meta=True, size='m'),
    ],
    alts=['FAQ: Ich hab kaum Zeit für Krypto. Wer am meisten handelte, bekam 11,4 Prozent statt 17,9 Prozent. Warum wenig Zeit dich schützen kann',
          'Der Beleg: Die fleißigsten Anleger bekamen am wenigsten. 11,4 Prozent im Jahr für die Haushalte, die am meisten handelten, der Markt brachte 17,9 Prozent. 66.465 Haushalte mit Aktien, 1991 bis 1996. Quelle: Barber und Odean, Journal of Finance 2000',
          'Mein Fall: Ich hab viel Zeit investiert, in Fragen an Fremde. Lange hab ich vor jedem Kauf andere gefragt. Viel Zeit, wenig Verstehen',
          'Meine Antwort: Zeit brauchst du einmal, zum Verstehen. Was kaufe ich, wo liegt es, wer hält den Schlüssel',
          'Danach: fester Tag, feste Summe, kein tägliches Kurs-Gucken. Mein System ist einfach und langfristig gebaut. Keine Gewinnzusage, keine Kursprognose',
          'Die Ausnahme: Zeit nimmst du dir immer dann, wenn jemand drängt. Eine Frist, ein Anruf, eine Gebühr vor der Auszahlung. Wer dir keine Zeit lässt, will dein Geld',
          'Merkzettel, wenig Zeit in 4 Zeilen: die aktivsten Anleger bekamen am wenigsten; Zeit brauchst du einmal zum Verstehen; fester Tag, feste Summe; wer drängt, bekommt deine Zeit, nie dein Geld. Speichere dir das für deinen ersten Kauf',
          'Das kostenlose Training findest du im Link in meiner Bio'],
    caption='''„Dafür hab ich keine Zeit.“ Den Satz höre ich von Krypto-Anfängern oft. Bei mir hat viel Zeit mehr gekostet als wenig.

Zuerst die Zahl: Forscher haben 66.465 Haushalte mit Aktien-Depots untersucht, 1991 bis 1996. Die Haushalte, die am meisten handelten, kamen auf 11,4 % im Jahr. Der Markt brachte 17,9 % (Quelle: Barber & Odean, „Trading Is Hazardous to Your Wealth“, Journal of Finance 2000). Mehr Aktivität, weniger Ergebnis.

Dann mein Fall: Ich hab viel Zeit in Krypto gesteckt. Vor allem in Fragen an Fremde. Lange hab ich vor jedem Kauf andere gefragt, ob er richtig ist. Viel Zeit, wenig Verstehen.

Was ich heute darauf antworte:
– Zeit brauchst du einmal: zum Verstehen. Was kaufe ich? Wo liegt es? Wer hält den Schlüssel der Wallet?
– Danach: fester Tag, feste Summe. Kein tägliches Kurs-Gucken bei Bitcoin oder an der Börse.
– Die Ausnahme: Drängt dich jemand mit Frist, Anruf oder Gebühr vor der Auszahlung, nimmst du dir Zeit. Wer dir keine Zeit lässt, will dein Geld.

Keine Gewinnzusage, keine Kursprognose, keine Anbieter-Empfehlung. Meine Erfahrung, kein Versprechen für dich.

Für alle, die Krypto verstehen wollen und dafür nur wenig Zeit haben.

Das kostenlose Training findest du im Link in meiner Bio.''')

# ---------- Beitrag 37: Aufzaehlung (Liebesbetrug mit Krypto: die 5 Phasen) ----------
Q_LKA = 'Quelle: LKA Baden-Württemberg laut dpa (Stuttgarter Zeitung); Verbraucherzentrale Hessen'
POSTS['beitrag-37'] = dict(
    date='2026-11-03', fmt='Aufzählung', topic='Liebesbetrug mit Krypto: die 5 Phasen vom Chat bis zur Gebühr vor der Auszahlung (fast 1.000 Fälle 2025 in Baden-Württemberg laut LKA, eigene Netzwerkgebühr)',
    slides=[
        s_hook('AUFZÄHLUNG', 'Fast 1.000 Fälle Liebesbetrug in einem Jahr, allein in Baden-Württemberg. %s' % A('Die 5 Phasen, in denen aus einem Chat Krypto-Betrug wird.'),
               sub='Wenn du sie kennst, steigst du in Phase 1 aus.', cue='Zuerst die Zahl hinter dem Satz &#8594;', size=''),
        s_proof('DER BELEG', 'Liebesbetrug ist kein Einzelfall.',
                big='Fast 1.000', big_sub='Fälle von Love Scamming 2025, allein in Baden-Württemberg. Oft geht es dabei um eine angebliche Geldanlage.',
                src=Q_LKA, cue='Phase 1 beginnt mit einer netten Nachricht &#8594;'),
        s_point('PHASE 1', 'Eine fremde Person %s' % A('schreibt dich zuerst an.'),
                ['Auf Instagram, in einer Dating-App, per Messenger.', D('Kontakt über soziale Medien und Messenger nennt auch die EU-Aufsicht als Warnzeichen für Krypto-Betrug.')],
                src=Q_ESAS, size='m', cue='Phase 2 fühlt sich gut an, genau das ist der Plan &#8594;'),
        s_point('PHASE 2', 'Jeden Tag Nachrichten. %s' % A('Viel Gefühl, nie ein Treffen.'),
                ['Komplimente, schnelle Liebeserklärungen, lange Geschichten aus dem Leben.', D('Vertrauen ist hier das Produkt. Dein Geld kommt später.')],
                size='m', cue='Phase 3: das erste Wort über Geld &#8594;'),
        s_point('PHASE 3', 'Plötzlich geht es %s' % A('um Krypto.'),
                ['Eine Trading-Plattform, eine App, ein Investment, mit dem die Person angeblich selbst verdient.', D('Liebesmasche plus Anlagebetrug: Das nennt man Pig Butchering.')],
                src='Quelle: BTC-ECHO Academy, Love Scamming', size='m', cue='Phase 4 sieht aus wie Erfolg &#8594;'),
        s_point('PHASE 4', 'Auf dem Bildschirm %s' % A('wächst dein Geld.'),
                ['Die Plattform zeigt Gewinne. Du zahlst nach, weil es läuft.', D('Eine Zahl auf dem Bildschirm ist kein Geld. Geld ist, was auf deinem Konto ankommt.')],
                src='Quelle: FBI, Internet Crime Report 2025', size='m', cue='Phase 5 kenne ich aus eigener Tasche &#8594;'),
        s_point('PHASE 5', 'Auszahlen? %s' % A('Erst eine Gebühr.'),
                ['Steuern, Gebühren, eine neue Einzahlung. Das Geld kommt nie.', D('Bei mir war es ein Instagram-Kontakt, ganz ohne Liebe. Er wollte vor der Auszahlung eine „Netzwerkgebühr“. Ich hab gezahlt. Die Auszahlung kam nie.')],
                src='Quelle: Verbraucherzentrale Hamburg, Vorsicht vor Trading-Plattformen', size='m', cue='Die 5 Phasen als Test zum Speichern &#8594;'),
        s_memo('ZUM SPEICHERN', 'Gefühl oder Falle? %s' % A('Dein Test in 5 Zeilen.'), 'Dein Merkzettel', [
            'Eine fremde Person schreibt zuerst? Wachsam bleiben.',
            'Viel Gefühl, nie ein Treffen? Warnsignal.',
            'Erstes Wort über Krypto oder eine Plattform? Gespräch beenden.',
            'Gewinne auf dem Bildschirm? Es zählt nur, was ankommt.',
            'Gebühr vor der Auszahlung? Betrug, jedes Mal.',
        ], 'Schick das jemandem, der gerade auf Dating-Apps unterwegs ist.'),
    ],
    alts=['Aufzählung: Fast 1.000 Fälle Liebesbetrug in einem Jahr, allein in Baden-Württemberg. Die 5 Phasen, in denen aus einem Chat Krypto-Betrug wird',
          'Der Beleg: Fast 1.000 Fälle von Love Scamming 2025, allein in Baden-Württemberg, oft geht es um eine angebliche Geldanlage. Quelle: LKA Baden-Württemberg laut dpa, Verbraucherzentrale Hessen',
          'Phase 1: Eine fremde Person schreibt dich zuerst an, auf Instagram, in einer Dating-App, per Messenger. Quelle: ESMA, EBA, EIOPA, Faktenblatt zu Krypto-Betrug',
          'Phase 2: Jeden Tag Nachrichten, viel Gefühl, nie ein Treffen. Komplimente, schnelle Liebeserklärungen, lange Geschichten aus dem Leben',
          'Phase 3: Plötzlich geht es um Krypto. Eine Trading-Plattform, eine App, ein Investment. Liebesmasche plus Anlagebetrug heißt Pig Butchering. Quelle: BTC-ECHO Academy',
          'Phase 4: Auf dem Bildschirm wächst dein Geld. Die Plattform zeigt Gewinne, du zahlst nach. Eine Zahl auf dem Bildschirm ist kein Geld. Quelle: FBI, Internet Crime Report 2025',
          'Phase 5: Auszahlen nur gegen eine Gebühr. Bei mir war es ein Instagram-Kontakt, er wollte eine Netzwerkgebühr, ich hab gezahlt, die Auszahlung kam nie. Quelle: Verbraucherzentrale Hamburg',
          'Merkzettel, Gefühl oder Falle, dein Test in 5 Zeilen: fremde Person schreibt zuerst; viel Gefühl, nie ein Treffen; erstes Wort über Krypto, Gespräch beenden; Gewinne auf dem Bildschirm zählen nur, wenn sie ankommen; Gebühr vor der Auszahlung ist Betrug. Schick das jemandem, der gerade auf Dating-Apps unterwegs ist'],
    caption='''Erst schreibt jemand jeden Morgen. Nach ein paar Wochen kommt die Trading-App.

Fast 1.000 Fälle von Love Scamming gab es 2025 allein in Baden-Württemberg (Quelle: LKA Baden-Württemberg laut dpa, Stuttgarter Zeitung). Oft geht es dabei um eine angebliche Geldanlage (Quelle: Verbraucherzentrale Hessen). Aus Liebesmasche plus Krypto-Betrug wird Pig Butchering (Quelle: BTC-ECHO Academy).

Die 5 Phasen:
1. Der Kontakt: Eine fremde Person schreibt dich zuerst an, auf Instagram, in einer Dating-App oder per Messenger. Die EU-Aufsicht nennt genau diese Wege als Warnzeichen (Quelle: ESMA, EBA, EIOPA, Faktenblatt zu Krypto-Betrug).
2. Die Nähe: jeden Tag Nachrichten, viel Gefühl, nie ein Treffen.
3. Die Gelegenheit: Plötzlich geht es um Krypto, eine Trading-Plattform oder eine App, mit der die Person angeblich selbst verdient.
4. Die Gewinne: Die Plattform zeigt Gewinne, du zahlst nach (Quelle: FBI, Internet Crime Report 2025).
5. Die Sperre: Auszahlen geht nur gegen Steuern, Gebühren oder eine neue Einzahlung (Quelle: Verbraucherzentrale Hamburg).

Phase 5 kenne ich selbst. Bei mir war es ein Instagram-Kontakt, ganz ohne Liebe. Er wollte vor der Auszahlung eine „Netzwerkgebühr“. Ich hab gezahlt. Die Auszahlung kam nie.

Dein Test in 5 Zeilen:
– Eine fremde Person schreibt zuerst? Wachsam bleiben.
– Viel Gefühl, nie ein Treffen? Warnsignal.
– Erstes Wort über Krypto oder eine Plattform? Gespräch beenden.
– Gewinne auf dem Bildschirm? Es zählt nur, was auf deinem Konto, in deiner Wallet oder bei deiner Börse ankommt.
– Gebühr vor der Auszahlung? Betrug, jedes Mal.

Keine Anbieter-Empfehlung. Für jeden Anfänger, der Bitcoin und Krypto entdeckt und dabei online neue Leute trifft.

In welcher Phase wärst du ausgestiegen? Schreib die Zahl in die Kommentare.

Schick das jemandem, der gerade auf Dating-Apps unterwegs ist.''')

# ---------- Beitrag 38: Statement-Karussell (Wirbt ein bekanntes Gesicht, kaufe ich keinen Cent; Influencer-Coin 5.000 $, LIBRA laut Nansen) ----------
Q_NANSEN = 'Quelle: Nansen Research, Februar 2025 (Wallets mit über 1.000 $ Gewinn oder Verlust)'
POSTS['beitrag-38'] = dict(
    date='2026-11-04', fmt='Statement-Karussell', topic='Wirbt ein bekanntes Gesicht für einen Coin, kaufe ich keinen Cent (Influencer-Coin 5.000 $, LIBRA: 86 % der Käufer mit Verlust laut Nansen)',
    slides=[
        s_hook('STATEMENT', 'Wirbt ein bekanntes Gesicht für einen Coin, %s' % A('kaufe ich keinen Cent.'),
               sub='Für viele ist ein Promi der Beweis. Für mich ist er ein Warnsignal. So ein Coin hat mich 5.000 $ gekostet.',
               cue='Was mich 5.000 $ gekostet hat &#8594;', size=''),
        s_proof('MEIN BELEG', 'Ein Influencer-Coin. Das Gesicht kannte ich. Den Coin kaum.',
                big='5.000 $', big_sub='hab ich in diesen Coin gesteckt. Das Geld ist weg.',
                cue='Dann kam der Coin mit dem Präsidenten &#8594;'),
        s_proof('KEIN EINZELFALL', 'LIBRA wurde durch einen Post des Präsidenten von Argentinien bekannt.',
                big='86 %', big_sub='der Käufer verkauften mit Verlust. Zusammen rund 251 Mio. $.',
                src=Q_NANSEN, cue='Warum das Gesicht dich blind macht &#8594;'),
        s_point('WARUM', 'Das Gesicht leiht dir Vertrauen. %s' % A('Das Wissen fehlt trotzdem.'),
                ['Du kaufst, weil du die Person kennst. Den Coin kennst du kaum.',
                 D('Wer hat ihn gebaut? Wer hält wie viel? Das zeigt dir kein Gesicht.')],
                cue='Heißt das, jeder Promi lügt? &#8594;'),
        s_point('FAIR BLEIBEN', 'Will jeder Promi dein Geld? %s' % A('Nein.'),
                ['Viele wissen selbst kaum, wofür sie werben.',
                 D('Für dein Geld ist das egal. Ein Gesicht ersetzt kein Verstehen.')],
                cue='Worauf ich statt des Gesichts schaue &#8594;'),
        s_point('MEINE REGEL', 'Ich schaue auf den Coin, %s' % A('nie auf das Gesicht.'),
                ['Wer hat ihn gebaut, und wer antwortet auf Fragen? Kann ich ihn in zwei Sätzen erklären?',
                 D('Bleibt eine Antwort aus, bleibt mein Geld, wo es ist.')],
                cue='Dein Merkzettel zum Speichern &#8594;'),
        s_memo('ZUM SPEICHERN', 'Bevor dich ein Gesicht überzeugt, %s' % A('in 4 Zeilen.'), 'Dein Merkzettel', [
            'Ein bekanntes Gesicht ist kein Beleg.',
            'Wer hat den Coin gebaut? Ohne Antwort kein Kauf.',
            'Kannst du ihn in zwei Sätzen erklären?',
            'Eile und Hype im Feed heißen: warten.',
        ], 'Schick das jemandem, der gerade einen Promi-Coin kaufen will.'),
    ],
    alts=['Statement: Wirbt ein bekanntes Gesicht für einen Coin, kaufe ich keinen Cent. Für viele ist ein Promi der Beweis, für mich ein Warnsignal. So ein Coin hat mich 5.000 Dollar gekostet',
          'Mein Beleg: Ein Influencer-Coin. Das Gesicht kannte ich, den Coin kaum. 5.000 Dollar hab ich in diesen Coin gesteckt, das Geld ist weg',
          'Kein Einzelfall: LIBRA wurde durch einen Post des Präsidenten von Argentinien bekannt. 86 Prozent der Käufer verkauften mit Verlust, zusammen rund 251 Millionen Dollar. Quelle: Nansen Research, Februar 2025',
          'Warum: Das Gesicht leiht dir Vertrauen, das Wissen fehlt trotzdem. Wer hat den Coin gebaut, wer hält wie viel? Das zeigt dir kein Gesicht',
          'Fair bleiben: Will jeder Promi dein Geld? Nein. Viele wissen selbst kaum, wofür sie werben. Für dein Geld ist das egal, ein Gesicht ersetzt kein Verstehen',
          'Meine Regel: Ich schaue auf den Coin, nie auf das Gesicht. Wer hat ihn gebaut, wer antwortet auf Fragen, kann ich ihn in zwei Sätzen erklären? Bleibt eine Antwort aus, bleibt mein Geld, wo es ist',
          'Merkzettel, bevor dich ein Gesicht überzeugt: ein bekanntes Gesicht ist kein Beleg; wer hat den Coin gebaut, ohne Antwort kein Kauf; kannst du ihn in zwei Sätzen erklären; Eile und Hype im Feed heißen warten. Schick das jemandem, der gerade einen Promi-Coin kaufen will'],
    caption='''Ein bekanntes Gesicht hat mich 5.000 $ gekostet. Seitdem ist es für mich ein Warnsignal.

Damals hab ich 5.000 $ in einen Influencer-Coin gesteckt. Das Gesicht kannte ich. Den Coin kannte ich kaum. Das Geld ist weg.

Kein Einzelfall:
– LIBRA wurde durch einen Post des Präsidenten von Argentinien bekannt.
– 86 % der Käufer verkauften mit Verlust, zusammen rund 251 Mio. $ (Quelle: Nansen Research, Februar 2025; gezählt wurden Wallets mit über 1.000 $ Gewinn oder Verlust).

Warum das Gesicht so gefährlich ist:
– Es leiht dir Vertrauen. Das Wissen über den Coin fehlt trotzdem.
– Wer ihn gebaut hat und wer wie viel hält, zeigt dir kein Gesicht.

Will jeder Promi dein Geld? Nein. Viele wissen selbst kaum, wofür sie werben. Für dein Geld ist das egal. Ein Gesicht ersetzt kein Verstehen.

Dein Merkzettel:
– Ein bekanntes Gesicht ist kein Beleg.
– Wer hat den Coin gebaut? Ohne Antwort kein Kauf.
– Kannst du ihn in zwei Sätzen erklären?
– Eile und Hype im Feed heißen: warten.

Keine Coin-Empfehlung, keine Kursprognose. Nur mein Lehrgeld gegen Betrug mit Promi-Coins, für jeden Anfänger, der Bitcoin, Krypto und die erste Börse gerade entdeckt.

Hast du schon mal einen Coin gekauft, weil ein bekanntes Gesicht dafür warb? Schreib Ja oder Nein in die Kommentare.

Schick das jemandem, der gerade einen Promi-Coin kaufen will.''')

# ---------- Beitrag 39: Gegenueberstellung (Fall Lena: Hilfe in der Krypto-Gruppe, falscher Support, rund 1.000 €; Was er schreibt vs. was es heisst) ----------
Q_MIMIKAMA = 'Quelle: Mimikama, „Telegram-Betrug erkennen“'
POSTS['beitrag-39'] = dict(
    date='2026-11-05', fmt='Gegenüberstellung', topic='Fall Lena: In der Krypto-Gruppe um Hilfe gebeten, der falsche „Support“ kostete rund 1.000 €; was er schreibt vs. was es heißt (Mimikama)',
    slides=[
        s_vs('ECHTER FALL · NAME GEÄNDERT', 'Lena bat eine Krypto-Gruppe um Hilfe. Kosten: %s' % A('rund 1.000 €.'),
             'ER SCHREIBT', ['„Schicken Sie mir einen Screenshot …“', '„Die Münze steigt jetzt …“', '„… unsere Dapp senden …“', '„Sie werden sicherlich Ihr gesamtes Geld zurückbekommen.“'],
             'DAS HEISST', ['Er sieht, was du hast', 'Eile soll dich blind machen', 'Ein fremder Link greift nach deiner Wallet', 'Wer alles verspricht, will mehr'],
             'Schick das jemandem, der in Krypto-Gruppen um Hilfe fragt.', src=Q_MIMIKAMA),
    ],
    alts=['Gegenüberstellung, echter Fall, Name geändert: Lena bat eine Krypto-Gruppe um Hilfe. Kosten: rund 1.000 Euro. Der falsche Support schreibt: Schicken Sie mir einen Screenshot; die Münze steigt jetzt; unsere Dapp senden; Sie werden sicherlich Ihr gesamtes Geld zurückbekommen. Das heißt: Er sieht, was du hast; Eile soll dich blind machen; ein fremder Link greift nach deiner Wallet; wer alles verspricht, will mehr. Quelle: Mimikama, Telegram-Betrug erkennen. Schick das jemandem, der in Krypto-Gruppen um Hilfe fragt'],
    caption='''Sie wollte Hilfe. Sie bekam einen „Support“, der freundlich war bis zum Schluss.

Echter Fall aus meiner Community, Name geändert, veröffentlicht mit Zustimmung: Lena bat in einer Krypto-Gruppe um Hilfe. Ein falscher „Community Support“ meldete sich. Sie folgte seinen Anweisungen. Währenddessen wurde ihre Wallet leergeräumt. In wenigen Wochen waren rund 1.000 € aus zwei Wallets weg.

Was der „Support“ ihr schrieb, und was es heißt:
– „Schicken Sie mir einen Screenshot … damit ich sehen kann.“ Er will sehen, was in deiner Wallet liegt.
– „Die Münze steigt jetzt, also ist es zu Ihrem eigenen Vorteil …“ Eile mit dem Kurs ist Druck, keine Hilfe.
– „… damit ich Ihnen unsere Dapp senden kann, um die Wallet vor unbekannten internen Hacks zu schützen.“ Ein fremder Link, über den du deine Wallet verbinden sollst.
– „Sie werden sicherlich Ihr gesamtes Geld zurückbekommen.“ Wer dir alles zurück verspricht, will meist mehr.

Lena schrieb mir: „Mir schreibt unter Deinem Namen jemand und bedrängt mich.“ Sie hat den „Support“ blockiert und sich Hilfe vor Ort gesucht.

Behauptet jemand, Admin, Support oder ein Unternehmen zu sein, geh selbst auf die offizielle Seite und nimm dort Kontakt auf (Quelle: Mimikama, „Telegram-Betrug erkennen“). Nie über einen Link aus dem Chat.

Keine Anbieter-Empfehlung. Nur ein echter Fall, damit du Betrug in Krypto-Gruppen erkennst, bevor deine Wallet leer ist. Für jeden Anfänger, der mit Bitcoin, Wallet und Börse gerade anfängt.

Welcher der 4 Sätze hätte dich am ehesten überzeugt? Schreib die Zahl in die Kommentare.

Schick das jemandem, der in Krypto-Gruppen um Hilfe fragt.''')

# ---------- Beitrag 40: Nischenmythos (Wallet verifizieren ist wie Ausweis zeigen; AML-Supporter, vier Wallets leer) ----------
Q_TOFR = 'Quelle: Börse Stuttgart Digital Exchange, „Was bedeutet die Transfer of Funds Regulation?“'
Q_SEED = 'Quelle: boerse.de, Börsenlexikon „Seed Phrase“'
POSTS['beitrag-40'] = dict(
    date='2026-11-06', fmt='Nischenmythos entlarven', topic='Mythos: „Wallet verifizieren ist wie Ausweis zeigen“ (Fall Elena, Markus, Leon, Sabine: falscher AML-Supporter, 4 von 4 gaben die Seed-Phrase; Travel Rule echt, Prüfung ohne Wörter)',
    slides=[
        s_hook('MYTHOS', '„Wallet verifizieren ist wie %s“' % A('Ausweis zeigen.'),
               sub='4 Menschen aus meiner Community haben das geglaubt. Danach waren 4 Wallets leer. Wo der Unterschied liegt.',
               cue='Was die vier geschrieben bekamen &#8594;'),
        s_proof('ECHTE FÄLLE · NAMEN GEÄNDERT', 'Eine Nachricht. Vier leere Wallets.',
                big='4 von 4', big_sub='gaben einem „AML-Supporter“ ihre Seed-Phrase. Er schrieb: Wegen neuer Geldwäscheregeln müsst ihr eure Wallet verifizieren.',
                ps=[D('Elena, Markus, Leon und Sabine. Danach war das Geld weg.')],
                cue='Warum die Nachricht so echt klang &#8594;'),
        s_point('WARUM ES ECHT KLINGT', 'Die Regeln gibt es %s' % A('wirklich.'),
                ['Seit dem 30.12.2024 gilt in der EU die Travel Rule. Bei Transfers ab 1.000 € an oder von einer eigenen Wallet will die Börse einen Nachweis, dass sie dir gehört.',
                 D('Der Betrüger leiht sich ein echtes Gesetz.')],
                src=Q_TOFR, size='m', cue='Der Unterschied, der alles entscheidet &#8594;'),
        s_point('DIE WAHRHEIT', 'Dein Ausweis zeigt, wer du bist. Deine 12 Wörter %s' % A('sind dein Geld.'),
                ['Wer deinen Ausweis sieht, kennt deinen Namen.',
                 D('Wer deine 12 Wörter hat, braucht kein Handy und keine PIN. Er hat die Wallet.')],
                size='m', cue='So sieht eine echte Prüfung aus &#8594;'),
        s_point('ECHTE PRÜFUNG', 'Eine echte Prüfung braucht %s' % A('deine Wörter nie.'),
                ['Sie kommt im Konto deiner Börse, in der App, die du selbst öffnest. Der Nachweis läuft zum Beispiel über einen kleinen Testbetrag.',
                 D('Seriöse Anbieter brauchen die Seed-Phrase nie, um eine Wallet zu prüfen.')],
                src='%s; %s' % (Q_TOFR, Q_SEED.replace('Quelle: ', '')), size='m', cue='Dein Test in 5 Sekunden &#8594;'),
        s_memo('ZUM SPEICHERN', 'Prüfung oder %s' % A('Raub?'), 'Dein Merkzettel', [
            'Ausweis hochladen in deiner Börsen-App: normal.',
            'Privatnachricht von einem „Supporter“: kein Support.',
            'Neue Gesetze als Grund? Prüfe in der App, nie im Chat.',
            'Deine 12 Wörter in Chat oder Formular: nie.',
        ], 'Schick das jemandem, der gerade seine erste Wallet eingerichtet hat.'),
    ],
    alts=['Mythos: Wallet verifizieren ist wie Ausweis zeigen. 4 Menschen aus meiner Community haben das geglaubt, danach waren 4 Wallets leer. Wo der Unterschied liegt',
          'Echte Fälle, Namen geändert: Eine Nachricht, vier leere Wallets. 4 von 4 gaben einem AML-Supporter ihre Seed-Phrase, wegen angeblich neuer Geldwäscheregeln. Elena, Markus, Leon und Sabine, danach war das Geld weg',
          'Warum es echt klingt: Die Regeln gibt es wirklich. Seit dem 30.12.2024 gilt in der EU die Travel Rule, bei Transfers ab 1.000 Euro will die Börse einen Nachweis, dass die eigene Wallet dir gehört. Der Betrüger leiht sich ein echtes Gesetz. Quelle: Börse Stuttgart Digital Exchange',
          'Die Wahrheit: Dein Ausweis zeigt, wer du bist. Deine 12 Wörter sind dein Geld. Wer sie hat, braucht kein Handy und keine PIN, er hat die Wallet',
          'Echte Prüfung: Sie braucht deine Wörter nie. Sie kommt im Konto deiner Börse, der Nachweis läuft zum Beispiel über einen kleinen Testbetrag. Seriöse Anbieter brauchen die Seed-Phrase nie. Quelle: Börse Stuttgart Digital Exchange, boerse.de',
          'Merkzettel, Prüfung oder Raub: Ausweis hochladen in deiner Börsen-App ist normal; Privatnachricht von einem Supporter ist kein Support; neue Gesetze als Grund, prüfe in der App, nie im Chat; deine 12 Wörter in Chat oder Formular: nie. Schick das jemandem, der gerade seine erste Wallet eingerichtet hat'],
    caption='''Ein Gesetz gibt es wirklich. Die Nachricht dazu war trotzdem Betrug.

Der Mythos: „Wallet verifizieren ist wie Ausweis zeigen.“ Klingt harmlos. Bei deiner Börse lädst du ja auch deinen Ausweis hoch.

Echte Fälle aus meiner Community, Namen geändert, veröffentlicht mit Zustimmung: Elena, Markus, Leon und Sabine bekamen eine Nachricht von einem angeblichen „AML-Supporter“. AML steht für Anti-Geldwäsche. Wegen neuer Geldwäscheregeln müssten sie ihre Wallet aktualisieren und verifizieren. Dafür wollte er ihre Seed-Phrase. Alle vier haben sie herausgegeben. Danach war das Geld weg.

Warum die Nachricht so echt klang:
– Seit dem 30.12.2024 gilt in der EU die Travel Rule. Bei Transfers ab 1.000 € an oder von einer eigenen Wallet will die Börse einen Nachweis, dass die Wallet dir gehört (Quelle: Börse Stuttgart Digital Exchange, „Was bedeutet die Transfer of Funds Regulation?“).
– Der Betrüger leiht sich ein echtes Gesetz.

Der Unterschied:
– Dein Ausweis zeigt, wer du bist.
– Deine 12 Wörter sind dein Geld. Wer sie hat, braucht kein Handy und keine PIN. Er hat die Wallet.

So sieht eine echte Prüfung aus:
– Sie kommt im Konto deiner Börse, in der App, die du selbst öffnest.
– Der Nachweis läuft zum Beispiel über einen kleinen Testbetrag.
– Seriöse Anbieter brauchen die Seed-Phrase nie, um eine Wallet zu prüfen (Quelle: boerse.de, Börsenlexikon „Seed Phrase“).

Dein Merkzettel:
– Ausweis hochladen in deiner Börsen-App: normal.
– Privatnachricht von einem „Supporter“: kein Support.
– Neue Gesetze als Grund? Prüfe in der App, nie im Chat.
– Deine 12 Wörter in Chat oder Formular: nie.

Keine Anbieter-Empfehlung. Nur echte Fälle, damit du Betrug rund um Wallet und Börse erkennst, bevor dein Bitcoin weg ist. Für jeden Krypto-Anfänger.

Hat dich schon mal jemand gebeten, deine Wallet zu „verifizieren“? Schreib Ja oder Nein in die Kommentare.

Schick das jemandem, der gerade seine erste Wallet eingerichtet hat.''')

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
