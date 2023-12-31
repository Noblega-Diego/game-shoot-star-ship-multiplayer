import math

import pygame
from pygame import Surface
from .basicSpriteGame import BasicSpriteGame


class Shoot(BasicSpriteGame):
    image = pygame.image.load('client/assets/vala.png')
    __velocidad = 12
    def __init__(self, initPos, grados):
        super().__init__()
        self.__grados = grados
        self.__rotate = True
        self.__duracion = 100
        self.setPos(initPos)
        self.__testColor = (255,255,255)

    def event(self, event):
        pass

    def update(self):
        if (self.__duracion > 0):
            self.__duracion -= 1
            if (self.__rotate):
                r = self.__velocidad
                y = math.sin(math.radians(self.__grados + 90)) * r
                x = math.cos(math.radians(self.__grados + 90)) * r
                self.__direction = (x, y)
                self.setImageDraw(pygame.transform.rotate(self.image, self.__grados))
                self.__rotate = False
            x, y = self.__direction
            self.setPos((self.getPos()[0] + x, self.getPos()[1] - y))

    def draw(self, surface: Surface):
        super().draw(surface)
       # kk = self.getMask().to_surface()
       # kk.fill(self.__testColor)
       # surface.blit(kk, (self.getRect().x, self.getRect().y))

    def setTestColor(self, param):
        self.__testColor = param
