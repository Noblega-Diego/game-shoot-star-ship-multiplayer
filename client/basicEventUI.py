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

    def equalsTo(self, origin, type = None):
        if(type is None):
            return (self.get_source() == origin)
        else:
            return (self.get_source() == origin and self.type == type)

#Escuchador de evento
class ListeinerEventUI(ABC):
    @abstractmethod
    def handlee_event(self, event: EventUI):
        pass

    @abstractmethod
    def getScene(self):
        pass
    
class Update(ABC):  

    @abstractmethod
    def update(self):
        pass    

class Draw(Update, ABC):

    @abstractmethod
    def draw(self, surface):
        pass  

    
#Iniciador del evento
class ElementActive(Update):
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



class ElementUI(ElementActive, Draw):
    def __init__(self):
        super().__init__()

    def event(self, evnt):
        pass

    def draw(self, surface):
        pass