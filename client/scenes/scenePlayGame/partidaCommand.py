# template v1.0
from client.inputController.command import Command


class moveCommand(Command):
    MOVE_UP = 'up'
    MOVE_LEFT = 'left'
    MOVE_RIGHT = 'right'
    MOVE_DOWN = 'down'
    def __init__(self, direction:str, player):
        from client.scenes.scenePlayGame.playGameController import Player
        from client.globalContext import GlobalContext
        self.__context = GlobalContext
        self.__player:Player = player
        self.__direction = direction

    def ejecute(self):
            self.__player.change_direccion(self.__direction)