
from typing import Type
from client.director import DirectorGame 


class ManagerScenes():

    def __init__(self, game:DirectorGame) -> None:
        self.__Scenes = {}
        self.__game = game

    def changeTo(self, name:str):
        self.__game.changeScene(self.__Scenes.get(name))

    def _getGame(self):
        return self.__game
    
    def _addScene(self, name, scene):
        self.__Scenes[name] = scene


        