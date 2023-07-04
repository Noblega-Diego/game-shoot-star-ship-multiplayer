
import abc
from typing import Generic, List, TypeVar

T = TypeVar("T")


class DirectorGame(abc.ABC,Generic[T]):

    def __init__(self):
        self.__scene:T = None

    @abc.abstractmethod
    def runGame(self):
        pass

    def changeScene(self,  scene:T):
        self.__scene = scene

    def get_scene(self)-> T:
        return self.__scene