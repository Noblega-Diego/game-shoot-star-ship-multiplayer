import abc
import socket
import threading
import json
from typing import Dict, Tuple, List, TypedDict


class Player():
    def __init__(self):
        self.__pos = None
        self.__id = None
        self.__color = None
        self.__gr = None
        self.__vida = 100

    def set_Pos(self, pos:Tuple[int,int]):
        self.__pos = pos
        return self

    def set_Id(self, id:str):
        self.__id = id
        return self

    def get_pos(self):
        return self.__pos

    def get_id(self):
        return self.__id

    def set_gr(self, gr):
        self.__gr = gr
        return  self

    def get_gr(self):
        return self.__gr

    def set_vida(self, vida):
        self.__vida = vida
        return self

    def get_vida(self):
        return self.__vida

PARTIDA_STATUS_ROOM = "PARTIDA_STATUS_ROOM"
PARTIDA_STATUS_ACTIVE = "PARTIDA_STATUS_ACTIVE"

OP_ACTIONS_LOGIN = "OP_ACTIONS_LOGIN"
OP_SEND_ACCEPT = "OP_SEND_ACCEPT"
OP_SEND_ADDUSER = "OP_SEND_ADDUSER"
OP_ACTIONS_CONFIRMPLAYERSTART = "OP_ACTIONS_CONFIRMPLAYERSTART"
OP_SEND_START = "OP_SEND_START"
OP_ACTIONS_MOVEPLAYER = "OP_ACTIONS_MOVEPLAYER"
OP_SEND_UPDATEPLAYER = "OP_SEND_UPDATEPLAYER"
OP_ACTIONS_KILLPLAYER = "OP_ACTIONS_KILLPLAYER"
OP_ACTIONS_EXITLAYER = "OP_ACTIONS_EXITLAYER"
OP_SEND_KILLPLAYER = "OP_SEND_KILLPLAYER"
OP_SEND_END = "OP_SEND_END"
OP_SEND_EXIT = "OP_SEND_EXIT"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addres = ('localhost', 15555)

sock.bind(server_addres) #le damos el puerto y la direccion ip
op = TypedDict('OP',{'type':str})
UserType = TypedDict('UserType', {'id': int,'conexion': socket.socket, 'player': Player | None, 'middlemessages': str, 'confirm': bool})
Data = TypedDict('Data', {'OP': op, 'data': dict[str,any]})

list_users:Dict[int,UserType] = dict()
list_conexionesProcess = []
partida = {
    'status': PARTIDA_STATUS_ROOM,
    'jugadores':[]
}
def getUser(id: int):
    return list_users[id]
def createSendData(data:List[Data]):
    return ('{}/end'.format(json.dumps(data))).encode('utf-8')

def recv(userConnection:UserType) -> str:
    res = userConnection['conexion'].recv(2048).decode('utf-8')

    if (res.endswith("/end")):
        finalres = userConnection['middlemessages'] + res
        userConnection['middlemessages'] = ''
        return finalres
    else:
        total = (userConnection['middlemessages'] + res).split("/end")
        userConnection['middlemessages'] = total.pop(-1)
        return ('/end'.join(total))
def readData(userConnection:UserType):
    data: str = recv(userConnection)
    #data = data.replace("'","\"")
    print("request:" +data)
    json_data:list[Data] = []
    if data.find('/end') >= 1:
        dall = data.split('/end')
        for j in dall:
            print('indall[j]'+ j)
            if j != '':
                # print('{}>{}'.format(id,j))
                l = json.loads(j)
                if(isinstance(l, list)):
                    for g in l:
                        json_data.append(g)
                else:
                    json_data.append(l)
    print("json_data:" + str(json_data))
    return json_data

class Command(abc.ABC):
    @abc.abstractmethod
    def ejecute(self):
        pass

