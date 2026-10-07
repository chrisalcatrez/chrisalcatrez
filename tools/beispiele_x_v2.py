# Tweets nach dem Bauplan v2 (ab 08.10.2026): HOOK (erste Zeile allein) -> BEWEIS (Zahl oder Handlung)
# -> ERKENNTNIS (ein Satz aus dem Fall) -> FRAGE (genau eine, polarisierend, kurz beantwortbar).
# Training nur im Wochen-Thread (vorletzter Tweet Link, letzter Tweet Frage) und im Format Damals–Heute (ein Satz, keine Frage).
# Jeder Eintrag: d (Datum), t (Uhrzeit Europe/Berlin), f (Format wie in der Aufgabe, Abschnitt 4), text, optional thread,
# optional bild (Datei in x/) und alt. MUSTER = eingeplant; VORLAGEN = Beispiele fuer Formate, die in der ersten Woche fehlen;
# FAELLE = oeffentliche Betrugsfaelle mit Kernzahlen, Quelle und Rechtsstand (Stand 07.10.2026, vor Verwendung per Websuche bestaetigen).
import re
LINK = 'https://chrisalcatrez.de'

def xlen(s):
    """Gewichtete Zeichenzahl wie bei X: URL 23, Zeichen bis 0x10FF und einige Bereiche 1, alle anderen 2."""
    n = 0
    for url in re.findall(r'https?://\S+', s):
        s = s.replace(url, '')
        n += 23
    for ch in s:
        cp = ord(ch)
        n += 1 if (cp <= 0x10FF or 0x2000 <= cp <= 0x200D or 0x2010 <= cp <= 0x201F or 0x2032 <= cp <= 0x2037) else 2
    return n

