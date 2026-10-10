import { useCallback, useEffect, useState } from 'react';
import type { MouseEvent } from 'react';
import ConsentBanner from './ConsentBanner';
import { readConsent, revokeTracking, saveConsent, startTracking, trackInitiateCheckout, trackingIsRunning } from './tracking';
import './kryptobetrug.css';

// Verkaufsseite „Echt oder Fake? Der 5-Minuten-Check“ unter chrisalcatrez.de/kryptobetrug.
// Alle Klassen beginnen mit „eof-“ und hängen unter .eof, damit sie keine andere Seite berühren.

const CHECKOUT_URL = 'https://www.checkout-ds24.com/product/741539?ds24tr=a-ads';
const PAGE_TITLE = 'Echt oder Fake? Der 5-Minuten-Check';
const PAGE_DESCRIPTION =
  'Erkenne Betrugs-Mails, SMS und Chat-Nachrichten in 5 Minuten. Ohne Technikwissen. E-Book für Krypto-Anfänger.';

const CONTENTS = [
  'Den 5-Minuten-Check: fünf feste Schritte für jede Mail, SMS und Chat-Nachricht',
  'Sechs Maschen und vier echte Betrugs-Mails, Stelle für Stelle entlarvt',
  'Vier wahre Geschichten, eine davon meine eigene',
  'Den Notfall-Plan, falls du schon geklickt hast',
  'Spickzettel und Lesezeichen-Liste zum Ausdrucken',
];

const PAIN_POINTS = [
  'Eine Mail verspricht dir eine Auszahlung. Du sollst nur kurz deinen Ausweis hochladen. Du denkst: »So viel Geld lässt man ungern liegen.« Und gleichzeitig: »Was, wenn das Betrüger sind?«',
  'Seit du deine ersten Euro in Krypto gesteckt hast, zuckst du bei jeder Nachricht zusammen. Manche Mails lässt du tagelang ungeöffnet. Aus Angst, mit einem einzigen Klick alles zu verlieren.',
  'Ein freundlicher »Support-Mitarbeiter« schreibt dir auf WhatsApp oder Telegram. Er will dir helfen. Er braucht dafür nur dein Passwort. Oder deine 12 Wörter. Dein Bauchgefühl sagt: Da ist was faul. Woran du es festmachen sollst, weißt du kaum.',
  'Du hast schon gegoogelt und Videos geschaut. Überall heißt es: »Achte auf schlechtes Deutsch.« Dann landet eine Mail in makellosem Deutsch bei dir. Mit Logo. Mit Aktenzeichen. Und du bist so schlau wie vorher.',
  'Du fragst jedes Mal jemanden aus der Familie oder einen Bekannten. Langsam ist dir das unangenehm. Und heimlich denkst du: »Bin ich für Krypto einfach zu wenig Technik-Mensch?«',
];

const BENEFITS = [
  'Du prüfst jede verdächtige Mail, SMS und Chat-Nachricht in fünf Minuten. Selbst. Ohne jemanden zu fragen.',
  'Du erkennst Betrüger auch dann, wenn alles täuschend echt aussieht. Mit Logo, Aktenzeichen und makellosem Deutsch.',
  'Du bleibst ruhig, wenn eine Nachricht Druck macht. »24 Stunden«, »letzte Mahnung«, »Konto gesperrt« lassen dich kalt.',
  'Du kennst deine rote Linie. Du weißt, was niemand per Nachricht von dir verlangen darf. Dein Ausweis, dein Passwort und deine 12 Wörter bleiben bei dir.',
  'Du weißt sofort, was zu tun ist, falls der Klick schon passiert ist.',
  'Du schützt auch deine Familie. Du erkennst die Masche, wenn sie bei deinen Eltern oder deinem Partner landet.',
  'Du öffnest dein Postfach wieder ohne Herzklopfen. Und dein Erspartes bleibt, wo es hingehört: bei dir.',
];

