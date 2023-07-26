import abc
from typing import TypeVar, Generic

from client.director import DirectorGame
from client.scene import Scene

T = TypeVar("T")
class ManagerScenes(abc.ABC):

    def __init__(self, game:DirectorGame) -> None:
        self.__history:list[str] = []
        self.__Scenes:dict[str,any] = {}
        self.__game = game

    def changeTo(self, name:str):
        if(not (self.__game.get_scene() is None)):
            self.__game.get_scene().end()
        self.__game.changeScene(self.getScene(name))
        self.__history.append(name)

    def _getGame(self):
        return self.__game

    @abc.abstractmethod
    def getScene(self,name:str)-> Scene:
        pass

    def getAll(self)->dict[str,any]:
        return self.__Scenes
    
    def _addScene(self, name, scene):
        self.__Scenes[name] = scene

    def getHistory(self)->list[str]:
        return [h for h in self.__history]

    def getLastHistory(self)->str:
        if(len(self.__history) > 1):
            return self.__history[-2]
        else:
            return self.__history[0]

        