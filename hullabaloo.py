import pyTTS
import random
from time import sleep

tts = pyTTS.Create()

def say(text):
    tts.Speak(text, pyTTS.tts_is_xml)

def a(word):
    if word[0] in 'aeiou':
        article = 'an'
    else:
        article = 'a'
    return '%s %s' % (article, word)

class RList:
    def __init__(self, *args, **kwargs):
        self.items = args
    def random(self, omit=None):
        rest = [x for x in self.items if x != omit]
        return random.choice(rest)

class RDict:
    def __init__(self, *args, **kwargs):
        self.items = kwargs
    def random(self, omitkey=None, omit=None):
        rest = [x for x in self.items.keys() if x != omitkey]
        choice = random.choice(rest)
        return choice, self.items[choice].random(omit)
    
actions = RList('Dance','Hop','Crawl','<pron sym="t ih p - t ow"/>')
items = RDict(shapes=RList('star','square','circle','triangle'),
              colors=RList('blue shape','orange shape','yellow shape','brown shape'),
              foods=RList('pear','pizza','carrot','egg'))

for i in range(3):
    say("Let's Play!")
    sleep(1)
    last_key, last_item = None, None
    for i in range(6):
        last_key, last_item = items.random(None, last_item)
        callout = '%s to %s.' % (actions.random(),a(last_item))
        say(callout)
        sleep(5)
    last_key, last_item = items.random(last_key, last_item)
    winner = 'Whoever is standing on %s wins!' % (a(last_item))
    say(winner)
    sleep(1)
    say('Winner take a <pron sym="b aw"/>!')
    sleep(1)
say('Great game, everybody!')
