import pygame
import sys
from pygame.locals import *

MAPWIDTH = 50
MAPHEIGHT = 50
TILESIZE = 10

pygame.init()
surface = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

while True:

    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            #and the game and close the window
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if(event.key == K_q):
                pygame.quit()
                sys.exit()

    #loop through each row
    for row in range(MAPHEIGHT):
        #loop through each column in the row
        for column in range(MAPWIDTH):
            #draw the resource at that position in the tilemap, using the correct colour
            pygame.draw.rect(surface, (255, 0, 0), (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))

    #update the display
    pygame.display.update()
