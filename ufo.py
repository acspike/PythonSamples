import sys, pygame
import random
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
direction = [1, 1]
black = 0, 0, 0
maxspeed = 4
border = [10,10,10,20]
#bg = 0, 255, 255
bg = black

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)

ufo = pygame.image.load("ufo.bmp").convert()
ufo.set_colorkey(black,pygame.RLEACCEL)
blk = pygame.Surface((ufo.get_width(), ufo.get_height())).convert()

uforect = ufo.get_rect()
blrect = blk.get_rect()
uforect = uforect.move([border[0],border[1]])


screen.fill(bg)
blk.fill(bg)
screen.blit(ufo, uforect)
pygame.display.flip()

leave = False
i = 1
c = 1

while 1:
    clock.tick(30)
    for event in pygame.event.get():
	if event.type == pygame.QUIT: leave = True

    #randomize speed every 20 ticks
    i += 1
    if i>20:
        i = 1
        speed = [random.randrange(maxspeed),random.randrange(maxspeed)]
	
    #blrect = blrect.move([uforect.left, uforect.top])
    blrect.top = uforect.top
    blrect.left = uforect.left
    uforect = uforect.move([speed[0]*direction[0], speed[1]*direction[1]])

    #reverse direction when sprite hits the border
    if uforect.left < border[0] or uforect.right > (width - border[2]):
        direction[0] = -direction[0]
    if uforect.top < border[1] or uforect.bottom > (height - border[3]):
	direction[1] = -direction[1]
	
    screen.blit(blk, blrect)
    screen.blit(ufo, uforect)
    pygame.display.flip()
    #pygame.display.update([blrect, uforect])

    if leave: break

pygame.quit()

