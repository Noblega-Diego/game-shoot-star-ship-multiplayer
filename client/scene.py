
from abc import ABC,abstractmethod

from client.basicEventUI import ElementUI, ListeinerEventUI
class Scene(ABC):

    @abstractmethod
    def event(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, surface):
        pass

class SceneAppendListeiner(Scene):
    __ObjectEvents:list[ElementUI]  = []

    def addObjectsEvents(self, element:ElementUI):
        self.__ObjectEvents.append(element)

    def set_listeinerEvent(self, listeiner:ListeinerEventUI):
        for element in self.__ObjectEvents:
            element.add_listeinerEvent(listeiner)