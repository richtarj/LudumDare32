import pygame

class Character(object):
    MAIN_CHARACTER = ("characters/dumb.jpg", 5, 6)

    surface = None
    position = (0.0,0.0)
    _tileSize = 0
    TILES_IN_SECOND = 10

    movingUp, movingRight, movingDown, movingLeft = False, False, False, False

    def __init__(self, (imageName, wTiles, hTiles), tileSize):
        self.surface = pygame.image.load(imageName)
        self._tileSize = tileSize

        self.surface = pygame.transform.smoothscale(self.surface, (wTiles*tileSize, hTiles*tileSize))

    @staticmethod
    def genMainCharacter(tileSize):
        return Character(Character.MAIN_CHARACTER, tileSize)

    def _deltaToDistance(self, delta):
        return delta * self.TILES_IN_SECOND * self._tileSize

    def moveUp(self, delta, bounds):
        newY = self.position[1] - self._deltaToDistance(delta)
        if(newY < 0):
            newY = 0
        self.position = (self.position[0], newY)

    def moveRight(self, delta, bounds):
        newX = self.position[0] + self._deltaToDistance(delta)
        if(newX + self.surface.get_width() > bounds.right):
            newX = bounds.right - self.surface.get_width()
        self.position = (newX, self.position[1])

    def moveDown(self, delta, bounds):
        newY = self.position[1] + self._deltaToDistance(delta)
        if(newY + self.surface.get_height() > bounds.bottom):
            newY = bounds.bottom - self.surface.get_height()
        self.position = (self.position[0], newY)

    def moveLeft(self, delta, bounds):
        newX = self.position[0] - self._deltaToDistance(delta)
        if(newX < 0):
            newX = 0
        self.position = (newX, self.position[1])

    def update(self, delta, bounds):
        if self.movingUp:
            self.moveUp(delta, bounds)
        if self.movingRight:
            self.moveRight(delta, bounds)
        if self.movingDown:
            self.moveDown(delta, bounds)
        if self.movingLeft:
            self.moveLeft(delta, bounds)
