from client.basicEventUI import ListeinerEventUI, EventUI
from client.manejadorScenas.ManagerScenes import ManagerScenes
from client.scene import Scene, SceneAppendListeiner
from client.scenes.initScene import InitScene;



class InitController(ListeinerEventUI):

    def __init__(self, scene:InitScene, uimanager: ManagerScenes) -> None:
        super().__init__()
        scene.set_listeinerEvent(self)
        self.__scene = scene
        self.__context = uimanager

    def handlee_event(self, event: EventUI):
        if(event.equalsTo(self.__scene.Etime)):
            self.__context.changeTo("home")

    def getScene(self)->Scene:
        return self.__scene
        