from typing import List
from abc import ABC, abstractmethod
#Evento de ui
class EventUI():
    def __init__(self, source, type):
        self.__source = source
        self.type = type

    def get_source(self):
        return self.__source

    def get_type(self):
        return self.type

    def equalsTo(self, origin, type):
        if(self.get_source() == origin and self.type == type):
            return True
        else:
            return False
    def equalsTo(self, origin):
        if(self.get_source() == origin):
            return True
        else:
            return False

#Escuchador de evento
class ListeinerEventUI(ABC):
    @abstractmethod
    def handlee_event(self, event: EventUI):
        pass

    @abstractmethod
    def getScene(self):
        pass
    

#Iniciador del evento
class ElementActive():
    def __init__(self):
        self.__listeinertsEvent: List[ListeinerEventUI] = []

    def _lunchEvent(self, type):
        for listeiner in self.__listeinertsEvent:
            listeiner.handlee_event(EventUI(self, type))

    def add_listeinerEvent(self, listeiner: ListeinerEventUI):
        self.__listeinertsEvent.append(listeiner)

    def get_listeinersEvent(self):
        return self.__listeinertsEvent
    
    def update(self):
        pass

class ElementUI(ElementActive):
    def __init__(self):
        super().__init__()

    def event(self, evnt):
        pass

    def draw(self, surface):
        pass