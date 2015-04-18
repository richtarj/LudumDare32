import pygame
import sys
from pygame.locals import *

from level import Level
from character import Character
from input_manager import InputManager, Actions

TILESIZE = 10

level1 = Level("levels/first.lvl")
mainChar = Character.genMainCharacter()
inputs = InputManager()

pygame.init()
surface = pygame.display.set_mode((level1.width*TILESIZE,level1.height*TILESIZE))

clock = pygame.time.Clock()

while True:

    clock.tick()
    delta = clock.get_time() / 1000.0

    for event in inputs.eventQueue():
        if event == Actions.QUIT:
            pygame.quit()
            sys.exit()
        elif event == Actions.START_USER_LEFT:
            mainChar.movingLeft = True
        elif event == Actions.START_USER_RIGHT:
            mainChar.movingRight = True
        elif event == Actions.START_USER_UP:
            mainChar.movingUp = True
        elif event == Actions.START_USER_DOWN:
            mainChar.movingDown = True
        elif event == Actions.STOP_USER_LEFT:
            mainChar.movingLeft = False
        elif event == Actions.STOP_USER_RIGHT:
            mainChar.movingRight = False
        elif event == Actions.STOP_USER_UP:
            mainChar.movingUp = False
        elif event == Actions.STOP_USER_DOWN:
            mainChar.movingDown = False

    mainChar.update(delta, TILESIZE, level1.surface.get_rect())
    level1.update(TILESIZE)

    surface.blit(level1.surface, (0,0))
    surface.blit(mainChar.surface, mainChar.position)
    pygame.display.update()