MUSTER = [
 dict(d='2026-10-08', t='08:47', f='Persönliche Case Study',
      text="""Unter meinem Namen wurden Wallets leergeräumt. Rund 4.000 bis 5.000 €.

Ich war Admin einer Telegram-Gruppe. Ein zweiter Account mit meinem Namen schrieb Mitglieder privat an. Danach waren Wallets leer.

Ein Name beweist null.

Hat dich je ein „Admin“ privat angeschrieben?"""),

 dict(d='2026-10-08', t='18:33', f='Mythos → Realität', bild='x/x-16.png',
      alt='Zwei Spalten: links der Mythos, mit dem richtigen Memecoin habe man ausgesorgt, rechts, was Chris mit einem Memecoin erlebt hat.',
      text="""Den „richtigen“ Memecoin hatte ich. Dachte ich.

Gekauft, ohne zu verstehen, was ich kaufe. Beim Absturz konnte ich keinem erklären, was ich da gehalten hatte.

Seitdem kaufe ich nur, was ich in zwei Sätzen erklären kann.

Memecoins: Spielgeld oder echte Chance?"""),

 dict(d='2026-10-09', t='09:16', f='Persönliche Case Study',
      text="""Drei Meinungen pro Abend, null eigene. Mein Anfang.

1. Video: jetzt kaufen.
2. Nächstes Video: bloß raus.
3. Chat: ein Coin, den keiner kennt.

Lange hab ich jemanden gesucht, der nickt. Gefunden hab ich Leute, die mein Geld wollten.

Wem glaubst du: Videos, Chats oder keinem?"""),

 dict(d='2026-10-09', t='19:02', f='Contrarian Take + Beweis',
      text="""Zu spät für Bitcoin war ich nie. Zu hastig schon.

Ende 2024 hab ich alle Bitcoin in Panik verkauft, weil ich den richtigen Moment wollte.

„Zu spät?“ sucht einen Tag. Der Markt kennt keinen, mein Sparplan auch keinen. Fester Tag, feste Summe.

Sparplan oder warten?"""),

 dict(d='2026-10-10', t='10:04', f='Scam-Teardown kurz', bild='x/x-19.png',
      alt='Nachgestellter Chat: Ein angeblicher Wallet-Support droht mit einer Sperre in 24 Stunden und schickt einen Link zum Bestätigen.',
      text="""24 Stunden Frist, ein Link, eine Drohung. Nachgestellt.

Laut Verbraucherzentrale erkennt man Phishing an Eile und Drohung. Wer hinter dem Link seine 12 Wörter eingibt, hat sie verschenkt.

Die Frist ist der Trick.

Schon mal unter Zeitdruck auf so einen Link geklickt?"""),

 dict(d='2026-10-10', t='18:26', f='Damals–Heute',
      text="""70.000 $ weg. Mein größter Fehlgriff war nie Bitcoin.

Eine Wallet-App, die nur echt aussah. Den Anbieter gab es als Handy-App nie. Der Kurs war unbeteiligt.

Heute zahle ich in Venezuela mit Krypto. Den Weg dazwischen zeige ich im kostenlosen Training, Link im Profil."""),

 dict(d='2026-10-11', t='09:51', f='Contrarian Take + Beweis',
      text="""Jeden Betrüger, der mich erwischt hat, hab ich selbst reingelassen.

Eingebrochen ist keiner. Die Wallet-App selbst geladen, 70.000 $. Den Coin selbst gekauft, 5.000 $. Jedes Mal mein Finger.

Gier macht die Tür von innen auf.

Gefährlicher: der Betrüger oder die eigene Gier?"""),

 dict(d='2026-10-11', t='18:39', f='Contrarian Take + Beweis',
      text="""Du brauchst keine 10.000 €, um mit Krypto anzufangen. 100 reichen.

Ich hab mit Tausendern angefangen. 5.000 $ in einem Influencer-Coin, weg. Mit 100 $ hätte ich denselben Kurs fallen sehen.

Groß anfangen lehrt dasselbe. Nur teurer.

Mit welcher Summe hast du angefangen?"""),

 dict(d='2026-10-12', t='08:14', f='Thread (Die 5 Regeln)',
      text="""5 Regeln, die ich nach 70.000 $ Verlust nie wieder breche.

Jede davon hat mich vorher Geld gekostet. Die erste gleich 70.000 $.""",
      thread=[
"""1. Keine Wallet-App ohne Prüfung auf der Website des Anbieters.
Meine sah echt aus, den Anbieter gab es als Handy-App nie. 70.000 $ weg.

2. Keine Gebühr vor einer Auszahlung.
Die „Netzwerkgebühr“ hab ich gezahlt. Die Auszahlung kam nie.""",
"""3. Die 12 Wörter verlassen das Papier nie.
Ein Anrufer wollte sie zum „Synchronisieren“. Er bekam zwölf erfundene.

4. Keine feste Rendite.
Cloud-Mining mit festem Ertrag hat mich 4.000 bis 5.000 $ gekostet.""",
"""5. Kein Verkauf aus Panik.
Ende 2024 hab ich alle Bitcoin verkauft, weil der Kurs fiel. Verkauft hat meine Angst, nie mein Plan.

Fünf Regeln, fünf Narben. Keine davon kam vom Markt. Jedes Mal war es mein Finger.""",
"""Die drei teuersten davon zeige ich im kostenlosen Training: %s""" % LINK,
"""Welche der fünf Regeln würdest du am ehesten brechen?"""]),

 dict(d='2026-10-12', t='18:51', f='Mythos → Realität', bild='x/x-24.png',
      alt='Zwei Felder. Links, was der Chat sagt: Bitcoin ist langweilig, das große Geld liegt in den kleinen Coins. Rechts, was dein Konto sagt: Langweilig hätte ich jetzt gern zurück.',
      text="""Der Chat hat bei kleinen Coins nie Geld verloren. Mein Konto schon.

Ich hab gekauft, was der Chat feierte. Beim Absturz feierte er schon den nächsten. Ich saß mit dem Rest da.

Ein Chat haftet nie. Dein Konto immer.

Womit bist du gestartet: Bitcoin oder kleine Coins?"""),

 dict(d='2026-10-13', t='09:03', f='Persönliche Case Study',
      text="""Zwölf Wörter hab ich dem Betrüger am Telefon diktiert. Alle erfunden.

Er wollte meine Wallet „synchronisieren“, dafür brauche er die 12 Wörter. Als keins davon stimmte, ist er ausgerastet.

Wer deine 12 Wörter will, will dein Geld.

Auflegen oder mitspielen: Was würdest du tun?"""),

 dict(d='2026-10-13', t='19:13', f='Mythos → Realität', bild='x/x-26.png',
      alt='Zwei Spalten: links der Mythos, Krypto sei nur Zocken, rechts, was Chris erlebt hat. Gezockt hat er, solange er blind kaufte, heute läuft ein System mit vier Schritten.',
      text="""„Krypto ist nur Zocken.“ Stimmte. Bis ich aufgehört hab zu zocken.

Blind gekauft, Influencer-Coin, 5.000 $ weg. Heute verstehe ich jeden Kauf und halte lange. Aufregend ist daran wenig.

Zocken ist eine Entscheidung, kein Merkmal von Krypto.

Krypto: Zocken oder Anlage?"""),

 dict(d='2026-10-14', t='08:58', f='1 Begriff in 60 Sekunden',
      text="""2.861 $ pro Coin. Minuten später 0. Rug Pull.

Squid-Token, November 2021. Verkaufen ging nie, die Funktion fehlte. Die Macher zogen laut BBC rund 3,4 Mio. $ ab.

Mein Influencer-Coin lief genauso, nur langsamer. 5.000 $.

Wer ist schuld: die Macher oder die Käufer?"""),

 dict(d='2026-10-14', t='18:37', f='Datenpunkt → Bedeutung',
      text="""25 Jahre Haft, im Juni 2026 bestätigt (Bloomberg Law).

So lange sitzt der FTX-Gründer. 2022 fehlten in seiner Börse rund 8 Mrd. $ Kundengeld. Dann war sie zu.

Auf der Börse sind Coins ein Versprechen. In der Wallet Besitz.

Wo liegen deine Coins: Börse oder eigene Wallet?"""),
]

