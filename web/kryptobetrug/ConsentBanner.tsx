import { useEffect, useRef } from 'react';

// Zustimmungs-Banner der Verkaufsseite. Beide Knöpfe sind gleich groß und gleich gestaltet.

type ConsentBannerProps = {
  open: boolean;
  focusOnOpen: boolean;
  onAccept: () => void;
  onReject: () => void;
};

export default function ConsentBanner({ open, focusOnOpen, onAccept, onReject }: ConsentBannerProps) {
  const titleRef = useRef<HTMLParagraphElement>(null);

  useEffect(() => {
    if (open && focusOnOpen) titleRef.current?.focus();
  }, [open, focusOnOpen]);

  if (!open) return null;

  return (
    <>
      <div className="eof-consent-spacer" aria-hidden="true" />
      <div className="eof-consent" role="dialog" aria-modal="false" aria-labelledby="eof-consent-title">
        <div className="eof-consent-inner">
          <div className="eof-consent-copy">
            <p id="eof-consent-title" className="eof-consent-title" tabIndex={-1} ref={titleRef}>
              Darf ich messen, wie diese Seite ankommt?
            </p>
            <p className="eof-consent-text">
              Mit deiner Zustimmung nutze ich den Meta-Pixel (Werbung auf Facebook und Instagram) und Microsoft Clarity
              (Klicks und Scrollen auf dieser Seite). Beide setzen Cookies, Daten können dabei in die USA gehen. Widerruf
              jederzeit unten über „Cookie-Einstellungen“. Details in der <a href="/datenschutz">Datenschutzerklärung</a>.
            </p>
          </div>
          <div className="eof-consent-actions">
            <button type="button" className="eof-consent-button" onClick={onReject}>
              Ablehnen
            </button>
            <button type="button" className="eof-consent-button" onClick={onAccept}>
              Zustimmen
            </button>
          </div>
        </div>
      </div>
    </>
  );
}
