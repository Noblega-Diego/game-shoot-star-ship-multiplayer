import pygame

from . import command
from .command import Command, CommandExtend
from . import PYGAME_MOUSE_POS

class KeyInput:
    def __init__(self, type_input:str, cod, typeEventPygame = -1):
        self.type = type_input
        if(typeEventPygame > -1):
            self.type +="_"+ str(typeEventPygame)
        self.cod = cod

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
                if ((k.type == 'key' and keys[k.cod])):
                    com.addComand(map.getMapInputs().setdefault(k, None))
                elif ((k.type == 'mouse' and k.cod == PYGAME_MOUSE_POS)):
                    com.addComand(map.getMapInputs().setdefault(k, None))

    def handleEvent(self,com, map, event):
        if (not map is None):
            for k in map.getMapInputs().keys():
                if (k.type == 'event_' + str(event.type)):
                    c = None
                    if(event.type == pygame.KEYDOWN and k.cod == event.key):
                        c = map.getMapInputs().setdefault(k, None)
                    elif(event.type == pygame.KEYUP and k.cod == event.key):
                        c = map.getMapInputs().setdefault(k, None)
                    elif(event.type == pygame.JOYBUTTONDOWN and k.cod == event.button):
                        c = map.getMapInputs().setdefault(k, None)
                    elif(event.type == pygame.JOYBUTTONUP and k.cod == event.button):
                        c = map.getMapInputs().setdefault(k, None)
                    elif(event.type == pygame.MOUSEBUTTONDOWN and k.cod == event.button):
                        c = map.getMapInputs().setdefault(k, None)
                    if(not c is None):
                        com.addComand(c)

    def changeInputMap(self, inputMap: InputMap):
        self.__inputMap = inputMap
        return self
