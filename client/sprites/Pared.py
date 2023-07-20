import pygame
from pygame import Surface
from .basicSpriteGame import BasicSpriteGame


class Pared(BasicSpriteGame):
    __image = pygame.image.load("client/assets/pared.png")
    def __init__(self):
        super().__init__()
        self.setImageDraw(self.__image)

    def event(self, event):
        pass

    def update(self):
        pass

    def draw(self, surface: Surface):
        super().draw(surface)
