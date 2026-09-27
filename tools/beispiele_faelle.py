# Beispiele: echte Fälle aus der Community, anonymisiert (Beiträge 10 bis 16)
# Aufruf wie beispiele.py; NM und OUT als Umgebungsvariablen setzen
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen import *

A = lambda t: '<span class="acc">%s</span>' % t
D = lambda t: (t, 'dim')
C = lambda t: (t, 'acc')
TAGS = '#krypto #kryptowährung #kryptowährungen #bitcoindeutschland #bitcoinkaufen #bitcoinfüranfänger #kryptofüranfänger #kryptobetrug #anlagebetrug #onlinebetrug #betrugsmasche #kryptosicherheit #kryptowallet #finanzbildung #geldanlage #vermögensaufbau'

Q_EZB = 'Quelle: Europäische Zentralbank, Warnung vor Betrug mit Namen und Logo der EZB'
Q_POL = 'Quelle: Polizeiliche Kriminalprävention, „Finanzagenten“'
Q_BAFIN = 'Quellen: BaFin, „Betrug mit dem Namen der BaFin“; EZB, Betrugswarnung'
Q_FCA = 'Quelle: FCA (britische Finanzaufsicht), „Recovery room scams“'
Q_TOFR = 'Quelle: Börse Stuttgart Digital Exchange, „Was bedeutet die Transfer of Funds Regulation?“'
TRAINING = 'Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich dir im %s' % A('kostenlosen Training.')

POSTS = {}

