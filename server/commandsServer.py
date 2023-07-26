import abc
from typing import Dict, TypedDict
from .variables import OP_ACTIONS_LOGIN, OP_SEND_ACCEPT, OP_SEND_ADDUSER, OP_ACTIONS_CONFIRMPLAYERSTART, OP_SEND_START, \
    OP_ACTIONS_MOVEPLAYER, OP_ACTIONS_SHOOT, OP_SEND_UPDATEPLAYER, OP_SEND_SHOOT
from .entities import Player
from .serverTypes import UserType, Data
from .mapa import MapBasic


class Command(abc.ABC):
    @abc.abstractmethod
    def ejecute(self):
        pass


class CommandLogin(Command):
    def __init__(self, message: Data, user: UserType, listAllUsers: list[Dict[int, UserType]], server):
        self.__user = user
        self.__listAllUsers = listAllUsers[0]
        self.__message = message
        self.__server = server

    def ejecute(self):
        print("ejecute:" + str(self.__class__))
        conexion = self.__user['conexion']
        messages: list[Data] = []
        self.__user['player'] = Player().set_Id(str(self.__user["id"])).set_vida(100).set_gr(0).set_Pos((0, 0))
        id = self.__user["id"]
        op_accept: Data = \
            {
                'OP': {
                    'type': OP_SEND_ACCEPT
                },
                'data': {
                    'id': id,
                    'vida': self.__listAllUsers[id]['player'].get_vida(),
                    'pos': self.__listAllUsers[id]["player"].get_pos(),
                    'gr': self.__listAllUsers[id]["player"].get_gr(),
                }
            }
        messages.append(op_accept)
        op_sendUser: Data = \
            {
                'OP': {
                    'type': OP_SEND_ADDUSER
                },
                'data': {
                    'id': id,
                    'vida': self.__listAllUsers[id]['player'].get_vida(),
                    'pos': self.__listAllUsers[id]["player"].get_pos(),
                    'gr': self.__listAllUsers[id]["player"].get_gr()
                }
            }
        for id_user, user in self.__listAllUsers.items():
            if (id_user != id):
                user['conexion'].sendall(
                    self.__server.createSendData([op_sendUser]))  # enviamos el nuevo jugador a los demas usuarios
                op_newUser: Data = \
                    {
                        'OP': {
                            'type': OP_SEND_ADDUSER
                        },
                        'data': {
                            'id': id_user,
                            'vida': user["player"].get_vida(),
                            'pos': user["player"].get_pos(),
                            'gr': user["player"].get_gr()
                        }
                    }
                messages.append(op_newUser)
        conexion.sendall(self.__server.createSendData(messages))


class CommandConfirm(Command):
    def __init__(self, message: Data, user: UserType, listAllUsers: list[Dict[int, UserType]], server):
        self.__user = user
        self.__listAllUsers = listAllUsers[0]
        self.__message = message
        self.__server = server

    def ejecute(self):
        self.__user['confirm'] = True
        allConfirm = True
        print("sssssssssssssss")
        for id_user, user in self.__listAllUsers.items():
            if (user["confirm"] == False):
                allConfirm = False
                break

        if (allConfirm):
            map = MapBasic()
            i = 0
            for id_user, user in self.__listAllUsers.items():
                user["player"].set_Pos(map.getPositions()[i])
            users = [{'id': u["id"],
                      'vida': u["player"].get_vida(),
                      'pos': u["player"].get_pos(),
                      'gr': u["player"].get_gr()
                      } for id, u in self.__listAllUsers.items()]
            paredes = map.getMap()
            for id_user, user in self.__listAllUsers.items():
                messages: list[Data] = []
                init: Data = {"OP": {'type': OP_SEND_START},
                              "data": {
                                  'map': {
                                      'paredes': paredes
                                  },
                                  'users': users
                              }}
                messages.append(init)
                i += 1
                user["conexion"].sendall(self.__server.createSendData(messages))


class CommandShootPlayer(Command):
    def __init__(self, message: Data, user: UserType, listAllUsers: list[Dict[int, UserType]], server):
        self.__user = user
        self.__listAllUsers = listAllUsers[0]
        self.__message = message
        self.__server = server

    def ejecute(self):
        print("::" + str(self.__class__) + " message:" + str(self.__message) + "len users:" + str(len(self.__listAllUsers.items())))
        datareq =self.__message['data']
        player = self.__listAllUsers[datareq["playerId"]]
        print("id" + str(id))
        for id_user, user in self.__listAllUsers.items():
            print("sssssid" + str(user["player"].get_id()))
            if(str(user["player"].get_id()) != str(id)):
                print(user)
                data: Data = {"OP": {'type': OP_SEND_SHOOT},
                              "data": datareq}
                user['conexion'].sendall(self.__server.createSendData([data]))

class CommandMovePlayer(Command):
    def __init__(self, message: Data, user: UserType, listAllUsers: list[Dict[int, UserType]], server):
        self.__user = user
        self.__listAllUsers = listAllUsers[0]
        self.__message = message
        self.__server = server

    def ejecute(self):
        print("::" + str(self.__class__) + " message:" + str(self.__message) + "len users:" + str(len(self.__listAllUsers.items())))
        datareq =self.__message['data']
        player = self.__listAllUsers[datareq["id"]]
        player["player"].set_Pos(datareq["pos"])
        player["player"].set_gr(datareq["gr"])
        id = datareq["id"]
        print("id" + str(id))
        for id_user, user in self.__listAllUsers.items():
            print("sssssid" + str(user["player"].get_id()))
            if(str(user["player"].get_id()) != str(id)):
                print(user)
                data: Data = {"OP": {'type': OP_SEND_UPDATEPLAYER},
                              "data": {
                                  "user":{
                                  "pos": player["player"].get_pos(),
                                  "id": player["player"].get_id(),
                                  "gr": player["player"].get_gr()}
                              }}
                user['conexion'].sendall(self.__server.createSendData([data]))


class MapEvent(object):

    def __init__(self, server, user: UserType, listAllUsers: list[Dict[int, UserType]]):
        self.__user = user
        self.__listAllUsers = listAllUsers
        self.__server = server
        self.list: dict[str, Command.__class__] = {
            OP_ACTIONS_LOGIN: CommandLogin,
            OP_ACTIONS_CONFIRMPLAYERSTART: CommandConfirm,
            OP_ACTIONS_MOVEPLAYER: CommandMovePlayer,
            OP_ACTIONS_SHOOT: CommandShootPlayer,
        }

    def getCommand(self, acction: str, message: Data) -> Command:
        return self.list[acction](server = self.__server ,message=message, user=self.__user, listAllUsers=self.__listAllUsers)
