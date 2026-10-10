// Einwilligung, Meta-Pixel und Microsoft Clarity für die Verkaufsseite /kryptobetrug.
// Beide Dienste laden erst nach Zustimmung. Ohne Zustimmung verlässt kein Tracking-Aufruf die Seite.

export const META_PIXEL_ID = '1927196884927557';
export const CLARITY_ID = 'ythsao0s8j';
export const CONSENT_STORAGE_KEY = 'ca-consent-v1';

// Nach einem Jahr fragt das Banner erneut.
const CONSENT_MAX_AGE_MS = 365 * 24 * 60 * 60 * 1000;

export type ConsentChoice = 'granted' | 'denied';

const PRODUCT_DATA = {
  content_ids: ['741539'],
  content_name: 'Echt oder Fake? Der 5-Minuten-Check',
  content_type: 'product',
  value: 37,
  currency: 'EUR',
};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
type AnyWindow = Window & Record<string, any>;

function getWindow(): AnyWindow {
  return window as AnyWindow;
}

export function readConsent(): ConsentChoice | null {
  try {
    const raw = window.localStorage.getItem(CONSENT_STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as { choice?: unknown; at?: unknown };
    if (parsed.choice !== 'granted' && parsed.choice !== 'denied') return null;
    const savedAt = typeof parsed.at === 'string' ? Date.parse(parsed.at) : Number.NaN;
    if (Number.isNaN(savedAt) || Date.now() - savedAt > CONSENT_MAX_AGE_MS) return null;
    return parsed.choice;
  } catch {
    return null;
  }
}

export function saveConsent(choice: ConsentChoice): void {
  try {
    window.localStorage.setItem(
      CONSENT_STORAGE_KEY,
      JSON.stringify({ choice, at: new Date().toISOString(), version: 1 }),
    );
  } catch {
    // Ohne Browser-Speicher gilt die Auswahl für diesen Besuch; beim nächsten Besuch fragt das Banner erneut.
  }
}

let pixelStarted = false;
let clarityStarted = false;

function startMetaPixel(): void {
  if (pixelStarted) return;
  pixelStarted = true;
  const w = getWindow();
  if (typeof w.fbq !== 'function') {
    // Gleiche Warteschlange wie im offiziellen Meta-Code: Aufrufe sammeln sich, bis fbevents.js geladen ist.
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const queueFn: any = function (this: unknown) {
      // eslint-disable-next-line prefer-rest-params
      const args = arguments;
      if (queueFn.callMethod) {
        queueFn.callMethod.apply(queueFn, args);
      } else {
        queueFn.queue.push(args);
      }
    };
    w.fbq = queueFn;
    if (!w._fbq) w._fbq = queueFn;
    queueFn.push = queueFn;
    queueFn.loaded = true;
    queueFn.version = '2.0';
    queueFn.queue = [];
    const script = document.createElement('script');
    script.id = 'eof-meta-pixel';
    script.async = true;
    script.src = 'https://connect.facebook.net/en_US/fbevents.js';
    document.head.appendChild(script);
  }
  w.fbq('init', META_PIXEL_ID);
  w.fbq('track', 'PageView');
  w.fbq('track', 'ViewContent', PRODUCT_DATA);
}

function startClarity(): void {
  if (clarityStarted) return;
  clarityStarted = true;
  const w = getWindow();
  if (typeof w.clarity !== 'function') {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const queueFn: any = function (this: unknown) {
      // eslint-disable-next-line prefer-rest-params
      (queueFn.q = queueFn.q || []).push(arguments);
    };
    w.clarity = queueFn;
  }
  w.clarity('consentv2', { ad_Storage: 'granted', analytics_Storage: 'granted' });
  if (!document.getElementById('eof-clarity')) {
    const script = document.createElement('script');
    script.id = 'eof-clarity';
    script.async = true;
    script.src = `https://www.clarity.ms/tag/${CLARITY_ID}`;
    document.head.appendChild(script);
  }
}

export function startTracking(): void {
  startMetaPixel();
  startClarity();
}

export function trackingIsRunning(): boolean {
  return pixelStarted || clarityStarted;
}

// Meldet „InitiateCheckout“, sobald jemand auf einen Kauf-Button drückt. Gibt true zurück, wenn ein Event rausging.
export function trackInitiateCheckout(): boolean {
  const w = getWindow();
  if (!pixelStarted || typeof w.fbq !== 'function') return false;
  w.fbq('track', 'InitiateCheckout', { ...PRODUCT_DATA, num_items: 1 });
  return true;
}

function deleteCookies(names: string[]): void {
  const host = window.location.hostname;
  const parts = host.split('.');
  const domains = new Set<string>(['', host, `.${host}`]);
  for (let index = 1; index < parts.length - 1; index += 1) {
    domains.add(`.${parts.slice(index).join('.')}`);
  }
  for (const name of names) {
    for (const domain of domains) {
      document.cookie = `${name}=; Max-Age=0; path=/${domain ? `; domain=${domain}` : ''}`;
    }
  }
}

// Widerruf: Dienste stoppen und ihre Cookies auf dieser Domain löschen. Danach lädt die Seite neu, ohne Tracking.
export function revokeTracking(): void {
  const w = getWindow();
  try {
    if (typeof w.fbq === 'function') w.fbq('consent', 'revoke');
  } catch {
    // Pixel war unvollständig geladen; die Cookies werden trotzdem gelöscht.
  }
  try {
    if (typeof w.clarity === 'function') {
      w.clarity('consentv2', { ad_Storage: 'denied', analytics_Storage: 'denied' });
    }
  } catch {
    // Clarity war unvollständig geladen; die Cookies werden trotzdem gelöscht.
  }
  deleteCookies(['_fbp', '_fbc', '_clck', '_clsk']);
}
