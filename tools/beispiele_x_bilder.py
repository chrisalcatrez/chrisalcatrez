import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from x_gen import *

def A(t):
    return '<span class="acc">%s</span>' % t

BILDER = {
 'meme_gebuehr': lambda: build_x('x-meme-gebuehr', [x_meme('Übersetzungshilfe',
      'Was der „Support“ schreibt. Und was er meint.',
      'Er schreibt', '„Ihre Auszahlung ist freigegeben. Es fehlt nur die Netzwerkgebühr von 2 %.“',
      'Er meint', '„Schick mir ein letztes Mal Geld. Dann bin ich weg.“')]),
 'vs_betrug': lambda: build_x('x-vs-betrug', [x_vs('Mythos', '„Krypto ist doch alles Betrug.“',
      'Was viele glauben', ['Bitcoin ist ein Schneeballsystem.', 'Irgendwer verschwindet mit dem Geld.', 'Seriös geht das gar nie.'],
      'Was ich erlebt habe', ['Betrogen haben mich Menschen, nie das Netzwerk.', 'Gefälschte App, falscher Berater, erfundene Gebühr.', 'Bitcoin hat keinen Chef, der dich anruft.'])]),
 'chat_gebuehr': lambda: build_x('x-chat-gebuehr', [x_chat('Nachgestellter Chat', 'Der Chat, der mich die Netzwerkgebühr gekostet hat.', [
      ('Support', 'Ihre Auszahlung ist freigegeben. Es fehlt nur die Netzwerkgebühr.', False),
      ('Ich', 'Zieht die Gebühr einfach vom Guthaben ab.', True),
      ('Support', 'Das geht bei uns nur per Vorkasse. Danach wird sofort ausgezahlt.', False),
      ('Ich', 'Dann bleibt das Geld eben bei euch.', True)])]),
}

if __name__ == '__main__':
    names = sys.argv[1:] or list(BILDER)
    out = {}
    for n in names:
        out[n] = BILDER[n]()
    print(out)
