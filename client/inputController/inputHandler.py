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
        from .uiMainInputMap import UiMainInputMap
        self.__masterInputMap = UiMainInputMap()
        self.__context = context

    def handleInputEvent(self, event) -> Command:
        keys = pygame.key.get_pressed()
        com = command.CommandCombined()
        self.handleEvent(com,self.__masterInputMap,event)
        self.handleEvent(com,self.__inputMap,event)
        return com

    def handleInputKey(self) -> Command:
        keys = pygame.key.get_pressed()
        com = command.CommandCombined()
        self.handleKey(com,self.__masterInputMap,keys)
        self.handleKey(com,self.__inputMap,keys)
        return com

    def handleKey(self,com, map, keys):
        if (not map is None):
            for k in map.getMapInputs().keys():
                if ((k.type == 'key' and keys[k.num])):
                    print(k.num)
                    com.addComand(map.getMapInputs().setdefault(k, None))

    def handleEvent(self,com, map, event):
        if (not map is None):
            for k in map.getMapInputs().keys():
                if (k.type == 'event' and k.num == event.type):
                    c = map.getMapInputs().setdefault(k, None)
                    if (isinstance(c, CommandExtend)):
                        com.addComand(c.addEvent(event))
                    else:
                        com.addComand(c)

    def changeInputMap(self, inputMap: InputMap):
        self.__inputMap = inputMap
        return self
