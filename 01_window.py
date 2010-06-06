#
# get pygame ready for use
#
import pygame
pygame.init()

#
# some values we want to remember for later use
#
width = 320
height = 240
size = (width, height)

# colors are tuples of length three (r, g, b)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

#
# create, draw and display the picture
#
# In pygame we work with surfaces, which are canvases of various sizes.
# pygame.display is a special surface that you can see on the screen.
# flip() is a special method that causes what you've drawn on the display to be painted to the screen.
# blit() is a method of all surfaces that allows you to quickly copy one surface onto another.
screen = pygame.display.set_mode(size)
screen.fill(blue)
pygame.display.flip()

#
# A loop keeps this program running so we can see the screen
#
clock = pygame.time.Clock()
leave = False
# "True" is always True so the loop continues until a "break"
while True:
    # This timer makes sure there are never more than 30 loops in a second
    clock.tick(30)
    # This loop looks through the event queue for a "QUIT" (the x in the upper right)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
            break
    if leave:
        break
