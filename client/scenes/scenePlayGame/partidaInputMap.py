import pygame

from client.inputController import PYGAME_MOUSE_POS
from client.inputController.command import Command
from client.inputController.inputHandler import InputMap, EventInput


class UiMainInputMap(InputMap):

    def __init__(self, player):
        from . import partidaCommand as commandPartida
        self.__mapComand: dict[EventInput, Command] = {
            EventInput("key", pygame.K_w): commandPartida.moveCommand(commandPartida.moveCommand.MOVE_UP, player),
            EventInput("key", pygame.K_a): commandPartida.moveCommand(commandPartida.moveCommand.MOVE_LEFT, player),
            EventInput("key", pygame.K_s): commandPartida.moveCommand(commandPartida.moveCommand.MOVE_DOWN, player),
            EventInput("key", pygame.K_d): commandPartida.moveCommand(commandPartida.moveCommand.MOVE_RIGHT, player),
            EventInput("event", 1, pygame.MOUSEBUTTONDOWN): commandPartida.shoot(player),
            EventInput("event", pygame.K_SPACE, pygame.KEYDOWN): commandPartida.shoot(player),
            EventInput("mouse", PYGAME_MOUSE_POS): commandPartida.rotate(player)
        }

    def getMapInputs(self) -> dict[EventInput, Command]:
        return self.__mapComand


