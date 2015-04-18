import json
import pygame

class Level(object):
    _levelDef = None
    surface = None
    tileSize = 0

    def __init__(self, levelName, tileSize):
        with open(levelName, "r") as levelData:
            self._levelDef = json.load(levelData)
            self.tileSize = tileSize
            self.width = self._levelDef['w']
            self.height = self._levelDef['h']

            self.surface = pygame.Surface((self.width*tileSize, self.height*tileSize))
            pixels = pygame.PixelArray(self.surface)

            for item in self._levelDef['map']:
                x = item['x'] * tileSize
                y = item['y'] * tileSize
                color = tuple(self._levelDef['materials'][item['mat']])
                for dx in range(0, item['w'] * tileSize):
                    for dy in range(0, item['h'] * tileSize):
                        pixels[x+dx, y+dy] = color
