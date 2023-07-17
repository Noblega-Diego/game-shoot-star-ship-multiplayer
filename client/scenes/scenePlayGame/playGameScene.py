from client.basicEventUI import ElementUI, Draw, Update
from client.scene import SceneAppendListeiner
from client.sprites import BasicSpriteGame
from client.uiElements.uiPunterConst import UIPUNTER_OFFSET_MIND
from client.utilsElemets.basicBackGround import BasicBackGround


class PlayGameScene(SceneAppendListeiner):

    def __init__(self):
        super().__init__()
        self.__update = None
        self.__start = None
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()
        self.__ships: list[BasicSpriteGame] = []
        self.__mapa = None
        self.Background = self.addObjectsEvents(BasicBackGround()
                                                .setDimencion((1200, 800))
                                                .setImage('client/assets/imageMenu.jpg'))

    def start(self):
        if (not self.__start is None):
            self.__start()
        self.__context.getUiMause().setImage('client/assets/pointb.png').setOffset \
            (UIPUNTER_OFFSET_MIND).setVisibleMouse(False)

    def event(self, event):
        for elemts in self.__ships + self.getObjectsEvents():
            if (isinstance(elemts, ElementUI)):
                elemts.event(event)
            elif (isinstance(elemts, BasicSpriteGame)):
                elemts.event(event)

    def update(self):
        if(not self.__update is None):
            self.__update()
        for elemts in self.__ships + self.getObjectsEvents():
            if (isinstance(elemts, Update)):
                elemts.update()
            elif (isinstance(elemts, BasicSpriteGame)):
                elemts.update()

    def draw(self, surface):
        for elemts in self.getObjectsEvents() + self.__ships:
            if (isinstance(elemts, Draw)):
                elemts.draw(surface)
            elif (isinstance(elemts, BasicSpriteGame)):
                elemts.draw(surface)

    def end(self):
        self.resetInit()

    def setShips(self, ships:list[BasicSpriteGame]):
        self.__ships = ships

    def setUpdate(self, callback):
        self.__update = callback

    def setStart(self, callback):
        self.__start = callback