

import pygame
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.event import Event
from client.uiElements.text import Text

from client.basicEventUI import ElementUI

class Button(ElementUI):
    def __init__(self, pos = None, size = None):
        super().__init__()
        self.__pos = pos
        self.__size = size
        if((self.__pos == None)):
             self.__pos = [0,0]
        if((self.__size == None)):
             self.__size = [0,0]
        self.__rect = Rect(self.__pos[0], self.__pos[1], self.__size[0], self.__size[1])
        self.__color = (122,50,121)

    def event(self, event:Event):
        if event != None:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                mousePos = pygame.mouse.get_pos()
                if(self.__rect.collidepoint(mousePos)):
                    self._lunchEvent('click')

    def update(self):
        pass

    def draw(self, surface: Surface):
        pygame.draw.rect(surface,self.__color, self.__rect)

    def set_pos(self, pos):
        self.__pos = pos
        self.__rect = Rect(self.__pos[0], self.__pos[1], self.__size[0], self.__size[1])
        return self

    def set_size(self, size):
        self.__size = size
        self.__rect = Rect(self.__pos[0], self.__pos[1], self.__size[0], self.__size[1])
        return self

    def set_color(self, color:tuple[int,int,int]):
        self.__color = color
        return self

    def _lunchEvent(self, type):
        super()._lunchEvent(type)

    def getSize(self):
        return self.__size
    
    def getPos(self):
        return self.__pos

class ButtonText(Button):
    def __init__(self):
        super().__init__(None, None)
        self.__EText = Text()

    def set_pos(self, pos):
        super().set_pos(pos)
        
        return self
    
    def draw(self, surface: Surface):
        super().draw(surface)
        dimencionText = self.__EText.getDimencion()
        mind =dimencionText[-1] / 2
        a =(self.getSize()[-1] / 2) - mind
        self.__EText.setPos((self.getPos()[0] + 8, self.getPos()[-1] + a)).draw(surface)

    def setText(self, text):
        self.__EText.setText(text)
        return self
    
    def setSize(self, size):
        self.__EText.setSize(size)
        return self
