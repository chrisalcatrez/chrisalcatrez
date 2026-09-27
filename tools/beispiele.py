import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen import *

A = lambda t: '<span class="acc">%s</span>' % t
D = lambda t: (t, 'dim')
TAGS = '#krypto #kryptowährung #kryptowährungen #bitcoindeutschland #bitcoinkaufen #bitcoinfüranfänger #kryptofüranfänger #kryptobetrug #anlagebetrug #onlinebetrug #betrugsmasche #kryptosicherheit #kryptowallet #finanzbildung #geldanlage #vermögensaufbau'

POSTS = {}

# ---------- Beitrag 3: Statement-Karussell ----------
POSTS['beitrag-3'] = dict(
    date='2026-09-28', fmt='Statement-Karussell', topic='Der gefährlichste Moment ist der erste Gewinn (Gebühr vor Auszahlung)',
    slides=[
        s_hook('KRYPTO FÜR EINSTEIGER', 'Der gefährlichste Moment beim Krypto-Einstieg ist dein %s.' % A('erster Gewinn')),
        s_point('WARUM', 'Ein Verlust macht dich vorsichtig. Ein Gewinn macht dich mutig.',
                ['Nach dem ersten Plus fühlst du dich sicher. Du vertraust schneller. Du legst nach.', D('Genau auf diesen Moment warten Betrüger.')]),
        s_point('BEI MIR', 'Bei mir stand ein Gewinn auf dem Bildschirm.',
                ['Ein Kontakt auf Instagram. Ein Guthaben, das gut aussah.', D('Dann wollte ich auszahlen. Vorher sollte ich eine „Netzwerkgebühr“ überweisen.')]),
        s_point('DAS MUSTER', 'Erst zeigen sie dir Gewinne. Dann verlangen sie Geld.',
                ['Auf solchen Plattformen wirken die Gewinne echt. Sie sind komplett gefälscht.', D('Die Auszahlung hängt dann an einer weiteren Zahlung: angebliche Steuern, Gebühren oder Sicherheiten.')],
                src='Quelle: Verbraucherzentrale, „Online-Trading: So entlarven Sie Betrüger“'),
        s_point('HEISST DAS: GEWINNE SIND SCHLECHT?', 'Nein. Ein Gewinn gehört dir, wenn du ihn erklären kannst.',
                ['Du weißt, was du gekauft hast. Du weißt, wo es liegt. Du kannst es jederzeit bewegen.', D('Alles andere ist eine Zahl auf einem fremden Bildschirm.')]),
        s_point('ZUM MERKEN', 'Ein Gewinn zählt erst, wenn er %s ist.' % A('auf deinem Konto'), ['Bis dahin ist er ein Versprechen.'], meta=True),
        s_point('DEINE MEINUNG', 'Siehst du das genauso? Schreib %s in die Kommentare.' % A('Ja oder Nein'), None, meta=True),
    ],
    alts=['Der gefährlichste Moment beim Krypto-Einstieg ist dein erster Gewinn',
          'Ein Verlust macht vorsichtig, ein Gewinn macht mutig',
          'Bei mir stand ein Gewinn auf dem Bildschirm, dann kam die Netzwerkgebühr',
          'Erst zeigen Betrüger Gewinne, dann verlangen sie Geld',
          'Ein Gewinn gehört dir, wenn du ihn erklären kannst',
          'Ein Gewinn zählt erst, wenn er auf deinem Konto ist',
          'Siehst du das genauso? Schreib Ja oder Nein in die Kommentare'],
    caption='''Alle fürchten den Kurssturz. Gefährlicher ist der erste Gewinn.

Ein Verlust macht dich vorsichtig. Ein Gewinn macht dich mutig. Du vertraust schneller. Du legst nach. Genau auf diesen Moment warten Betrüger.

Bei mir stand ein Gewinn auf dem Bildschirm. Ein Kontakt auf Instagram, ein Guthaben, das gut aussah. Dann wollte ich auszahlen. Vorher sollte ich eine „Netzwerkgebühr“ überweisen.

Das Muster hinter vielen Krypto-Betrugsmaschen:
– Erst zeigen sie dir Gewinne.
– Dann verlangen sie Geld: angebliche Steuern, Gebühren oder Sicherheiten.
– Die Gewinne auf solchen Plattformen wirken echt und sind komplett gefälscht (Quelle: Verbraucherzentrale).

Heißt das, Gewinne sind schlecht? Nein. Ein Gewinn gehört dir, wenn du ihn erklären kannst: Du weißt, was du gekauft hast, du weißt, wo es liegt, und du kannst es jederzeit bewegen.

Ein Gewinn zählt erst, wenn er auf deinem Konto ist. Bis dahin ist er ein Versprechen.

Für alle, die gerade mit Krypto oder Bitcoin anfangen und sich vor Betrug schützen wollen.

Siehst du das genauso? Schreib Ja oder Nein in die Kommentare.''')

