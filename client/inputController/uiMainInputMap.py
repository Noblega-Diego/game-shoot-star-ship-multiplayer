import pygame

from client.inputController import command
from client.inputController.command import Command
from client.inputController.inputHandler import InputMap, EventInput


class UiMainInputMap(InputMap):

    def __init__(self):
        self.__mapComand: dict[EventInput, Command] = {
            EventInput("key", pygame.K_ESCAPE): command.CommandExit(),
            EventInput("event", 0,pygame.QUIT): command.CommandExit()
        }

    def getMapInputs(self) -> dict[EventInput, Command]:
        return self.__mapComand


