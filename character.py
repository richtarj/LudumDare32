import pygame

class Character(object):
    MAIN_CHARACTER = ("characters/dumb.jpg", 5, 6)

    surface = None
    _widthInTiles, _heightInTiles = None, None
    positionInTiles = [0.0,0.0]
    _tileSize = None
    TILES_IN_SECOND = 10

    movingUp, movingRight, movingDown, movingLeft = False, False, False, False

    def __init__(self, (imageName, wTiles, hTiles)):
        self._baseSurface = pygame.image.load(imageName)
        self._widthInTiles = wTiles
        self._heightInTiles = hTiles

    @staticmethod
    def genMainCharacter():
        return Character(Character.MAIN_CHARACTER)

    def _deltaToDistance(self, delta):
        return delta * self.TILES_IN_SECOND

    def moveUp(self, delta, bounds):
        self.positionInTiles[1] = self.positionInTiles[1] - self._deltaToDistance(delta)
        if(self.positionInTiles[1] < 0):
            self.positionInTiles[1] = 0.0

    def moveRight(self, delta, bounds):
        self.positionInTiles[0] = self.positionInTiles[0] + self._deltaToDistance(delta)
        if(self.positionInTiles[0] + self.surface.get_width() > bounds.right):
            self.positionInTiles[0] = bounds.right - self.surface.get_width()

    def moveDown(self, delta, bounds):
        self.positionInTiles[1] = self.positionInTiles[1] + self._deltaToDistance(delta)
        if(self.positionInTiles[1] + self.surface.get_height() > bounds.bottom):
            self.positionInTiles[1] = bounds.bottom - self.surface.get_height()

    def moveLeft(self, delta, bounds):
        self.positionInTiles[0] = self.positionInTiles[0] - self._deltaToDistance(delta)
        if(self.positionInTiles[0] < 0):
            self.positionInTiles[0] = 0.0

    def update(self, delta, tileSize, bounds):
        if tileSize != self._tileSize:
            self.surface = pygame.transform.smoothscale(self._baseSurface, (self._widthInTiles*tileSize, self._heightInTiles*tileSize))
            self._tileSize = tileSize

        if self.movingUp:
            self.moveUp(delta, bounds)
        if self.movingRight:
            self.moveRight(delta, bounds)
        if self.movingDown:
            self.moveDown(delta, bounds)
        if self.movingLeft:
            self.moveLeft(delta, bounds)

        self.position = (self.positionInTiles[0] * self._tileSize, self.positionInTiles[1] * self._tileSize)
        