// Dieselben zwei Stimmen, die auf der Startseite von chrisalcatrez.de stehen.
const VOICES = [
  {
    name: 'Sabine Merschkötter',
    role: 'Anfängerin, inzwischen mit eigenem Portfolio',
    image: '/testimonials/sabine-merschkoetter-poster.jpg',
    quote:
      'Krypto war für mich absolutes Neuland — ich kannte mich überhaupt nicht aus. Chris erklärt es so, dass ich es verstanden habe. Inzwischen habe ich mein eigenes kleines Portfolio.',
  },
  {
    name: 'Sebastian Paul',
    role: 'Edelmetall-Investor',
    image: '/testimonials/sebastian-paul.webp',
    quote:
      'Es ist nachvollziehbar aufbereitet – auch für jeden, der sich vielleicht in der Finanzwelt nicht so gut auskennt. Ganz Step by Step, an praktischen Beispielen, wird erklärt, wie der Kryptomarkt funktioniert, was eine Blockchain ist – und so weiter.',
  },
];

// Leseprobe: Seite 11 aus dem E-Book, Original-Mail mit Markierungen (Name des Teilnehmers entfernt).
const SAMPLE_NOTES = [
  {
    number: 2,
    title: 'Der Absender',
    text: 'Eine kostenlose Outlook-Adresse. Die echte FCA schreibt dazu: Sie nutzt nie Gratis-Mail-Dienste, um Verbraucher anzuschreiben.',
  },
  {
    number: 5,
    title: 'Die rote Linie',
    text: 'Ausweisfoto und Adressnachweis per Mail an eine Fremde. Damit können Kriminelle versuchen, in deinem Namen Konten zu eröffnen.',
  },
  {
    number: 7,
    title: 'Geliehenes Vertrauen',
    text: 'Der Link führt ins echte Register der FCA. Ein echter Link macht eine Mail kein Stück echter.',
  },
];

const CLOSING_POINTS = [
  'Fünf feste Schritte für jede verdächtige Nachricht',
  'Sechs Maschen, vier echte Betrugs-Mails entlarvt',
  'Notfall-Plan, falls du schon geklickt hast',
  'PDF, 35 Seiten, sofort als Download',
];

function PriceNote() {
  return (
    <p className="eof-price-note">
      <strong>Einmalig 37 €.</strong> PDF, sofort als Download. 14 Tage Geld-zurück-Garantie.
    </p>
  );
}

// Mit Zustimmung meldet der Klick „InitiateCheckout“ an Meta; die Kasse öffnet sich 250 ms später.
function handlePurchaseClick(event: MouseEvent<HTMLAnchorElement>) {
  if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
    return;
  }
  if (!trackInitiateCheckout()) return;
  event.preventDefault();
  const target = event.currentTarget.href;
  window.setTimeout(() => window.location.assign(target), 250);
}

function PurchaseLink({ children = 'Jetzt den 5-Minuten-Check holen' }: { children?: string }) {
  return (
    <a className="eof-cta" href={CHECKOUT_URL} onClick={handlePurchaseClick}>
      {children}
    </a>
  );
}

function usePageMeta() {
  useEffect(() => {
    const previousTitle = document.title;
    document.title = PAGE_TITLE;
    const description = document.querySelector('meta[name="description"]');
    const previousDescription = description?.getAttribute('content') ?? null;
    description?.setAttribute('content', PAGE_DESCRIPTION);
    return () => {
      document.title = previousTitle;
      if (description && previousDescription !== null) {
        description.setAttribute('content', previousDescription);
      }
    };
  }, []);
}

// Meta-Pixel und Microsoft Clarity laden erst nach Zustimmung im Banner und nur auf dieser Seite.
function useConsent() {
  const [bannerOpen, setBannerOpen] = useState(false);
  const [focusBanner, setFocusBanner] = useState(false);

  useEffect(() => {
    const choice = readConsent();
    if (choice === 'granted') startTracking();
    if (choice === null) setBannerOpen(true);
  }, []);

  const accept = useCallback(() => {
    saveConsent('granted');
    setBannerOpen(false);
    startTracking();
  }, []);

  const reject = useCallback(() => {
    saveConsent('denied');
    setBannerOpen(false);
    if (trackingIsRunning()) {
      revokeTracking();
      window.location.reload();
    }
  }, []);

  const openSettings = useCallback(() => {
    setFocusBanner(true);
    setBannerOpen(true);
  }, []);

  return { bannerOpen, focusBanner, accept, reject, openSettings };
}