# ---------- Beitrag 10: Statement-Karussell (Fall Peter) ----------
POSTS['beitrag-10'] = dict(
    date='2026-10-05', fmt='Statement-Karussell', topic='Fall Peter: 83.000 € auf dem Bildschirm, 5 € ausgezahlt (Trading-Werbung, Handelspartnerin, Finanzagent, falsche EZB)',
    slides=[
        s_hook('ECHTER FALL · NAME GEÄNDERT', 'Auf dem Bildschirm: 83.000 €. Ausgezahlt: %s' % A('5 €.'), cue='So lief es ab &#8594;'),
        s_point('WIE ES ANFING', 'Mit einer Werbung auf Instagram. %s' % A('Genau hier.'),
                ['Gute Gewinne, ein Nebeneinkommen. Peter trug Name und Nummer ein.',
                 D('Kurz darauf rief eine freundliche Frau an. Für gut 250 € wurde sein Handelskonto „aktiviert“.')]),
        s_point('DANN KAM LAURA', 'Seine persönliche Handelspartnerin.',
                ['Zehn Jahre Erfahrung, Abteilungsleiterin. So stellte sie sich vor.',
                 D('Sie telefonierten mehrmals am Tag. Sie handelte für ihn. Sein Kontostand stieg jeden Tag.')]),
        s_point('DER ERSTE HAKEN', '„Ich lege 5.000 € dazu.“',
                ['Für ein Sechs-Monats-Angebot fehlten Peter 10.000 €. Laura bot an, die Hälfte privat zu zahlen.',
                 D('Peter holte die anderen 5.000 € als Bargeld von seiner Kreditkarte.')]),
        s_point('DIE AUSZAHLUNG', 'Auszahlen ging nie.',
                ['Stattdessen landete Geld von fremden Leuten auf seinem Girokonto. Er sollte es über eine Krypto-Börse an ein „Sicherheitskonto“ weiterschicken.',
                 D('Drei seiner Girokonten wurden geschlossen.')]),
        s_point('IMMER DABEI', 'Laura sah jeden Schritt mit.',
                ['Vor jeder Überweisung kam ein Videoanruf. Peter sollte seinen Bildschirm teilen, damit sie „helfen“ konnte.',
                 D('So lief alles unter ihren Augen.')]),
        s_point('DAS FINALE', 'Dann schrieb die „Europäische Zentralbank“.',
                ['Dazu ein angeblicher Vorgesetzter. In den Mails: Frist, Aktenzeichen, Geldwäsche-Paragrafen. Nachweis über 10.000 € bis 14 Uhr, sonst Sperre.',
                 D('Die echte EZB kontaktiert Bürger nie, um persönliche Finanzdaten anzufordern.')],
                src=Q_EZB, size='m'),
        s_point('DIE BILANZ', 'Rund 62.000 € Schaden.',
                ['So steht es in seiner Anzeige, Forderungen aus zurückgebuchten Zahlungen eingeschlossen.',
                 D('Die Polizei warnt: Wer fremdes Geld über sein Konto weiterleitet, riskiert ein Verfahren wegen Geldwäsche und bleibt auf Rückbuchungen sitzen.')],
                src=Q_POL),
        s_point('ZUM MERKEN', 'Drei Sätze, bei denen du %s' % A('auflegst.'),
                ['„Wir aktivieren dein Konto.“', '„Ich lege privat etwas dazu.“', '„Leite dieses Geld kurz weiter.“',
                 C('Schick das jemandem, der gerade mit Trading anfängt.')], meta=True),
    ],
    alts=['Echter Fall: Auf dem Bildschirm standen 83.000 Euro, ausgezahlt wurden 5 Euro',
          'Es fing mit einer Werbung auf Instagram an, danach wurde sein Handelskonto für gut 250 Euro aktiviert',
          'Dann kam Laura, seine persönliche Handelspartnerin, und der Kontostand stieg jeden Tag',
          'Der erste Haken: Laura bot an, 5.000 Euro dazuzulegen, Peter holte 5.000 Euro Bargeld von der Kreditkarte',
          'Auszahlen ging nie, stattdessen sollte er Geld von Fremden weiterschicken, drei Girokonten wurden geschlossen',
          'Vor jeder Überweisung kam ein Videoanruf mit geteiltem Bildschirm',
          'Zum Schluss schrieb eine falsche Europäische Zentralbank mit Frist und Geldwäsche-Paragrafen',
          'Bilanz laut Anzeige: rund 62.000 Euro Schaden, die Polizei warnt vor dem Weiterleiten fremden Geldes',
          'Drei Sätze, bei denen du auflegst. Schick das jemandem, der gerade mit Trading anfängt'],
    caption='''Auf dem Bildschirm standen 83.000 €. Ausgezahlt wurden 5 €.

Echter Fall aus meiner Community, Name geändert.

Es fing mit einer Werbung auf Instagram an: gute Gewinne, ein Nebeneinkommen. Peter trug Name und Nummer ein. Kurz darauf rief eine freundliche Frau an. Für gut 250 € wurde sein Handelskonto „aktiviert“.

Dann kam Laura, seine persönliche Handelspartnerin. Zehn Jahre Erfahrung, Abteilungsleiterin, so stellte sie sich vor. Sie telefonierten mehrmals am Tag, sie handelte für ihn, sein Kontostand stieg jeden Tag.

Für ein Sechs-Monats-Angebot fehlten ihm 10.000 €. Laura bot an, die Hälfte privat zu zahlen. Peter holte die anderen 5.000 € als Bargeld von seiner Kreditkarte.

Auszahlen ging nie. Stattdessen landete Geld von fremden Leuten auf seinem Girokonto, und er sollte es über eine Krypto-Börse an ein angebliches Sicherheitskonto weiterschicken. Vor jeder Überweisung kam ein Videoanruf, sein Bildschirm war geteilt. Drei seiner Girokonten wurden geschlossen.

Zum Schluss meldeten sich ein angeblicher Vorgesetzter und die „Europäische Zentralbank“, mit Frist, Aktenzeichen und Geldwäsche-Paragrafen. Die echte EZB kontaktiert Bürger nie, um persönliche Finanzdaten anzufordern (Quelle: EZB).

Bilanz laut seiner Anzeige: rund 62.000 € Schaden, Forderungen aus zurückgebuchten Zahlungen eingeschlossen. Die Polizei warnt: Wer fremdes Geld über sein Konto weiterleitet, riskiert ein Verfahren wegen Geldwäsche, die Kündigung seines Kontos und bleibt auf Rückbuchungen sitzen (Quelle: Polizeiliche Kriminalprävention, „Finanzagenten“).

Drei Sätze, bei denen du auflegst:
„Wir aktivieren dein Konto.“
„Ich lege privat etwas dazu.“
„Leite dieses Geld kurz weiter.“

Für alle, die mit Krypto, Bitcoin oder Trading anfangen und sich vor Anlagebetrug schützen wollen.

Schick das jemandem, der gerade mit Trading anfängt.''')

