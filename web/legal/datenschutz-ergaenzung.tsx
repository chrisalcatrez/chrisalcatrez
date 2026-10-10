// Ergänzung für artifacts/landing/src/pages/datenschutz.tsx (Stand 9. Oktober 2026).
//
// 1) In Abschnitt 7 den Absatz „Falls künftig optionale Analyse- oder Marketingdienste …“ ersetzen durch:
//    <p>
//      Optionale Analyse- und Marketingdienste aktivieren wir erst nach deiner Zustimmung. Welche das sind, steht
//      in Abschnitt 7a.
//    </p>
// 2) Die zwei Abschnitte unten (7a und 7b) unmittelbar nach Abschnitt 7 und vor Abschnitt 8 einfügen.
// 3) „Stand: 11. September 2026“ ersetzen durch „Stand: 9. Oktober 2026“.
// Übernommen werden nur die beiden <LegalSection>-Blöcke, ohne die export-Zeilen.

export const Abschnitt7a = (
  <LegalSection title="7a. Verkaufsseite „Echt oder Fake?“: Einwilligung, Meta-Pixel und Microsoft Clarity">
    <p>
      Auf der Verkaufsseite chrisalcatrez.de/kryptobetrug fragen wir dich beim ersten Besuch, ob du dem Einsatz des
      Meta-Pixels und von Microsoft Clarity zustimmst. Beide Dienste laden erst, wenn du auf „Zustimmen“ klickst.
      Lehnst du ab, bleiben sie aus. Deine Auswahl speichern wir im lokalen Speicher deines Browsers (Eintrag
      „ca-consent-v1“), damit wir dich beim nächsten Besuch kein zweites Mal fragen; nach einem Jahr fragen wir
      erneut. Diese Speicherung ist für die Verwaltung deiner Auswahl erforderlich (§ 25 Abs. 2 Nr. 2 TDDDG). Über
      den Link „Cookie-Einstellungen“ unten auf der Verkaufsseite kannst du deine Auswahl jederzeit ändern und eine
      erteilte Einwilligung mit Wirkung für die Zukunft widerrufen. Bei einem Widerruf löschen wir die Cookies der
      beiden Dienste in deinem Browser.
    </p>
    <p>
      <strong>Meta-Pixel.</strong> Anbieter ist die Meta Platforms Ireland Limited, Merrion Road, Dublin 4, D04 X2K5,
      Irland. Mit dem Pixel messen wir, ob Menschen nach einem Klick auf unsere Werbeanzeigen bei Facebook und
      Instagram die Verkaufsseite aufrufen und auf einen Kauf-Button klicken. Außerdem können wir Anzeigen an Menschen
      ausspielen, die unsere Seite besucht haben. Dabei setzt Meta Cookies (zum Beispiel „_fbp“, Speicherdauer bis zu
      90 Tage) und erhält Daten wie IP-Adresse, Browser- und Geräteinformationen, die aufgerufene Seite und diese
      Ereignisse. Meta kann diese Daten deinem Facebook- oder Instagram-Konto zuordnen und für eigene Zwecke
      verwenden; dafür ist Meta allein verantwortlich. Für die Erhebung auf unserer Seite und die Übermittlung an Meta
      sind wir gemeinsam mit Meta verantwortlich (Art. 26 DSGVO). Die Vereinbarung dazu findest du unter{' '}
      <a className="text-white underline decoration-white/30 underline-offset-4 hover:text-red-400" href="https://www.facebook.com/legal/controller_addendum" target="_blank" rel="noreferrer">
        facebook.com/legal/controller_addendum
      </a>
      , die Datenschutzrichtlinie von Meta unter{' '}
      <a className="text-white underline decoration-white/30 underline-offset-4 hover:text-red-400" href="https://www.facebook.com/privacy/policy/" target="_blank" rel="noreferrer">
        facebook.com/privacy/policy
      </a>
      .
    </p>
    <p>
      <strong>Microsoft Clarity.</strong> Anbieter ist die Microsoft Ireland Operations Limited, One Microsoft Place,
      South County Business Park, Leopardstown, Dublin 18, Irland. Clarity zeigt uns als Heatmaps und
      Sitzungsaufzeichnungen, wie Besucher die Verkaufsseite nutzen, etwa Klicks, Scrollen und Verweildauer. So sehen
      wir, welche Teile der Seite gelesen werden und wo Besucher abspringen. Clarity setzt Cookies („_clck“ mit einer
      Speicherdauer von einem Jahr, „_clsk“ mit einem Tag) und verarbeitet unter anderem IP-Adresse, Geräte- und
      Browserdaten. Weitere Informationen findest du in der{' '}
      <a className="text-white underline decoration-white/30 underline-offset-4 hover:text-red-400" href="https://privacy.microsoft.com/de-de/privacystatement" target="_blank" rel="noreferrer">
        Datenschutzerklärung von Microsoft
      </a>
      .
    </p>
    <p>
      Rechtsgrundlage für beide Dienste ist deine Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO und § 25 Abs. 1
      TDDDG. Meta und Microsoft können Daten in die USA übermitteln. Dabei werden die jeweils verfügbaren gesetzlichen
      Übermittlungsmechanismen und Schutzmaßnahmen eingesetzt.
    </p>
  </LegalSection>
);

export const Abschnitt7b = (
  <LegalSection title="7b. Kauf über Digistore24">
    <p>
      Das E-Book „Echt oder Fake? Der 5-Minuten-Check“ verkauft Digistore24 als Wiederverkäufer (Digistore24 GmbH,
      St.-Godehard-Straße 32, 31139 Hildesheim, Deutschland, je nach Land des Käufers auch die Digistore24 Inc.). Mit
      einem Klick auf einen Kauf-Button wechselst du auf das Bestellformular von Digistore24. Für deine Angaben dort
      gilt die Datenschutzerklärung von Digistore24, die im Bestellformular verlinkt ist. Von Digistore24 erhalten wir
      die Daten, die wir für Auslieferung und Kundenbetreuung brauchen, etwa Name, E-Mail-Adresse und gekauftes
      Produkt. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO.
    </p>
    <p>
      Auf unserer Website ist außerdem ein Skript von Digistore24 eingebunden. Es liest Kennungen aus aufgerufenen
      Links, zum Beispiel zu Partnern, Kampagnen und Werbeklicks, speichert sie in deinem Browser (Cookie „ds24c.v1“,
      je nach Einstellung für die Dauer des Besuchs oder bis zu 7 Tage) und gibt sie an das Bestellformular weiter,
      damit ein Kauf der richtigen Empfehlung zugeordnet wird. Dabei überträgt das Skript auch technische Daten wie
      die zuvor besuchte Seite an Digistore24. Rechtsgrundlage ist unser berechtigtes Interesse an einer korrekten
      Zuordnung und Abrechnung von Verkäufen nach Art. 6 Abs. 1 lit. f DSGVO. Sofern eine Einwilligung abgefragt
      wurde, erfolgt die Verarbeitung auf Grundlage von Art. 6 Abs. 1 lit. a DSGVO und § 25 Abs. 1 TDDDG.
    </p>
    <p>
      Stimmst du auf dem Bestellformular von Digistore24 dem Tracking zu, meldet die Bestellbestätigung deinen Kauf
      über den Meta-Pixel an Meta. So sehen wir, welche Anzeige zu einem Kauf geführt hat. Die Einwilligung dafür
      fragt Digistore24 auf dem Bestellformular ab; Rechtsgrundlage ist Art. 6 Abs. 1 lit. a DSGVO und § 25 Abs. 1
      TDDDG.
    </p>
  </LegalSection>
);
