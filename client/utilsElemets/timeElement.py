from client.basicEventUI import ElementActive
from client.utils.Temporizador import Temporizar


class TimeElement(ElementActive):
    def __init__(self):
        super().__init__()
        self.__timeActive = -1
        self.__temporizar = Temporizar()
        self.__active = False

    def update(self):
        print(self.__active)
        print(self.__timeActive)
        print(self.__temporizar.getStatus())
        if ((not self.__active) and (self.__timeActive > 0) and (self.__timeActive < self.__temporizar.getStatus())):
            self.__active = True
            self._lunchEvent("Ftime")

    def setTimeActive(self, time):
        self.__timeActive = time
        return self

    def startTime(self):
        self.__temporizar.resetTime()
        self.__active = False
        return self

