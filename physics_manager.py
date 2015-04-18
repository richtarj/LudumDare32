import pygame

class PhysicsAttributes:
    position = [0.0,0.0]
    velocity = [0.0, 0.0]
    acceleration = [0.0, 0.0]


class PhysicsManager(object):
    _actors = {}
    _worldWidth, _worldHeight = None, None

    UNITS_PER_TILE = 10

    def __init__(self, worldWidth, worldHeight):
        self._worldWidth = worldWidth
        self._worldHeight = worldHeight

    def add_actor(self, actor, has_gravity=False):
        self._actors[actor] = PhysicsAttributes()
        if has_gravity:
            self._actors[actor].acceleration[1] = 9.8 #units/second
    def remove_actor(self, actor):
        self._actors[actor] = None

    def set_velocity(self, actor, velocity):
        self._actors[actor].velocity = velocity
    def set_velocity_x(self, actor, velocity_x):
        self._actors[actor].velocity[0] = velocity_x
    def set_velocity_y(self, actor, velocity_y):
        self._actors[actor].velocity[1] = velocity_y
    def add_velocity_x(self, actor, velocity_dx):
        self._actors[actor].velocity[0] += velocity_dx
    def add_velocity_y(self, actor, velocity_dy):
        self._actors[actor].velocity[1] += velocity_dy
    def get_velocity(self, actor):
        return self._actors[actor].velocity
    def get_velocity_x(self, actor):
        return self._actors[actor].velocity[0]
    def get_velocity_y(self, actor):
        return self._actors[actor].velocity[1]

    def update(self, delta, tileSize):
        for actor, attributes in self._actors.iteritems():

            attributes.velocity[0] += delta * attributes.acceleration[0] #every frame, we update the velocity based on how fast it is changing
            attributes.velocity[1] += delta * attributes.acceleration[1]

            attributes.position[0] += delta * attributes.velocity[0] * self.UNITS_PER_TILE
            if(attributes.position[0] < 0):
                attributes.position[0] = 0
                attributes.velocity[0] = 0
            elif(attributes.position[0] > self._worldWidth - actor.widthInTiles):
                attributes.position[0] = self._worldWidth - actor.widthInTiles
                attributes.velocity[0] = 0 #the object has stopped moving

            attributes.position[1] += delta * attributes.velocity[1] * self.UNITS_PER_TILE
            if(attributes.position[1] < 0):
                attributes.position[1] = 0
                attributes.velocity[1] = 0
            elif(attributes.position[1] > self._worldHeight - actor.heightInTiles):
                attributes.position[1] = self._worldHeight - actor.heightInTiles
                attributes.velocity[1] = 0

            actor.position = (attributes.position[0] * tileSize, attributes.position[1] * tileSize)