# ---------- Beitrag 11: Nischenmythos (Fall Thomas, Rueckhol-Betrug) ----------
POSTS['beitrag-11'] = dict(
    date='2026-10-06', fmt='Nischenmythos entlarven', topic='Fall Thomas: Mythos, eine Behörde holt dein Geld zurück (Rückhol-Betrug, falsche BaFin, Kanzlei, Börse)',
    slides=[
        s_hook('MYTHOS', '„Eine Behörde holt dir dein verlorenes Geld %s“' % A('zurück.'), cue='Stimmt das? Weiterwischen &#8594;', size=''),
        s_point('ECHTER FALL · NAME GEÄNDERT', 'Thomas hat einmal verloren. Seitdem kommt Post.',
                ['Rund 40.000 $ sind weg, so hat er es mir erzählt.',
                 D('Seitdem schreiben ihm „Anwälte“, „Behörden“ und „Börsen“. Jede neue Mail leitet er mir weiter und fragt: echt?')], size='m'),
        s_mail('AUS SEINEM POSTFACH', 'Vier Absender. %s' % A('Ein Ziel.'), [
            ('„BaFin Team“ · <b>blockchainauszahlung.com</b>', '„Bafin ist ein legitimes und seriöses Unternehmen …“ Dazu ein Link auf die echte BaFin-Seite.'),
            ('„Kanzlei“ aus London, angeblich im Auftrag der britischen Finanzaufsicht', '„Eine Zahlung wird nur fällig, wenn Sie tatsächlich eine Rückzahlung erhalten.“'),
            ('„Blockchain Support“ · <b>office-de-help.info</b>', '„… dass Ihre Transaktion … vorübergehend ausgesetzt wurde.“ 2,08 BTC. Bitte Ausweis und Stromrechnung.'),
            ('„Coinbase Wallet“ · <b>coinbase-wallet.online</b>', '„Auszahlungsprozess – Nächste Schritte“'),
        ]),
        s_point('DIE WAHRHEIT', 'Die BaFin holt kein verlorenes Geld zurück.',
                ['Das gehört laut BaFin zu keiner ihrer Aufgaben. Sie beauftragt damit auch keine Firma.',
                 D('Und die Europäische Zentralbank kontaktiert Bürger nie, um Entschädigungen anzubieten.')],
                src=Q_BAFIN, size='m'),
        s_point('WARUM GERADE ER', 'Wer einmal verloren hat, wird wieder angeschrieben.',
                ['Die Täter vom ersten Betrug können sich unter neuem Namen melden. Oder sie verkaufen die Daten ihrer Opfer weiter.',
                 D('So beschreibt es die britische Finanzaufsicht. Der Name dafür: Rückhol-Betrug.')],
                src=Q_FCA, size='m'),
        s_point('ZUM MERKEN', 'Wer dir Hilfe verspricht, bevor du fragst, %s' % A('will dein Geld.'),
                ['Antworte nie. Keine Gebühr, kein Ausweisfoto, kein Klick.', D('Zeig die Mails der Polizei.')], meta=True, size='m'),
        s_point('SPEICHERN', 'Speichere den Beitrag. Für den Tag, an dem %s' % A('die zweite Mail kommt.'), None, meta=True, size='m'),
    ],
    alts=['Mythos: Eine Behörde holt dir dein verlorenes Geld zurück',
          'Echter Fall: Thomas hat einmal verloren, seitdem schreiben ihm angebliche Anwälte, Behörden und Börsen',
          'Vier echte Betrugsmails: falsches BaFin Team, falsche Londoner Kanzlei, falscher Blockchain Support, falsche Coinbase Wallet',
          'Die Wahrheit: Die BaFin holt kein verlorenes Geld zurück und beauftragt damit keine Firma',
          'Wer einmal verloren hat, wird wieder angeschrieben, das nennt man Rückhol-Betrug',
          'Wer dir Hilfe verspricht, bevor du fragst, will dein Geld',
          'Speichere den Beitrag für den Tag, an dem die zweite Mail kommt'],
    caption='''Nach dem Verlust kommt die zweite Welle.

Mythos: Eine Behörde holt dir dein verlorenes Geld zurück.

Ein echter Fall, Name geändert: Thomas hat beim Online-Trading rund 40.000 $ verloren, so hat er es mir erzählt. Seitdem kommt Post. Eine angebliche Londoner Kanzlei im Auftrag der britischen Finanzaufsicht. Ein „BaFin Team“, das schreibt, die BaFin sei ein „legitimes und seriöses Unternehmen“, und zum Beweis auf die echte BaFin-Seite verlinkt. Ein „Blockchain Support“, der eine gesperrte Transaktion über 2,08 BTC meldet und dafür Ausweis und Stromrechnung will. Eine „Coinbase Wallet“ von einer fremden Adresse.

Jede neue Mail leitet Thomas mir weiter und fragt: echt? Die Antwort ist jedes Mal dieselbe.

Die Wahrheit: Die Rückholung verlorener Gelder gehört laut BaFin zu keiner ihrer Aufgaben, und sie beauftragt damit auch keine Firmen (Quelle: BaFin, „Betrug mit dem Namen der BaFin“). Die Europäische Zentralbank kontaktiert Bürgerinnen und Bürger nie, um Entschädigungen anzubieten oder persönliche Finanzdaten anzufordern (Quelle: EZB).

Warum gerade er? Die britische Finanzaufsicht FCA beschreibt es so: Die Täter vom ersten Betrug können sich unter neuem Namen wieder melden oder die Daten ihrer Opfer an andere weiterverkaufen (Quelle: FCA, „Recovery room scams“).

Wer dir Hilfe verspricht, bevor du fragst, will dein Geld. Antworte nie. Keine Gebühr, kein Ausweisfoto, kein Klick. Zeig die Mails der Polizei.

Für alle, die mit Krypto oder Bitcoin Geld verloren haben oder sich davor schützen wollen.

Speichere den Beitrag. Für den Tag, an dem die zweite Mail kommt.''')

