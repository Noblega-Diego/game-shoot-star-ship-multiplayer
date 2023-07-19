import pygame

from client.inputController import PYGAME_MOUSE_POS
from client.inputController.command import Command
from client.inputController.inputHandler import InputMap, KeyInput


class UiMainInputMap(InputMap):

    def __init__(self, player):
        from . import partidaCommand as commandPartida
        self.__mapComand: dict[KeyInput, Command] = {
            KeyInput("key", pygame.K_w): commandPartida.moveCommand(commandPartida.moveCommand.MOVE_UP,player),
            KeyInput("key", pygame.K_a): commandPartida.moveCommand(commandPartida.moveCommand.MOVE_LEFT,player),
            KeyInput("key", pygame.K_s): commandPartida.moveCommand(commandPartida.moveCommand.MOVE_DOWN,player),
            KeyInput("key", pygame.K_d): commandPartida.moveCommand(commandPartida.moveCommand.MOVE_RIGHT,player),
            KeyInput("event", 1,pygame.MOUSEBUTTONDOWN): commandPartida.shoot(player),
            KeyInput("mouse", PYGAME_MOUSE_POS): commandPartida.rotate(player)
        }

    def getMapInputs(self) -> dict[KeyInput, Command]:
        return self.__mapComand


