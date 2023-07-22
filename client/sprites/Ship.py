import pygame
from pygame import Surface
from .basicSpriteGame import BasicSpriteGame


class Ship(BasicSpriteGame):
    def __init__(self):
        super().__init__()
        self.changeImageDraw('client/assets/sprite_nave.png')\
            .setPos((0,0))
        self.__basicImage = pygame.image.load('client/assets/sprite_nave.png')
        self.__grados = 0

    def event(self, event):
        super().event(event)

    def update(self):
        img = pygame.transform.rotate(self.__basicImage, self.__grados)
        self.setImageDraw(img)

    def draw(self, surface: Surface):
        super().draw(surface)
    #    mask = pygame.mask.from_surface(self.getImageDraw())
    #    surface.blit(mask.to_surface(),(self.getRect().x,self.getRect().y))
        pygame.draw.rect(surface,(255,255,255),self.getRect(),2)

    def setGr(self, grados):
        self.__grados = grados
        self.refresh()
        return self