# ---------- Beitrag 4: Gegenueberstellung ----------
POSTS['beitrag-4'] = dict(
    date='2026-09-29', fmt='Gegenüberstellung', topic='Früher vs. heute: fünf Gewohnheiten beim Krypto-Einstieg',
    slides=[
        s_vs('FRÜHER VS. HEUTE', 'Früher habe ich bezahlt. %s' % A('Heute prüfe ich.'),
             'FRÜHER', ['Gekauft, was ein Influencer empfahl', 'An feste Renditen geglaubt', 'Die Wallet-App aus dem Store geladen', 'In Panik verkauft', 'Fremde um Bestätigung gefragt'],
             'HEUTE', ['Nur, was ich selbst erklären kann', 'Feste Renditen sind mein Warnsignal', 'Wallet nur über die Seite des Herstellers', 'Ein Plan statt Bauchgefühl', 'Eigene Entscheidung, eigene Verantwortung'],
             'Schick das jemandem, der gerade mit Krypto anfängt.'),
    ],
    alts=['Gegenüberstellung früher und heute: früher gekauft, was ein Influencer empfahl, an feste Renditen geglaubt, die Wallet-App aus dem Store geladen, in Panik verkauft, Fremde um Bestätigung gefragt. Heute nur, was ich selbst erklären kann, feste Renditen als Warnsignal, Wallet nur über die Seite des Herstellers, ein Plan statt Bauchgefühl, eigene Entscheidung und Verantwortung'],
    caption='''Fünf Gewohnheiten haben mich Geld gekostet. Fünf andere schützen es heute.

Früher:
– gekauft, was ein Influencer empfahl
– an feste Renditen geglaubt
– die Wallet-App aus dem Store geladen
– in Panik verkauft
– Fremde um Bestätigung gefragt

Heute:
– ich kaufe nur, was ich selbst erklären kann
– feste Renditen sind für mich ein Warnsignal
– meine Wallet kommt nur über die Seite des Herstellers
– ich folge einem Plan statt meinem Bauchgefühl
– ich entscheide selbst und trage die Verantwortung

Die linke Spalte hat mich über 70.000 $ gekostet. Die rechte kostet nur etwas Geduld.

Für alle, die mit Krypto und Bitcoin anfangen und sich vor Betrug schützen wollen.

Schick das jemandem, der gerade mit Krypto anfängt.''')

