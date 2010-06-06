#
# get pygame ready for use
#
import random
import pygame
pygame.init()

#
# some values we want to remember for later use
#
width = 320
height = 240
size = (width, height)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


# Rects are rectangular objects that are very useful 
# they have position and size and we can check to see if 
# they overlap. Many games will depend on this collision 
# detection.
dot = pygame.Rect(0,0,10,10)
dot.center = [40,36]

target = pygame.Rect(0,0,20,20)
target.center = [140,136]


#
# create, draw and display the picture
#
screen = pygame.display.set_mode(size)

screen.fill(black)

# instead of using a special surface this time we use an optional parameter
# of fill and pass our rectangles
screen.fill(white, dot)
screen.fill(red, target)

pygame.display.flip()


#
# A loop keeps this program running so we can see the screen
# otherwise the window would close when the thread of execution finished
#
clock = pygame.time.Clock()
leave = False
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.mod & pygame.KMOD_ALT:
                offset = 50
            elif event.mod & pygame.KMOD_CTRL:
                offset = random.randint(-60, 60)
            else:
                offset = 10
            
            # calculate the direction of the movement based on which key was pressed to cause the event
            # we move the top and left of the dot, but we could just as easily move it in another way
            # because the motion is relative
            if event.key == pygame.K_RIGHT:
                dot.left += offset
            elif event.key == pygame.K_LEFT:
                dot.left -= offset
            elif event.key == pygame.K_UP:
                dot.top -= offset
            elif event.key == pygame.K_DOWN:
                dot.top += offset
        
        # we use a special method of rects to check for collisions
        # if the rects overlap we have hit the target
        # move the target randomly
        if dot.colliderect(target):
            target.center = (random.randint(0, width), random.randint(0, height))
    
    # erase the last frame and draw the next
    screen.fill(black)
    screen.fill(white, dot)
    screen.fill(red, target)
    pygame.display.flip()
    
    if leave:
        break
