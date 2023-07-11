import pygame
import sys

from client.director import DirectorGame
from client.globalContext import GlobalContext
from client.scene import Scene

class Game(DirectorGame[Scene]):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.__context = GlobalContext().initialize(self)
        self.__size = (1200, 800)
        self.__surface = pygame.display.set_mode(self.__size, vsync=0)
        pygame.display.set_caption('nave war')

    def start(self):
        self.__flag_run = True
        self.__context.getSceneManager().changeTo('inicio')
        self.runGame()

    def runGame(self):
        clock = pygame.time.Clock()
        while self.__flag_run:
            clock.tick(30)  #se setea a 30fps
            for event in pygame.event.get(pygame.QUIT):
                if (event.type == pygame.QUIT):
                    self.__flag_run = False
                    
            if self.get_scene():
                self.get_scene().activeEventStart()
                for event in pygame.event.get():
                    self.get_scene().event(event)
                self.__context.getUiMause().update()
                self.get_scene().update()
                self.get_scene().draw(self.__surface)
                self.__context.getUiMause().draw(self.__surface)
            pygame.display.update()
        pygame.quit()
        sys.exit()