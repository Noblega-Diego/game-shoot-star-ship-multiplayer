from client.inputController.command import CommandNetwork
from client.models import MShip


class addPlayer(CommandNetwork):
    def __init__(self):
        super().__init__()
        from client.globalContext import GlobalContext
        self.__context = GlobalContext

    def ejecute(self):
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()
        players: list = self.__context.getPartidaContext()["players"]
        players.append(MShip()
                       .set_id(str(self.getData()['id']))
                       .set_position((self.getData()['pos'][0], self.getData()['pos'][1]))
                       .set_gr(self.getData()['gr']))

class loadUser(CommandNetwork):
    def __init__(self):
        super().__init__()
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()

    def ejecute(self):
        print("mi data" + str(self.getData()))
        self.__context.getPartidaContext()["userId"] = str(self.getData()['id'])
        players: list = self.__context.getPartidaContext()["players"]
        players.append(MShip()
                       .set_id(str(self.getData()['id']))
                       .set_position((self.getData()['pos'][0],self.getData()['pos'][1]))
                       .set_gr(self.getData()['gr']))