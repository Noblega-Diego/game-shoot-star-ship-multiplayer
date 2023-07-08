from client.basicEventUI import ListeinerEventUI, EventUI
from client.manejadorScenas.ManagerScenes import ManagerScenes
from client.scene import Scene
from client.scenes.menuScene import MenuScene



class MenuController(ListeinerEventUI):

    def __init__(self, menu:MenuScene, uimanager:ManagerScenes) -> None:
        super().__init__()
        menu.set_listeinerEvent(self)
        self.__scene = menu
        self.__context = uimanager

    def handlee_event(self, event: EventUI):
        if(event.equalsTo(self.__scene.EButtonToLoby, "click")):
            self.__context.changeTo('inicio')

    def getScene(self)->Scene:
        return self.__scene
        