import pygame

from . import command
from .command import Command, CommandExtend


class KeyInput:
    def __init__(self, type_input:str, num):
        self.type = type_input
        self.num = num

class InputMap:
    def getMapInputs(self) -> dict[KeyInput, Command]:
        pass

class InputHandle:


    def __init__(self, context):
        self.__inputMap = None
        self.__context = context

    def handleInput(self, event) -> Command:
        keys = pygame.key.get_pressed()
        com = command.CommandCombined()
        if(not self.__inputMap is None):
            for k in self.__inputMap.getMapInputs().keys():
                if((k.type == 'key' and keys[k.num])):
                    com.addComand(self.__inputMap.getMapInputs().setdefault(k,None))
                if(k.type == 'event' and k.num == event.type):
                    c = self.__inputMap.getMapInputs().setdefault(k,None)
                    if(isinstance(c,CommandExtend)):
                        com.addComand(c.addEvent(event))
                    else:
                        com.addComand(c)
        return com



    def changeInputMap(self, inputMap: InputMap):
        self.__inputMap = inputMap
        return self