# Vorlagen fuer Formate, die in der ersten Woche fehlen. Nie wortgleich uebernehmen, nur als Muster fuer Ton und Bau.
VORLAGEN = [
 dict(f='Thread (Scam-Teardown)',
      text="""83.000 € standen auf seinem Handelskonto. Ausgezahlt wurden 5 €.

Peter (Name geändert) aus meiner Community. So lief der Betrug ab, Schritt für Schritt.""",
      thread=[
"""1. Der Köder. Eine Werbung auf Instagram. Für gut 250 € wurde sein Handelskonto „aktiviert“.

2. Das Vertrauen. „Laura“, angeblich zehn Jahre Erfahrung, rief mehrmals täglich an und handelte für ihn.""",
"""3. Die große Zahlung. Für ein Sechs-Monats-Angebot über 10.000 € legte „Laura“ angeblich 5.000 € privat dazu. Er holte 5.000 € als Bargeld von der Kreditkarte.

4. Die Zahl auf dem Bildschirm. 83.000 €. Ausgezahlt: 5 €.""",
"""5. Der Druck. Vor jeder Überweisung ein Videoanruf mit geteiltem Bildschirm. Am Ende Mails einer falschen „Europäischen Zentralbank“ mit Frist.

Schaden laut Anzeige rund 62.000 €. Jeder Schritt sah für sich harmlos aus.""",
"""Die drei Fehlgriffe, an denen Anfänger am meisten verlieren, zeige ich im kostenlosen Training: %s""" % LINK,
"""Bei welchem Schritt wärst du ausgestiegen?"""]),

 dict(f='Thread (Entscheidungs-Fragen)',
      text="""Bevor du einen Coin kaufst, beantworte diese 4 Fragen.

Jede davon hat mich Geld gekostet, bevor ich sie kannte.""",
      thread=[
"""1. Wer hat den Coin gemacht? Name, Gesicht, ein Team, das antwortet. In meiner Telegram-Gruppe kam auf die Frage nach dem Entwicklerteam nie eine Antwort.

2. Wie viel halten die Macher selbst? Halten sie den Großteil, gehört der Coin ihnen.""",
"""3. Welche Börse handelt ihn? Ein Token ohne Börse ist nur ein Name im Wallet-Bildschirm.

4. Kannst du ihn in zwei Sätzen erklären? Meinen Influencer-Coin konnte ich keinem erklären. 5.000 $ weg.""",
"""Vier Fragen, 5.000 $ billiger als meine Version. Wie sie in mein System aus vier Schritten passen, zeige ich im kostenlosen Training: %s""" % LINK,
"""Welche Frage überspringst du am ehesten?"""]),

 dict(f='Red Flags',
      text="""5 Warnzeichen, an denen ich heute jeden Krypto-Betrug erkenne. Jedes hat mich vorher Geld gekostet.

1. Gebühr vor der Auszahlung.
2. Jemand will deine 12 Wörter.
3. Feste Rendite.
4. Frist mit Drohung.
5. Der Support schreibt dich zuerst an.

Welches hast du schon erlebt?"""),

 dict(f='A gegen B',
      text="""Börse oder eigene Wallet? Verloren hab ich auf keiner Börse.

Meine 70.000 $ gingen an eine gefälschte Wallet-App. Der falsche Download hat mir geschadet, die Börse nie.

Die Wallet gehört dir, mit allem, was du damit falsch machst.

Börse oder Wallet: Wo liegt dein Geld?"""),

 dict(f='Was ich heute anders machen würde',
      text="""Wenn ich heute mit 500 € anfangen würde, wären das meine 4 Regeln.

1. 100 € zuerst, Rest wartet.
2. Wallet-App nur von der Anbieter-Website.
3. Kein Chat mit Fremden über Geld.
4. Jeden Kauf erklären können.

Ich hatte keine davon. Fast 80.000 $.

Welche brichst du zuerst?"""),

 dict(f='Meme', bild='x_meme',
      alt='Zwei Felder: links, was der Support schreibt, rechts, was er meint.',
      text="""Kleine Übersetzungshilfe für Krypto-Chats.

Diese Zeile hat mich eine Auszahlung gekostet. Die Gebühr war echt, die Auszahlung erfunden.

Hättest du die Gebühr gezahlt?"""),

 dict(f='Frage an die Zielgruppe',
      text="""Hand aufs Herz: Hast du schon mal Geld an jemanden geschickt, den du nur aus dem Internet kennst?

Ich schon. Zweimal. Beide Male weg.

Ja oder Nein?"""),

 dict(f='Live-Reaktion (Vorlage, nur mit belegter Nachricht)',
      text="""<Zahl aus der Nachricht>. <Was gerade passiert ist, ein Satz, laut <Medium>>.

<Was das für Anfänger bedeutet, zwei Sätze, mit Chris' Erfahrung derselben Masche im Kleinen.>

<Erkenntnis aus genau diesem Fall, ein Satz.>

<Polarisierende Frage, in einem Wort beantwortbar?>"""),
]

