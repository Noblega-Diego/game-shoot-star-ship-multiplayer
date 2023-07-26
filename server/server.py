import socket
import threading
import json
from typing import Dict, List

from .commandsServer import MapEvent
from .serverTypes import UserType, Data
from .variables import PARTIDA_STATUS_ROOM, OP_SEND_ACCEPT, OP_SEND_EXIT

  # le damos el puerto y la direccion ip


list_conexionesProcess = []
partida = {
    'status': PARTIDA_STATUS_ROOM,
    'jugadores': []
}

class Server():
    def __init__(self):
        self.list_users: Dict[int, UserType] = dict()

    def start(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addres = ('localhost', 15555)
        self.__socket.bind(server_addres)
        self.__run()

    def __run(self):
        self.__socket.listen(1)  # En espera a una conexion
        increment = 10000
        while True:
            try:
                print('Esperando conexion')
                conexion, client_adress = self.__socket.accept()
                print('conectado con :', client_adress)
                id = increment
                user: UserType = {"id": id, "conexion": conexion, "confirm": False, "player": None,
                                  "middlemessages": ""}
                self.list_users[id] = user
                connect = threading.Thread(target=self.atenderPlayer, args=[conexion, id])
                list_conexionesProcess.append(connect)
                increment += 1
                connect.start()
            except:
                self.__socket.close()
                break

    def getUser(self,id: int):
        return self.list_users[id]

    def createSendData(self,data: List[Data]):
        return ('{}/end'.format(json.dumps(data))).encode('utf-8')


    def recv(self,userConnection: UserType) -> str:
        res = userConnection['conexion'].recv(2048).decode('utf-8')

        if (res.endswith("/end")):
            finalres = userConnection['middlemessages'] + res
            userConnection['middlemessages'] = ''
            return finalres
        else:
            total = (userConnection['middlemessages'] + res).split("/end")
            userConnection['middlemessages'] = total.pop(-1)
            return ('/end'.join(total))

    def readData(self,userConnection: UserType):
        data: str = self.recv(userConnection)
        # data = data.replace("'","\"")
        print("request:" + data)
        json_data: list[Data] = []
        if data.find('/end') >= 1:
            dall = data.split('/end')
            for j in dall:
                print('indall[j]' + j)
                if j != '':
                    # print('{}>{}'.format(id,j))
                    l = json.loads(j)
                    if (isinstance(l, list)):
                        for g in l:
                            json_data.append(g)
                    else:
                        json_data.append(l)
        print("json_data:" + str(json_data))
        return json_data


    def login(self,conexion, id):
        mess_login: Data = {'OP': {
            'type': OP_SEND_ACCEPT
        }, 'data': {}}
        conexion.sendall(self.createSendData([mess_login]))


    def exitPlayer(self, conexion, id):
        conexion.sendall([{
            'OP': {
                'type': OP_SEND_EXIT
            },
            'data': {}
        }])
        conexion.close()
        self.list_users.pop(id)

    def atenderPlayer(self, conexion, id):
        if (partida['status'] != PARTIDA_STATUS_ROOM):
            self.exitPlayer(conexion, id)
            return
        eventHandle = MapEvent( self ,self.getUser(id), [self.list_users])
        try:
            while True:
                print("ss")
                allMessages = self.readData(self.getUser(id))
                print(allMessages)
                for message in allMessages:
                    eventHandle.getCommand(message["OP"]["type"], message).ejecute()
        except (RuntimeError, TypeError, NameError) as e:
            print(e)
            print('mensaje no enviado')
        finally:
            print('conexion finalizada: {}'.format(id))
            conexion.close()
            it = self.list_users.pop(id)

            res = [{'OP': {
                'type': 'QUITPLAYER',
            },
                'data': {}
            }]
            for id_user, user in self.list_users.items():
                if (id_user != id):
                    user["conexion"].sendall(self.createSendData(res))



