import json
import pygame

class Level(object):
    _levelDef = None
    surface = None
    _tileSize = None

    def __init__(self, levelName):
        with open(levelName, "r") as levelData:
            self._levelDef = json.load(levelData)
            self.width = self._levelDef['w']
            self.height = self._levelDef['h']

            self.surface = pygame.Surface((self.width, self.height))
            pixels = pygame.PixelArray(self.surface)

            for item in self._levelDef['map']:
                x = item['x']
                y = item['y']
                color = tuple(self._levelDef['materials'][item['mat']])
                for dx in range(0, item['w']):
                    for dy in range(0, item['h']):
                        pixels[x+dx, y+dy] = color

    def update(self, tileSize):
        if(tileSize != self._tileSize):
            self.surface = pygame.transform.scale(self.surface, (self.width * tileSize, self.height * tileSize))
            self._tileSize = tileSize
