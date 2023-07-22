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
        self.refresh()
        if(not self.__imagedraw is None):
            surface.blit(self.__imagedraw, self.__rect)

    def changeImageDraw(self, src):
        self.__imagedraw = pygame.image.load(src)
        return self

    def setImageDraw(self, image):
        self.__imagedraw = image
        return self

    def getImageDraw(self) -> Surface:
        return self.__imagedraw

    def setPos(self, pos: Tuple[int, int]):
        self.__pos = pos
        return self

    def getPos(self):
        return self.__pos

    def getRect(self):
        return self.__rect

    def getMask(self):
        if(not self.__imagedraw is None):
            return pygame.mask.from_surface(self.getImageDraw())
        return None

    def detectCollider(self, sprite):
        mask = self.getMask()
        maskOther = sprite.getMask()
        vrect = sprite.getRect()
        if((not self.getRect() is None) and (not vrect is None)):
            oX = vrect.x - self.getRect().x
            oY = vrect.y - self.getRect().y
            if mask.overlap(maskOther, (oX, oY)):
                return True
            return False
        else:
            return False

    def refresh(self):
        if (not self.__imagedraw is None):
            self.__rect = self.__imagedraw.get_rect()
            self.__rect.center = self.__pos
