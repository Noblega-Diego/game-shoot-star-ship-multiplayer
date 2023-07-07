from client.basicEventUI import ListeinerEventUI, EventUI
from client.scene import Scene
from client.scenes.menuScene import MenuScene



class MenuController(ListeinerEventUI):

    def __init__(self, menu:MenuScene, uimanager) -> None:
        super().__init__()
        menu.set_listeinerEvent(self)
        self.__scene = menu
        self.__context = uimanager

    def handlee_event(self, event: EventUI):
        pass

    def getScene(self)->Scene:
        return self.__scene
        