# ---------- Beitrag 12: Gegenueberstellung (vier Teilnehmer, falscher AML-Support) ----------
POSTS['beitrag-12'] = dict(
    date='2026-10-07', fmt='Gegenüberstellung', topic='Vier Teilnehmer, falscher AML-Supporter: Wallet verifizieren wegen Geldwäscheregeln (Seed-Phrase)',
    slides=[
        s_hook('ECHTE FÄLLE · NAMEN GEÄNDERT', 'Vier Teilnehmer. Eine Nachricht. %s' % A('Vier leere Wallets.')),
        s_point('DIE NACHRICHT', '„Wegen neuer Geldwäscheregeln musst du deine Wallet aktualisieren.“',
                ['Sinngemäß schrieb das ein angeblicher „AML-Supporter“. AML steht für Anti-Geldwäsche.',
                 D('Elena, Markus, Leon und Sabine sollten ihre Wallet verifizieren. Dafür wollte er ihre Seed-Phrase. Alle vier haben sie herausgegeben.')], size='sm'),
        s_point('DER TRICK', 'Die Regeln gibt es wirklich.',
                ['Seit dem 30. Dezember 2024 gilt in der EU die Travel Rule. Bei Transfers ab 1.000 € an oder von einer eigenen Wallet verlangen Börsen einen Nachweis, dass sie dir gehört.',
                 D('Genau deshalb klingt die Nachricht echt.')], src=Q_TOFR),
        s_vs('BETRUG VS. ECHTE PRÜFUNG', 'Woran du den Unterschied erkennst.',
             'BETRUG', ['Private Nachricht von einem „Supporter“', 'Beruft sich auf neue Gesetze', 'Will deine Seed-Phrase'],
             'ECHTE PRÜFUNG', ['Anfrage im Konto deiner Börse', 'Nachweis zum Beispiel per kleinem Testbetrag', 'Deine Seed-Phrase bleibt bei dir'],
             'Deine Seed-Phrase gehört in kein Formular.'),
        s_point('ZUM MERKEN', 'Kein Gesetz verlangt deine %s' % A('Seed-Phrase.'),
                ['Wer sie hat, hat dein Geld. Egal, wie das Formular heißt.'], meta=True),
        s_point('KOSTENLOSES TRAINING', TRAINING, ['Link in meiner Bio.'], meta=True, size='m'),
    ],
    alts=['Echte Fälle: Vier Teilnehmer, eine Nachricht, vier leere Wallets',
          'Die Nachricht: Wegen neuer Geldwäscheregeln musst du deine Wallet aktualisieren, dafür wollte ein angeblicher AML-Supporter die Seed-Phrase',
          'Der Trick: Die Regeln gibt es wirklich, seit dem 30. Dezember 2024 gilt in der EU die Travel Rule',
          'Gegenüberstellung: Betrug will per Privatnachricht deine Seed-Phrase, eine echte Prüfung läuft über das Konto deiner Börse und deine Seed-Phrase bleibt bei dir',
          'Kein Gesetz verlangt deine Seed-Phrase',
          'Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich dir im kostenlosen Training, Link in meiner Bio'],
    caption='''Vier meiner Teilnehmer. Eine Nachricht. Vier leere Wallets.

Echte Fälle, Namen geändert: Elena, Markus, Leon und Sabine bekamen eine Nachricht von einem angeblichen „AML-Supporter“. AML steht für Anti-Geldwäsche. Wegen neuer Geldwäscheregeln müssten sie ihre Wallet aktualisieren und verifizieren. Dafür wollte er ihre Seed-Phrase. Alle vier haben sie herausgegeben. Danach war das Geld weg.

Der Trick: Die Regeln gibt es wirklich. Seit dem 30. Dezember 2024 gilt in der EU die Travel Rule. Bei Transfers ab 1.000 € an oder von einer eigenen Wallet verlangen Börsen einen Nachweis, dass die Wallet dir gehört, zum Beispiel über einen kleinen Testbetrag (Quelle: Börse Stuttgart Digital Exchange). Genau deshalb klingt die Nachricht echt.

Echte Prüfung: Anfrage im Konto deiner Börse, Nachweis zum Beispiel per Testbetrag, deine Seed-Phrase bleibt bei dir.
Betrug: private Nachricht, ein „Supporter“, die Bitte um deine Seed-Phrase.

Kein Gesetz verlangt deine Seed-Phrase. Wer sie hat, hat dein Geld. Egal, wie das Formular heißt.

Für alle, die mit Krypto und Bitcoin anfangen und ihre Wallet sicher halten wollen.

Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich dir im kostenlosen Training. Link in meiner Bio.''')

