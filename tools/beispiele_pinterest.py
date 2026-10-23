# Erste Pins fuer Pinterest (ab 01.10.2026), ein Pin pro Tag. Zeiten Europe/Berlin.
# Jeder Eintrag: d, t, board (exakter Name der Pinnwand), f (Format), farbe (schwarz/hell/akzent), titel (Pin-Titel,
# Keyword zuerst, bis 100 Zeichen), text (Beschreibung, bis 500 Zeichen, ohne Hashtags: Pinterest ordnet ueber
# Suchbegriffe ein; hier steht die Geschichte, das Bild traegt nur das Was), alt (Alt-Text), bild (Dateiname unter
# pinterest/), build (Bildfunktion); Karussell: folien=N und Dateien pinterest/p-N-1.png bis p-N-4.png, alts je Folie.
# Bilder rendern: python3 tools/beispiele_pinterest.py [p-N ...]
# (OUT und NM als Umgebungsvariablen, siehe gen.py)
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from pin_gen import *

LINK = 'https://chrisalcatrez.de'
IMG = 'https://raw.githubusercontent.com/chrisalcatrez/chrisalcatrez/main/pinterest/%s.png'

def pin_link(bild):
    # Ziel jedes Pins: das kostenlose Training; UTM-Parameter, damit Pinterest-Klicks in der Auswertung erkennbar sind
    return '%s/?utm_source=pinterest&utm_medium=pin&utm_content=%s' % (LINK, bild)

# Pinnwände (exakte Namen; Beschreibungen in themen-pinterest.md). ALIASE: frühere Namensvorschläge, die der Nutzer
# ebenfalls angelegt haben kann; beim Einplanen zuerst den Hauptnamen, dann die Aliase probieren.
B_ANF = 'Krypto für Anfänger'
B_BET = 'Krypto-Betrug erkennen'
B_SIC = 'Bitcoin sicher aufbewahren'
B_INF = 'Geld anlegen und Inflation'
ALIASE = {B_SIC: ['Bitcoin Wallet und Sicherheit'], B_INF: ['Geld vor Inflation schützen', 'Inflation und Geldentwertung']}
# Pinterest-IDs der Pinnwände (seit 30.09.2026 angelegt); beim Einplanen die ID als boardId verwenden.
BOARD_ID = {B_ANF: '1101693196287264183', B_BET: '1101693196287264186', B_SIC: '1101693196287264188', B_INF: '1101693196287264189'}
# Erste Pinnwand des Kontos: 'Krypto', Pinterest-ID 1101693196287264156. Nur Rückfall, falls eine Themen-Pinnwand fehlt.
B_FALLBACK = 'Krypto'
B_FALLBACK_ID = '1101693196287264156'

