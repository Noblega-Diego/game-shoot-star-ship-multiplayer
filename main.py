
from client.game import Game
from client.scenes.menu import Menu
def main():
    game = Game()
    game.changeScene(Menu())
    game.start()

if (__name__ == "__main__"):
    main()