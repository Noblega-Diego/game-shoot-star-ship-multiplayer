


from client.basicEventUI import EventUI, ListeinerEventUI
from client.models.mShip import MShip
from client.network import LocalMultiplayer, PublicEventPygame
from client.network.network import Data
from client.scenes.lobyScene import LobyScene
from client.uiElements.button import ButtonText


class LobyController(ListeinerEventUI):

    def __init__(self) -> None:
        super().__init__()
        from client.globalContext import GlobalContext
        self.__isSendLogin = False
        self.__context = GlobalContext()
        self.__scene = LobyScene()
        self.__scene.set_listeinerEvent(self)
        self.__scene.setEventUpdate(self.update)
        self.__scene.setEventStart(self.start)
        self.__context.getPartidaContext()['players'] = []

    def start(self):
        self.__context.setMultiplayer(None)
        multiplayer = LocalMultiplayer("localhost",15555).setPublicEvent(PublicEventPygame())
        self.__context.setMultiplayer(multiplayer)
        self.__context.getMultiplayer().start()


    def update(self):
        if(self.__isSendLogin != True):
            if(self.__context.getMultiplayer() is None or self.__context.getMultiplayer().getConnected() is None):
                return
            if (self.__context.getMultiplayer().getConnected().is_conected()):
                print("Conected")
                self.sendLogin()
            else:
                print("No conected")
                last = self.__context.getSceneManager().getLastHistory()
                self.__context.getSceneManager().changeTo(last)
        else:
            players:list[MShip] = self.__context.getPartidaContext()['players']
            listNames = []
            i = 0
            for p in players:
                listNames.append(ButtonText().setText('player: ' +str(p.get_id())).set_pos((50, 50 + i*54)))
                i +=1
            self.__scene.Eusers = listNames

    def handlee_event(self, event: EventUI):
        if (event.equalsTo(self.__scene.EButtonToPartida, "click")):
            self.onListo()

    def getScene(self):
        return self.__scene

    def sendLogin(self):
        self.__isSendLogin = True
        multiplayer = self.__context.getMultiplayer()
        data:Data = {
            'OP': {'type':"OP_ACTIONS_LOGIN"},
            'data':{}
        }
        multiplayer.sendObject(data)

    def onListo(self):
        self.__isSendLogin = True
        multiplayer = self.__context.getMultiplayer()
        data: Data = {
            'OP': {'type': "OP_ACTIONS_CONFIRMPLAYERSTART"},
            'data': {}
        }
        multiplayer.sendObject(data)
