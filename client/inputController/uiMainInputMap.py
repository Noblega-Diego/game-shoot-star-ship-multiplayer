import pygame

from client.inputController import command
from client.inputController.command import Command
from client.inputController.inputHandler import InputMap, KeyInput


class UiMainInputMap(InputMap):

    def __init__(self):
        self.__mapComand: dict[KeyInput, Command] = {
            KeyInput("key", pygame.K_ESCAPE): command.CommandExit(),
            KeyInput("event", pygame.QUIT): command.CommandExit()
        }

    def getMapInputs(self) -> dict[KeyInput, Command]:
        return self.__mapComand


