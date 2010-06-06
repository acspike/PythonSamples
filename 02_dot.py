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

spot = [40,36]

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#
# create, draw and display the picture
#
screen = pygame.display.set_mode(size)
screen.fill(black)

#
# dot
#
dot = pygame.Surface((10,10))
dot.fill(red)

screen.blit(dot, spot)

pygame.display.flip()



#
# A loop keeps this program running so we can see the screen
# otherwise the window would close when the thread of execution finished
#
clock = pygame.time.Clock()
leave = False
# "True" is always True so the loop continues until a "break"
while True:
    # This timer makes sure there are never more than 30 loops in a second
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
            break
        # Here we check to see if any keys have been pressed 
        # KEYDOWN is the even triggered when a key is pressed down
        # KEYUP is triggered when the key is released
        elif event.type == pygame.KEYDOWN:
            # Now we can check which keys were pressed
            # every key has a special name (look them up in the docs)
            # some keys are considered "modifiers" by pygame
            # ctrl and alt are such keys. 
            # They are usually depressed in conjunction with other keys.
            
            # "&" is a bitwise boolean logic operator
            # boolean logic is very simple but a full explanation can wait.
            
            # If ALT is depressed move with a large offset of 50 px
            if event.mod & pygame.KMOD_ALT:
                offset = 50
            # If CTRL is pressed move randomly in a range of 0-60px in either direction
            elif event.mod & pygame.KMOD_CTRL:
                offset = random.randint(-60, 60)
            # standard movement is 10px per key press
            else:
                offset = 10
            
            # calculate the direction of the movement based on which key was pressed to cause the event
            # the 0 index in spot holds X values
            # the 1 index holds Y values
            if event.key == pygame.K_RIGHT:
                spot[0] += offset
            elif event.key == pygame.K_LEFT:
                spot[0] -= offset
            elif event.key == pygame.K_UP:
                spot[1] -= offset
            elif event.key == pygame.K_DOWN:
                spot[1] += offset
            
            # There are also many mouse events we could make our program respond to.
    
    # erase the last frame
    screen.fill(black)
    # copy the dot onto the screen at the new spot
    screen.blit(dot, spot)
    # show the new frame
    pygame.display.flip()
    
    if leave:
        break
