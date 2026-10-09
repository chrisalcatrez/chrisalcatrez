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
]

if __name__ == '__main__':
    names = sys.argv[1:]
    out = {}
    for p in PINS:
        if names and p['bild'] not in names:
            continue
        out[p['bild']] = p['build']()
    print(out)
