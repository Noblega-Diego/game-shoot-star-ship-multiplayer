from client.basicEventUI import ListeinerEventUI, EventUI

from client.scene import Scene
from client.scenes.initScene import InitScene



class InitController(ListeinerEventUI):

    def __init__(self) -> None:
        super().__init__()
        self.__scene = InitScene()
        self.__scene.set_listeinerEvent(self)
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()

    def handlee_event(self, event: EventUI):
        if(event.equalsTo(self.__scene.Etime)):
            self.__context.getSceneManager().changeTo("home")

    def getScene(self)->Scene:
        return self.__scene
        