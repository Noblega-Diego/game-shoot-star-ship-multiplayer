import abc

from .network import Network, Data, Connection
import json
import threading



class PublicEvent(abc.ABC):

    @abc.abstractmethod
    def public(self, param, data:Data):
        pass

class LocalMultiplayer(threading.Thread):
    
    def __init__(self, host:str,port:int):
        super().__init__()
        self.net:Network = Network(host,port)
        self.__conection:Connection = None
        self.__send = False
        self.__publicEvent = None

    def run(self) -> None:
        print("Multiplayer run")
        self.newConect()
        while self.__conection.is_conected():
            print("mmmmmmmmm")
            self.handleGetObject()

    def newConect(self):
        a = self.net.connect()
        self.__conection = a
        print(a)

    def sendObject(self, obj:Data | list[Data]):
        return self.__conection.send(obj)

    def handleGetObject(self):
        data_json = self.__conection.readData()
        print("server:" + str(data_json))
        if(type(data_json) == list):
            for op in data_json:
                if(not self.__publicEvent is None):
                    self.__publicEvent.public(op['OP']['type'], op)

    def setPublicEvent(self,publicEvent: PublicEvent):
        self.__publicEvent = publicEvent
        return self

    def getConnected(self):
        return self.__conection
