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
