import random
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LTBLUE = (0,255,255)

class ClickySquare(object):
    def __init__(self, left, top, width, height, color, sound):
        self.rect = pygame.Rect(left, top, width, height)
        self._color = color
        self._current_color = color
        self._sound = sound
    def on_mousedown(self, (x,y)):
        if self.rect.collidepoint(x,y):
            self._current_color = WHITE
            self._sound.play()
    def on_mouseup(self):
        self._current_color = self._color
    def draw(self, surface):
        surface.fill(self._current_color, self.rect)

def load_sound(name):
    class NoneSound:
        def play(self): pass
    try:
        sound = pygame.mixer.Sound(name)
    except:
        print 'Cannot load sound: ', name
        return NoneSound()
    return sound

sounds_to_choose = ['tada','ringout','ringin','ding','chord']
sounds = ['C:\\Windows\\media\\%s.wav' % x for x in sounds_to_choose]
    
width = 200
height = 200
size = (width, height)

s1 = ClickySquare(20, 20, 80, 80, RED, load_sound(sounds[0]))
s2 = ClickySquare(20, 100, 80, 80, BLUE, load_sound(sounds[1]))
s3 = ClickySquare(100, 20, 80, 80, GREEN, load_sound(sounds[2]))
s4 = ClickySquare(100, 100, 80, 80, LTBLUE, load_sound(sounds[3]))

squares = [s1,s2,s3,s4]

screen = pygame.display.set_mode(size)
screen.fill(BLACK)

for i in squares:
    i.draw(screen)

pygame.display.flip()

clock = pygame.time.Clock()
leave = False
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in squares:
                i.on_mousedown(event.pos)
                i.draw(screen)
        elif event.type == pygame.MOUSEBUTTONUP:    
            for i in squares:
                i.on_mouseup()
                i.draw(screen)
    
    pygame.display.flip()
            
    if leave:
        break