# ---------- Beitrag 5: Nischenmythos ----------
WAPO = 'Quelle: The Washington Post, 30.03.2021'
POSTS['beitrag-5'] = dict(
    date='2026-09-30', fmt='Nischenmythos entlarven', topic='Mythos: Was im App Store steht, ist sicher (gefälschte Wallet-Apps)',
    slides=[
        s_hook('MYTHOS', '„Was im App Store steht, ist %s.“' % A('geprüft und sicher'), cue='Stimmt das? Weiterwischen &#8594;'),
        s_point('DIE WAHRHEIT', 'Gefälschte Wallet-Apps schaffen es bis in offizielle Stores.',
                ['Gleicher Name. Gleiches Logo. Gute Bewertungen.', D('2021 stand eine gefälschte Trezor-App in Apples App Store, fast fünf Sterne, 155 Bewertungen. Ein Nutzer verlor darüber 17,1 Bitcoin, damals rund 600.000 $.')],
                src=WAPO),
        s_point('BEI MIR', 'Mich hat eine gefälschte Wallet-App 70.000 $ gekostet.',
                ['Ich habe sie geladen, weil sie echt aussah.', D('Danach war das Geld weg.')]),
        s_point('WARUM DAS PASSIERT', 'Ein Store ist ein Marktplatz. Kein Tresor.',
                ['Betrüger kopieren Namen und Logos und laden ihre Kopie hoch.', D('Bis jemand sie meldet, haben die ersten schon eingezahlt. Die gefälschte Trezor-App stand elf Tage im Store.')],
                src=WAPO),
        s_point('ZUM MERKEN', 'Fünf Sterne sind %s.' % A('kein Echtheitssiegel'), ['Woher deine Wallet kommt, entscheidet, wem dein Geld gehört.'], meta=True),
        s_point('DEINE ERFAHRUNG', 'Woher hast du deine Wallet? Schreib %s in die Kommentare.' % A('Store oder Website'), None, meta=True),
    ],
    alts=['Mythos: Was im App Store steht, ist geprüft und sicher',
          'Gefälschte Wallet-Apps schaffen es bis in offizielle Stores',
          'Mich hat eine gefälschte Wallet-App 70.000 Dollar gekostet',
          'Ein Store ist ein Marktplatz, kein Tresor',
          'Fünf Sterne sind kein Echtheitssiegel',
          'Woher hast du deine Wallet? Schreib Store oder Website in die Kommentare'],
    caption='''Fünf Sterne, 155 Bewertungen und trotzdem gefälscht.

Mythos: Was im App Store steht, ist geprüft und sicher.

Die Wahrheit: Gefälschte Wallet-Apps schaffen es bis in offizielle Stores. Gleicher Name, gleiches Logo, gute Bewertungen. 2021 stand eine gefälschte Trezor-App elf Tage in Apples App Store. Ein Nutzer verlor darüber 17,1 Bitcoin, damals rund 600.000 $ (Quelle: The Washington Post, 30.03.2021).

Mich hat eine gefälschte Wallet-App 70.000 $ gekostet. Ich habe sie geladen, weil sie echt aussah. Danach war das Geld weg.

Ein Store ist ein Marktplatz, kein Tresor. Betrüger kopieren Namen und Logos und laden ihre Kopie hoch. Bis jemand sie meldet, haben die ersten schon eingezahlt.

Fünf Sterne sind kein Echtheitssiegel. Woher deine Wallet kommt, entscheidet, wem dein Geld gehört. Das gilt für jeden Krypto-Anfänger, egal ob Bitcoin oder andere Coins.

Woher hast du deine Wallet? Schreib Store oder Website in die Kommentare.''')

