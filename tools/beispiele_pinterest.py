# Erste Pins fuer Pinterest (ab 01.10.2026), ein Pin pro Tag. Zeiten Europe/Berlin.
# Jeder Eintrag: d, t, board (exakter Name der Pinnwand), f (Format), farbe (schwarz/hell/akzent), titel (Pin-Titel,
# Keyword zuerst, bis 100 Zeichen), text (Beschreibung, bis 500 Zeichen, ohne Hashtags: Pinterest ordnet ueber
# Suchbegriffe ein; hier steht die Geschichte, das Bild traegt nur das Was), alt (Alt-Text), bild (Dateiname unter
# pinterest/), build (Bildfunktion). Bilder rendern: python3 tools/beispiele_pinterest.py [p-N ...]
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

 dict(d='2026-10-08', t='20:26', board=B_ANF, f='Aussage mit Foto (Damals–Heute)', farbe='schwarz', bild='p-8',
      titel='Krypto für Anfänger: Was ich nach 70.000 $ Verlust anders mache (4 Schritte)',
      text="""Krypto für Anfänger, erzählt von jemandem, der am Anfang alles falsch gemacht hat: gefälschte Wallet-App, Gebühr vor der Auszahlung, Panikverkauf. 70.000 $ Lehrgeld. Heute lebe ich in Venezuela, zahle digital mit Krypto und arbeite mit einem einfachen System aus vier Schritten. Ein fünfstelliger Gewinn im Jahr, meine Zahl, kein Versprechen für dich. Die 3 Fehlgriffe, an denen Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Chris Alcatrez im blauen Hemd, darüber die Aussage: 70.000 $ verloren, heute ein System mit vier Schritten.',
      build=lambda: build_pin('p-8', [pin_photo('Damals · Heute', 'trend-up',
          '70.000 $ verloren. Heute ein System mit 4 Schritten.', cta='read')])),

 dict(d='2026-10-09', t='11:37', board=B_BET, f='Checkliste', farbe='akzent', bild='p-9',
      titel='Krypto-Betrug erkennen: 4 Sätze, nach denen ich jedes Gespräch sofort beende',
      text="""Krypto-Betrug erkennen, bevor Geld fließt: Vier Sätze tauchen in fast jeder Masche auf, im Chat, am Telefon, per Mail. Jeden davon hab ich früher geglaubt. Die Gebühr vor der Auszahlung hab ich bezahlt, die Auszahlung kam nie. Am Telefon wollte mal einer meine 12 Wörter, ich hab ihm ausgedachte gegeben. Die vier Sätze stehen im Pin. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Checkliste auf gelbem Grund: vier Sätze von Betrügern, nach denen Chris Alcatrez jedes Krypto-Gespräch beendet.',
      build=lambda: build_pin('p-9', [pin_check('Checkliste', 'alert',
          '4 Sätze.<br>Danach ist Schluss.',
          ['„Vor der Auszahlung fällt eine kleine Gebühr an.“',
           '„Ich brauche kurz Ihre 12 Wörter.“',
           '„Wir holen Ihr Geld zurück, gegen Vorkasse.“',
           '„Garantierte Rendite, jeden Monat.“'],
          lead='Jeder davon hat mich Geld gekostet.', numbered=True, quote=True, size='sm', theme='acc')])),

 dict(d='2026-10-10', t='19:41', board=B_BET, f='Chart (Balken)', farbe='schwarz', bild='p-10',
      titel='Krypto-Betrug: Mein Lehrgeld in Zahlen (gefälschte Wallet-App, Influencer-Coin, Cloud-Mining)',
      text="""Krypto-Betrug erkennen fängt bei den eigenen Zahlen an. Drei Maschen haben mich am Anfang Geld gekostet: eine gefälschte Wallet-App 70.000 $, ein Influencer-Coin 5.000 $, Cloud-Mining mit „garantierter“ Rendite 4.000 bis 5.000 $. Alle drei sahen echt aus, alle drei kamen über Menschen, denen ich vertraut habe. Heute erkenne ich sie am ersten Satz. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training über den Link.""",
      alt='Balkenchart im Handy-Rahmen: Lehrgeld von Chris Alcatrez, gefälschte Wallet-App 70.000 $, Coin, Cloud-Mining.',
      build=lambda: build_pin('p-10', [pin_bars('Meine Zahlen', 'bars',
          'Mein Lehrgeld<br>in Krypto',
          [('Gefälschte Wallet-App', '70.000 $', 100),
           ('Influencer-Coin', '5.000 $', 8),
           ('Cloud-Mining', '4.000–5.000 $', 7)],
          note='Heute erkenne ich sie am ersten Satz.', lead='Alle drei sahen echt aus.', head='Verluste am Anfang', size='sm')])),

 dict(d='2026-10-11', t='11:08', board=B_ANF, f='Chart (Kurven)', farbe='hell', bild='p-11',
      titel='Bitcoin Sparplan statt Timing: Warum ich den richtigen Moment aufgegeben habe',
      text="""Bitcoin Sparplan statt Timing: Ende 2024 hab ich alle Bitcoin in Panik verkauft, weil ich den richtigen Moment treffen wollte. Den gibt es für mich seitdem nur auf dem Kalender. Ich kaufe mit fester Summe an einem festen Tag und schaue den Kurs kaum an. Keine Kursprognose, keine Gewinnzusage, meine Erfahrung nach 70.000 $ Lehrgeld. Wie mein System mit vier Schritten aussieht, zeige ich im kostenlosen Training über den Link.""",
      alt='Zwei Kurven-Karten: Timing mit Fragezeichen gegen Sparplan mit Punkten in festem Abstand.',
      build=lambda: build_pin('p-11', [pin_compare_chart('Anfänger-Guide', 'repeat',
          'Sparplan statt Timing',
          'Timing', 'Raten, wann der richtige Moment ist',
          'Sparplan', 'Fester Tag, feste Summe, egal wo der Kurs steht',
          lead='Ende 2024 hab ich in Panik verkauft. Seitdem entscheidet der Kalender, nie der Kurs.', size='sm', theme='light')])),
]

if __name__ == '__main__':
    names = sys.argv[1:]
    out = {}
    for p in PINS:
        if names and p['bild'] not in names:
            continue
        out[p['bild']] = p['build']()
    print(out)
