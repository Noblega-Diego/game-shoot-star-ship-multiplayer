
from client.director import DirectorGame
from client.manejadorScenas.ManagerScenes import ManagerScenes
from client.scenes.initController import InitController
from client.scenes.initScene import InitScene
from client.scenes.menuScene import MenuScene
from client.scenes.menuController import MenuController



class UiManager(ManagerScenes):

    def __init__(self, game: DirectorGame) -> None:
        super().__init__(game)
        self._addScene("home", MenuController(MenuScene(), self).getScene())
        self._addScene("inicio", InitController(InitScene(), self).getScene())


    