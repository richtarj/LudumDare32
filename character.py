import pygame

class Character(object):
    MAIN_CHARACTER = ("characters/dumb.jpg", 5, 6)

    surface = None
    widthInTiles, heightInTiles = None, None
    position = (0,0)
    _tileSize = None

    def __init__(self, (imageName, wTiles, hTiles)):
        self._baseSurface = pygame.image.load(imageName)
        self.widthInTiles = wTiles
        self.heightInTiles = hTiles

    @staticmethod
    def genMainCharacter():
        return Character(Character.MAIN_CHARACTER)

    def update(self, delta, tileSize):
        if tileSize != self._tileSize:
            self.surface = pygame.transform.smoothscale(self._baseSurface, (self.widthInTiles*tileSize, self.heightInTiles*tileSize))
            self._tileSize = tileSize
