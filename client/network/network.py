import socket
from typing import TypedDict
import json
op = TypedDict('OP',{'type':str})
Data = TypedDict('Data', {'OP': op, 'data': dict[str,any]})

class Connection():
    def __init__(self, socket: socket, addr, status):
        self.__addr = addr
        self.__connection = socket
        self.__isConected:bool = status
        self.__out_res = ""

    def __recv(self) -> str:
        res = self.__connection.recv(2048).decode('utf-8')

        if (res.endswith("/end")):
            finalres = self.__out_res + res
            self.__out_res = ''
            return finalres
        else:
            total = (self.__out_res + res).split("/end")
            self.__out_res = total.pop(-1)
            return ('/end'.join(total))

    def send(self, data: Data | list[Data]):
        try:
            self.__connection.sendall(('{}/end'.format(json.dumps(data))).encode('utf-8'))
        except socket.error as e:
            self.__connection.close()

    def readData(self):
        data: str = self.__recv()
        json_data: list[Data] = []
        if data.find('/end') >= 1:
            dall = data.split('/end')
            for j in dall:
                if j != '':
                    l = json.loads(j)
                    for g in l:
                        json_data.append(g)
        return json_data

    def is_conected(self):
        return self.__isConected

    def disconnect(self):
        self.__connection.close()



class Network:

    def __init__(self, host: str, port: int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)

    def connect(self):
        try:
            self.socket.connect(self.addr)
            return Connection(self.socket, self.addr, True)
        except:
            print("not connect")
            return Connection(self.socket, self.addr, False)