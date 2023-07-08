
from typing import Type
from client.director import DirectorGame
from client.scene import Scene 


class ManagerScenes():

    def __init__(self, game:DirectorGame) -> None:
        self.__Scenes = {}
        self.__game = game

    def changeTo(self, name:str):
        if(not (self.__game.get_scene() is None)):
            self.__game.get_scene().end()
        self.__game.changeScene(self.__Scenes.get(name))

    def _getGame(self):
        return self.__game
    
    def _addScene(self, name, scene):
        self.__Scenes[name] = scene


        