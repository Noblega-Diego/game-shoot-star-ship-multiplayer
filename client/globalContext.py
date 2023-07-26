from client.director import DirectorGame
from client.inputController.inputHandler import InputHandle
from client.manejadorScenas.uiManager import UiManager
from client.network import LocalMultiplayer, Network, PublicEventPygame
from client.uiElements.uiPunter import UiPunter

class GlobalContext(object):

    def initialize(self, game):
        from .game import Game
        self.__game:Game = game
        self.__size = self.__game.getSize()
        self.__partidaContext: dict[str, any] = {}
        self.__multiplayer:LocalMultiplayer = None
        self.__uiPunter = UiPunter().setImage('client/assets/sprite_nave.png')
        self.__inputHandler = InputHandle(self)
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

    def getDirectorGame(self)-> DirectorGame:
        return self.__game

    def getInputHandler(self):
        return self.__inputHandler

    def getMultiplayer(self):
        return self.__multiplayer

    def setMultiplayer(self, multiplayer:LocalMultiplayer):
        self.__multiplayer = multiplayer

    def getSize(self):
        return self.__size

    def getPartidaContext(self):
        return self.__partidaContext