# Oeffentliche Faelle. Rechtsstand: 'verurteilt' (Betrug/Betrueger erlaubt), 'angeklagt' (nur angeklagt, gesucht, laut Anklage),
# 'verfahren' (Verfahren laeuft, Verdacht), 'zahlen' (kein Verfahren: nur belegte Zahlen, keine Bewertung, kein Wort Betrug),
# 'ereignis' (ohne Taeter). Vor jeder Verwendung per Websuche bestaetigen und Quelle im Tweet nennen.
FAELLE = {
 'FTX': dict(stand='verurteilt', fakten='Börse, November 2022 zusammengebrochen, Loch von rund 8 Mrd. $ Kundengeld; Sam Bankman-Fried November 2023 in sieben Punkten verurteilt, März 2024 25 Jahre Haft und 11 Mrd. $ Einziehung; Berufung am 12.06.2026 vom Bundesberufungsgericht (2nd Circuit) abgewiesen.', quelle='Bloomberg Law, Bitcoin Magazine (Juni 2026)'),
 'Terra/Luna': dict(stand='verurteilt', fakten='Mai 2022 Zusammenbruch von UST und LUNA, rund 40 Mrd. $ Wert ausgelöscht; Do Kwon März 2023 in Montenegro mit gefälschtem Pass festgenommen, Ende 2024 an die USA ausgeliefert, August 2025 schuldig bekannt, am 11.12.2025 zu 15 Jahren Haft verurteilt.', quelle='The Block, Bloomberg (Dezember 2025)'),
 'Celsius': dict(stand='verurteilt', fakten='Juni 2022 Auszahlungen eingefroren, Milliarden Kundengeld; Alex Mashinsky Dezember 2024 schuldig bekannt, Mai 2025 12 Jahre Haft.', quelle='US-Justizministerium (Mai 2025)'),
 'Thodex': dict(stand='verurteilt', fakten='Türkische Börse, April 2021 über Nacht offline, Gründer Faruk Fatih Özer nach Albanien geflohen, 2022 gefasst, September 2023 in der Türkei zu 11.196 Jahren Haft verurteilt.', quelle='Reuters, BBC (September 2023)'),
 'OneCoin': dict(stand='angeklagt', fakten='2014 bis 2017, laut US-Justiz rund 4 Mrd. $ und nie eine echte Blockchain; Gründerin Ruja Ignatova („Cryptoqueen“) seit Oktober 2017 verschwunden, seit 2022 auf der FBI-Liste der zehn meistgesuchten Flüchtigen, 5 Mio. $ Belohnung (2024); Mitgründer Karl Sebastian Greenwood September 2023 20 Jahre Haft (verurteilt).', quelle='FBI, US-Justizministerium'),
 'BitConnect': dict(stand='angeklagt', fakten='Januar 2018 Zusammenbruch, laut US-Justiz rund 2,4 Mrd. $; Gründer Satish Kumbhani 2022 angeklagt und flüchtig; Promoter Glenn Arcaro 38 Monate Haft (verurteilt).', quelle='US-Justizministerium'),
 'PlusToken': dict(stand='verurteilt', fakten='Schneeballsystem aus China 2018 bis 2019, laut chinesischem Gericht 2020 Millionen Beteiligte und Einzahlungen im Milliardenbereich, Haftstrafen bis 11 Jahre. Zahlen vor Verwendung prüfen.', quelle='Urteil Yancheng 2020, Berichte Reuters/CoinDesk'),
 'LIBRA': dict(stand='verfahren', fakten='Argentinien, 14.02.2025, Präsident Milei postete den Token; Kurs in Stunden von 0,01 $ auf rund 5 $, binnen vier Stunden abgestürzt; über 44.000 Betroffene; Verfahren in Buenos Aires und vor einem Gericht in New York, keine Verurteilung (Stand Februar 2026).', quelle='Buenos Aires Times (Februar 2026)'),
 'TRUMP': dict(stand='zahlen', fakten='Memecoin, gestartet 17.01.2025; laut Chainalysis/CNBC (Mai 2025) rund 2 Mio. Käuferkonten, 764.000 davon mit Verlust, 58 Wallets mit je über 10 Mio. $ Gewinn; Trump-nahe Firmen halten laut Projektseite den Großteil; Mai 2025 Abendessen für die größten Halter.', quelle='CNBC/Chainalysis (Mai 2025)'),
 'MELANIA': dict(stand='zahlen', fakten='Memecoin, gestartet 19.01.2025, danach deutlich unter dem Startkurs. Zahlen vor Verwendung prüfen.', quelle='Reuters'),
 'WLFI': dict(stand='zahlen', fakten='World Liberty Financial (Trump-Familie), Handel seit 01.09.2025; Frühkäufer zahlten laut Wall Street Journal 1,5 Cent, Eröffnung 24 Cent, am ersten Tag unter den Eröffnungskurs gefallen; Familie hält rund 22,5 Mrd. Token.', quelle='Wall Street Journal/dpa (September 2025)'),
 'HAWK': dict(stand='zahlen', fakten='Memecoin von Haliey Welch, 04.12.2024, Marktwert binnen Stunden um über 90 % gefallen; die SEC stellte 2025 keine Anklage gegen Welch.', quelle='Decrypt, DL News (2025)'),
 'LAPTOP': dict(stand='zahlen', fakten='Memecoin von Hunter Biden, Start 09.09.2026 auf Base, 1 Mrd. Token; laut Coin360 binnen Stunden um über 90 % gefallen, Berichte über Insider-Wallets und Sniper-Bots; das Team bestreitet einen Rug Pull. Die Kurs- und Marktwertzahlen in den Berichten widersprechen sich: nur „um über 90 % gefallen laut <Medium>“.', quelle='Fortune, Coin360 (September 2026)'),
 'EthereumMax': dict(stand='zahlen', fakten='Kim Kardashian zahlte 2022 1,26 Mio. $ an die SEC, weil sie eine Bezahlung für Werbung verschwieg, ohne Schuldeingeständnis.', quelle='SEC (Oktober 2022)'),
 'CryptoZoo': dict(stand='zahlen', fakten='Logan Paul bot 2024 Rückzahlungen von 2,3 Mio. $ an; Zivilklage.', quelle='Berichte 2024'),
 'Mt. Gox': dict(stand='ereignis', fakten='Börse in Japan, Februar 2014 insolvent, 850.000 Bitcoin verschwunden; Rückzahlungen an Gläubiger seit Juli 2024.', quelle='Reuters'),
 'QuadrigaCX': dict(stand='ereignis', fakten='Kanadische Börse, Gründer Gerald Cotten starb Dezember 2018, angeblich als einziger Inhaber der Schlüssel; laut kanadischer Aufsicht OSC (2020) ein Schneeballsystem.', quelle='Ontario Securities Commission (2020)'),
 'Squid-Token': dict(stand='ereignis', fakten='Ab 20.10.2021 handelbar, Höchstkurs 2.861 $, am 01.11.2021 in Minuten auf nahe null; keine Verkaufsfunktion für Käufer; Macher anonym, rund 3,38 Mio. $ abgezogen. „Rug Pull“ erlaubt.', quelle='BBC (November 2021)'),
}

if __name__ == '__main__':
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from gen import check_text
    ok = True
    for name, liste in (('MUSTER', MUSTER), ('VORLAGEN', VORLAGEN)):
        for e in liste:
            for i, t in enumerate([e['text']] + list(e.get('thread', []))):
                n = xlen(t)
                if n > 280 or not check_text('%s %s T%d' % (name, e['f'], i), t):
                    ok = False
                    print('!!', name, e['f'], 'T%d' % i, n)
            if e.get('alt') and not check_text('alt', e['alt']):
                ok = False
    for k, v in FAELLE.items():
        if not check_text(k, v['fakten']):
            ok = False
    print('ok' if ok else 'pruefen')