export default function KryptobetrugPage() {
  usePageMeta();
  const consent = useConsent();

  return (
    <div className="eof">
      <main>
        <section className="eof-hero">
          <div className="eof-hero-inner">
            <p className="eof-eyebrow">Der 5-Minuten-Check für Krypto-Anfänger</p>
            <h1>
              Erkenne Betrugs-Mails, SMS und Chat-Nachrichten in <span className="eof-highlight">5 Minuten</span>.
            </h1>
            <p className="eof-hero-sub">Ohne Technikwissen und ohne jemanden zu fragen.</p>

            <div className="eof-hero-product">
              <div className="eof-hero-offer">
                <p className="eof-offer-copy">
                  Fünf feste Schritte, vier echte Betrugs-Mails Stelle für Stelle entlarvt und ein Notfall-Plan, falls
                  du schon geklickt hast. PDF, 35 Seiten, in 30 Minuten gelesen.
                </p>
                <PurchaseLink />
                <PriceNote />
              </div>

              <div className="eof-hero-book">
                <img
                  className="eof-book-image"
                  src="/eof/buch.jpg"
                  alt="E-Book „Echt oder Fake? Der 5-Minuten-Check“ von Chris Alcatrez"
                  width={1024}
                  height={1280}
                  decoding="async"
                />
              </div>

              <div className="eof-hero-scene">
                <p>Dein Handy brummt.</p>
                <p className="eof-message">»Ihr Konto wird in 24 Stunden gesperrt.«</p>
                <p>Dein Puls geht hoch. Dein Daumen schwebt über dem Link.</p>
                <p className="eof-question">Echt oder Fake?</p>
                <p className="eof-answer">
                  Nach diesem E-Book beantwortest du diese Frage selbst. Bei jeder Nachricht. In fünf Minuten.
                </p>
              </div>
            </div>
          </div>
        </section>

        <section className="eof-get" aria-labelledby="eof-get-title">
          <div className="eof-get-inner">
            <div>
              <h2 id="eof-get-title">Das bekommst du</h2>
              <ul className="eof-get-list">
                {CONTENTS.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
              <p className="eof-facts">PDF · 35 Seiten · in 30 Minuten gelesen · sofort als Download</p>
            </div>
            <aside className="eof-guarantee">
              <strong>14 Tage Geld-zurück-Garantie</strong>
              <p>Bist du unzufrieden, bekommst du innerhalb von 14 Tagen dein Geld zurück. Die Abwicklung läuft über Digistore24.</p>
            </aside>
          </div>
        </section>

        <section className="eof-section eof-section-dark">
          <div className="eof-section-inner">
            <h2>Kennst du das?</h2>
            <ol className="eof-pain-list">
              {PAIN_POINTS.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ol>
          </div>
        </section>

        <section className="eof-sample" aria-labelledby="eof-sample-title">
          <div className="eof-sample-inner">
            <p className="eof-kicker">Leseprobe · Seite 11 von 35</p>
            <h2 id="eof-sample-title">Eine echte Mail unter der Lupe</h2>
            <p className="eof-sample-intro">
              Diese Mail bekam einer meiner Kursteilnehmer. Im E-Book ist jede verräterische Stelle markiert und erklärt.
            </p>
            <div className="eof-sample-grid">
              <figure className="eof-sample-figure">
                <a className="eof-sample-image-link" href="/eof/leseprobe-mail.webp" target="_blank" rel="noopener">
                  <img
                    className="eof-sample-image"
                    src="/eof/leseprobe-mail.webp"
                    alt="Original-Mail einer angeblichen Mitarbeiterin der Finanzaufsicht, die Ausweisfotos verlangt, mit sieben markierten Stellen"
                    width={871}
                    height={1485}
                    loading="lazy"
                    decoding="async"
                  />
                </a>
                <figcaption>
                  <a href="/eof/leseprobe-mail.webp" target="_blank" rel="noopener">
                    Mail in voller Größe öffnen
                  </a>
                </figcaption>
              </figure>
              <div className="eof-sample-notes">
                <ol>
                  {SAMPLE_NOTES.map((note) => (
                    <li key={note.number}>
                      <span className="eof-sample-number" aria-hidden="true">
                        {note.number}
                      </span>
                      <span>
                        <strong>{note.title}</strong>
                        {note.text}
                      </span>
                    </li>
                  ))}
                </ol>
                <p className="eof-sample-verdict">
                  <span>Fake</span> Eine Behörde, die von einer Gratis-Adresse schreibt.
                </p>
                <p className="eof-sample-more">
                  Was die Stellen 1, 3, 4 und 6 verraten, drei weitere echte Mails und den 5-Minuten-Check selbst findest
                  du im E-Book.
                </p>
              </div>
            </div>
          </div>
        </section>

        <section className="eof-section eof-section-white">
          <div className="eof-section-inner">
            <h2>Ich weiß, wie sich das anfühlt.</h2>
            <div className="eof-story">
              <p>Du willst dein hart erarbeitetes Geld in Sicherheit bringen. Deshalb hast du mit Krypto angefangen.</p>
              <p>Und genau dort warten Leute, die es dir wegnehmen wollen.</p>
              <p className="eof-emphasis">
                Mir ging es genauso. Krypto klang für mich lange nach Betrug und nach viel zu kompliziert. Und auch mich
                hat es erwischt. Ich bin selbst auf einen Köder hereingefallen.
              </p>
              <p>Heute leiten mir meine Kursteilnehmer ihre Mails weiter. Darüber steht fast immer dieselbe Frage: »Ist das echt?«</p>
              <p>Dabei habe ich zwei Dinge herausgefunden.</p>
              <div className="eof-numbered">
                <b>1</b>
                <p>
                  Erstens: Du hast es mit Betrugsbanden zu tun. Sie arbeiten mit Vorlagen, Callcentern und künstlicher
                  Intelligenz. Deine Unsicherheit ist ihr Geschäft. An dir liegt es also kaum.
                </p>
              </div>
              <div className="eof-numbered">
                <b>2</b>
                <p>
                  Zweitens: Betrüger wechseln ständig ihr Kostüm. Mal sind sie deine Börse. Mal eine Behörde. Mal ein
                  Anwalt. Ihr Bauplan bleibt immer derselbe.
                </p>
              </div>
              <p>
                <strong>Wer den Bauplan kennt, erkennt ihn in jeder Nachricht wieder.</strong>
              </p>
            </div>
          </div>
        </section>

        <section className="eof-section eof-vision">
          <div className="eof-section-inner">
            <h2>Stell dir vor, die nächste Mail kommt. Und du bleibst ruhig.</h2>
            <div className="eof-vision-intro">
              <p>»Dringend. Ihr Konto wird gesperrt.«</p>
              <p>Früher wäre dein Puls hochgegangen.</p>
              <p>Jetzt gehst du fünf Schritte durch. Nach fünf Minuten weißt du: Fake.</p>
              <p>Du löschst die Mail. Und dein Abend gehört wieder dir.</p>
            </div>
            <div className="eof-comparison">
              <article>
                <h3>Heute</h3>
                <ul>
                  <li>Herzklopfen bei jeder Mail von der Börse.</li>
                  <li>Du fragst andere: »Ist das echt?«</li>
                  <li>Du klickst auf gut Glück. Oder du lässt alles liegen.</li>
                </ul>
              </article>
              <article>
                <h3>Nach 30 Minuten</h3>
                <ul>
                  <li>Du prüfst jede Nachricht selbst.</li>
                  <li>Du bleibst ruhig, wenn jemand Druck macht.</li>
                  <li>Dein Erspartes bleibt bei dir.</li>
                </ul>
              </article>
            </div>
          </div>
        </section>

        <section className="eof-section eof-section-white">
          <div className="eof-section-inner">
            <h2>Genau dafür habe ich »Echt oder Fake? Der 5-Minuten-Check« geschrieben.</h2>
            <div className="eof-solution">
              <p>Nach 30 Minuten Lesezeit prüfst du jede verdächtige E-Mail, SMS und Chat-Nachricht selbst.</p>
              <p>Du bekommst fünf feste Schritte. Immer in derselben Reihenfolge. Du gehst sie durch und weißt, woran du bist.</p>
              <p>
                Du siehst den Trick an echten Betrugs-Mails aus dem Postfach eines meiner Kursteilnehmer. So erkennst du
                ihn sofort wieder, wenn er bei dir landet.
              </p>
              <p>Alles in einfachen Worten. Ganz ohne Technikwissen.</p>
            </div>
          </div>
        </section>

        <section className="eof-section eof-section-soft">
          <div className="eof-section-inner">
            <h2>Das hast du davon</h2>
            <ul className="eof-benefit-list">
              {BENEFITS.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </div>
        </section>

        <section className="eof-section eof-section-white" aria-labelledby="eof-voices-title">
          <div className="eof-section-inner">
            <p className="eof-kicker">Stimmen aus meinem Krypto-Kurs</p>
            <h2 id="eof-voices-title">Beide haben bei null angefangen.</h2>
            <div className="eof-voices">
              {VOICES.map((voice) => (
                <figure className="eof-voice" key={voice.name}>
                  <blockquote>„{voice.quote}“</blockquote>
                  <figcaption>
                    <img src={voice.image} alt={voice.name} width={56} height={56} loading="lazy" decoding="async" />
                    <span>
                      <span className="eof-voice-name">{voice.name}</span>
                      <span className="eof-voice-role">{voice.role}</span>
                    </span>
                  </figcaption>
                </figure>
              ))}
            </div>
          </div>
        </section>

        <section className="eof-mid-cta">
          <div className="eof-mid-cta-inner">
            <p className="eof-mid-question">Willst du die nächste Betrugs-Mail in fünf Minuten selbst entlarven?</p>
            <p className="eof-mid-lead">Dann hol dir jetzt den 5-Minuten-Check.</p>
            <PurchaseLink />
            <PriceNote />
          </div>
        </section>

        <section className="eof-section eof-section-white">
          <div className="eof-section-inner eof-about">
            <img
              className="eof-author-image"
              src="/eof/chris.png"
              alt="Chris Alcatrez"
              width={880}
              height={1184}
              loading="lazy"
              decoding="async"
            />
            <div className="eof-about-copy">
              <h2>Ich bin Chris.</h2>
              <p>Ich begleite Krypto-Anfänger bei ihren ersten Schritten.</p>
              <p>Ich bin kein IT-Fachmann und kein Ermittler. Auch mich haben Betrüger schon erwischt.</p>
              <p>Heute prüfe ich erst. Immer mit denselben fünf Schritten.</p>
              <p>Wenn ich das kann, kannst du das auch.</p>
            </div>
          </div>
        </section>

        <section className="eof-closing">
          <div className="eof-closing-inner">
            <h2>Die nächste Betrugs-Mail kommt bestimmt. Diesmal bist du vorbereitet.</h2>
            <ul className="eof-closing-list">
              {CLOSING_POINTS.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
            <PurchaseLink />
            <PriceNote />
          </div>
        </section>
      </main>

      <footer className="eof-footer">
        <span>Chris Alcatrez. Alle Rechte vorbehalten.</span>
        <nav className="eof-footer-links" aria-label="Rechtliches">
          <a href="/impressum">Impressum</a>
          <a href="/datenschutz">Datenschutz</a>
          <button type="button" className="eof-footer-button" onClick={consent.openSettings}>
            Cookie-Einstellungen
          </button>
        </nav>
      </footer>

      <ConsentBanner
        open={consent.bannerOpen}
        focusOnOpen={consent.focusBanner}
        onAccept={consent.accept}
        onReject={consent.reject}
      />
    </div>
  );
}