PINS = [
 dict(d='2026-10-01', t='20:17', board=B_BET, f='Checkliste', farbe='schwarz', bild='p-1',
      titel='Krypto-Betrug erkennen: 5 Zeichen, dass eine Wallet-App gefälscht ist',
      text="""Gefälschte Krypto-Apps sehen aus wie das Original: gleiches Logo, gleicher Name, gute Bewertungen. Mich hat so eine Wallet-App 70.000 $ gekostet. Diese 5 Zeichen prüfe ich seitdem vor jedem Download, in einer Minute. Bitcoin und Krypto für Anfänger, ohne Fachchinesisch, aus eigener Erfahrung. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training (Link).""",
      alt='Checkliste mit fünf Icons: Zeichen, an denen man eine gefälschte Krypto-Wallet-App erkennt.',
      build=lambda: build_pin('p-1', [pin_check('Checkliste', 'shield-check',
          'Gefälschte App?<br>5 Zeichen.',
          [('link', 'Link aus Chat, Mail oder Anzeige'),
           ('globe', 'Auf der Anbieter-Website fehlt die App'),
           ('user', 'Name des Entwicklers passt nur fast'),
           ('star', 'Nur frische 5-Sterne-Bewertungen'),
           ('key', 'Fragt zuerst nach den 12 Wörtern')],
          lead='Mich hat so eine App <b>70.000 $</b> gekostet.', size='sm')])),

 dict(d='2026-10-02', t='20:41', board=B_ANF, f='Mythos', farbe='hell', bild='p-2',
      titel='Krypto ist doch alles Betrug? Mythos und Wirklichkeit nach 70.000 $ Verlust',
      text="""Krypto ist alles Betrug, den Satz hab ich früher selbst gesagt, nachdem mich zwei Betrüger erwischt hatten. Heute unterscheide ich: Betrogen haben mich Menschen mit gefälschten Apps, erfundenen Gebühren und falschem Support. Bitcoin selbst hat keinen Chef, der dich anruft. Was Anfänger schützt, ist ein einfaches System und Geduld. Krypto verständlich erklärt aus eigener Erfahrung, das kostenlose Training findest du über den Link.""",
      alt='Gegenüberstellung: Mythos „Krypto ist alles Betrug“ gegen das, was Chris Alcatrez erlebt hat.',
      build=lambda: build_pin('p-2', [pin_vs('Mythos-Check', 'help',
          '„Krypto ist doch alles Betrug.“',
          'Der Mythos', ['Bitcoin selbst ist die Masche', 'Wer einsteigt, wird abgezockt'],
          'Was ich erlebt habe', ['Betrogen haben mich Menschen: falsche App, falscher Support', 'Bitcoin hat keinen Chef, der dich anruft'],
          theme='light')])),

 dict(d='2026-10-03', t='21:05', board=B_SIC, f='Begriff erklärt', farbe='schwarz', bild='p-3',
      titel='Seed-Phrase erklärt: die 12 Wörter, die dein Bitcoin-Geld sind',
      text="""Seed-Phrase einfach erklärt: 12 oder 24 Wörter stellen deine Krypto-Wallet wieder her. Wer sie kennt, kann alles abräumen, ohne Passwort. Am Telefon wollte mal ein angeblicher Support meine 12 Wörter zum „Synchronisieren“. Ich hab ihm zwölf ausgedachte gegeben, er ist ausgerastet. Drei Regeln, mit denen die Wörter bei dir bleiben, stehen im Pin. Bitcoin-Sicherheit für Anfänger aus eigener Erfahrung, kostenloses Training über den Link.""",
      alt='Begriff erklärt: Seed-Phrase, zwölf Wort-Kacheln und drei Sätze, warum die Wörter dein Geld sind.',
      build=lambda: build_pin('p-3', [pin_term('Begriff erklärt', 'key', 'Seed-Phrase',
          '12 Wörter stellen deine Wallet wieder her. Wer sie hat, hat dein Geld.',
          [('shield', 'Niemand braucht sie außer dir'),
           ('lock', 'Kein Support, keine Börse, keine App braucht sie'),
           ('call', 'Wer danach fragt, will dein Geld')])])),

 dict(d='2026-10-04', t='11:23', board=B_ANF, f='Schritte (System-Teaser)', farbe='hell', bild='p-4',
      titel='Bitcoin für Anfänger: Wie ich heute mit 100 € starten würde (4 Schritte)',
      text="""Bitcoin für Anfänger, ohne 10.000 € und ohne Fachchinesisch. Ich hab am Anfang 70.000 $ verloren, weil ich schnell sein wollte. Heute würde ich mit 100 € anfangen, bei einer Börse mit Sitz in der EU, mit einer Wallet von der Website des Anbieters und ohne Chats mit Fremden über mein Geld. Die vier Schritte stehen im Pin, das System dahinter zeige ich im kostenlosen Training über den Link.""",
      alt='Vier nummerierte Schritte mit Pfeilen: Wie Chris Alcatrez heute mit 100 Euro in Krypto starten würde.',
      build=lambda: build_pin('p-4', [pin_flow('4-Schritte-Start', 'trend-up',
          'Mit 100 € in Krypto starten',
          ['Klein anfangen: 100 € statt 10.000 €',
           'Börse mit Sitz in der EU',
           'Eigene Wallet statt Börsen-Konto',
           'Kein Chat mit Fremden über dein Geld'],
          size='sm', theme='light')])),

 dict(d='2026-10-05', t='10:48', board=B_BET, f='Chat nachgestellt', farbe='schwarz', bild='p-5',
      titel='Netzwerkgebühr vor der Auszahlung? So erkennst du den Krypto-Betrug im Chat',
      text="""Krypto-Betrug im Chat erkennen: Ein angeblicher Support meldet eine Auszahlung, vorher soll eine „Netzwerkgebühr“ bezahlt werden. Bei mir kam die Nachricht damals über Instagram. Ich hab gezahlt, die Auszahlung kam nie. Eine echte Börse zieht Gebühren vom Guthaben ab, Vorkasse für die eigene Auszahlung verlangen nur Betrüger. Der Chat im Pin ist nachgestellt, meine Antwort darauf heute auch. Kostenloses Training über den Link.""",
      alt='Nachgestellter Chat im Handy-Rahmen: falscher Support verlangt vor der Auszahlung eine Netzwerkgebühr.',
      build=lambda: build_pin('p-5', [pin_chat('Nachgestellt', 'chat',
          'Gebühr vor der Auszahlung?',
          [('Support', 'Ihre Auszahlung ist freigegeben. Es fehlt nur die Netzwerkgebühr.', False),
           ('Ich', 'Zieht sie vom Guthaben ab.', True),
           ('Support', 'Das geht bei uns nur per Vorkasse.', False),
           ('Ich', 'Dann bleibt das Geld bei euch.', True)],
          lead='Vorkasse für die Auszahlung gibt es nie.')])),

 dict(d='2026-10-06', t='20:33', board=B_INF, f='Venezuela-Beobachtung', farbe='hell', bild='p-6',
      titel='Inflation verstehen: Was Venezuela mir über Erspartes zeigt',
      text="""Inflation und Geldentwertung sind in Venezuela kein Schulbuchthema, sie stehen an jeder Kasse. Preise in Dollar, Krypto im Alltag, digital bezahlt. Ich lebe hier freiwillig und sehe jeden Tag, was mit Erspartem passiert, das nur auf dem Konto liegt. Genau deshalb bin ich bei Krypto gelandet, erst mit Verlusten, dann mit einem einfachen System. Wie ich heute Erspartes und Krypto zusammendenke, zeige ich im kostenlosen Training über den Link.""",
      alt='Drei Icons mit Beobachtungen aus Venezuela: Preise in Dollar, Krypto im Alltag, Entwertung an der Kasse.',
      build=lambda: build_pin('p-6', [pin_check('Aus Venezuela', 'map-pin',
          'Inflation: Was Venezuela zeigt',
          [('tag', 'Preise stehen in Dollar'),
           ('phone', 'Krypto ist Alltag, digital bezahlt'),
           ('cart', 'Entwertung sieht man an der Kasse, nie auf dem Kontoauszug'),
           ('dollar', 'Die Landeswährung rechnet kaum jemand um')],
          lead='Ich lebe hier. Freiwillig.', size='sm', theme='light')])),

 dict(d='2026-10-07', t='20:12', board=B_ANF, f='FAQ', farbe='schwarz', bild='p-7',
      titel='Zu spät für Bitcoin? Was ich Anfängern 2026 antworte',
      text="""Ist es zu spät für Bitcoin? Die Frage stellen mir Anfänger am häufigsten. Ich hab sie mir selbst gestellt. Ende 2024 hab ich dann in Panik alles verkauft. Zu spät war ich nie, zu hastig schon. Was ich heute anders mache: Sparplan statt Timing, kleine Beträge, bis ich verstehe, was ich kaufe. Keine Kursprognose, keine Gewinnzusage, nur meine Erfahrung. Das System mit vier Schritten zeige ich im kostenlosen Training über den Link.""",
      alt='Frage und kurze Antwort: Ist es 2026 zu spät für Bitcoin? Dazu drei Stichworte aus der Erfahrung von Chris.',
      build=lambda: build_pin('p-7', [pin_faq('Anfänger-FAQ', 'help',
          'Bitcoin 2026:<br>Zu spät?',
          'Zu spät war ich nie. Zu hastig schon. Ende 2024 hab ich in Panik verkauft.',
          [('calendar', 'Sparplan statt Timing'), ('coins', 'Kleine Beträge zuerst'), ('eye', 'Verstehen, was du kaufst')], size='')])),

 # Ab Pin 8 (07.10.2026 umgebaut) gilt Stil 2: eine Aussage, ein Visual, drei bis fuenf Punkte, ein CTA; keine Badges, keine Icons.
 # Titel: Keyword + Schmerzpunkt + Nutzen, die wichtigsten Woerter in den ersten 40 Zeichen. Save Value: Regel, Checkliste, Zahl.
 dict(d='2026-10-08', t='20:26', board=B_ANF, f='Foto (Regeln)', farbe='schwarz', bild='p-8',
      titel='Krypto für Anfänger: 4 Regeln nach 70.000 $ Verlust',
      text="""Krypto für Anfänger, 4 Regeln aus 70.000 $ Lehrgeld: gefälschte Wallet-App, Gebühr vor der Auszahlung, Seed-Phrase am Telefon, Panikverkauf Ende 2024. Jede Regel im Pin hat mich vorher Geld gekostet. Heute lebe ich in Venezuela, zahle digital mit Krypto und arbeite mit einem einfachen System aus vier Schritten; ein fünfstelliger Gewinn im Jahr, meine Zahl, kein Versprechen für dich. Die 3 Fehlgriffe, an denen Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Krypto für Anfänger: vier Regeln nach 70.000 $ Verlust, darunter Chris Alcatrez im blauen Hemd.',
      build=lambda: build_pin('p-8', [pin2('', 'Krypto für Anfänger: <em>4 Regeln</em> nach 70.000 $ Verlust',
          points=['App nur vom Anbieter selbst', 'Keine Gebühr vor Auszahlung', '12 Wörter bekommt niemand', 'Sparplan statt Panikverkauf'],
          cta='Kostenloses Training: chrisalcatrez.de', size='xs', photo=True)])),

 dict(d='2026-10-09', t='11:37', board=B_BET, f='Beispielsatz (Sprechblase)', farbe='akzent', bild='p-9',
      titel='Krypto-Betrug erkennen: 4 Sätze, bei denen du sofort auflegst',
      text="""Krypto-Betrug erkennen, bevor Geld fließt: Vier Sätze tauchen in fast jeder Masche auf: Chat, Telefon, Mail. Satz 1 hab ich geglaubt und die Gebühr bezahlt, die Auszahlung kam nie. Satz 2 kam am Telefon, ich hab zwölf erfundene Wörter vorgelesen. Satz 3 kommt nach dem ersten Verlust, verkleidet als Kanzlei oder Behörde. Satz 4 hat mich 4.000 bis 5.000 $ Cloud-Mining gekostet. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Krypto-Betrug erkennen: vier Sätze von Betrügern, der erste groß in einer Sprechblase, drei weitere darunter.',
      build=lambda: build_pin('p-9', [pin2('acc', 'Krypto-Betrug erkennen: <em>4 Sätze</em>, bei denen du sofort auflegst',
          visual=vz_bubble('„Vor der Auszahlung fällt nur eine kleine Gebühr an.“', 'Satz 1, nachgestellt. Ich hab gezahlt. Die Auszahlung kam nie.'),
          points=['„Ich brauche kurz Ihre 12 Wörter.“', '„Wir holen Ihr Geld zurück, gegen Vorkasse.“', '„Garantierte Rendite, jeden Monat.“'],
          cta='Speichern für den nächsten „Support“-Chat', size='xs', quote=True, start=2)])),

 dict(d='2026-10-10', t='19:41', board=B_BET, f='Balken (Zahlen)', farbe='schwarz', bild='p-10',
      titel='Krypto-Betrug erkennen: 3 Maschen, die mich fast 80.000 $ gekostet haben',
      text="""Krypto-Betrug erkennen fängt bei den eigenen Zahlen an. Drei Maschen haben mich am Anfang fast 80.000 $ gekostet: eine gefälschte Wallet-App 70.000 $, ein Influencer-Coin 5.000 $, Cloud-Mining mit „garantierter“ Rendite 4.000 bis 5.000 $. Alle drei sahen echt aus, alle drei kamen über Menschen, denen ich vertraut habe. Woran ich sie heute am ersten Satz erkenne, steht im Pin. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Krypto-Betrug: drei Balken mit Verlusten, gefälschte Wallet-App 70.000 $, Influencer-Coin 5.000 $, Cloud-Mining.',
      build=lambda: build_pin('p-10', [pin2('', 'Krypto-Betrug: <em>3 Maschen</em>, die mich fast 80.000 $ gekostet haben',
          visual=vz_bars([('Gefälschte Wallet-App', '70.000 $', 100), ('Influencer-Coin', '5.000 $', 9), ('Cloud-Mining', '4.000–5.000 $', 8)]),
          points=['App aus einem Chat-Link', 'Coin mit Gesicht, ohne Team', 'Feste Rendite, jeden Monat'],
          cta='Speichern, bevor du das erste Mal kaufst', size='xs')])),

 dict(d='2026-10-11', t='11:08', board=B_ANF, f='Kurve (Regeln)', farbe='hell', bild='p-11',
      titel='Bitcoin Sparplan für Anfänger: 3 Regeln statt Timing',
      text="""Bitcoin Sparplan statt Timing: Ende 2024 hab ich alle Bitcoin in Panik verkauft, weil ich den richtigen Moment treffen wollte. Den gibt es für mich seitdem nur auf dem Kalender: fester Tag, feste Summe, der Kurs entscheidet nie. Die drei Regeln im Pin sind das, was ich seitdem anders mache. Keine Kursprognose, keine Gewinnzusage, meine Erfahrung nach 70.000 $ Lehrgeld. Wie der Sparplan in mein System mit vier Schritten passt, zeige ich im kostenlosen Training über den Link.""",
      alt='Bitcoin Sparplan für Anfänger: eine Kurve mit Punkten in festem Abstand und drei Regeln statt Timing.',
      build=lambda: build_pin('p-11', [pin2('light', 'Bitcoin Sparplan: <em>3 Regeln</em> statt Timing',
          visual=vz_curve('Fester Tag, feste Summe, egal wo der Kurs steht.'),
          points=['Ein fester Tag im Monat', 'Eine feste Summe, jedes Mal gleich', 'Der Kurs entscheidet nie'],
          cta='Speichern für deinen ersten Sparplan', size='sm')])),

 dict(d='2026-10-12', t='20:04', board=B_BET, f='Beispielsatz (Sprechblase)', farbe='schwarz', bild='p-12',
      titel='Falscher Support in Krypto-Gruppen: 5 Warnsignale, bevor dein Geld weg ist',
      text="""Falscher Support in Krypto-Gruppen: Lena (Name geändert) bat in einer Gruppe um Hilfe, ein „Community Support“ meldete sich privat. Sie folgte seinen Anweisungen, währenddessen wurde ihre Wallet leergeräumt, in wenigen Wochen rund 1.000 € aus zwei Wallets. Die Sätze im Pin stammen aus ihrem Chat. Echter Support schreibt dich nie zuerst privat an und will nie Screenshots deiner Konten. Lena hat den „Support“ blockiert und sich Hilfe vor Ort gesucht. Kostenloses Training über den Link.""",
      alt='Falscher Support in Krypto-Gruppen: eine echte Nachricht in einer Sprechblase und fünf Warnsignale.',
      build=lambda: build_pin('p-12', [pin2('', 'Falscher Support: <em>5 Warnsignale</em> in Krypto-Gruppen',
          visual=vz_bubble('„Schicken Sie mir einen Screenshot … damit ich sehen kann.“', 'Echte Nachricht. Fall aus meiner Community, Name geändert.'),
          points=['Schreibt dich privat an', 'Will Screenshots deiner Wallet', 'Drängt: „Die Münze steigt jetzt“', 'Schickt einen Link zum Schützen', 'Verspricht dein Geld zurück'],
          cta='Speichern, bevor du in einer Gruppe um Hilfe bittest', size='sm', dense=True)])),

 # Zweite Vorgabe vom 07.10.2026: Cheat-Sheet-Formate (Entscheidungsbaum, Echt gegen Fake, Karussell), Stempel-Optik,
 # Warnzeichen als Punktmarken, Lesezeichen oben rechts, situative Speicher-CTAs.
 dict(d='2026-10-13', t='11:46', board=B_BET, f='Entscheidungsbaum', farbe='hell', bild='p-13',
      titel='Krypto-Betrug erkennen: 3 Fragen, die es in 10 Sekunden zeigen',
      text="""Krypto-Betrug erkennen in 10 Sekunden: Drei Fragen stoppen die häufigsten Maschen, bevor Geld fließt. Jede davon hat mich früher Geld gekostet: feste Rendite beim Cloud-Mining (4.000 bis 5.000 $), die 12 Wörter am Telefon, die Gebühr vor der Auszahlung. Einmal Ja, und das Gespräch ist beendet. Speichern, dann hast du den Entscheidungsbaum vor der nächsten Überweisung parat. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Krypto-Betrug erkennen: Entscheidungsbaum mit drei Fragen, Ja heißt Betrug, Nein führt weiter.',
      build=lambda: build_pin('p-13', [pin2('light', 'Krypto-Betrug? <em>3 Fragen</em>, 10 Sekunden.',
          visual=vz_flow(['Verspricht man dir feste Rendite?', 'Will jemand deine 12 Wörter?', 'Gebühr, bevor du Geld bekommst?'],
                         'Kein Warnsignal. Trotzdem klein anfangen.'),
          cta='Speichern, bevor du das nächste Mal Geld überweist', size='sm')])),

 dict(d='2026-10-14', t='20:21', board=B_BET, f='Echt gegen Fake', farbe='schwarz', bild='p-14',
      titel='Echter Support vs. Fake: 3 Unterschiede im Krypto-Chat, die du sofort siehst',
      text="""Falscher Support im Krypto-Chat erkennen: Echter Support antwortet nur, wenn du fragst, will nie deine 12 Wörter und zieht Gebühren vom Guthaben ab. Der Fake schreibt dich zuerst privat an, will die 12 Wörter und verlangt Vorkasse. Zwei davon hab ich erlebt: Gebühr gezahlt, Auszahlung nie gekommen; am Telefon zwölf erfundene Wörter vorgelesen. Der Vergleich ist nachgestellt. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Echter Support gegen Fake im Krypto-Chat: links drei Haken, rechts drei Kreuze und ein Stempel Fake.',
      build=lambda: build_pin('p-14', [pin2('', 'Echter Support vs. Fake: <em>3 Unterschiede</em>',
          visual=vz_vs2('Echter Support', ['Antwortet nur, wenn du fragst', 'Fragt nie nach 12 Wörtern', 'Zieht Gebühren vom Guthaben ab'],
                        'Fake', ['Schreibt dich zuerst privat an', 'Will deine 12 Wörter', 'Gebühr vor der Auszahlung'],
                        note='Nachgestellt. Zwei der drei hab ich selbst erlebt.'),
          cta='Speichern für den nächsten „Support“-Chat', size='sm')])),

 dict(d='2026-10-15', t='11:03', board=B_BET, f='Karussell (4 Folien)', farbe='hell', bild='p-15', folien=4,
      titel='Krypto-Betrug erkennen: 3 Maschen, jede einzeln erklärt (fast 80.000 $ Lehrgeld)',
      text="""Krypto-Betrug erkennen an drei Maschen, jede auf einer eigenen Folie: die gefälschte Wallet-App (70.000 $, geladen, weil sie echt aussah), der Influencer-Coin (5.000 $, bekanntes Gesicht, unbekanntes Team, Rug Pull) und Cloud-Mining mit fester Rendite (4.000 bis 5.000 $). Zusammen fast 80.000 $ Lehrgeld. Jede Folie nennt zwei Zeichen, an denen ich die Masche heute erkenne. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Karussell: Stempel Betrug, dann drei Folien mit 70.000 $, 5.000 $ und 4.000 $ Verlust und je zwei Warnzeichen.',
      alts=['Fast 80.000 $ weg, drei Maschen, Stempel Betrug.', 'Masche 1: gefälschte Wallet-App, 70.000 $, zwei Warnzeichen.', 'Masche 2: Influencer-Coin, 5.000 $, zwei Warnzeichen.', 'Masche 3: Cloud-Mining mit fester Rendite, 4.000 bis 5.000 $, zwei Warnzeichen.'],
      build=lambda: build_pin('p-15', [
          pin2('light', 'Fast 80.000 $ weg. <em>3 Maschen.</em>', visual=vz_stamp('Betrug', 'Drei Maschen, die mich als Anfänger erwischt haben. Eine pro Folie.'),
               cta='Speichern. Jede Masche einzeln auf den nächsten Folien', size='', center=True),
          pin2('light', 'Masche 1: Die gefälschte <em>Wallet-App</em>', visual=vz_num('70.000 $', 'Geladen, weil sie echt aussah. Den Anbieter gab es als App nie.'),
               points=['App nur vom Anbieter selbst', 'Kein Link aus Chat oder Mail'], marks='warn', cta='Speichern, bevor du die nächste App lädst', size='sm'),
          pin2('light', 'Masche 2: Der <em>Influencer-Coin</em>', visual=vz_num('5.000 $', 'Bekanntes Gesicht, unbekanntes Team. Rug Pull.'),
               points=['Macher verkaufen auf einmal', 'Kurs senkrecht nach unten'], marks='warn', cta='Speichern, bevor du einem Gesicht Geld gibst', size='sm'),
          pin2('light', 'Masche 3: <em>Cloud-Mining</em> mit fester Rendite', visual=vz_num('4.000 $', 'Bis 5.000 $. Feste Rendite, jeden Monat versprochen.'),
               points=['Rendite fest, egal was passiert', 'Auszahlung bleibt aus'], marks='warn', cta='Speichern, bevor du Rendite garantiert bekommst', size='sm'),
      ])),

 dict(d='2026-10-15', t='20:47', board=B_BET, f='Beispielsatz (Sprechblase)', farbe='akzent', bild='p-16',
      titel='Phishing Krypto erkennen: 3 Warnsignale in der Mail, die deine Wallet sperren will',
      text="""Phishing Krypto kommt oft als Mail mit Frist. Angeblich wird deine Wallet gesperrt, nur der Link soll helfen. Dahinter fragt eine gefälschte Seite deine 12 Wörter ab (Quellen: Verbraucherzentrale, „Phishing-Mails: Woran Sie sie erkennen“; Kantonspolizei Zürich). Druck kenn ich auch ohne Betrüger. Ende 2024 hab ich alle Bitcoin in Panik verkauft. In meinem System kommt Eile nie vor. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Phishing Krypto: nachgestellte Mail droht mit Wallet-Sperre in 24 Stunden, darunter drei Warnsignale vor dem Klick.',
      build=lambda: build_pin('p-16', [pin2('acc', 'Phishing bei Krypto: <em>3&nbsp;Warnsignale</em> vor dem Klick',
          visual=vz_bubble('„Ihre Wallet wird in 24 Stunden gesperrt. Jetzt bestätigen.“', 'Nachgestellt. Die Frist soll dich hetzen.'),
          points=['Anrede ohne deinen Namen', 'Kurze Frist plus Drohung', 'Link will deine 12 Wörter'],
          marks='warn', cta='Speichern für die nächste Mail mit Frist', size='sm')])),
 dict(d='2026-10-16', t='10:34', board=B_INF, f='Balken (Zahlen)', farbe='schwarz', bild='p-17',
      titel='Inflation frisst Erspartes: 10.000 € auf dem Konto, nur 8.200 € Kaufkraft (3 Schritte)',
      text="""Inflation frisst Erspartes leise. Von 2020 bis 2025 stiegen die Verbraucherpreise in Deutschland um 21,9 % (Quelle: Statistisches Bundesamt, Verbraucherpreisindex). 10.000 € ohne Zinsen kaufen danach nur so viel wie vorher rund 8.200 €. Auf dem Konto steht die alte Zahl. Ich lebe in Venezuela, Preise stehen hier in Dollar. Was Entwertung mit Erspartem macht, sieht man hier jeden Tag. Wie ich nach 70.000 $ Lehrgeld heute mit Krypto umgehe, zeige ich im kostenlosen Training über den Link.""",
      alt='Inflation und Erspartes: zwei Balken, Kontostand 10.000 €, Kaufkraft nach 5 Jahren 8.200 €, darunter drei Rechenschritte.',
      build=lambda: build_pin('p-17', [pin2('', 'Inflation: 10.000&nbsp;€ Erspartes, nur <em>8.200&nbsp;€</em> Kaufkraft',
          visual=vz_bars([('Kontostand', '10.000 €', 100), ('Kaufkraft nach 5 Jahren', '8.200 €', 82)], 'Deutschland: Preise plus 21,9 % in fünf Jahren.'),
          points=['Zins minus Inflation rechnen', 'Unter null: Kaufkraft sinkt', 'Einmal im Jahr prüfen'],
          cta='Speichern für den nächsten Kontoauszug', size='xs')])),

 dict(d='2026-10-16', t='20:58', board=B_ANF, f='Kurve (Regeln)', farbe='hell', bild='p-18',
      titel='Bitcoin für Anfänger: Kurs fällt? 3 Regeln gegen den Panikverkauf',
      text="""Bitcoin für Anfänger hat einen Moment, den fast jeder erlebt. Der Kurs fällt, und der Finger liegt schon auf Verkaufen. Ende 2024 hab ich in so einem Moment alle Bitcoin verkauft. Entschieden hat damals meine Angst, einen Plan gab es keinen. Danach hab ich Schritt für Schritt verstanden, was ich kaufe. Die drei Regeln im Pin hätten mich gebremst. Wohin der Kurs läuft, weiß ich so wenig wie du. Mein System mit vier Schritten zeige ich im kostenlosen Training über den Link.""",
      alt='Bitcoin für Anfänger: Kurve mit einem Kreuz am Tiefpunkt für den Panikverkauf, darunter drei Regeln.',
      build=lambda: build_pin('p-18', [pin2('light', 'Bitcoin fällt? <em>3&nbsp;Regeln</em> gegen den&nbsp;Panikverkauf',
          visual=vz_curve('Hier hab ich alles verkauft. In Panik.', marks='x'),
          points=['Plan steht vor dem Kauf', 'Nur kaufen, was du verstehst', 'Eine Nacht drüber schlafen'],
          cta='Speichern für den nächsten Kurssturz', size='sm')])),

 # Ab 17.10.2026 zwei Pins pro Tag (Vormittag und Abend, am Wochenende 10 bis 13 und 19 bis 21 Uhr).
 dict(d='2026-10-17', t='11:14', board=B_ANF, f='Zahl', farbe='schwarz', bild='p-19',
      titel='Bitcoin oder Altcoins? 4 Fragen vor jedem Coin-Kauf (mein 5.000 $ Influencer-Coin)',
      text="""Bitcoin oder Altcoins? Einer meiner Altcoins kam mit bekanntem Gesicht. Gewusst hab ich nur, wer ihn empfahl. Die Macher verkauften auf einmal, der Kurs fiel senkrecht, 5.000 $ weg. Heute stelle ich vor jedem Kauf vier Fragen, sie stehen im Pin. Fehlt mir eine Antwort, bleibt das Geld, wo es ist. Keine Coin-Empfehlung, nur mein Lehrgeld. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Bitcoin oder Altcoins: große Zahl 5.000 $ für einen Influencer-Coin, darunter vier Fragen vor jedem Kauf.',
      build=lambda: build_pin('p-19', [pin2('', 'Bitcoin oder Altcoin? <em>4&nbsp;Fragen</em> vor jedem Kauf',
          visual=vz_num('5.000 $', 'Ein Coin mit bekanntem Gesicht. Die Macher verkauften auf einmal.'),
          points=['Wer hat den Coin gemacht?', 'Wer hält den Großteil?', 'Warum kenne ich ihn?', 'Wofür gibt es ihn?'],
          cta='Speichern, bevor du den nächsten Coin kaufst', size='sm')])),

 dict(d='2026-10-17', t='20:22', board=B_BET, f='Stempel', farbe='hell', bild='p-20',
      titel='Cloud-Mining Betrug erkennen: 3 Warnsignale, bevor du einzahlst (4.000 $ Lehrgeld)',
      text="""Cloud-Mining Betrug fängt mit einem Versprechen an. Feste Rendite, jeden Monat. Ich hab 4.000 bis 5.000 $ in so ein Angebot gesteckt. Rechner hab ich nie gesehen, das Geld auch nie wieder. Krypto-Kurse schwanken jeden Tag. Wer dir trotzdem eine feste Rendite verspricht, verspricht etwas, das er selbst nie wissen kann. Die drei Warnsignale im Pin hätten mir damals gereicht. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Cloud-Mining Betrug: Stempel Garantie schräg im Rahmen, darunter drei Warnsignale mit Warnzeichen.',
      build=lambda: build_pin('p-20', [pin2('light', 'Cloud-Mining Betrug: <em>3&nbsp;Warnsignale</em> vor der Einzahlung',
          visual=vz_stamp('Garantie', 'Das Wort hat mich beim Cloud-Mining 4.000 bis 5.000 $ gekostet.', small=True),
          points=['Feste Rendite, jeden Monat', 'Rechner, die du nie siehst', 'Vom Risiko kein Wort'],
          marks='warn', cta='Speichern für die nächste Rendite-Werbung', size='sm', center=True)])),

 dict(d='2026-10-18', t='10:41', board=B_SIC, f='Foto', farbe='schwarz', bild='p-21',
      titel='Krypto Wallet für Anfänger: 4 Regeln, bevor Geld reingeht (nach 70.000 $ in einer falschen App)',
      text="""Krypto Wallet statt Börse, der Satz fällt in jeder Anfängergruppe. Bei mir hat die eigene Wallet 70.000 $ gekostet. Eine gefälschte App, geladen, weil sie echt aussah. Eine Handy-App hatte der Anbieter nie. Seitdem kommt eine Wallet bei mir nur über die Website des Anbieters aufs Handy, und bevor Geld reingeht, geht erst ein kleiner Betrag rein. Die vier Regeln im Pin sind mein Mindestmaß. Wie die Wallet in mein System mit vier Schritten passt, zeige ich im kostenlosen Training über den Link.""",
      alt='Krypto Wallet für Anfänger: vier Regeln, bevor Geld in die Wallet geht, darunter Chris Alcatrez im blauen Hemd.',
      build=lambda: build_pin('p-21', [pin2('', 'Krypto Wallet: <em>4&nbsp;Regeln</em>, bevor Geld reingeht',
          points=['Download nur beim Anbieter', 'Erst ein kleiner Testbetrag', 'Die 12 Wörter bleiben bei dir', 'Keine App aus einem Chat'],
          cta='Kostenloses Training: chrisalcatrez.de', size='sm', photo=True)])),

 dict(d='2026-10-18', t='19:53', board=B_ANF, f='Entscheidungsbaum', farbe='hell', bild='p-22',
      titel='Bitcoin kaufen für Anfänger: 3 Fragen vor dem ersten Kauf, einmal Ja heißt warten',
      text="""Bitcoin kaufen als Anfänger, bei mir lief das anders herum. Erst gekauft, dann verstanden. Ende 2024 hab ich alle Bitcoin in Panik verkauft, weil ich vorher nie gefragt hatte, warum ich überhaupt kaufe. Die drei Fragen im Pin stelle ich mir seitdem vor jedem Kauf. Einmal Ja, und ich warte. Dreimal Nein, dann klein, an einem festen Tag, mit fester Summe. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Bitcoin kaufen für Anfänger: Entscheidungsbaum mit drei Fragen, Ja heißt warten, Nein führt zum nächsten Schritt.',
      build=lambda: build_pin('p-22', [pin2('light', 'Bitcoin kaufen? <em>3 Fragen</em>, bevor du klickst',
          visual=vz_flow(['Brauchst du das Geld bald wieder?', 'Kaufst du, weil der Kurs läuft?', 'Kaufst du, weil alle drin sind?'],
                         'Dann klein anfangen. Fester Tag, feste Summe.', ja='Warten'),
          cta='Speichern, bevor du auf Kaufen drückst', size='sm')])),

 # Woche ab 19.10.2026: Fall der Woche Thomas (Rückhol-Betrug, p-23); p-24 bis p-26 nur eigene Fakten und belegte Zahlen.

 dict(d='2026-10-19', t='11:27', board=B_BET, f='Echt gegen Fake', farbe='akzent', bild='p-23',
      titel='Rückhol-Betrug erkennen: 3 Unterschiede zwischen echter Hilfe und Fake (nach 40.000 $ Verlust)',
      text="""Rückhol-Betrug kommt nach dem Verlust. Thomas (Name geändert) aus meiner Community verlor rund 40.000 $. Seitdem schreiben ihm ein „BaFin Team“ und ein „Blockchain Support“, der vor der Auszahlung Ausweis und Stromrechnung will. Jede Mail leitet er mir weiter. Echt war keine. Wer ungefragt anbietet, verlorenes Geld zurückzuholen, ist höchst verdächtig (Verbraucherzentrale Hessen). Mehr zu den 3 Fehlgriffen der Krypto-Anfänger im kostenlosen Training über den Link.""",
      alt='Rückhol-Betrug: links echte Hilfe mit drei Haken, rechts der Fake mit drei Kreuzen und einem Stempel Fake.',
      build=lambda: build_pin('p-23', [pin2('acc', 'Rückhol-Betrug: <em>3&nbsp;Unterschiede</em> zu echter Hilfe',
          visual=vz_vs2('Echte Hilfe', ['Du suchst sie selbst', 'Will kein Geld vorab', 'Kein Ausweis per Mail'],
                        'Fake', ['Schreibt dir ungefragt', 'Gebühr vor der Rückzahlung', 'Will deinen Ausweis'],
                        note='Nachgestellt nach echten Mails. Name geändert.'),
          cta='Speichern für die nächste Mail nach einem Verlust', size='sm')])),

 dict(d='2026-10-19', t='20:38', board=B_ANF, f='Karussell (4 Folien)', farbe='schwarz', bild='p-24', folien=4,
      titel='Krypto für Anfänger: 3 Gefühle, die mich Geld gekostet haben, und je eine Regel dagegen',
      text="""Krypto für Anfänger, drei Gefühle haben mich mehr gekostet als jede Zahl. Eile: einen Coin am Tag der Empfehlung gekauft, 5.000 $ weg. Panik: Ende 2024 alle Bitcoin verkauft. Zweifel: lange Fremde um Bestätigung gebeten, statt selbst zu verstehen, was ich kaufe. Jede Folie zeigt ein Gefühl, zwei Warnzeichen und die Regel, die ich seitdem halte. Keine Kursprognose, mein Lehrgeld. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Karussell: 5.000 $ für einen Coin aus dem Gefühl, dann drei Folien zu Eile, Panik und Zweifel mit je zwei Warnzeichen.',
      alts=['Krypto für Anfänger: große Zahl 5.000 $, ein Coin aus einem Gefühl gekauft, drei Gefühle folgen.',
            'Gefühl 1, Eile: 5.000 $ für einen Coin am Tag der Empfehlung, zwei Warnzeichen.',
            'Gefühl 2, Panik: 100 Prozent, alle Bitcoin Ende 2024 verkauft, zwei Warnzeichen.',
            'Gefühl 3, Zweifel: eine Frage statt Bestätigung von Fremden, zwei Warnzeichen.'],
      build=lambda: build_pin('p-24', [
          pin2('', 'Krypto für Anfänger: <em>3&nbsp;Gefühle</em>, die Geld kosten',
               visual=vz_num('5.000 $', 'Ein Coin, gekauft aus einem Gefühl. Drei davon haben mich Geld gekostet, eins pro Folie.'),
               cta='Speichern. Ein Gefühl pro Folie', size='sm', center=True),
          pin2('', 'Gefühl 1: <em>Eile</em>', visual=vz_num('5.000 $', 'Ein Coin mit bekanntem Gesicht, gekauft am Tag der Empfehlung. Regel seitdem: kein Kauf am selben Tag.'),
               points=['Kauf am Tag der Empfehlung', 'Coin, den du keinem erklärst'], marks='warn', cta='Speichern, bevor du auf eine Empfehlung kaufst', size='hero'),
          pin2('', 'Gefühl 2: <em>Panik</em>', visual=vz_num('100 %', 'Ende 2024 hab ich alle Bitcoin verkauft. Regel seitdem: Verkauf nur nach Plan, nie aus dem Bauch.'),
               points=['Verkaufen, weil der Kurs fällt', 'Entscheidung in Minuten'], marks='warn', cta='Speichern, bevor du im Minus verkaufst', size='hero'),
          pin2('', 'Gefühl 3: <em>Zweifel</em>', visual=vz_num('1 Frage', 'Verstehe ich, was ich kaufe? Lange hab ich stattdessen Fremde um Bestätigung gebeten.'),
               points=['Kauf, weil andere nicken', 'Fragen statt verstehen'], marks='warn', cta='Speichern, bevor du in der Gruppe nachfragst', size='hero'),
      ])),

 dict(d='2026-10-20', t='10:49', board=B_BET, f='Beispielsatz (Sprechblase)', farbe='hell', bild='p-25',
      titel='Krypto-Betrug in Telegram-Gruppen: 3 Regeln, seit ein Fake mit meinem Namen Wallets leerte',
      text="""Krypto-Betrug in Telegram-Gruppen hab ich von innen gesehen. Ich war Admin in der Gruppe eines Coin-Projekts. Ein zweiter Account mit meinem Namen schrieb Mitglieder privat an. Danach waren Wallets leer, geschätzt 4.000 bis 5.000 €. Meine Fragen nach dem Entwicklerteam blieben ohne Antwort. Seitdem gilt für mich: Hilfe nur offen in der Gruppe, Nutzername statt Anzeigename prüfen, schweigt das Team, kein Geld. Das kostenlose Training für Krypto-Anfänger findest du über den Link.""",
      alt='Krypto-Betrug in Telegram-Gruppen: nachgestellte Nachricht eines Fake-Admins in einer Sprechblase, darunter drei Regeln.',
      build=lambda: build_pin('p-25', [pin2('light', 'Fake-Admin mit meinem Namen: <em>3&nbsp;Regeln</em> für Krypto-Gruppen',
          visual=vz_bubble('„Hallo, hier Chris vom Team. Ich helfe dir kurz mit deiner Wallet.“', 'Nachgestellt. Der Account trug meinen Namen.'),
          points=['Kein Admin schreibt privat', 'Nutzername prüfen', 'Schweigt das Team, raus'],
          cta='Speichern, bevor du in einer Gruppe antwortest', size='xs')])),

 dict(d='2026-10-20', t='20:16', board=B_ANF, f='Balken (Zahlen)', farbe='schwarz', bild='p-26',
      titel='Memecoin kaufen? 764.000 Wallets verloren, 58 gewannen Millionen (Chainalysis) und 3 Regeln',
      text="""Memecoin kaufen klingt nach schnellem Geld. Bei einem der größten Memecoins 2025 verloren laut Chainalysis rund 764.000 Wallets Geld, 58 Wallets gewannen je über 10 Mio. $ (Quelle: CNBC, Mai 2025). Mein eigener Memecoin endete mit Verlust. Die drei Regeln im Pin sind das, was ich seitdem vor jedem Coin prüfe. Keine Coin-Empfehlung, keine Prognose, nur Zahlen und mein Lehrgeld. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Memecoin: zwei Balken, 764.000 Wallets mit Verlust gegen 58 Wallets mit Millionengewinn, darunter drei Regeln.',
      build=lambda: build_pin('p-26', [pin2('', 'Memecoin: <em>764.000</em> verloren, 58&nbsp;wurden reich',
          visual=vz_bars([('Wallets mit Verlust', '764.000', 100), ('Wallets mit über 10 Mio. $ Gewinn', '58', 1)], 'Zahlen: Chainalysis, ein großer Memecoin.'),
          points=['Nur Hype hält den Kurs', 'Billig pro Stück, nie günstig', 'Erklären, sonst kein Kauf'],
          cta='Speichern für den nächsten Hype-Coin', size='sm')])),

 # 23. und 24.10.2026: kein Fall der Woche (Thomas lief am 19.10.), nur eigene Fakten und belegte Zahlen.
 dict(d='2026-10-23', t='11:19', board=B_ANF, f='Kurve', farbe='hell', bild='p-27',
      titel='Kryptowährung erklärt: Warum Bitcoin schwankt, 3 Fakten und 1 Regel für Anfänger',
      text="""Kryptowährung erklärt an der Frage, die jeder Anfänger kennt: Warum schwankt Bitcoin so stark? Es wird nie mehr als 21 Millionen geben (Quelle: Decrypt), und jeder Kurs entsteht aus Käufen und Verkäufen, ohne Bank in der Mitte. Ende 2024 hab ich alle Bitcoin in Panik verkauft, weil ich die Schwankung für Gefahr hielt. Heute gilt bei mir: nur Geld, das fehlen darf, fester Tag, feste Summe. Keine Kursprognose. Die 3 Fehlgriffe der Krypto-Anfänger zeige ich im kostenlosen Training über den Link.""",
      alt='Kryptowährung erklärt: eine schwankende Kurve mit Punkten in festem Abstand, darunter drei Fakten und eine Regel.',
      build=lambda: build_pin('p-27', [pin2('light', 'Warum Bitcoin schwankt: <em>3&nbsp;Fakten</em>, kein Alarm',
          visual=vz_curve('Sechs Tage, sechs Kurse. Normal.'),
          points=['Menge fest: 21 Millionen', 'Kein fester Kurs', 'Schwankung ist normal', 'Nur Geld, das fehlen darf'],
          cta='Speichern für den roten Tag', size='xs')])),

 dict(d='2026-10-23', t='20:37', board=B_SIC, f='Zahl', farbe='akzent', bild='p-28',
      titel='Hardware-Wallet oder Börse? 850.000 Bitcoin weg bei Mt. Gox, 4 Regeln, wer den Schlüssel hält',
      text="""Hardware-Wallet oder Börse, die Frage stellt sich jeder Anfänger. Bei Mt. Gox verschwanden 2014 rund 850.000 Bitcoin. Sie lagen auf der Börse, samt Schlüsseln (Quelle: CoinMarketCap Academy). Meine 70.000 $ lagen in einer Wallet-App, die nur echt aussah. Beide Male hielt ein Fremder den Schlüssel. Seitdem zählt für mich eine Frage: Wer hat den Schlüssel? Eine Hardware-Wallet ist ein Gerät, auf dem er bei dir liegt. Wie ich aufbewahre, zeige ich im kostenlosen Training über den Link.""",
      alt='Hardware-Wallet oder Börse: große Zahl 850.000 Bitcoin, die bei Mt. Gox verschwanden, darunter vier Regeln zum Schlüssel.',
      build=lambda: build_pin('p-28', [pin2('acc', 'Hardware-Wallet oder Börse? <em>850.000</em> Bitcoin weg',
          visual=vz_num('850.000', 'Bitcoin, verschwunden bei Mt. Gox. Sie lagen auf der Börse, mit den Schlüsseln.'),
          points=['Börse hält den Schlüssel', 'Hardware-Wallet: bei dir', 'Halten? Dann bei dir', 'Die 12 Wörter nie online'],
          cta='Speichern, bevor du Bitcoin lagerst', size='xs')])),

 dict(d='2026-10-24', t='11:52', board=B_ANF, f='Karte', farbe='schwarz', bild='p-29',
      titel='Krypto für Anfänger: 4 Dinge, die ich nach 70.000 $ Verlust anders mache (damals gegen heute)',
      text="""Krypto für Anfänger, damals bei mir: Ich hab einer Wallet-App vertraut, weil sie echt aussah. 70.000 $ weg. Der Wendepunkt war ein Wort. Verstehen. Schritt für Schritt hab ich mir angesehen, was ich kaufe, und daraus ein einfaches System mit vier Schritten gebaut. Die vier Wechsel im Pin sind der Kern davon. Ich bin kein Genie. Wenn ich das nach so viel Lehrgeld geschafft hab, schaffst du den sicheren Einstieg auch. Die 3 Fehlgriffe zeige ich im kostenlosen Training über den Link.""",
      alt='Krypto für Anfänger: Karte mit dem Wort Verstehen, darunter vier Wechsel von damals zu heute mit Pfeilen.',
      build=lambda: build_pin('p-29', [pin2('', 'Damals vs. heute: <em>4&nbsp;Dinge</em>, die ich anders mache',
          visual=vz_card('Verstehen', 'Mein Wendepunkt nach 70.000 $ Verlust.'),
          points=['Glauben → prüfen', 'Chat-Link → Anbieter-Seite', 'Timing → fester Tag', 'Panik → Plan'],
          cta='Speichern vor dem ersten Kauf', size='xs')])),

 dict(d='2026-10-24', t='20:23', board=B_ANF, f='Foto', farbe='schwarz', bild='p-30',
      titel='Krypto Börse EU: 4 Prüfungen vor der Anmeldung, von der Zulassung bis zur ersten Auszahlung',
      text="""Krypto Börse in der EU, so prüfe ich sie heute: Seit Juli 2026 brauchen Anbieter in der EU eine MiCA-Zulassung. Das ESMA-Register listet sie, für Deutschland führt die BaFin eine Unternehmensdatenbank (Quelle: ESMA, BaFin). Damals hab ich einem Instagram-Kontakt Geld anvertraut. Vor der Auszahlung verlangte er eine Netzwerkgebühr. Ich hab gezahlt, die Auszahlung kam nie. Eine geprüfte Börse war das nie. Keine Anbieter-Empfehlung. Den ersten Kauf zeige ich im kostenlosen Training über den Link.""",
      alt='Krypto Börse EU: vier Prüfungen vor der Anmeldung, darunter Chris Alcatrez im blauen Hemd.',
      build=lambda: build_pin('p-30', [pin2('', 'Krypto Börse: <em>4&nbsp;Prüfungen</em>, bevor Geld fließt',
          points=['Zulassung im EU-Register', 'Sie schreibt dich nie an', 'Klein kaufen, klein auszahlen', 'Keine feste Rendite, nirgends'],
          cta='Kostenloses Training: chrisalcatrez.de', size='sm', photo=True)])),

 # 25.10.2026 (Sonntag, Winterzeit ab 03:00): nur eigene Fakten, kein Fall (Thomas lief in dieser Woche am 19.10.).
 dict(d='2026-10-25', t='11:34', board=B_BET, f='Entscheidungsbaum', farbe='hell', bild='p-31',
      titel='Krypto Sicherheit am Telefon: 3 Fragen, bevor du dem Anrufer antwortest (er wollte meine 12 Wörter)',
      text="""Krypto Sicherheit fängt am Telefon an. In der Community eines Mining-Anbieters rief mich jemand an. Er müsse meine Wallet synchronisieren und brauche dafür meine 12 Wörter. Ich hab ihm zwölf ausgedachte vorgelesen. Er rastete aus. Mit den echten wäre meine Wallet leer gewesen. Die drei Fragen im Pin stelle ich seitdem, bevor ich am Telefon ein Wort über Krypto sage. Einmal Ja, und ich lege auf. Die 3 Fehlgriffe der Krypto-Anfänger zeige ich im kostenlosen Training über den Link.""",
      alt='Krypto Sicherheit am Telefon: Entscheidungsbaum mit drei Fragen, Ja heißt auflegen, Nein führt zur nächsten Frage.',
      build=lambda: build_pin('p-31', [pin2('light', 'Anruf wegen deiner Wallet? <em>3&nbsp;Fragen</em>, dann auflegen',
          visual=vz_flow(['Kam der Anruf ungefragt?', 'Will er Wörter, PIN oder Code?', 'Soll etwas sofort passieren?'],
                         'Kein Warnsignal. Trotzdem: Auflegen, selbst zurückrufen.', ja='Auflegen'),
          cta='Speichern für den nächsten Anruf', size='sm')])),

 dict(d='2026-10-25', t='20:19', board=B_SIC, f='Echt gegen Fake', farbe='schwarz', bild='p-32',
      titel='Krypto Wallet echt oder Fake? 3 Unterschiede, die ich vor dem 70.000 $ Download nie geprüft hab',
      text="""Krypto Wallet echt oder Fake, den Unterschied hab ich erst nach 70.000 $ gesehen. Ich hab eine Wallet-App geladen, weil sie echt aussah. Logo, Name, alles passte. Den Anbieter gab es als Handy-App nie. Das Geld war weg. Heute kommt eine App bei mir nur über die Website des Anbieters aufs Handy. Eine echte App erzeugt neue 12 Wörter für dich, die gefälschte fragt deine ab. Der Vergleich im Pin ist nachgestellt. Wie die Wallet in mein System passt, zeige ich im kostenlosen Training über den Link.""",
      alt='Krypto Wallet echt oder Fake: links die echte App mit drei Haken, rechts die gefälschte mit drei Kreuzen und Stempel Fake.',
      build=lambda: build_pin('p-32', [pin2('', 'Echte Wallet-App vs. Fake: <em>3&nbsp;Unterschiede</em>',
          visual=vz_vs2('Echte App', ['Link von der Anbieter-Seite', 'Entwickler: der Anbieter selbst', 'Erzeugt deine 12 Wörter'],
                        'Fake', ['Link aus Chat oder Werbung', 'Anbieter hat keine App', 'Will 12 Wörter'],
                        note='Nachgestellt. Rechts: meine 70.000 $.'),
          cta='Speichern vor dem nächsten Download', size='sm')])),

 # Woche ab 26.10.2026: Fall der Woche Peter (Trading-Masche, p-33); p-34 eigene Fakten plus Quelle.
 dict(d='2026-10-26', t='10:58', board=B_BET, f='Karussell (4 Folien)', farbe='hell', bild='p-33', folien=4,
      titel='Krypto-Betrug erkennen: 3 Stufen einer Trading-Masche, von 250 € Start bis 62.000 € Schaden',
      text="""Krypto-Betrug erkennen an einem echten Ablauf. Peter (Name geändert) kam über eine Werbung auf Instagram zu einem Trading-Angebot. Für gut 250 € wurde sein Konto „aktiviert“. „Laura“ rief täglich an und handelte für ihn. Das Konto zeigte 83.000 €, ausgezahlt wurden 5 €. Dann kam Geld von Fremden auf sein Girokonto, er sollte es über eine Krypto-Börse weiterschicken. Drei Konten geschlossen, Schaden laut Anzeige rund 62.000 €. Mit Zustimmung veröffentlicht. Kostenloses Training über den Link.""",
      alt='Karussell: 62.000 € Schaden nach 250 € Start, dann drei Folien mit je einer Stufe der Trading-Masche und zwei Warnzeichen.',
      alts=['Trading-Betrug: große Zahl 62.000 € Schaden laut Anzeige, angefangen mit 250 €. Fall aus meiner Community, Name geändert.',
            'Stufe 1: 250 €, damit das Handelskonto aktiviert wird. Zwei Warnzeichen: Werbung auf Instagram, Gebühr zum Start.',
            'Stufe 2: 83.000 € auf dem Bildschirm, 5 € ausgezahlt. Zwei Warnzeichen: Fremde handeln für dich, Zahl ist kein Geld.',
            'Stufe 3: drei Girokonten geschlossen. Zwei Warnzeichen: fremdes Geld weiterschicken, Videoanruf bei jeder Überweisung.'],
      build=lambda: build_pin('p-33', [
          pin2('light', 'Trading-Betrug: 250&nbsp;€ Start, <em>62.000&nbsp;€</em> Schaden',
               visual=vz_num('<span style="font-size:150px">62.000 €</span>', 'Schaden laut Anzeige. Fall aus meiner Community, Name geändert. Eine Stufe pro Folie.'),
               cta='Speichern. Eine Stufe pro Folie', size='sm', center=True),
          pin2('light', 'Stufe 1: Das <em>aktivierte</em> Konto', visual=vz_num('250 €', 'Peter kam über eine Werbung auf Instagram. Für gut 250 € wurde sein Handelskonto „aktiviert“.'),
               points=['Werbung auf Instagram', 'Gebühr, um zu starten'], marks='warn', cta='Speichern vor der nächsten Werbung', size='sm'),
          pin2('light', 'Stufe 2: <em>Jemand handelt</em> für dich', visual=vz_num('<span style="font-size:150px">83.000 €</span>', '„Laura“ rief mehrmals täglich an und handelte für ihn. Das Konto zeigte 83.000 €. Ausgezahlt wurden 5 €.'),
               points=['Fremde handeln für dich', 'Bildschirm-Zahl, kein Geld'], marks='warn', cta='Speichern, bevor jemand für dich handelt', size='sm'),
          pin2('light', 'Stufe 3: Fremdes Geld <em>weiterleiten</em>', visual=vz_num('3 Konten', 'geschlossen. Statt Auszahlung kam Geld von Fremden auf sein Girokonto. Er sollte es über eine Krypto-Börse weiterschicken.'),
               points=['Fremdes Geld weiterschicken', 'Videoanruf bei Überweisung'], marks='warn', cta='Speichern, bevor du etwas weiterleitest', size='sm'),
      ])),

 dict(d='2026-10-26', t='20:43', board=B_BET, f='Beispielsatz (Sprechblase)', farbe='akzent', bild='p-34',
      titel='Krypto-Betrug auf Instagram erkennen: 3 Warnsignale in der ersten Nachricht (ich hab damals gezahlt)',
      text="""Krypto-Betrug auf Instagram beginnt mit einer freundlichen Nachricht. Bei mir meldete ein Instagram-Kontakt eine Auszahlung. Vorher sollte ich eine „Netzwerkgebühr“ zahlen. Ich hab gezahlt, die Auszahlung kam nie. Die EU-Aufsichtsbehörden ESMA, EBA und EIOPA nennen in ihrem Faktenblatt zu Krypto-Betrug (Dezember 2025) dieselben Zeichen: ungefragter Kontakt, garantierte Gewinne. Der Satz im Pin ist nachgestellt. Die 3 Fehlgriffe der Krypto-Anfänger zeige ich im kostenlosen Training über den Link.""",
      alt='Krypto-Betrug auf Instagram: nachgestellte erste Nachricht eines Betrügers in einer Sprechblase, darunter drei Warnsignale.',
      build=lambda: build_pin('p-34', [pin2('acc', 'Instagram-Nachricht über Krypto? <em>3&nbsp;Warnsignale</em>',
          visual=vz_bubble('„Hallo, ich hab dein Profil gesehen. Ich hätte da etwas für dich.“', 'Nachgestellt. Mein Betrüger kam über Instagram.'),
          points=['Schreibt dich zuerst an', 'Garantierte Gewinne', 'Gebühr vor der Auszahlung'],
          marks='warn', cta='Speichern, bevor du Fremden antwortest', size='sm')])),
]

if __name__ == '__main__':
    names = sys.argv[1:]
    out = {}
    for p in PINS:
        if names and p['bild'] not in names:
            continue
        out[p['bild']] = p['build']()
    print(out)
