import math

class Estrella:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def distancia(self, otra_estrella):
        dx = self.x - otra_estrella.x
        dy = self.y - otra_estrella.y
        dz = self.z - otra_estrella.z
        return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

    def distancia_origen(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)