import pygame
from client.basicEventUI import ElementUI


class BasicBackGround(ElementUI):
    def __init__(self):
        super().__init__()
        self.__background = None
        self.__dimencion = None

    def update(self):
        pass

    def event(self, evnt):
        pass

    def draw(self, surface:pygame.SurfaceType):
        surface.blit(self.__background, (0, 0))

    def setImage(self,src):
        self.__src = src
        if(self.__dimencion == None):
            self.__dimencion = (1200,800)
        self.__background = pygame.transform.scale( pygame.image.load(self.__src), self.__dimencion)
        return self
    
    def setDimencion(self, dimencion):
        self.__dimencion = dimencion
        return self