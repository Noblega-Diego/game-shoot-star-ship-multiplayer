
import pygame

class Temporizar():
    
    def resetTime(self):
        self.__timeA = pygame.time.get_ticks()

    def getStatus(self):
        actualTime = pygame.time.get_ticks()
        return (actualTime - self.__timeA)