class CommandLogin(Command):
    def __init__(self,message: Data, user:UserType, listAllUsers:list[Dict[int,UserType]]):
        self.__user = user
        self.__listAllUsers = listAllUsers
        self.__message = message

    def ejecute(self):
        print("ejecute:"+str(self.__class__))
        conexion = self.__user['conexion']
        messages:list[Data] = []
        self.__user['player'] = Player().set_Id(str(self.__user["id"])).set_vida(100).set_gr(0).set_Pos((0,0))
        op_accept: Data = \
            {
                'OP': {
                    'type': OP_SEND_ACCEPT
                },
                'data': {
                    'id': id,
                    'vida': list_users[id]['player'].get_vida(),
                    'pos': list_users[id]["player"].get_pos(),
                    'gr': list_users[id]["player"].get_gr()
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
                    'vida': list_users[id]['player'].get_vida(),
                    'pos': list_users[id]["player"].get_pos(),
                    'gr': list_users[id]["player"].get_gr()
                }
            }
        for id_user, user in self.__listAllUsers[0].items():
            if (id_user != id):
                user['conexion'].sendall(createSendData([op_sendUser]))  # enviamos el nuevo jugador a los demas usuarios
                op_newUser:Data = \
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
        conexion.sendall(createSendData(messages))

class CommandConfirm(Command):
    def __init__(self, message: Data, user:UserType, listAllUsers:list[Dict[int,UserType]]):
        self.__user = user
        self.__listAllUsers = listAllUsers[0]
        self.__message = message

    def ejecute(self):
        self.__user['confirm'] = True
        allConfirm = True
        for id_user, user in self.__listAllUsers.items():
            if(user["confirm"] == False):
                allConfirm = False
                break
        for id_user, user in self.__listAllUsers.items():
            messages: list[Data] = []
            accept: Data = {"OP": {'type':OP_SEND_ACCEPT},
                              "data": {"id":user["id"]}}
            messages.append(accept)
            if(allConfirm):
                init: Data = {"OP": {'type': OP_SEND_START},
                                  "data": {}}
                messages.append(init)
            user["conexion"].sendall(createSendData(messages))





class MapEvent(object):

    def __init__(self, user:UserType, listAllUsers:list[Dict[int,UserType]]):
        self.__user = user
        self.__listAllUsers = listAllUsers
        self.list:dict[str, Command.__class__] = {
            OP_ACTIONS_LOGIN: CommandLogin,
            OP_ACTIONS_CONFIRMPLAYERSTART: CommandConfirm,
            OP_ACTIONS_MOVEPLAYER: CommandConfirm,
            OP_ACTIONS_KILLPLAYER: CommandConfirm
        }

    def getCommand(self, acction:str, message:Data) -> Command:
        return self.list[acction](message = message,user = self.__user, listAllUsers = self.__listAllUsers)

def login(conexion, id):
    mess_login:Data = {'OP': {
        'type': OP_SEND_ACCEPT
    },'data':{}}
    conexion.sendall(createSendData([mess_login]))

def exitPlayer(conexion, id):
    conexion.sendall([{
        'OP': {
            'type': OP_SEND_EXIT
        },
        'data': {}
    }])
    conexion.close()
    list_users.pop(id)

def atenderPlayer(conexion, id):
    if(partida['status'] != PARTIDA_STATUS_ROOM):
        exitPlayer(conexion,id)
        return
    eventHandle = MapEvent(getUser(id), [list_users])
    try:
        while True:
            print("ss")
            allMessages = readData(getUser(id))
            print(allMessages)
            for message in allMessages:
                eventHandle.getCommand(message["OP"]["type"],message).ejecute()
    except (RuntimeError, TypeError, NameError) as e:
        print(e)
        print('mensaje no enviado')
    finally:
        print('conexion finalizada: {}'.format(id))
        conexion.close()
        it = list_users.pop(id)

        res = [{'OP': {
            'type': 'QUITPLAYER',
            },
            'data':{}
        }]
        for id_user, user in list_users.items():
            if (id_user != id):
                user[0].sendall(createSendData(res))




sock.listen(1) #En espera a una conexion
increment = 10000
while True:
    try:
        print('Esperando conexion')
        conexion, client_adress = sock.accept()
        print('conectado con :', client_adress)
        id = increment
        user: UserType = {"id": id,"conexion": conexion, "confirm": False, "player": None, "middlemessages": ""}
        list_users[id] = user
        connect = threading.Thread(target=atenderPlayer, args=[conexion, id])
        list_conexionesProcess.append(connect)
        increment += 1
        connect.start()
    except:
        sock.close()
        break

