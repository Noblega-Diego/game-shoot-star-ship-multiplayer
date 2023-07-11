


from client.basicEventUI import Draw, ElementActive, ElementUI
from client.scene import Scene,SceneAppendListeiner
from client.uiElements.button import Button
from client.utils.Temporizador import Temporizar
from client.utilsElemets.basicBackGround import BasicBackGround


class InitScene(SceneAppendListeiner):
    
    def __init__(self):
        super().__init__()
        self.Background = self.addObjectsEvents(BasicBackGround()
                                                .setImage('client/assets/space.png'))
        self.Etime = self.addObjectsEvents(TimeElement())
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()
        
    def start(self):
        self.Etime.setTimeActive(5000)
        self.Etime.startTime()
        self.__context.getUiMause().setImage('client/assets/sprite_nave.png')
    
    def event(self, event):
        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, ElementUI)):
                elemts.event(event)

    def update(self):
        for elemts in self.getObjectsEvents():
            elemts.update()

    def draw(self, surface):
        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, Draw)):
                elemts.draw(surface)

    def end(self):
        self.resetInit()


class TimeElement(ElementActive):
    def __init__(self):
        super().__init__()
        self.__timeActive = -1
        self.__temporizar = Temporizar()
        self.__active = False

    def update(self):
        print(self.__active)
        print(self.__timeActive)
        print(self.__temporizar.getStatus())
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
    
