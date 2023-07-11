
import pygame
from client.basicEventUI import ElementUI


class UiPunter(ElementUI):
    def __init__(self) -> None:
        super().__init__()
        self.__pos = (0,0)
        self.__cursor = None
        self.__offset = (0,0)

    def update(self):
        pass

    def draw(self, surface:pygame.Surface):
        self.__pos = pygame.mouse.get_pos()
        if(not (self.__cursor is None)):
            surface.blit(self.__cursor,(self.__pos[0] + self.__offset[0],self.__pos[1] + self.__offset[1]))

    def event(self, evnt):
        pass
    
    def setImage(self, src):
        if(not (src is None)):
            cursor = pygame.image.load(src)
            self.__cursor = pygame.transform.scale(cursor, [32,32])
        else:
            self.__cursor = None
        return self

    def setOffset(self, offset):
        self.__offset = offset
        return self
    
    def setVisibleMouse(self, active):
        pygame.mouse.set_visible(active)
        return self