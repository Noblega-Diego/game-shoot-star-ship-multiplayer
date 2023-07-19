import math
from typing import Tuple, List

from client.basicEventUI import ListeinerEventUI, EventUI
from client.models import MShip
from client.scenes.scenePlayGame.playGameScene import PlayGameScene
from client.sprites import Ship
from client.sprites.Shoot import Shoot


# template v1.0
class Player:
    MOVE_UP = 'up'
    MOVE_LEFT = 'left'
    MOVE_RIGHT = 'right'
    MOVE_DOWN = 'down'

    def __init__(self, mship, sprite):
        self.__mship = mship
        self.__sprite = sprite
        self.__miDisparos = []

    def getmShip(self) ->MShip:
        return self.__mship

    def getSprite(self) -> Ship:
        return self.__sprite

    def change_direccion(self, direccion):
        traslate:Tuple[int,int] = (0,0)
        x, y = self.getmShip().get_pos()
        velocity = self.getmShip().get_velocity()
        if (direccion == self.MOVE_UP):
            traslate = (0, -velocity)
        elif (direccion == self.MOVE_DOWN):
            traslate = (0, velocity)
        elif (direccion == self.MOVE_LEFT):
            traslate = (-velocity, 0)
        elif (direccion == self.MOVE_RIGHT):
            traslate = (velocity, 0)
        self.getmShip().set_position((x + traslate[0], y + traslate[1]))

    def rotate(self, mousePos:Tuple[int,int]):
        posPlayer = self.getmShip().get_pos()
        gr = math.degrees(math.atan2(-mousePos[1] + posPlayer[1], mousePos[0] - posPlayer[0])) - 90
        self.getmShip().set_gr(int(gr))

    def shoot(self):
        self.__miDisparos.append(Disparo(self))
        print(self.__miDisparos)

    def getDisparos(self):
        d:List[Disparo] = self.__miDisparos
        self.__miDisparos = []
        return d


class Disparo:
    def __init__(self, player):
        self.__player:Player = player
        self.__sprite = Shoot(self.__player.getmShip().get_pos(),self.__player.getmShip().get_gr())

    def getSprite(self) -> Shoot:
        return self.__sprite

class PlayGameController(ListeinerEventUI):

    def __init__(self, scene:PlayGameScene):
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()
        self.__scene = scene
        self.__players:List[Player] = []
        self.__shoots:List[Disparo] = []
        self.addParticipantes([MShip().set_id("123").set_position((12,12)).set_velocity(10), MShip().set_id("333").set_position((40,100)).set_velocity(2)])
        self.__scene.setUpdate(self.update)
        self.__scene.setStart(self.start)

    def handlee_event(self, event: EventUI):
        pass

    def getScene(self):
        return self.__scene

    def addParticipantes(self, participantes:list[MShip]):
        self.__players = [Player(mschip,Ship()) for mschip in participantes]
        self.__scene.setShips([player.getSprite() for player in self.__players])

    def removeParticipant(self, id):
        pass

    def update(self):
        print("ss"+ str(len(self.__shoots)))
        for player in self.__players:
            player.getSprite().setPos(player.getmShip().get_pos())
            player.getSprite().setGr(player.getmShip().get_gr())
            for sh in player.getDisparos():
                self.__shoots.append(sh)
        self.__scene.setShots([sh.getSprite() for sh in self.__shoots])


    def start(self):
        from .partidaInputMap import UiMainInputMap
        self.__context.getInputHandler().changeInputMap(UiMainInputMap(self.__players[0]))
