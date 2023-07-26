from client.inputController.command import CommandNetwork
from client.inputController.inputHandler import InputMap, EventInput
from client.network import OpMultiplayer
from client.network.PublicEventPygame import NetworkEvents
from client.network import networkCommandsMap


class NetworkMap(InputMap):

    def __init__(self):
        self.__mapComand: dict[EventInput, CommandNetwork] = {
            EventInput("event", OpMultiplayer.OP_ADDUSER, NetworkEvents.EVENT_NETWORK): networkCommandsMap.addPlayer(),
            EventInput("event", OpMultiplayer.OP_ACCEPT, NetworkEvents.EVENT_NETWORK): networkCommandsMap.loadUser(),
            EventInput("event", OpMultiplayer.OP_START, NetworkEvents.EVENT_NETWORK): networkCommandsMap.start(),
            EventInput("event", OpMultiplayer.OP_UPDATEPLAYER, NetworkEvents.EVENT_NETWORK): networkCommandsMap.updatePlayer(),
            EventInput("event", OpMultiplayer.OP_SHOOT,NetworkEvents.EVENT_NETWORK): networkCommandsMap.updateDisparos(),
        }

    def getMapInputs(self) -> dict[EventInput, CommandNetwork]:
        return self.__mapComand




