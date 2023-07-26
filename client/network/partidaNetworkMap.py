from client.inputController.command import CommandNetwork
from client.inputController.inputHandler import InputMap, EventInput
from client.network import OpMultiplayer
from client.network.PublicEventPygame import NetworkEvents
from client.network.networkCommandsMap import addPlayer, loadUser


class NetworkMap(InputMap):

    def __init__(self):
        self.__mapComand: dict[EventInput, CommandNetwork] = {
            EventInput("event", OpMultiplayer.OP_ADDUSER, NetworkEvents.EVENT_NETWORK): addPlayer(),
            EventInput("event", OpMultiplayer.OP_ACCEPT, NetworkEvents.EVENT_NETWORK): loadUser(),
        }

    def getMapInputs(self) -> dict[EventInput, CommandNetwork]:
        return self.__mapComand