# ---------- Beitrag 6: Erfolgsgeschichte ----------
POSTS['beitrag-6'] = dict(
    date='2026-10-01', fmt='Erfolgsgeschichte', topic='Von 70.000 $ Verlust zu einem System mit fünfstelligem Jahresgewinn',
    slides=[
        s_hook('MEINE GESCHICHTE', '70.000 $ an Betrüger verloren. Heute bringt mir Krypto %s.' % A('jedes Jahr einen fünfstelligen Gewinn'), cue='So kam es &#8594;', size=''),
        s_point('DAMALS', 'Ich habe jede Abkürzung genommen.',
                ['Influencer-Coins. Cloud-Mining mit festen Renditen. Memecoins. Eine Wallet-App, die echt aussah.', D('Jede Abkürzung hat mich Geld gekostet. Die teuerste 70.000 $.')]),
        s_point('DER WENDEPUNKT', 'Ich habe aufgehört, anderen zu folgen.',
                ['Ich habe Schritt für Schritt selbst verstanden, was ich kaufe.', D('Daraus wurde ein einfaches, langfristiges System.')]),
        s_point('HEUTE', 'Ein System, das ich jedem erklären kann.',
                ['Es bringt mir jedes Jahr einen fünfstelligen Gewinn. Das ist meine Zahl, kein Versprechen für dich.', D('Über 250 Menschen sind diesen Weg inzwischen mit mir gegangen.')]),
        s_point('UND DU?', 'Ich bin kein Genie.',
                ['Ich habe mehr Lehrgeld bezahlt als die meisten.', D('Wenn ich nach 70.000 $ Verlust einen sicheren Weg gefunden habe, findest du ihn auch.')]),
        s_point('KOSTENLOSES TRAINING', 'Wie mein System funktioniert, zeige ich dir im %s.' % A('kostenlosen Training'),
                ['Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren. Link in meiner Bio.'], meta=True),
    ],
    alts=['70.000 Dollar an Betrüger verloren, heute bringt mir Krypto jedes Jahr einen fünfstelligen Gewinn',
          'Damals habe ich jede Abkürzung genommen',
          'Der Wendepunkt: Ich habe aufgehört, anderen zu folgen',
          'Heute: ein System, das ich jedem erklären kann',
          'Ich bin kein Genie, ich habe mehr Lehrgeld bezahlt als die meisten',
          'Wie mein System funktioniert, zeige ich dir im kostenlosen Training, Link in meiner Bio'],
    caption='''Mein teuerster Verlust kam aus einer App. Heute bringt mir Krypto jedes Jahr einen fünfstelligen Gewinn.

Damals habe ich jede Abkürzung genommen: Influencer-Coins, Cloud-Mining mit festen Renditen, Memecoins, eine Wallet-App, die echt aussah. Jede Abkürzung hat mich Geld gekostet. Die teuerste 70.000 $.

Der Wendepunkt: Ich habe aufgehört, anderen zu folgen. Ich habe Schritt für Schritt selbst verstanden, was ich kaufe. Daraus wurde ein einfaches, langfristiges System.

Heute bringt mir dieses System jedes Jahr einen fünfstelligen Gewinn. Das ist meine Zahl, kein Versprechen für dich. Über 250 Menschen sind diesen Weg inzwischen mit mir gegangen.

Ich bin kein Genie. Ich habe mehr Lehrgeld bezahlt als die meisten. Wenn ich nach 70.000 $ Verlust einen sicheren Weg gefunden habe, findest du ihn auch.

Wie mein System funktioniert, zeige ich dir im kostenlosen Training: Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren. Für alle, die mit Krypto und Bitcoin sicher starten wollen.

Das kostenlose Training findest du im Link in meiner Bio.''')

# ---------- Beitrag 7: Visueller Post (Bingo) ----------
CELLS = ['„Garantiert 2 % Rendite am Tag.“', '„Das Angebot gilt nur heute.“', '„Zahl zuerst die Netzwerkgebühr.“',
         '„Hallo, ich bin vom Support.“', '„Schick mir deine 12 Wörter zur Prüfung.“', '„Lade diese App, die ist sicherer.“',
         '„Ein Promi steht hinter dem Projekt.“', '„Ich habe dich in der Gruppe gesehen.“', '„Wir holen dein verlorenes Geld zurück.“']
