
from abc import ABC,abstractmethod

from client.basicEventUI import ElementActive, ListeinerEventUI
from typing import TypeVar

T = TypeVar('T')

class Scene(ABC):
    __init = False

    def activeEventStart(self):
        if(not(self.__init)):
            self.__init = True
            print(self.__class__)
            self.start()
            

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def event(self, event):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def end(self):
        pass

    def isInit(self):
        return self.__init
    
    def resetInit(self):
        self.__init = False
    
 



class SceneAppendListeiner(Scene):

    def __init__(self) -> None:
        super().__init__()
        self.__ObjectEvents:list[ElementActive] = []

    def addObjectsEvents(self, element:T)->T:
        self.__ObjectEvents.append(element)
        return element

    def set_listeinerEvent(self, listeiner:ListeinerEventUI):
        for element in self.__ObjectEvents:
            element.add_listeinerEvent(listeiner)

    def getObjectsEvents(self):
        return self.__ObjectEvents
    