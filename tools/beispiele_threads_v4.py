# Threads nach der Vorgabe vom 07.10.2026: Hook als Ergebnis (1 Zahl + 1 Kontrast, hoechstens 12 Woerter),
# dann Beleg, eine Erkenntnis, ein Takeaway-Satz (ohne Ich, zum Weiterschicken), zuletzt genau eine Frage.
# MUSTER: Beitraege 15 bis 22 (08. bis 11.10.2026). RESERVE: weitere Varianten je Thema (Fall, These, Story),
# frei ab dem Datum in frei_ab; nach dem Einplanen verwendet='TT.MM.JJJJ' setzen. Neue Reserve-Varianten haengt die
# taegliche Aufgabe hier an. Alle Texte sind mit gen.check_text() geprueft und hoechstens 500 Zeichen lang.
LINK = 'https://chrisalcatrez.de'

MUSTER = [
 dict(n=15, d='2026-10-08', t='09:12', f='Geschichte', feld='Betrug', var='Story',
      thema='Köder-Wallet: fremde Seed-Phrase unter meinem Video, 10 $ TRX-Gebühr nach Minuten weg',
      text="""Fremde Wallet, fünfstellig voll. Meine 10 $ Gebühr: nach Minuten weg.

Die 12 Wörter standen unter einem Video auf meinem alten YouTube-Kanal. „Wallet gefunden, wer hilft mir?“ Ich hab sie eingegeben. Das Guthaben stand da, in USDT.

Zum Auszahlen fehlte Gebühr in TRX. 10 $ rein. Weg. Wieder 10 $. Wieder weg.

Die Wallet war der Köder, die Gebühr sein Verdienst. Bewegen kann das Geld nur er.

Wer eine Seed-Phrase verschenkt, hat die Wallet nie verloren.

Hättest du die 10 $ riskiert?"""),

 dict(n=16, d='2026-10-08', t='18:48', f='Nischenmythos', feld='Betrug', var='Fall',
      thema='Fall aus der Community: „USDT“ in der Wallet, Verkaufswert 0 € (USDTS, USDCF, selbstgebaute Token)',
      text="""„USDT“ in der Wallet. Verkaufswert: 0 €.

Ein Teilnehmer bat mich um Hilfe, seine Coins ließen sich nirgends verkaufen. Sie hießen USDTS und USDCF.

Selbstgebaute Token. Name wie ein Stablecoin, dahinter keine Börse, kein Markt, kein Käufer.

Einen Token baut jeder in Minuten und nennt ihn, wie er will. Der Name im Wallet-Bildschirm beweist null. Die Zahl dahinter auch.

Ohne Börse, die ihn handelt, ist ein Token nur ein Name.

Hattest du schon mal einen Coin, den du nirgends loswurdest?"""),

 dict(n=17, d='2026-10-09', t='08:36', f='Aufzählung', feld='Betrug', var='Fall',
      thema='Vier Sätze des falschen Traders: dieselbe Gebühr zwei-, dreimal an eine Solana-Adresse, null Auszahlung',
      text="""Drei Begründungen, eine Gebühr, null Auszahlung.

Fake-Account eines bekannten Traders, Gebühr für den „Trading-Bot“ an eine Solana-Adresse. Zwei-, dreimal gezahlt.

1. „Netzwerkschwankungen, erneut senden.“
2. „Internetstörung, die Zahlung kam nie an.“
3. „Der Bot verlangt vor dem Trade eine Gebühr.“
4. Als ich ihn Betrüger nannte: „Dann trade ich nie wieder für dich.“

Satz 4 war der erste wahre.

Eine Gebühr, die zweimal fällig wird, ist keine Gebühr.

Bei welchem Satz wärst du ausgestiegen?"""),

 dict(n=18, d='2026-10-09', t='19:07', f='Statement', feld='Psychologie', var='These',
      thema='„Selbst schuld“ unter dem ersten Beitrag: stimmt, Preis 70.000 $, darum steht es hier',
      text="""„Selbst schuld“ stand unter meinem Beitrag. Stimmt. Preis: 70.000 $.

Keiner hat mich gezwungen. Die App hab ich selbst geladen, die Gebühr selbst gezahlt, den Coin selbst gekauft. Jedes Mal mein Finger.

Dazu stand da: erfunden. Erfunden wäre billiger gewesen.

Darum steht das hier. Selbst schuld hat mich 70.000 $ gekostet. Bei dir darf es ein Beitrag bleiben.

Was hat dich dein teuerstes „selbst schuld“ gekostet?"""),

 dict(n=19, d='2026-10-10', t='09:44', f='Erfolgsgeschichte', feld='Einstieg', var='Story',
      thema='Damals–Heute: Influencer-Coins, jeder endete im Rug Pull (einer 5.000 $), heute nur, was ich in zwei Sätzen erklären kann',
      text="""Jeder meiner Influencer-Coins endete im Rug Pull. Einer kostete 5.000 $.

Jedes Mal ein bekanntes Gesicht, jedes Mal dasselbe Ende: Die Macher verkauften auf einmal, der Kurs fiel senkrecht, die Käufer hielten den Rest.

Heute kaufe ich nur, was ich in zwei Sätzen erklären kann. Satz eins: wer den Coin gemacht hat und wie viel er selbst hält.

Reichweite ist kein Beleg. Ein Gesicht hält keinen Kurs.

Würdest du 5.000 € in einen Coin stecken, nur weil jemand mit 100.000 Followern ihn empfiehlt?"""),

 dict(n=20, d='2026-10-10', t='18:53', f='Thread (Schritt-für-Schritt)', feld='Betrug', var='Fall',
      thema='Die Falle mit der öffentlichen Seed-Phrase in vier Schritten (Thread, Link in der vorletzten Antwort, Frage am Ende)',
      text="""Fünfstelliges Guthaben, Seed-Phrase öffentlich im Kommentar. Die Falle in 4 Schritten.""",
      thread=[
        """1. Der Köder. Unter Videos und in Gruppen postet jemand seine 12 Wörter: „Wallet gefunden, wer hilft mir beim Abheben?“ Wer sie eingibt, sieht ein Guthaben in USDT auf dem Tron-Netzwerk.""",
        """2. Die Sperre. Die Wallet gehört weiter dem Betrüger. Auf Tron lassen sich die Rechte am Konto auf einen anderen Schlüssel übertragen. Deine 12 Wörter öffnen die Tür. Bewegen darf nur er.""",
        """3. Die Gebühr. Fürs Auszahlen braucht das Konto TRX. Du zahlst ein paar Dollar ein, ein Bot räumt sie in Minuten ab. Du zahlst wieder. Das ist das ganze Geschäft, mit vielen Leuten gleichzeitig.""",
        """4. Der Trick. Die Falle fängt nur Leute, die fremdes Geld wollen. Ich wollte. Zweimal 10 $. Wer eine Seed-Phrase öffentlich postet, hat die Wallet nie verloren.""",
        """Die Köder-Wallet war mein billigster Fehlgriff. Die drei teuren zeige ich im kostenlosen Training: https://chrisalcatrez.de""",
        """Hättest du die 12 Wörter eingegeben?""",
      ]),

 dict(n=21, d='2026-10-11', t='09:23', f='Chat (Bild)', feld='Sicherheit', var='Story',
      thema='Nachgestellt: der Anruf, bei dem ich zwölf erfundene Wörter vorgelesen hab',
      bild='https://raw.githubusercontent.com/chrisalcatrez/chrisalcatrez/main/threads/t-21.png', alt='Nachgestellter Chat eines Anrufs: Ein angeblicher Support verlangt die 12 Wörter, Chris liest ausgedachte vor, der Anrufer rastet aus.',
      text="""Er wollte meine 12 Wörter. Bekam zwölf. Alle erfunden.

Anruf aus der Community eines Mining-Anbieters: Meine Wallet müsse „synchronisiert“ werden, dafür brauche er sie. Ich hab Wörter vorgelesen, die mir gerade einfielen. Nachgestellt im Bild.

Als er es merkte, ist er ausgerastet. Weil die Wörter die Wallet sind. Mit echten hätte er alles abgeräumt, ohne Handy, ohne PIN, ohne mich.

Wer deine 12 Wörter will, will dein Geld.

Hat dich schon mal jemand nach deinen 12 Wörtern gefragt?"""),

 dict(n=22, d='2026-10-11', t='19:14', f='Frage an die Zielgruppe', feld='Einstieg', var='Frage',
      thema='Admin bei einem Coin-Projekt, Entwicklerteam null Antwort. Frage: Coin gekauft, ohne zu wissen, wer ihn gemacht hat?',
      text="""Admin bei einem Coin-Projekt. Entwicklerteam: null Antwort.

Ich war in der Telegram-Gruppe des Projekts Admin und hab nach dem Entwicklerteam gefragt. Es kam nie eine Antwort. Die Mitglieder hatten gekauft, ohne ein einziges Gesicht zu kennen.

Ein Team, das sich versteckt, hat einen Grund.

Hand aufs Herz: Hast du schon mal einen Coin gekauft, ohne zu wissen, wer ihn gemacht hat? Ja oder Nein."""),

]

