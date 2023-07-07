

from client.basicEventUI import ElementActive, ElementUI
from client.scene import Scene,SceneAppendListeiner
from client.uiElements.button import Button
from client.utils.Temporizador import Temporizar


class InitScene(SceneAppendListeiner):
    
    def __init__(self):
        super().__init__()
        self.Etime:TimeElement = self.addObjectsEvents(TimeElement())
        
    def start(self):
        self.Etime.setTimeActive(5000)
        self.Etime.startTime()
    
    def event(self, event):
        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, ElementUI)):
                elemts.event(event)

    def update(self):
        for elemts in self.getObjectsEvents():
            elemts.update()

    def draw(self, surface):
        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, ElementUI)):
                elemts.draw(surface)


class TimeElement(ElementActive):
    def __init__(self):
        super().__init__()
        self.__timeActive = -1
        self.__temporizar = Temporizar()
        self.__active = False

    def update(self):
        if((not self.__active) and (self.__timeActive > 0) and (self.__timeActive < self.__temporizar.getStatus())):
            self.__active = True
            self._lunchEvent("Ftime")


    def setTimeActive(self, time):
        self.__timeActive = time
        return self
    
    def startTime(self):
        self.__temporizar.resetTime()
        self.__active = False
        return self
    