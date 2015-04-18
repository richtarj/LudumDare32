import pygame
import sys
from pygame.locals import *

from level import Level
from character import Character
from input_manager import InputManager, Actions
from physics_manager import PhysicsManager

TILESIZE = 10

level1 = Level("levels/first.lvl")
mainChar = Character.genMainCharacter()
inputs = InputManager()
physics = PhysicsManager(level1.width, level1.height)

physics.add_actor(mainChar, has_gravity=True)

pygame.init()
surface = pygame.display.set_mode((level1.width*TILESIZE,level1.height*TILESIZE))

clock = pygame.time.Clock()

USER_MOTION_SPEED = 3
USER_JUMP_SPEED = 5

while True:

    clock.tick()
    delta = clock.get_time() / 1000.0

    for event in inputs.eventQueue():
        if event == Actions.QUIT:
            pygame.quit()
            sys.exit()
        elif event == Actions.START_USER_LEFT:
            physics.add_velocity_x(mainChar, -USER_MOTION_SPEED)
        elif event == Actions.START_USER_RIGHT:
            physics.add_velocity_x(mainChar, USER_MOTION_SPEED)
        elif event == Actions.START_USER_UP:
            if physics.get_velocity_y(mainChar) == 0:
                physics.add_velocity_y(mainChar, -USER_JUMP_SPEED)
        elif event == Actions.STOP_USER_LEFT:
            physics.add_velocity_x(mainChar, USER_MOTION_SPEED)
        elif event == Actions.STOP_USER_RIGHT:
            physics.add_velocity_x(mainChar, -USER_MOTION_SPEED)

    physics.update(delta, TILESIZE)

    mainChar.update(delta, TILESIZE)
    level1.update(TILESIZE)

    surface.blit(level1.surface, (0,0))
    surface.blit(mainChar.surface, mainChar.position)
    pygame.display.update()
