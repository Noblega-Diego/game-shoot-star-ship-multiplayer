

from client.basicEventUI import ElementUI, Update
from client.scene import Scene,SceneAppendListeiner
from client.uiElements.button import Button, ButtonText
from client.utilsElemets.basicBackGround import BasicBackGround


class MenuScene(SceneAppendListeiner):
    
    def __init__(self):
        super().__init__()
        self.Background = self.addObjectsEvents(BasicBackGround()
                                                .setDimencion((1200,800))
                                                .setImage('client/assets/imageMenu.jpg'))
        self.EButtonToLoby = self.addObjectsEvents(ButtonText()
                                                .setSize(25)
                                                .set_size([250.,40])
                                                .setText("Play")
                                                .set_pos([50,50]))
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()
        
    def start(self):
        self.__context.getUiMause().setImage('client/assets/imageMenu.jpg')

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

    def end(self):
        self.resetInit()

    