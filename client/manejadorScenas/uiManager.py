from client.basicEventUI import ListeinerEventUI
from client.director import DirectorGame
from client.manejadorScenas.ManagerScenes import ManagerScenes
from client.scene import Scene
from client.scenes.initController import InitController
from client.scenes.lobyController import LobyController
from client.scenes.menuController import MenuController
from client.scenes.scenePlayGame.playGameController import PlayGameController


class UiManager(ManagerScenes):


    def __init__(self, game: DirectorGame) -> None:
        super().__init__(game)
        self._addScene("home", MenuController)
        self._addScene("inicio", InitController)
        self._addScene("loby", LobyController)
        self._addScene("playgame", PlayGameController)

    def getScene(self, name: str) -> Scene:
        controller = self.getAll()[name]
        return controller().getScene()
    