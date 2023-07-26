import math
from typing import Tuple, List

from client.basicEventUI import ListeinerEventUI, EventUI
from client.models import MShip
from client.network import OpMultiplayer
from client.network.network import Data
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
        dis = Disparo(self)
        self.__miDisparos.append(dis)
        return dis

    def getDisparos(self):
        d:List[Disparo] = self.__miDisparos
        self.__miDisparos = []
        return d + [Disparo(self,s.get_pos(),s.get_gr()) for s in self.getmShip().getAllShoot()]


class Disparo:

    def __init__(self, player, pos = None,gr = None):
        self.__player:Player = player
        if(pos is None):
            self.__pos = self.__player.getmShip().get_pos()
        else:
            self.__pos = pos
        if (gr is None):
            self.__gr = self.__player.getmShip().get_gr()
        else:
            self.__gr = gr
        self.__sprite = Shoot(self.__pos, self.__gr)
        self.__duracion = 40

    def getSprite(self) -> Shoot:
        return self.__sprite

    def disminuirDuracion(self):
        self.__duracion -=1

    def getDuracion(self):
        return self.__duracion

    def getPos(self):
        return self.__pos

    def getGr(self):
        return self.__gr


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
        self.__listParedes = []

    def start(self):
        from .partidaInputMap import UiMainInputMap
        players: list[MShip] = self.__context.getPartidaContext().get("players")
        map: list[str] = self.__context.getPartidaContext().get("map")
        print("mi mapa:"+ str(map))
        self.addParticipantes(players)
        self.construirMap(map)
        self.__context.getInputHandler().changeInputMap(UiMainInputMap(self.__players[0]))

    def handlee_event(self, event: EventUI):
        pass

    def getScene(self):
        return self.__scene

    def addParticipantes(self, participantes:list[MShip]):
        self.__players = [Player(mschip,Ship()) for mschip in participantes]
        self.__scene.setShips([player.getSprite() for player in self.__players])

    def construirMap(self, map: list[str]):
        posInitx = 12
        posInity = 12
        posY = posInity
        positions = []
        for f in map:
            posX = posInitx
            for x in f:
                if (x == "x" or x == "x"):
                    positions.append(Pared().setPos((posX,posY)))
                posX += 24
            posY += 24
        self.__listParedes = positions
        self.__scene.setParedes(self.__listParedes)


    def removeParticipant(self, id):
        pass

    def sendUpdateUser(self):

        player = None
        id = self.__context.getPartidaContext()["userId"]
        print( "sendUpdateUser:" + str(id) + "players:" + str(len(self.__players)) )
        for p in self.__players:
            print(p.getmShip().get_id())
            if(p.getmShip().get_id() == id):
                player = p.getmShip()
                break
        data: Data = {
            'OP': {'type':"OP_ACTIONS_MOVEPLAYER"},
            'data':{
                'id':int(player.get_id()),
                'pos':player.get_pos(),
                'gr':player.get_gr()
            }
        }
        print("sendUpdateUser:" + str(data))
        self.__context.getMultiplayer().sendObject(data)

    def update(self):
        if(len(self.__players) > 0):
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
            self.sendUpdateUser()
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



