
from client.game import Game
from client.manejadorScenas.uiManager import UiManager
from client.scenes.menuScene import MenuScene
from client.scenes.menuController import MenuController

def main():
    game = Game()
    manager = UiManager(game)
    manager.changeTo('inicio')
    game.start()

if (__name__ == "__main__"):
    main()