# ---------- Beitrag 13: Visueller Post (Fall Lena, falscher Support in der Gruppe) ----------
POSTS['beitrag-13'] = dict(
    date='2026-10-08', fmt='Visueller Post', topic='Fall Lena: Hilfe in der Krypto-Gruppe, falscher Community Support (echte Chat-Sätze)',
    slides=[
        s_hook('ECHTER FALL · NAME GEÄNDERT', 'Lena bat in einer Krypto-Gruppe um Hilfe. Die erste Antwort kam %s' % A('von einem Betrüger.'), size=''),
        s_point('WAS PASSIERTE', 'Ein „Community Support“ meldete sich.',
                ['Lena folgte seinen Anweisungen. Währenddessen wurde ihre Wallet leergeräumt.',
                 D('In wenigen Wochen verlor sie rund 1.000 € aus zwei Wallets.')], size='m'),
        s_chat('AUS IHREM CHAT', 'Sätze vom falschen Support.', [
            ('„Schicken Sie mir einen Screenshot … damit ich sehen kann.“', 'Ausspähen', 'Er will wissen, was es bei dir zu holen gibt.'),
            ('„Die Münze steigt jetzt, also ist es zu Ihrem eigenen Vorteil …“', 'Zeitdruck', 'Du sollst schneller handeln, als du denkst.'),
        ], sender='Community Support'),
        s_chat('AUS IHREM CHAT', 'Und so ging es weiter.', [
            ('„… damit ich Ihnen unsere Dapp senden kann, um die Wallet vor unbekannten internen Hacks zu schützen.“', 'Falscher Schutz', 'Ein Link zum „Schützen“ ist ein typischer Weg in deine Wallet.'),
            ('„Sie werden sicherlich Ihr gesamtes Geld zurückbekommen.“', 'Rückhol-Versprechen', 'Wer Rückholung verspricht, will die nächste Zahlung.'),
        ], sender='Community Support'),
        s_point('UND DANN', 'Lena hat aufgehört. %s' % A('Genau im richtigen Moment.'),
                ['Sie hat den „Support“ blockiert und sich Hilfe vor Ort gesucht.', D('Das war der wichtigste Schritt der ganzen Geschichte.')]),
        s_point('ZUM MERKEN', 'Wer in einer Gruppe um Hilfe bittet, bekommt %s' % A('Post von Betrügern.'),
                ['Offizieller Support schreibt dich nie zuerst privat an. Und er fragt nie nach Screenshots deiner Konten.'], meta=True, size='m'),
        s_point('TEILEN', 'Schick das in deine %s' % A('Krypto-Gruppe.'), None, meta=True),
    ],
    alts=['Echter Fall: Lena bat in einer Krypto-Gruppe um Hilfe, die erste Antwort kam von einem Betrüger',
          'Ein angeblicher Community Support meldete sich, währenddessen wurde ihre Wallet leergeräumt, rund 1.000 Euro aus zwei Wallets',
          'Chat-Sätze vom falschen Support: Screenshot zum Ausspähen und Zeitdruck, weil die Münze angeblich steigt',
          'Weitere Chat-Sätze: ein Link zum angeblichen Schutz der Wallet und das Versprechen, alles Geld zurückzubekommen',
          'Lena hat aufgehört, den Support blockiert und sich Hilfe vor Ort gesucht',
          'Wer in einer Gruppe um Hilfe bittet, bekommt Post von Betrügern, offizieller Support schreibt dich nie zuerst privat an',
          'Schick das in deine Krypto-Gruppe'],
    caption='''Lena bat in einer Krypto-Gruppe um Hilfe. Die erste Antwort kam von einem Betrüger.

Ein echter Fall, Name geändert. Ein „Community Support“ meldete sich bei ihr. Lena folgte seinen Anweisungen, und währenddessen wurde ihre Wallet leergeräumt. In wenigen Wochen verlor sie rund 1.000 € aus zwei Wallets.

Diese Sätze stammen aus ihrem Chat mit dem falschen Support:
„Schicken Sie mir einen Screenshot … damit ich sehen kann.“ Er wollte wissen, was es zu holen gibt.
„Die Münze steigt jetzt, also ist es zu Ihrem eigenen Vorteil …“ Zeitdruck, damit du schneller handelst, als du denkst.
„… damit ich Ihnen unsere Dapp senden kann, um die Wallet vor unbekannten internen Hacks zu schützen.“ Ein Link zum „Schützen“ ist ein typischer Weg in deine Wallet.
„Sie werden sicherlich Ihr gesamtes Geld zurückbekommen.“ Das Rückhol-Versprechen, kurz vor der nächsten Zahlung.

Lena hat aufgehört. Sie hat den „Support“ blockiert und sich Hilfe vor Ort gesucht. Das war der wichtigste Schritt der ganzen Geschichte.

Wer in einer Gruppe um Hilfe bittet, bekommt Post von Betrügern. Offizieller Support schreibt dich nie zuerst privat an und fragt nie nach Screenshots deiner Konten.

Für alle, die mit Krypto, Bitcoin oder Memecoins anfangen und in Telegram-Gruppen unterwegs sind.

Schick das in deine Krypto-Gruppe.''')

