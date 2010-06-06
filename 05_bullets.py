import random
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LTBLUE = (0,255,255)
ORANGE = (255,140,0)
YELLOW = (255,255,0)

def make_surface(size, color):
    surface = pygame.Surface(size)#.convert()
    surface.fill(color)
    return surface

class Gun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0,0,30,20)
        self.image = make_surface(self.rect.size, BLUE)
        self._move = 15
    def up(self):
        self.rect.top -= self._move
    def down(self):
        self.rect.top += self._move
    def fire(self):
        Bullet(self.rect.right, self.rect.centery)
        
class Bullet(pygame.sprite.Sprite):
    group = pygame.sprite.RenderPlain()
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0,0,10,2)
        self.rect.center = (x,y)
        self.image = make_surface(self.rect.size, LTBLUE)
        self._move = 5
        Bullet.group.add(self)
    def update(self):
        self.rect.left += self._move
        
class Explosion(pygame.sprite.Sprite):
    group = pygame.sprite.RenderPlain()
    r = make_surface((10,10), RED)
    o = make_surface((7,7), ORANGE)
    y = make_surface((4,4), YELLOW)
    surfs = [r,r,r,o,o,y,y]
    def __init__(self,bullet):
        pygame.sprite.Sprite.__init__(self)
        self.center = (bullet.rect.centerx, bullet.rect.centery)
        self.index = 0
        self.image = Explosion.surfs[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        Explosion.group.add(self)
    def update(self):
        self.index += 1
        if self.index < len(Explosion.surfs):
            self.image = Explosion.surfs[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = self.center
        else:
            self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(screen.get_width() - 20, 0, 20, screen.get_height())
        self.image = make_surface(self.rect.size, GREEN)
    
width = 600
height = 400
size = (width, height)

screen = pygame.display.set_mode(size)
screen.fill(BLACK)

gun = Gun()
wall = Wall(screen)
allsprites = pygame.sprite.RenderPlain(gun,wall)

allsprites.draw(screen)

pygame.display.flip()

clock = pygame.time.Clock()
leave = False
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gun.up()
            elif event.key == pygame.K_DOWN:
                gun.down()
            elif event.key == pygame.K_SPACE:
                gun.fire()
    
    screen.fill(BLACK)
    allsprites.draw(screen)
    Bullet.group.update()
    hits = pygame.sprite.spritecollide(wall, Bullet.group, True)
    for i in hits:
        Explosion(i)
    Explosion.group.update()
    Bullet.group.draw(screen)
    Explosion.group.draw(screen)
    
    pygame.display.flip()
            
    if leave:
        break