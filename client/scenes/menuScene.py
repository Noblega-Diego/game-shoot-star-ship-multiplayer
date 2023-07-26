

from client.basicEventUI import ElementUI, Update
from client.scene import Scene,SceneAppendListeiner
from client.uiElements.button import Button, ButtonText
from client.utilsElemets.basicBackGround import BasicBackGround
from client.uiElements.uiPunterConst import UIPUNTER_OFFSET_MIND

class MenuScene(SceneAppendListeiner):
    
    def __init__(self):
        super().__init__()
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()
        self.Background = self.addObjectsEvents(BasicBackGround()
                                                .setDimencion(self.__context.getSize())
                                                .setImage('client/assets/imageMenu.jpg'))
        self.EButtonToLoby = self.addObjectsEvents(ButtonText()
                                                .setSize(25)
                                                .set_size([250.,40])
                                                .setText("Play")
                                                .set_pos([50,50]))

        
    def start(self):
        self.__context.getUiMause().setImage(None).setVisibleMouse(True)

    def end(self):
        self.resetInit()

    def event(self, event):
        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, ElementUI)):
                elemts.event(event)

    def update(self):
        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, Update)):
                elemts.update()

    def draw(self, surface):
        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, ElementUI)):
                elemts.draw(surface)

    