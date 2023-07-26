from client.basicEventUI import ListeinerEventUI, EventUI

from client.scene import Scene
from client.scenes.menuScene import MenuScene



class MenuController(ListeinerEventUI):

    def __init__(self) -> None:
        super().__init__()
        self.__scene = MenuScene()
        self.__scene.set_listeinerEvent(self)
        from client.globalContext import GlobalContext
        self.__context:GlobalContext = GlobalContext()

    def handlee_event(self, event: EventUI):
        if(event.equalsTo(self.__scene.EButtonToLoby, "click")):
            self.__context.getSceneManager().changeTo('loby')

    def getScene(self)->Scene:
        return self.__scene
        