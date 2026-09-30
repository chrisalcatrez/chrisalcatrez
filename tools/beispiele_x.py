# Erste Ladung Tweets fuer X (01.10.–05.10.2026). Jeder Eintrag: datum, uhrzeit (Europe/Berlin), format, text,
# optional thread (weitere Tweets), optional bild (Name der Bildfunktion in bilder.py), alt-Text.
LINK = 'https://chrisalcatrez.de'

TWEETS = [
 dict(d='2026-10-01', t='08:12', f='Statement', bild=None,
      text="""Die teuerste App auf meinem Handy war kostenlos.

Eine Wallet-App aus dem App Store. Sah aus wie das Original. Den Anbieter gab es als Handy-App nie.

70.000 $ weg.

Seitdem lade ich keine Wallet mehr, ohne vorher die Adresse auf der Website des Anbieters zu prüfen."""),

 dict(d='2026-10-01', t='18:41', f='Frage an die Zielgruppe', bild=None,
      text="""Hand aufs Herz: Hast du schon mal Geld an jemanden geschickt, den du nur aus dem Internet kennst?

Ich schon. Zweimal. Beide Male weg.

Ja oder Nein reicht mir als Antwort."""),

 dict(d='2026-10-02', t='08:07', f='Thread (Aufzählung)', bild=None,
      text="""Drei Sätze, nach denen ich jedes Gespräch beende.

Alle drei haben mich früher Geld gekostet. Kurzer Thread.""",
      thread=[
"""1. „Vor der Auszahlung fällt eine kleine Gebühr an.“

Hab ich bezahlt. Die Auszahlung kam nie.

Eine echte Börse zieht Gebühren vom Guthaben ab. Vorkasse für die eigene Auszahlung gibt es nur bei Betrügern.""",
"""2. „Ich brauche kurz Ihre 12 Wörter, damit wir die Wallet synchronisieren können.“

Wollte mal jemand am Telefon von mir. Ich hab ihm zwölf ausgedachte Wörter gegeben. Er ist ausgerastet.

Die Wörter sind das Geld. Niemand braucht sie außer dir.""",
"""3. „Sie haben Anspruch auf eine Entschädigung. Wir holen Ihr Geld zurück.“

Kommt gern nach dem ersten Verlust, als Kanzlei oder Behörde verkleidet.

Echte Behörden schicken keine Mails mit Frist und Vorkasse.""",
"""Wer diese drei Sätze kennt, überspringt die teuersten Momente am Anfang.

Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren, zeige ich im kostenlosen Training: %s""" % LINK]),

 dict(d='2026-10-02', t='18:52', f='Meme (Bild)', bild='meme_gebuehr', alt='Zwei Felder: links, was der Betrüger schreibt, rechts, was er meint.',
      text="""Kleine Übersetzungshilfe für Krypto-Chats.

Diese Lektion hab ich mit echtem Geld bezahlt."""),

 dict(d='2026-10-03', t='09:33', f='Geschichte', bild=None,
      text="""Ich lebe in Venezuela. Freiwillig.

Hier zeigt dir jeder Einkauf, was Inflation mit Erspartem macht. Die Preise stehen in Dollar, die Landeswährung rechnet kaum jemand um.

Deshalb bin ich bei Krypto gelandet. Digital bezahlt, Ersparnisse weg vom Bankkonto."""),

 dict(d='2026-10-03', t='18:46', f='Nischenmythos (Bild)', bild='vs_betrug', alt='Zwei Spalten: links der Mythos, Krypto sei nur Betrug, rechts, was Chris erlebt hat.',
      text="""„Krypto ist doch alles Betrug.“

Hab ich früher auch gesagt, nachdem mich zwei Betrüger erwischt hatten.

Heute weiß ich: Der Betrug passiert um Krypto herum. Gefälschte Apps, falsche Berater, erfundene Gebühren.

Bitcoin selbst hat keinen Chef, der dich anruft."""),

 dict(d='2026-10-04', t='09:28', f='Aufzählung', bild=None,
      text="""5 Dinge, die ich vor meinem ersten Bitcoin gewusst hätte:

1. Verkaufsdruck kommt von innen, nie vom Kurs.
2. Feste Rendite heißt: Jemand hat einen Plan mit deinem Geld.
3. Die 12 Wörter sind das Geld.
4. Kleine Beträge sind die beste Schule.
5. Gewinn zählt erst auf dem Konto."""),

 dict(d='2026-10-04', t='18:49', f='Schritt-für-Schritt (Teaser)', bild=None,
      text="""Wenn ich heute mit Krypto bei null anfangen würde:

100 € statt 10.000 €.
Eine Börse mit Sitz in der EU.
Wallet-App nur von der Website des Anbieters.
Kein Chat mit Fremden über mein Geld.

Mein System hat vier Schritte. Der Rest steht im kostenlosen Training, Link im Profil."""),

 dict(d='2026-10-05', t='08:09', f='Chat (Bild)', bild='chat_gebuehr', alt='Nachgestellter Chat mit einem falschen Support, der vor der Auszahlung eine Netzwerkgebühr verlangt.',
      text="""Nachgestellt, so lief es damals bei mir ab.

Die Gebühr hab ich bezahlt. Die Auszahlung kam nie.

Meine Regel seitdem: Eine Auszahlung, für die ich vorher Geld schicken soll, gibt es nie."""),

 dict(d='2026-10-05', t='18:44', f='Erfolgsgeschichte', bild=None,
      text="""Damals: 70.000 $ weg, alle Bitcoin in Panik verkauft, jeden Tag zehn Meinungen gelesen.

Heute: vier Schritte, Sparplan statt Timing, fünfstelliger Gewinn im Jahr. Meine Zahl, kein Versprechen für dich.

Der Unterschied? Ich verstehe, was ich kaufe. Training im Profil."""),
]