# ---------- Beitrag 14: Erfolgsgeschichte (eigene Geschichte, Seed-Phrase am Telefon) ----------
POSTS['beitrag-14'] = dict(
    date='2026-10-09', fmt='Erfolgsgeschichte', topic='Eigene Geschichte: Betrüger wollte am Telefon meine Seed-Phrase, bekam eine ausgedachte (Wallet synchronisieren)',
    slides=[
        s_hook('MEINE GESCHICHTE', 'Ein Betrüger wollte am Telefon meine Seed-Phrase. %s' % A('Ich habe ihm eine gegeben.'), size=''),
        s_point('DIE SITUATION', 'Ich war in der Community eines Mining-Anbieters.',
                ['Einer im Chat versuchte ständig, anderen ihre Zugänge abzunehmen.', D('Dann rief er mich an.')], size='m'),
        s_point('SEINE BEGRÜNDUNG', 'Ich müsse meine Wallet %s' % A('synchronisieren.'),
                ['Sonst hätte ich keinen Zugang mehr zur Plattform. Dafür brauche er meine Seed-Phrase.', D('Klingt technisch. Ist eine Lüge.')]),
        s_point('MEINE ANTWORT', 'Ich habe ihm eine Seed-Phrase gegeben. %s' % A('Ausgedacht.'),
                ['Wort für Wort erfunden.', D('Kurz darauf ist er ausgerastet.')]),
        s_point('WAS DAHINTERSTECKT', 'Synchronisieren. Verifizieren. Aktualisieren.',
                ['Die Wörter wechseln. Die Bitte bleibt dieselbe: deine Seed-Phrase.', D('Keine echte Plattform fragt danach. Nie.')], size='m'),
        s_point('ZUM MERKEN', 'Deine Seed-Phrase gehört in %s' % A('keine Nachricht und kein Telefonat.'),
                ['Wer danach fragt, hat sich damit verraten.'], meta=True, size='m'),
        s_point('KOSTENLOSES TRAINING', TRAINING, ['Link in meiner Bio.'], meta=True, size='m'),
    ],
    alts=['Meine Geschichte: Ein Betrüger wollte am Telefon meine Seed-Phrase, ich habe ihm eine gegeben',
          'Ich war in der Community eines Mining-Anbieters, einer im Chat versuchte ständig, anderen ihre Zugänge abzunehmen',
          'Seine Begründung: Ich müsse meine Wallet synchronisieren',
          'Meine Antwort: eine ausgedachte Seed-Phrase, kurz darauf ist er ausgerastet',
          'Synchronisieren, verifizieren, aktualisieren: Die Wörter wechseln, die Bitte bleibt dieselbe',
          'Deine Seed-Phrase gehört in keine Nachricht und kein Telefonat',
          'Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich dir im kostenlosen Training, Link in meiner Bio'],
    caption='''Ein Betrüger wollte am Telefon meine Seed-Phrase. Ich habe ihm eine gegeben.

Ich war in der Community eines Mining-Anbieters. Einer im Chat versuchte ständig, anderen ihre Zugänge abzunehmen. Dann rief er mich an. Seine Begründung: Ich müsse meine Wallet synchronisieren, sonst hätte ich keinen Zugang mehr zur Plattform. Dafür brauche er meine Seed-Phrase.

Ich habe ihm eine gegeben. Ausgedacht, Wort für Wort. Kurz darauf ist er ausgerastet.

Synchronisieren. Verifizieren. Aktualisieren. Die Wörter wechseln, die Bitte bleibt dieselbe: deine Seed-Phrase. Keine echte Plattform fragt danach. Nie.

Deine Seed-Phrase gehört in keine Nachricht und kein Telefonat. Wer danach fragt, hat sich damit verraten.

Für alle, die mit Krypto und Bitcoin anfangen und ihre Wallet selbst verwahren.

Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich dir im kostenlosen Training. Link in meiner Bio.''')

