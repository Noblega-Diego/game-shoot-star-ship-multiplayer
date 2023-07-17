from typing import Tuple

import pygame
from pygame import Surface, Rect


class BasicSpriteGame(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__pos: Tuple[int, int] = (0,0)
        self.__imagedraw = None
        self.__rect:Rect = None

    def update(self):
        pass

    def event(self, event):
        pass

    def draw(self, surface:Surface):
        if(not self.__imagedraw is None):
            self.__rect = self.__imagedraw.get_rect()
            self.__rect.center = self.__pos
            surface.blit(self.__imagedraw, self.__rect)

    def changeImageDraw(self, src):
        self.__imagedraw = pygame.image.load(src)
        return self

    def setImageDraw(self, image):
        self.__imagedraw = image
        return self

    def setPos(self, pos: Tuple[int, int]):
        self.__pos = pos
        return self

    def getPos(self):
        return self.__pos

    def getRect(self):
        return self.__rect