RESERVE = [
 dict(thema='Köder-Wallet (öffentliche Seed-Phrase)', feld='Betrug', var='These', frei_ab='2026-10-22', verwendet=None,
      text="""Wer seine 12 Wörter öffentlich postet, verschenkt kein Geld. Er sammelt welches.

Unter meinen alten Videos stand das ständig: „Wallet gefunden, hier die Seed-Phrase.“ Dahinter fünfstellige Guthaben in USDT auf Tron. Zweimal hab ich 10 $ Gebühr eingezahlt, zweimal war sie nach Minuten weg.

Die Rechte am Konto liegen beim Betrüger. Die Gebühr ist sein Umsatz.

Eine verschenkte Wallet ist ein Köder mit Preisschild.

Hast du so einen Kommentar schon mal gesehen?"""),

 dict(thema='Köder-Wallet (öffentliche Seed-Phrase)', feld='Betrug', var='Fall', frei_ab='2026-10-22', verwendet=None,
      text="""Zwei fremde Wallets, zweimal 10 $ eingezahlt, zweimal nach Minuten leer.

Beide Seed-Phrasen standen unter meinen alten Videos. Beide zeigten fünfstellige USDT-Guthaben auf Tron. Beide verlangten TRX fürs Auszahlen.

Auf Tron liegen die Rechte am Konto bei einem anderen Schlüssel. Die 12 Wörter zeigen dir das Geld, bewegen darf es nur er. Ein Bot räumt das TRX ab (Quelle: Kaspersky-Blog).

Wer fremdes Geld abheben will, zahlt.

Was hättest du nach der ersten weggebuchten Gebühr gemacht?"""),

 dict(thema='Selbstgebaute Token mit Stablecoin-Namen (USDTS, USDCF)', feld='Betrug', var='These', frei_ab='2026-10-22', verwendet=None,
      text="""Der Name eines Coins ist Werbung, kein Wert.

Ein Teilnehmer hatte „USDT“ in der Wallet und fand keine Börse, die ihn nahm. Beim Hinsehen hießen die Coins USDTS und USDCF. Selbstgebaut, Verkaufswert 0 €.

Jeder kann in Minuten einen Token erstellen und ihn nennen, wie er will. Der Wallet-Bildschirm zeigt den Namen, den der Macher gewählt hat.

Was sich nirgends verkaufen lässt, war nie Geld.

Prüfst du vor dem Kauf, auf welcher Börse du den Coin wieder loswirst?"""),

 dict(thema='Selbstgebaute Token mit Stablecoin-Namen (USDTS, USDCF)', feld='Betrug', var='Story', frei_ab='2026-10-22', verwendet=None,
      text="""Ich wollte beim Verkaufen helfen. Käufer auf der Welt: null.

Die Wallet eines Teilnehmers zeigte „USDT“. Keine Börse nahm die Coins. Sie hießen USDTS und USDCF, zwei selbstgebaute Token mit Stablecoin-Namen. Wert: 0 €.

Mir ging es früher genauso, nur mit einem Memecoin. Die Zahl in der Wallet sah nach Geld aus. Geld wurde sie nie.

Ein Guthaben ist erst Geld, wenn jemand es dir abkauft.

Hast du schon mal etwas gehalten, das sich nirgends verkaufen ließ?"""),

 dict(thema='Gebühr vor der Auszahlung (falscher Trader, Solana-Adresse)', feld='Betrug', var='These', frei_ab='2026-10-23', verwendet=None,
      text="""Eine Gebühr vor der Auszahlung ist die Auszahlung. Für ihn.

Fake-Account eines bekannten Traders, Gebühr für den „Trading-Bot“ an eine Solana-Adresse. Zwei-, dreimal gezahlt, jedes Mal mit neuer Begründung: Netzwerkschwankungen, Internetstörung, der Bot verlangt es. Ausgezahlt wurde nie.

Eine echte Börse zieht Gebühren vom Guthaben ab. Vorkasse auf das eigene Geld verlangt nur einer.

Wer vor dem Auszahlen kassiert, zahlt danach nie aus.

Welche der drei Begründungen hättest du geglaubt?"""),

 dict(thema='Gebühr vor der Auszahlung (falscher Trader, Solana-Adresse)', feld='Betrug', var='Story', frei_ab='2026-10-23', verwendet=None,
      text="""Ich nannte ihn Betrüger. Antwort: „Dann trade ich nie wieder für dich.“

Davor hatte ich die Gebühr für seinen „Trading-Bot“ zwei-, dreimal an eine Solana-Adresse gezahlt. Netzwerkschwankungen. Internetstörung. Der Bot verlangt es. Die Auszahlung kam nie.

Der Satz war der erste wahre im ganzen Chat. Er hat nie getradet. Er hat kassiert.

Wer dich nach einer Gebühr bedroht, hatte nie vor zu zahlen.

Bei welcher Begründung hättest du aufgehört zu überweisen?"""),

 dict(thema='„Erfunden“ und „selbst schuld“ unter dem ersten Beitrag', feld='Psychologie', var='Fall', frei_ab='2026-10-23', verwendet=None,
      text="""Mein erster Beitrag hier: 1.657 Aufrufe, 21 Antworten, 2 Likes.

Die häufigsten Antworten: erfunden. Und: selbst schuld. Thema war die gefälschte Wallet-App, die mich 70.000 $ gekostet hat.

Erfunden wäre billiger gewesen. Selbst schuld stimmt, jede Entscheidung war mein Finger.

Die 21 Antworten haben mehr Leute erreicht als die 2 Likes. Spott verteilt Warnungen weiter als Zustimmung.

Was hat dich dein teuerstes „selbst schuld“ gekostet?"""),

 dict(thema='„Erfunden“ und „selbst schuld“ unter dem ersten Beitrag', feld='Psychologie', var='Story', frei_ab='2026-10-23', verwendet=None,
      text="""Drei Entscheidungen, drei Mal mein Finger, zusammen weit über 70.000 $.

App geladen, weil sie echt aussah. Gebühr gezahlt, weil die Auszahlung angeblich wartete. Coin gekauft, weil ein bekanntes Gesicht dahinterstand.

Keiner hat mich gezwungen. Das war das Teure daran: Jede Tür hab ich selbst aufgemacht.

Heute prüfe ich vor jedem Finger auf dem Bildschirm, wer auf der anderen Seite verdient.

Welche deiner Entscheidungen würdest du mit heutigem Wissen zurückholen?"""),

 dict(thema='Influencer-Coins, Rug Pull (einer 5.000 $)', feld='Einstieg', var='These', frei_ab='2026-10-24', verwendet=None,
      text="""100.000 Follower halten keinen Kurs.

Meine Influencer-Coins endeten alle im Rug Pull. Die Macher verkauften ihre Coins auf einmal, der Kurs fiel senkrecht, die Käufer hielten den Rest. Einer davon hat mich 5.000 $ gekostet.

Reichweite sagt, wie viele zuschauen. Über den Coin sagt sie null.

Wer den Coin gemacht hat und wie viel er selbst hält, zählt mehr als jede Followerzahl.

Würdest du 5.000 € in einen Coin stecken, nur weil jemand mit 100.000 Followern ihn empfiehlt?"""),

 dict(thema='Influencer-Coins, Rug Pull (einer 5.000 $)', feld='Einstieg', var='Fall', frei_ab='2026-10-24', verwendet=None,
      text="""5.000 $ rein, Kurs senkrecht runter, Käufer halten den Rest.

So läuft ein Rug Pull: Ein bekanntes Gesicht bringt einen Coin raus. Die Macher halten den Großteil. Fans kaufen, der Kurs steigt. Dann verkaufen die Macher alles auf einmal. Der Kurs fällt senkrecht, die Fans sitzen auf Coins ohne Käufer.

Bei mir ging das zwei-, dreimal so. Einer kostete 5.000 $.

Ein Coin, dessen Macher den Großteil hält, gehört ihm. Nie dir.

Hast du schon mal gekauft, weil ein bekannter Name dahinterstand?"""),

 dict(thema='Seed-Phrase am Telefon („synchronisieren“)', feld='Sicherheit', var='These', frei_ab='2026-10-25', verwendet=None,
      text="""Kein Support der Welt braucht deine 12 Wörter. Keiner.

Mich hat mal einer angerufen, aus der Community eines Mining-Anbieters. Meine Wallet müsse „synchronisiert“ werden. Ich hab ihm zwölf erfundene Wörter vorgelesen. Er ist ausgerastet.

Die 12 Wörter sind kein Passwort. Sie sind die Wallet. Wer sie hat, räumt ab, ohne Handy, ohne PIN, ohne dich.

Synchronisieren, verifizieren, aktualisieren: drei Wörter, eine Bitte, dein Geld.

Welches Wort hat dir ein „Support“ zuletzt angeboten?"""),

 dict(thema='Seed-Phrase am Telefon („synchronisieren“)', feld='Sicherheit', var='Fall', frei_ab='2026-10-25', verwendet=None,
      text="""Vier Leute aus meiner Community, ein „AML-Supporter“, vier leere Wallets.

Elena, Markus, Leon und Sabine, Namen geändert. Alle vier bekamen dieselbe Nachricht: Wegen neuer Geldwäscheregeln müsse die Wallet aktualisiert und verifiziert werden. Dafür brauche er die Seed-Phrase.

Alle vier gaben sie heraus. Danach war das Geld weg.

Geldwäscheregeln gelten für Börsen. Eine Wallet verifiziert niemand per Chat.

Wer deine 12 Wörter will, will dein Geld.

Hättest du bei „Geldwäscheregeln“ gezögert?"""),

 dict(thema='Coin ohne Entwicklerteam (Admin in der Telegram-Gruppe)', feld='Einstieg', var='These', frei_ab='2026-10-25', verwendet=None,
      text="""Ein Entwicklerteam, das sich versteckt, hat einen Grund.

Ich war Admin in der Telegram-Gruppe eines Coin-Projekts und hab nach dem Entwicklerteam gefragt. Antwort: keine. Viele Mitglieder, kein einziges Gesicht hinter dem Coin.

Wer einen Coin baut und dafür Geld einsammelt, kann seinen Namen nennen. Wer das verweigert, plant mit deinem Vertrauen, nie mit seinem Ruf.

Kein Name, kein Kauf.

Würdest du jemandem Geld geben, der dir seinen Namen verschweigt?"""),

 dict(thema='Coin ohne Entwicklerteam (Admin in der Telegram-Gruppe)', feld='Betrug', var='Story', frei_ab='2026-10-25', verwendet=None,
      text="""Admin bei einem Coin, Team unbekannt. Dann gab es mich doppelt.

In der Telegram-Gruppe hatte ich nach dem Entwicklerteam gefragt. Antwort: keine. Später schrieb ein zweiter Account mit meinem Namen Mitglieder privat an. Danach waren Wallets leer, geschätzt 4.000 bis 5.000 €.

Ein Projekt ohne Gesichter ist ein Projekt ohne Verantwortung. Dort gedeiht jeder Fake-Account.

Wer die Macher kennt, weiß, wen er fragt.

Schreibt dich in Krypto-Gruppen öfter mal ein „Admin“ privat an?"""),

 dict(thema='Rückhol-Betrug nach dem ersten Verlust (Fall Thomas, Name geändert)', feld='Betrug', var='These', frei_ab='2026-10-26', verwendet=None,
      text="""Nach dem Verlust kommt der Retter. Er ist Betrüger Nummer zwei.

Thomas (Name geändert) verlor nach eigener Aussage rund 40.000 $ beim Online-Trading. Seitdem schreiben ihm eine Londoner Kanzlei, ein „BaFin Team“ und ein „Blockchain Support“.

Die echte BaFin holt kein verlorenes Geld zurück und beauftragt damit keine Dritten (Quelle: BaFin, 04.05.2026).

Ungefragte Hilfe nach einem Verlust ist die nächste Rechnung.

Würdest du einer Kanzlei antworten, die dich von sich aus anschreibt?"""),

 dict(thema='Rückhol-Betrug nach dem ersten Verlust (Fall Thomas, Name geändert)', feld='Betrug', var='Story', frei_ab='2026-10-26', verwendet=None,
      text="""Vier Absender, ein Postfach, unter jeder Mail ein Wort: echt?

So leitet mir Thomas (Name geändert) seine Post weiter. Er verlor nach eigener Aussage rund 40.000 $ beim Online-Trading. Seitdem melden sich „Helfer“. Einer will Ausweis und Stromrechnung sehen.

Die Antwort steht bei der BaFin selbst. Sie holt kein verlorenes Geld zurück (Quelle: BaFin, 04.05.2026).

Nach einem Verlust greift man nach jeder Hand. Dort wartet die zweite Rechnung.

Wem hättest du nach 40.000 $ Verlust geglaubt?"""),

 dict(thema='Memecoin-Verlust (Chat gegen Konto, kleine Coins)', feld='Psychologie', var='These', frei_ab='2026-10-26', verwendet=None,
      text="""Ein Chat hat mit deinem Coin nie Geld verloren. Du schon.

In Krypto-Gruppen heißt es, Bitcoin sei langweilig und das große Geld liege in kleinen Coins. Mein Memecoin hat mich Geld gekostet. Die Gruppe schreibt am Tag danach über den nächsten.

Das Minus steht am Ende nur auf einem Konto. Deinem.

Wer einen Coin laut empfiehlt, trägt dein Minus nie mit.

Zählt für dich, was eine Gruppe schreibt, oder was du selbst prüfen kannst?"""),

 dict(thema='Memecoin-Verlust (Chat gegen Konto, kleine Coins)', feld='Einstieg', var='Fall', frei_ab='2026-10-26', verwendet=None,
      text="""Ein Memecoin im Depot. Erklären konnte ich ihn keinem. Ergebnis: Minus.

Was der Coin kann und wer ihn gemacht hat, wusste ich kaum. In der Wallet stand trotzdem eine schöne Zahl.

Am Ende stand da ein Verlust. Die schöne Zahl war nie Geld, sie sah nur so aus.

Was du keinem erklären kannst, gehört dir nur auf dem Papier.

Könntest du deinen letzten Kauf in zwei Sätzen erklären?"""),

 dict(thema='Bestätigungssuche (Fremde entscheiden über mein Geld)', feld='Psychologie', var='These', frei_ab='2026-10-27', verwendet=None,
      text="""Wer fragt, was er kaufen soll, sucht einen Schuldigen für später.

Ich hab das lange gemacht. Vor einem Kauf brauchte ich einen, der nickt. Genickt haben vor allem Leute, die mein Geld haben wollten. Gezahlt hab ich jedes Minus allein.

Ruhig wurde es, als ich selbst verstand, was ich kaufe. Heute sind es vier Schritte.

Eine Entscheidung, die du abgibst, bezahlst du trotzdem selbst.

Hast du schon mal gekauft, nur weil ein anderer es für richtig hielt?"""),

 dict(thema='Bestätigungssuche (Fremde entscheiden über mein Geld)', feld='Betrug', var='Fall', frei_ab='2026-10-27', verwendet=None,
      text="""„Laura“ handelte für Peter. Schaden laut Anzeige: rund 62.000 €.

Peter, Name geändert, kam über eine Werbung auf Instagram dorthin. „Laura“ hatte angeblich zehn Jahre Erfahrung. Sie rief mehrmals täglich an und handelte für ihn. Sein Handelskonto zeigte 83.000 €. Ausgezahlt wurden 5 €.

Handeln lassen klingt bequem. Die 62.000 € stehen heute in seiner Anzeige.

Wer für dich handelt, handelt zuerst für sich.

Würdest du jemanden für dich handeln lassen, den du nur vom Telefon kennst?"""),

 dict(thema='Mythos: Auf dem Konto ist mein Geld sicher (Kaufkraft seit 2020)', feld='Geldentwertung', var='Fall', frei_ab='2026-10-27', verwendet=None,
      text="""100 € Einkauf von 2020 kosten 2025 rund 122 €.

Das ist der Durchschnitt aller Verbraucherpreise in Deutschland. Nahrungsmittel und alkoholfreie Getränke: plus 36,2 %. Quelle: Statistisches Bundesamt, Verbraucherpreisindex.

Wer 2020 seine 100 € aufs Konto legte, hat heute weiter 100 €. Der Einkaufswagen dafür ist leichter geworden.

Dein Geld schrumpft leise, der Kontostand bleibt höflich.

Bei welchem Preis ist dir die Inflation zum ersten Mal aufgefallen?"""),

 dict(thema='Mythos: Auf dem Konto ist mein Geld sicher (Kaufkraft seit 2020)', feld='Geldentwertung', var='Story', frei_ab='2026-10-27', verwendet=None,
      text="""Ich lebe in Venezuela. Preise stehen hier in Dollar.

Die Landeswährung rechnet kaum einer um. Jeder Einkauf zeigt mir, was Inflation mit Erspartem macht. Krypto ist hier Alltag. Ich bezahle damit digital über das Internet.

In Deutschland läuft dasselbe langsamer. Von 2020 bis 2025 stiegen die Preise um 21,9 % (Quelle: Statistisches Bundesamt).

Inflation fragt nie, in welchem Land dein Konto liegt.

Wie viel teurer ist dein Wocheneinkauf seit 2020 geworden?"""),

]
