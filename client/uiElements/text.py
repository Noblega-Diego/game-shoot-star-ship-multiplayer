

import pygame


class Text():
    def __init__(self) -> None:
        self.__src =srcFont = pygame.font.match_font('arial', bold=False, italic=False)
        self.__fuente = pygame.font.Font(srcFont, 36)
        self.__pos = (0,0)
        self.__color = (0,0,0)
        self.__render = None
        self.__text = ""

    def draw(self, surface: pygame.Surface):
        self.render()
        if(not (self.__render is None)):
            surface.blit(self.__render, self.__pos)

    def setPos(self, pos):
        self.__pos = pos
        return self

    def setColor(self, color):
        self.__color = color
        return self
    
    def setText(self, text):
        self.__text = text
        return self
    
    def setSize(self, size):
        self.__size = size
        self.__fuente = pygame.font.Font(self.__src, self.__size)
        return self
    
    def render(self):
        self.__render = self.__fuente.render(self.__text, True, self.__color)
        return self
    
    def getRender(self):
        return self.__render
    
    def getDimencion(self):
        return self.__fuente.size(self.__text)
        