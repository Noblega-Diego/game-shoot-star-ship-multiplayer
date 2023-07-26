


from client.basicEventUI import Draw, ElementUI
from client.scene import SceneAppendListeiner
from client.utilsElemets.basicBackGround import BasicBackGround
from client.uiElements.uiPunterConst import UIPUNTER_OFFSET_MIND
from client.utilsElemets.timeElement import TimeElement


class InitScene(SceneAppendListeiner):
    
    def __init__(self):
        super().__init__()
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()
        self.Background = self.addObjectsEvents(BasicBackGround()
                                                .setDimencion(self.__context.getSize())
                                                .setImage('client/assets/imageMenu.jpg'))
        self.Etime = self.addObjectsEvents(TimeElement())
        
    def start(self):
        self.Etime.setTimeActive(5000)
        self.Etime.startTime()
        self.__context.getUiMause().setImage('client/assets/pointb.png').setOffset(UIPUNTER_OFFSET_MIND).setVisibleMouse(False)
    
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
