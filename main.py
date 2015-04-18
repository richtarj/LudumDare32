import pygame
import sys
from pygame.locals import *

from level import Level
from character import Character

MAPWIDTH = 100
MAPHEIGHT = 60
TILESIZE = 10

level1 = Level("levels/first.lvl", TILESIZE)
mainChar = Character.genMainCharacter(TILESIZE)

pygame.init()
surface = pygame.display.set_mode((level1.width*TILESIZE,level1.height*TILESIZE))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if(event.key == K_q):
                pygame.quit()
                sys.exit()

    surface.blit(level1.surface, (0,0))
    surface.blit(mainChar.surface, (20, 20))
    pygame.display.update()
