# Erste Woche Pinterest (01.10.–07.10.2026), ein Pin pro Tag. Zeiten Europe/Berlin.
# Jeder Eintrag: d, t, board (exakter Name der Pinnwand), f (Format), titel (Pin-Titel, Keyword zuerst, bis 100 Zeichen),
# text (Beschreibung, bis 500 Zeichen), alt (Alt-Text), bild (Dateiname unter pinterest/), build (Bildfunktion).
# Bilder rendern: python3 tools/beispiele_pinterest.py  (OUT und NM als Umgebungsvariablen, siehe gen.py)
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from pin_gen import *

LINK = 'https://chrisalcatrez.de'
IMG = 'https://raw.githubusercontent.com/chrisalcatrez/chrisalcatrez/main/pinterest/%s.png'

# Pinnwände (exakte Namen; Beschreibungen in themen-pinterest.md)
B_ANF = 'Krypto für Anfänger'
B_BET = 'Krypto-Betrug erkennen'
B_SIC = 'Bitcoin Wallet und Sicherheit'
B_INF = 'Inflation und Geldentwertung'

PINS = [
 dict(d='2026-10-01', t='20:17', board=B_BET, f='Checkliste', bild='p-1',
      titel='Krypto-Betrug erkennen: 5 Zeichen, dass eine Wallet-App gefälscht ist',
      text="""Gefälschte Krypto-Apps sehen aus wie das Original: gleiches Logo, gleicher Name, gute Bewertungen. Mich hat so eine Wallet-App 70.000 $ gekostet. Diese 5 Zeichen prüfe ich seitdem vor jedem Download, in einer Minute. Bitcoin und Krypto für Anfänger, ohne Fachchinesisch, aus eigener Erfahrung. Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training (Link). #Krypto #Bitcoin #Betrug""",
      alt='Checkliste auf schwarzem Grund: fünf Zeichen, an denen man eine gefälschte Krypto-Wallet-App erkennt.',
      build=lambda: build_pin('p-1', [pin_list('Krypto-Betrug erkennen',
          '5 Zeichen, dass eine Krypto-App gefälscht ist',
          ['Der Link kam aus einem Chat, einer Mail oder einer Anzeige. Nie von der Website des Anbieters.',
           'Auf der Website des Anbieters steht keine App. Im Store gibt es trotzdem eine.',
           'Der Name des Entwicklers im Store passt nur fast zum Anbieter.',
           'Hunderte Bewertungen, alle frisch, alle fünf Sterne.',
           'Die App will zuerst die 12 Wörter deiner alten Wallet.'],
          sub='Mich hat eine kostenlose Wallet-App 70.000 $ gekostet. Heute prüfe ich jede App in einer Minute.', dense=True)])),

 dict(d='2026-10-02', t='20:41', board=B_ANF, f='Mythos', bild='p-2',
      titel='Krypto ist doch alles Betrug? Mythos und Wirklichkeit nach 70.000 $ Verlust',
      text="""Krypto ist alles Betrug, den Satz hab ich früher selbst gesagt, nachdem mich zwei Betrüger erwischt hatten. Heute unterscheide ich: Betrogen haben mich Menschen mit gefälschten Apps, erfundenen Gebühren und falschem Support. Bitcoin selbst hat keinen Chef, der dich anruft. Was Anfänger schützt, ist ein einfaches System und Geduld. Krypto verständlich erklärt aus eigener Erfahrung, das kostenlose Training findest du über den Link. #Kryptowährung #Bitcoin #KryptoFürAnfänger""",
      alt='Gegenüberstellung: oben der Mythos, Krypto sei alles Betrug, unten, was Chris Alcatrez erlebt hat.',
      build=lambda: build_pin('p-2', [pin_vs('Mythos oder Wirklichkeit',
          '„Krypto ist doch alles Betrug.“',
          'Der Mythos', ['Bitcoin selbst ist die Masche.', 'Wer einsteigt, wird abgezockt.', 'Nur Zocker verdienen daran.'],
          'Was ich erlebt habe', ['Betrogen haben mich Menschen: gefälschte App, erfundene Gebühr, falscher Support.',
                                  'Bitcoin hat keinen Chef, der dich anruft.',
                                  'Mein Verlust kam aus Eile. Mein Gewinn aus einem System mit vier Schritten.'])])),

 dict(d='2026-10-03', t='21:05', board=B_SIC, f='Begriff erklärt', bild='p-3',
      titel='Seed-Phrase erklärt: die 12 Wörter, die dein Bitcoin-Geld sind',
      text="""Seed-Phrase einfach erklärt: 12 oder 24 Wörter stellen deine Krypto-Wallet wieder her. Wer sie kennt, kann alles abräumen, ohne Passwort. Am Telefon wollte mal ein angeblicher Support meine 12 Wörter zum „Synchronisieren“. Ich hab ihm zwölf ausgedachte gegeben, er ist ausgerastet. Drei Regeln, mit denen die Wörter bei dir bleiben, stehen im Pin. Bitcoin-Sicherheit für Anfänger aus eigener Erfahrung, kostenloses Training über den Link. #Bitcoin #Wallet #Krypto""",
      alt='Begriff erklärt: Seed-Phrase, die 12 Wörter einer Wallet, mit drei Regeln zum sicheren Aufbewahren.',
      build=lambda: build_pin('p-3', [pin_term('Begriff erklärt', 'Seed-Phrase',
          '12 oder 24 Wörter, die deine Wallet wiederherstellen. Wer sie hat, hat dein Geld. Ohne Passwort, ohne Nachfrage.',
          ['Niemand braucht sie außer dir. Kein Support, keine Börse, keine App zum „Synchronisieren“.',
           'Auf Papier, an zwei Orten. Nie als Foto, nie in der Cloud.',
           'Wer danach fragt, will dein Geld. Mich wollte mal einer am Telefon so leerräumen.'])])),

 dict(d='2026-10-04', t='11:23', board=B_ANF, f='Schritte (System-Teaser)', bild='p-4',
      titel='Bitcoin für Anfänger: Wie ich heute mit 100 € starten würde (4 Schritte)',
      text="""Bitcoin für Anfänger, ohne 10.000 € und ohne Fachchinesisch. Ich hab am Anfang 70.000 $ verloren, weil ich schnell sein wollte. Heute würde ich mit 100 € anfangen, bei einer Börse mit Sitz in der EU, mit einer Wallet von der Website des Anbieters und ohne Chats mit Fremden über mein Geld. Die vier Schritte stehen im Pin, das System dahinter zeige ich im kostenlosen Training über den Link. #Bitcoin #KryptoFürAnfänger #Sparplan""",
      alt='Vier nummerierte Schritte, wie Chris Alcatrez heute mit 100 Euro in Krypto starten würde.',
      build=lambda: build_pin('p-4', [pin_steps('Wenn ich heute bei null anfangen würde',
          'Mit 100 € in Krypto starten. Vier Schritte.',
          [('Klein anfangen', '100 € statt 10.000 €. Dieselbe Erfahrung, günstiger.'),
           ('Börse mit Sitz in der EU', 'Regeln, Aufsicht, ein Ansprechpartner mit Adresse.'),
           ('Eigene Wallet, richtig geladen', 'Nur über den Link auf der Website des Anbieters.'),
           ('Kein Chat mit Fremden über Geld', 'Kein Support im Messenger, kein Anruf, keine Beraterin auf Instagram.')],
          cta='Kostenloses Training')])),

 dict(d='2026-10-05', t='10:48', board=B_BET, f='Chat nachgestellt', bild='p-5',
      titel='Netzwerkgebühr vor der Auszahlung? So erkennst du den Krypto-Betrug im Chat',
      text="""Krypto-Betrug im Chat erkennen: Ein angeblicher Support meldet eine Auszahlung, vorher soll eine „Netzwerkgebühr“ bezahlt werden. Bei mir kam die Nachricht damals über Instagram. Ich hab gezahlt, die Auszahlung kam nie. Eine echte Börse zieht Gebühren vom Guthaben ab, Vorkasse für die eigene Auszahlung verlangen nur Betrüger. Der Chat im Pin ist nachgestellt, meine Antwort darauf heute auch. Kostenloses Training über den Link. #Krypto #Betrug #Bitcoin""",
      alt='Nachgestellter Chat mit einem falschen Support, der vor der Auszahlung eine Netzwerkgebühr verlangt.',
      build=lambda: build_pin('p-5', [pin_chat('Betrugsmasche · Netzwerkgebühr',
          'Eine Auszahlung, für die du vorher zahlen sollst, gibt es nie.',
          [('Support', 'Ihre Auszahlung ist freigegeben. Es fehlt nur die Netzwerkgebühr.', False),
           ('Ich', 'Zieht sie einfach vom Guthaben ab.', True),
           ('Support', 'Das geht bei uns nur per Vorkasse. Danach wird sofort ausgezahlt.', False),
           ('Ich', 'Dann bleibt das Geld eben bei euch.', True)])])),

 dict(d='2026-10-06', t='20:33', board=B_INF, f='Venezuela-Beobachtung', bild='p-6',
      titel='Inflation verstehen: Was Venezuela mir über Erspartes zeigt',
      text="""Inflation und Geldentwertung sind in Venezuela kein Schulbuchthema, sie stehen an jeder Kasse. Preise in Dollar, Krypto im Alltag, digital bezahlt. Ich lebe hier freiwillig und sehe jeden Tag, was mit Erspartem passiert, das nur auf dem Konto liegt. Genau deshalb bin ich bei Krypto gelandet, erst mit Verlusten, dann mit einem einfachen System. Wie ich heute Erspartes und Krypto zusammendenke, zeige ich im kostenlosen Training über den Link. #Inflation #Geldentwertung #Bitcoin""",
      alt='Drei Beobachtungen aus Venezuela über Inflation, Erspartes und Krypto im Alltag.',
      build=lambda: build_pin('p-6', [pin_list('Ich lebe in Venezuela',
          '3 Dinge, die mir Venezuela über Erspartes zeigt',
          ['Preise stehen in Dollar. Die Landeswährung rechnet kaum jemand um.',
           'Krypto ist hier Alltag, kein Hobby. Bezahlt wird digital, über das Internet.',
           'Geldentwertung sieht man beim Einkauf, nie auf dem Kontoauszug.'],
          sub='Genau deshalb bin ich bei Krypto gelandet. Erst mit Verlusten, dann mit System.', size='')])),

 dict(d='2026-10-07', t='20:12', board=B_ANF, f='FAQ', bild='p-7',
      titel='Zu spät für Bitcoin? Was ich Anfängern 2026 antworte',
      text="""Ist es zu spät für Bitcoin? Die Frage stellen mir Anfänger am häufigsten. Ich hab sie mir 2024 selbst gestellt und Ende 2024 in Panik alles verkauft. Zu spät war ich nie, zu hastig schon. Was ich heute anders mache: Sparplan statt Timing, kleine Beträge, bis ich verstehe, was ich kaufe. Keine Kursprognose, keine Gewinnzusage, nur meine Erfahrung. Das System mit vier Schritten zeige ich im kostenlosen Training über den Link. #Bitcoin #KryptoAnfänger #Sparplan""",
      alt='Frage und Antwort: Ist es 2026 zu spät für Bitcoin? Drei Punkte aus der Erfahrung von Chris Alcatrez.',
      build=lambda: build_pin('p-7', [pin_faq('Die häufigste Anfängerfrage',
          'Ist es 2026 zu spät für Bitcoin?',
          'Die Frage hab ich mir 2024 gestellt. Ende 2024 hab ich dann alles in Panik verkauft. Zu spät war ich nie. Zu hastig, ja.',
          ['Zu spät gibt es nur für Leute, die den perfekten Einstieg suchen.',
           'Sparplan statt Timing: feste Summe, fester Tag.',
           'Kleine Beträge, bis du verstehst, was du kaufst.'],
          cta='Kostenloses Training', size='sm')])),
]

if __name__ == '__main__':
    names = sys.argv[1:]
    out = {}
    for p in PINS:
        if names and p['bild'] not in names:
            continue
        out[p['bild']] = p['build']()
    print(out)
