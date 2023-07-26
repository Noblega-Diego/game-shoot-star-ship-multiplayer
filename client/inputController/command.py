import abc
from typing import TypeVar, Generic

from pygame.event import Event

from client.network.network import Data


class Command(abc.ABC):
    @abc.abstractmethod
    def ejecute(self):
        pass


T = TypeVar("T")


class CommandExtend(Command, Generic[T], abc.ABC):

    def __init__(self):
        self.__event:T = None

    def addEvent(self, event: T):
        neww = self.__copy(self)
        neww.__event = event
        return neww

    def getEvent(self):
        return self.__event

    def __copy(self, self1) -> Command:
        pass


class CommandCombined(Command):

    def __init__(self):
        self.__listCommand = []

    def addComand(self, command: Command):
        if (not command is None):
            self.__listCommand.append(command)

    def ejecute(self):
        for command in self.__listCommand:
            command.ejecute()

class CommandNetwork(Command):

    def __init__(self):
        self.__data: Data = None

    def getNew(self):
        return self.__class__()

    def setData(self, data:Data) -> Command:
        d = self.getNew()
        d.__data = data
        return d

    def getData(self):
        return self.__data


class CommandExit(Command):

    def __init__(self):
        from client.globalContext import GlobalContext
        self.__context: GlobalContext = GlobalContext()

    def ejecute(self):
        self.__context.getDirectorGame().exit()


class CommandTouch(CommandExtend[Event]):

    def __init__(self):
        super().__init__()
        from client.globalContext import GlobalContext
        self.__context: GlobalContext = GlobalContext()

    def __copy(self):
        return CommandTouch(self.__context)

    def ejecute(self):
        self.__context.getDirectorGame().exit()