# ---------- Beitrag 15: FAQ (Fake-Profil mit meinem Namen) ----------
POSTS['beitrag-15'] = dict(
    date='2026-10-10', fmt='FAQ beantworten', topic='FAQ: „Chris hat mir geschrieben“ – Fake-Account mit meinem Namen, woran man mich erkennt',
    slides=[
        s_hook('FAQ', '„Chris hat mir geschrieben.“ %s' % A('Ist das wirklich Chris?'), size=''),
        s_point('ECHTER FALL', 'Jemand hat sich als mich ausgegeben.',
                ['Ich war Admin in der Telegram-Gruppe eines Coin-Projekts. Ein Fake-Account mit meinem Namen schrieb Mitglieder an.',
                 D('Er räumte Wallets leer. Geschätzter Schaden: 4.000 bis 5.000 €.')], size='m'),
        s_point('WIE ICH ES ERFAHREN HABE', '„Mir schreibt unter Deinem Namen jemand und bedrängt mich.“',
                ['Diese Nachricht bekam ich von einer Teilnehmerin.', D('Sie hat es geahnt. Andere haben es zu spät gemerkt.')], size='sm'),
        s_point('UND DAS PROJEKT?', 'Ich wollte wissen, wer dahintersteckt.',
                ['Als Admin habe ich nach dem Entwicklerteam gefragt.', D('Antwort: keine. Heute weiß ich, warum.')], size='m'),
        s_point('SO ERKENNST DU MICH', 'Drei Dinge mache ich nie.',
                ['Ich frage nie nach deiner Seed-Phrase oder deinen Passwörtern.',
                 'Ich verlange nie eine Gebühr, damit du Geld zurückbekommst.',
                 D('Ich schicke dir nie einen Link, um deine Wallet zu „sichern“.')]),
        s_point('ZUM MERKEN', 'Namen und Bilder lassen sich kopieren. %s' % A('Prüf jedes Zeichen im Nutzernamen.'),
                ['Mein Krypto-Account auf Instagram: @_chrisalcatrez_'], meta=True, size='m'),
        s_point('SPEICHERN', 'Speichere den Beitrag. Dann weißt du im Ernstfall, %s' % A('woran du mich erkennst.'), None, meta=True, size='m'),
    ],
    alts=['FAQ: Chris hat mir geschrieben, ist das wirklich Chris?',
          'Echter Fall: Ein Fake-Account mit meinem Namen schrieb Mitglieder einer Telegram-Gruppe an, geschätzter Schaden 4.000 bis 5.000 Euro',
          'Eine Teilnehmerin schrieb mir: Mir schreibt unter Deinem Namen jemand und bedrängt mich',
          'Als Admin habe ich nach dem Entwicklerteam gefragt, Antwort: keine',
          'Drei Dinge mache ich nie: nach Seed-Phrase oder Passwörtern fragen, Gebühren für Rückholung verlangen, Links zum Sichern der Wallet schicken',
          'Namen und Bilder lassen sich kopieren, prüf jedes Zeichen im Nutzernamen, mein Krypto-Account auf Instagram ist @_chrisalcatrez_',
          'Speichere den Beitrag, dann weißt du im Ernstfall, woran du mich erkennst'],
    caption='''„Chris hat mir geschrieben.“ Ist das wirklich Chris?

Die Frage ist berechtigt. Denn jemand hat sich schon als mich ausgegeben.

Ich war Admin in der Telegram-Gruppe eines Coin-Projekts. Ein Fake-Account mit meinem Namen schrieb Mitglieder an und räumte Wallets leer. Geschätzter Schaden: 4.000 bis 5.000 €. Erfahren habe ich es von einer Teilnehmerin: „Mir schreibt unter Deinem Namen jemand und bedrängt mich.“ Sie hat es geahnt. Andere haben es zu spät gemerkt.

Ich wollte wissen, wer hinter dem Projekt steckt, und habe als Admin nach dem Entwicklerteam gefragt. Antwort: keine. Heute weiß ich, warum.

Drei Dinge mache ich nie:
– Ich frage nie nach deiner Seed-Phrase oder deinen Passwörtern.
– Ich verlange nie eine Gebühr, damit du Geld zurückbekommst.
– Ich schicke dir nie einen Link, um deine Wallet zu „sichern“.

Namen und Bilder lassen sich kopieren. Prüf jedes Zeichen im Nutzernamen. Mein Krypto-Account auf Instagram: @_chrisalcatrez_

Für alle, die in Krypto-Gruppen auf Telegram oder Instagram unterwegs sind.

Speichere den Beitrag. Dann weißt du im Ernstfall, woran du mich erkennst.''')

