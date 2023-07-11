import functools

from client.manejadorScenas.uiManager import UiManager
from client.uiElements.uiPunter import UiPunter

class GlobalContext(object):
    def initialize(self, game):
        self.__game = game
        self.__uiPunter = UiPunter().setImage('client/assets/sprite_nave.png')
        self.__sceneManager = UiManager(self.__game)
        return self

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GlobalContext, cls).__new__(cls)
        return cls.instance

    def getUiMause(self) -> UiPunter:
        return self.__uiPunter

    def getSceneManager(self) -> UiManager:
        return self.__sceneManager

    def getDirectorGame(self):
        return self.__game

