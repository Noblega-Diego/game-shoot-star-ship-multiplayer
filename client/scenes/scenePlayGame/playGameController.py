import math
from typing import Tuple, List

from client.basicEventUI import ListeinerEventUI, EventUI
from client.models import MShip
from client.scenes.scenePlayGame.playGameScene import PlayGameScene
from client.sprites import Ship
from client.sprites.Pared import Pared
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
        self.__duracion = 40

    def getSprite(self) -> Shoot:
        return self.__sprite

    def disminuirDuracion(self):
        self.__duracion -=1

    def getDuracion(self):
        return self.__duracion


class PlayGameController(ListeinerEventUI):

    def __init__(self):
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()
        self.__scene = PlayGameScene()
        self.__players:List[Player] = []
        self.__shoots:List[Disparo] = []
        #self.addParticipantes([MShip().set_id("123").set_position((100,100)).set_velocity(10), MShip().set_id("333").set_position((40,100)).set_velocity(2)])
        self.__scene.setUpdate(self.update)
        self.__scene.setStart(self.start)
        file1 = open('mapa/mapa.txt', 'r')
        count = 0
        self.__listParedes = []
        posInitx = 12
        posInity = 12
        posY = posInity
        while True:
            count += 1
            line = file1.readline()
            if not line:
                break
            posX = posInitx
            for x in line:
                if(x == "x"):
                    self.__listParedes.append(Pared().setPos((posX,posY)))
                posX += 24
            #print("Line{}: {}".format(count, line.strip()))
            posY += 24
        self.__scene.setParedes(self.__listParedes)

    def start(self):
        from .partidaInputMap import UiMainInputMap
        players: list[MShip] = self.__context.getPartidaContext().get("players")
        self.addParticipantes(players)
        self.__context.getInputHandler().changeInputMap(UiMainInputMap(self.__players[0]))

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
        for player in self.__players:
            antpos = player.getSprite().getPos()
            antgrados = player.getmShip().get_gr()
            if(player.getmShip().get_pos()[0] < 0):
                player.getmShip().set_position((player.getmShip().get_pos()[0]+ 1200,player.getmShip().get_pos()[1]))
            elif(player.getmShip().get_pos()[0] > 1200):
                player.getmShip().set_position((player.getmShip().get_pos()[0]- 1200,player.getmShip().get_pos()[1]))
            if (player.getmShip().get_pos()[1] < 0):
                player.getmShip().set_position((player.getmShip().get_pos()[0], player.getmShip().get_pos()[1] +840))
            elif (player.getmShip().get_pos()[1] > 840):
                player.getmShip().set_position((player.getmShip().get_pos()[0], player.getmShip().get_pos()[1] -840))
            player.getSprite().setPos(player.getmShip().get_pos())
            player.getSprite().setGr(player.getmShip().get_gr())
            for sh in player.getDisparos():
                self.__shoots.append(sh)
            for p in self.__listParedes:
                if(player.getSprite().detectCollider(p)):
                    player.getSprite().setPos(antpos)
                    player.getmShip().set_position(antpos)
                    player.getSprite().setGr(antgrados)
                    player.getmShip().set_gr(antgrados)

        newShoots = []
        for sh in self.__shoots:
            if(sh.getDuracion() >0):
                sh.disminuirDuracion()
                iscoll = False
                for p in self.__listParedes + [pla.getSprite() for pla in self.__players]:
                    m = sh.getSprite().getMask()
                    sh.getSprite().setTestColor((0, 0, 155))
                    if((not m is None) and p != self.__players[0].getSprite()  and sh.getSprite().detectCollider(p)):
                        iscoll = True
                if(not iscoll):
                    newShoots.append(sh)
        self.__shoots = newShoots
        self.__scene.setShots([sh.getSprite() for sh in self.__shoots])