POSTS['beitrag-7'] = dict(
    date='2026-10-02', fmt='Visueller Post', topic='Krypto-Betrugs-Bingo: neun Sätze von Betrügern',
    slides=[
        s_bingo('KRYPTO FÜR EINSTEIGER', 'Krypto-Betrugs-%s' % A('Bingo'), 'Jeder Satz hier ist ein Warnsignal. Wie viele hast du schon gehört?', CELLS, 4,
                'Schreib die Zahl in die Kommentare.'),
    ],
    alts=['Krypto-Betrugs-Bingo mit neun Sätzen: Garantiert 2 Prozent Rendite am Tag. Das Angebot gilt nur heute. Zahl zuerst die Netzwerkgebühr. Hallo, ich bin vom Support. Schick mir deine 12 Wörter zur Prüfung. Lade diese App, die ist sicherer. Ein Promi steht hinter dem Projekt. Ich habe dich in der Gruppe gesehen. Wir holen dein verlorenes Geld zurück'],
    caption='''Neun Sätze, die du von Krypto-Betrügern hörst. Einen davon habe ich selbst bezahlt.

„Garantiert 2 % Rendite am Tag.“
„Das Angebot gilt nur heute.“
„Zahl zuerst die Netzwerkgebühr.“
„Hallo, ich bin vom Support.“
„Schick mir deine 12 Wörter zur Prüfung.“
„Lade diese App, die ist sicherer.“
„Ein Promi steht hinter dem Projekt.“
„Ich habe dich in der Gruppe gesehen.“
„Wir holen dein verlorenes Geld zurück.“

Den Satz mit der Netzwerkgebühr habe ich selbst bezahlt. Und der letzte Satz kommt nach dem Verlust: Wer verloren hat, bekommt plötzlich Angebote, das Geld zurückzuholen. Auch das ist eine Masche.

Für alle, die mit Krypto und Bitcoin anfangen: Jeder dieser Sätze ist ein Warnsignal für Betrug.

Wie viele Felder hast du schon erlebt? Schreib die Zahl in die Kommentare.''')

# ---------- Beitrag 8: Frage an die Zielgruppe ----------
POSTS['beitrag-8'] = dict(
    date='2026-10-03', fmt='Frage an die Zielgruppe', topic='Hand aufs Herz: Geld an Internet-Bekanntschaft geschickt?',
    slides=[
        s_question('KRYPTO FÜR EINSTEIGER', 'Hand aufs Herz', 'Hast du schon einmal Geld an jemanden geschickt, den du nur aus dem Internet kennst?', 'Ich schon.',
                   'Schreib Ja oder Nein in die Kommentare.'),
    ],
    alts=['Hand aufs Herz: Hast du schon einmal Geld an jemanden geschickt, den du nur aus dem Internet kennst? Ich schon. Schreib Ja oder Nein in die Kommentare'],
    caption='''Hand aufs Herz. Ich fange an: Ja.

Ein Kontakt auf Instagram. Ein Guthaben, das ausgezahlt werden sollte. Vorher sollte ich eine „Netzwerkgebühr“ überweisen. Ich habe gezahlt. Die Auszahlung kam nie.

Viele schämen sich dafür und schweigen. Genau davon leben Betrüger. Wer darüber spricht, warnt andere Krypto-Anfänger.

Hast du schon einmal Geld an jemanden geschickt, den du nur aus dem Internet kennst? Schreib Ja oder Nein in die Kommentare.''')

