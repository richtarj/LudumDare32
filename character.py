import pygame

class Character(object):
    MAIN_CHARACTER = ("characters/dumb.jpg", 5, 6)

    surface = None

    def __init__(self, (imageName, wTiles, hTiles), tileSize):
        self.surface = pygame.image.load(imageName)

        self.surface = pygame.transform.smoothscale(self.surface, (wTiles*tileSize, hTiles*tileSize))

    @staticmethod
    def genMainCharacter(tileSize):
        return Character(Character.MAIN_CHARACTER, tileSize)
