from client.basicEventUI import ElementUI, Update
from client.scene import SceneAppendListeiner
from client.uiElements.button import ButtonText
from client.utilsElemets.basicBackGround import BasicBackGround


class LobyScene(SceneAppendListeiner):
    def __init__(self):
        super().__init__()
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()

        self.Background = self.addObjectsEvents(BasicBackGround()
                                                .setDimencion(self.__context.getSize())
                                                .setImage('client/assets/space.png'))
        self.EButtonToPartida = self.addObjectsEvents(ButtonText()
                                                   .setSize(25)
                                                   .set_size([250, 40])
                                                   .setText("Start")
                                                   .set_pos([self.__context.getSize()[0]-260, self.__context.getSize()[1] - 50]))
        self.Eusers:list[ElementUI] = []
        self.__eventUpdate = None
        self.__eventStart = None

    def start(self):
        if (not self.__eventStart is None):
            self.__eventStart()
        self.__context.getUiMause().setImage(None).setVisibleMouse(True)

    def end(self):
        self.resetInit()

    def event(self, event):
        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, ElementUI)):
                elemts.event(event)



    def update(self):
        if(not self.__eventUpdate is None):
            self.__eventUpdate()

        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, Update)):
                elemts.update()

    def draw(self, surface):
        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, ElementUI)):
                elemts.draw(surface)

    def removeElements(self, element):
        self.getObjectsEvents().remove(element)

    def setEventUpdate(self, updateEvent):
        self.__eventUpdate = updateEvent

    def getObjectsEvents(self):
        return super().getObjectsEvents() + self.Eusers

    def setEventStart(self, start):
        self.__eventStart = start
