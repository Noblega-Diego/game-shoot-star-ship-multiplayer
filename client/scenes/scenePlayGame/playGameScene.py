from client.basicEventUI import ElementUI, Draw
from client.scene import SceneAppendListeiner
from client.uiElements.uiPunterConst import UIPUNTER_OFFSET_MIND


class PlayGameScene(SceneAppendListeiner):

    def __init__(self):
        super().__init__()
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()
        self.__players = [{'player': None, 'sprite': None}]
        self.__mapa = None
    def start(self):
        self.__context.getUiMause().setImage('client/assets/pointb.png').setOffset \
            (UIPUNTER_OFFSET_MIND).setVisibleMouse(False)

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