# ---------- Beitrag 16: Frage an die Zielgruppe (Wochenrueckblick) ----------
POSTS['beitrag-16'] = dict(
    date='2026-10-11', fmt='Frage an die Zielgruppe', topic='Welche dieser sechs Maschen ist dir schon begegnet? (Rückblick auf die echten Fälle)',
    slides=[
        s_list('ECHTE FÄLLE DIESER WOCHE', 'Welche Masche ist dir %s' % A('schon begegnet?'), [
            'Werbung für Trading mit persönlicher Handelspartnerin',
            'Mail von „Behörde“ oder „Kanzlei“, die dein Geld zurückholen will',
            '„Wallet verifizieren wegen neuer Geldwäscheregeln“',
            '„Support“ meldet sich nach deiner Frage in der Gruppe',
            'Anruf: „Deine Wallet muss synchronisiert werden“',
            'Fake-Profil eines Admins',
        ], 'Schreib die Zahl in die Kommentare.', sub='Jede davon hat Menschen aus meiner Community Geld gekostet.'),
    ],
    alts=['Welche Masche ist dir schon begegnet? 1 Werbung für Trading mit persönlicher Handelspartnerin, 2 Mail von Behörde oder Kanzlei, die dein Geld zurückholen will, 3 Wallet verifizieren wegen neuer Geldwäscheregeln, 4 Support meldet sich nach deiner Frage in der Gruppe, 5 Anruf, deine Wallet muss synchronisiert werden, 6 Fake-Profil eines Admins. Schreib die Zahl in die Kommentare'],
    caption='''Diese Woche habe ich dir echte Fälle gezeigt. Welche Masche ist dir schon begegnet?

1. Werbung für Trading mit persönlicher Handelspartnerin
2. Mail von „Behörde“ oder „Kanzlei“, die dein Geld zurückholen will
3. „Wallet verifizieren wegen neuer Geldwäscheregeln“
4. „Support“ meldet sich nach deiner Frage in der Gruppe
5. Anruf: „Deine Wallet muss synchronisiert werden“
6. Fake-Profil eines Admins

Jede davon hat Menschen aus meiner Community Geld gekostet. Wer darüber spricht, warnt andere Krypto-Anfänger.

Für alle, die mit Krypto und Bitcoin anfangen und die Maschen kennen wollen, bevor sie ihnen begegnen.

Schreib die Zahl in die Kommentare.''')

if __name__ == '__main__':
    which = sys.argv[1:] or list(POSTS)
    allpng = {}
    ok_all = True
    for name in which:
        p = POSTS[name]
        ok = check_text(name + ' Caption', p['caption']) and all(check_text(name + ' Alt', a) for a in p['alts'])
        ok_all = ok_all and ok
        assert len(p['alts']) == len(p['slides']), name + ': Alt-Texte passen nicht'
        allpng[name] = build(name, p['slides'])
    json.dump(allpng, open(os.path.join(OUT, 'pngs.json'), 'w'), indent=1)
    print('Texte sauber:', ok_all)