# ---------- Beitrag 9: Schritt-fuer-Schritt-Anleitung ----------
POSTS['beitrag-9'] = dict(
    date='2026-10-04', fmt='Schritt-für-Schritt-Anleitung', topic='Mein Krypto-System in 4 Schritten (Teaser)',
    slides=[
        s_hook('MEIN SYSTEM', 'Mein Krypto-System nach 70.000 $ Lehrgeld. %s' % A('In 4 Schritten.')),
        s_point('SCHRITT 1 VON 4', 'Verstehen, bevor ich kaufe.', ['Ich kaufe nur, was ich in zwei Sätzen erklären kann.', D('Alles andere ist Hoffnung.')]),
        s_point('SCHRITT 2 VON 4', 'Geprüft einkaufen.', ['Über eine Börse, die ich vorher geprüft habe.', D('Keine Links aus Nachrichten. Keine Plattformen von Fremden.')]),
        s_point('SCHRITT 3 VON 4', 'Selbst verwahren.', ['Was ich langfristig halte, liegt in meiner eigenen Wallet.', D('Die Wörter dazu kennt nur ich.')]),
        s_point('SCHRITT 4 VON 4', 'Ein Plan statt Bauchgefühl.', ['Ich lege vorher fest, wann ich kaufe.', D('Dann halte ich mich daran. Auch an roten Tagen.')]),
        s_point('DAS WIE', 'Das Was kennst du jetzt. Das Wie zeige ich dir im %s.' % A('kostenlosen Training'), ['Link in meiner Bio.'], meta=True),
    ],
    alts=['Mein Krypto-System nach 70.000 Dollar Lehrgeld in 4 Schritten',
          'Schritt 1: Verstehen, bevor ich kaufe',
          'Schritt 2: Geprüft einkaufen',
          'Schritt 3: Selbst verwahren',
          'Schritt 4: Ein Plan statt Bauchgefühl',
          'Das Wie zeige ich dir im kostenlosen Training, Link in meiner Bio'],
    caption='''Kein Geheimnis, kein Hype. Vier Schritte, die ich heute jedes Mal gehe.

1. Verstehen, bevor ich kaufe: Ich kaufe nur, was ich in zwei Sätzen erklären kann. Alles andere ist Hoffnung.
2. Geprüft einkaufen: über eine Börse, die ich vorher geprüft habe. Keine Links aus Nachrichten, keine Plattformen von Fremden.
3. Selbst verwahren: Was ich langfristig halte, liegt in meiner eigenen Wallet. Die Wörter dazu kennt nur ich.
4. Ein Plan statt Bauchgefühl: Ich lege vorher fest, wann ich kaufe, und halte mich daran. Auch an roten Tagen.

Dieses System habe ich mir nach 70.000 $ Lehrgeld aufgebaut. Für Krypto-Anfänger, die Bitcoin sicher kaufen und langfristig halten wollen.

Das Was kennst du jetzt. Das Wie zeige ich dir im kostenlosen Training. Das kostenlose Training findest du im Link in meiner Bio.''')

# ---------- Storys ----------
STORIES = {
    'story-a': dict(date='2026-09-28', slides=[s_story('KOSTENLOSES TRAINING', 'Ich habe 70.000 $ an Krypto-Betrüger verloren.',
        ['Im kostenlosen Training zeige ich dir die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren.', D('Damit du sie überspringst.')], 'Link in meiner Bio')]),
    'story-b': dict(date='2026-09-30', slides=[s_story('KOSTENLOSES TRAINING', 'Ich habe alles ausprobiert.',
        ['Influencer-Coins. Cloud-Mining. Memecoins. Eine App, die echt aussah.', D('Der einfachste Weg, sicher einzusteigen: Schau dir genau dieses Training an.')], 'Link in meiner Bio')]),
    'story-c': dict(date='2026-10-02', slides=[s_story('NEU HIER?', 'Starte mit meinem %s.' % A('kostenlosen Training'),
        ['Die 3 Fehlgriffe, an denen Krypto-Anfänger ihr Geld verlieren.', D('Kostenlos. Ohne Vorwissen.')], 'Link in meiner Bio')]),
}

if __name__ == '__main__':
    which = sys.argv[1:] or list(POSTS) + list(STORIES)
    allpng = {}
    for name in which:
        if name in POSTS:
            p = POSTS[name]
            ok = check_text(name + ' Caption', p['caption']) and all(check_text(name + ' Alt', a) for a in p['alts'])
            assert len(p['alts']) == len(p['slides']), name + ': Alt-Texte passen nicht'
            pngs = build(name, p['slides'])
        else:
            pngs = build(name, STORIES[name]['slides'], 1080, 1920)
        allpng[name] = pngs
    json.dump(allpng, open(os.path.join(OUT, 'pngs.json'), 'w'), indent=1)
