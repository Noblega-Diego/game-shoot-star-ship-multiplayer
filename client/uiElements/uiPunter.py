
import pygame
from client.basicEventUI import ElementUI


class UiPunter(ElementUI):
    def __init__(self) -> None:
        super().__init__()
        self.__pos = (0,0)
        pygame.mouse.set_visible(False)
        self.__cursor = None

    def update(self):
        self.__pos = pygame.mouse.get_pos()

    def draw(self, surface:pygame.Surface):
        if(not (self.__cursor is None)):
            surface.blit(self.__cursor,self.__pos)

    def event(self, evnt):
        pass
    
    def setImage(self, src):
        cursor = pygame.image.load(src)
        self.__cursor = pygame.transform.scale(cursor, [32,32])
        return self
    
