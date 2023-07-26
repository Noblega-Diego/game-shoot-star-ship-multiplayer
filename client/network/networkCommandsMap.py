from client.inputController.command import CommandNetwork
from client.models import MShip


class addPlayer(CommandNetwork):
    def __init__(self):
        super().__init__()
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()

    def ejecute(self):
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

class start(CommandNetwork):
    def __init__(self):
        super().__init__()
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()

    def ejecute(self):
        data = self.getData()
        print("mi data" + str(data))
        self.__context.getPartidaContext()["map"] = data['map']['paredes']
        for users in data['users']:
            for player in self.__context.getPartidaContext()["players"]:
                if(player.get_id() == str(users['id'])):
                    player.set_position((users['pos'][0],users['pos'][1]))
        self.__context.getSceneManager().changeTo("playgame")

class updatePlayer(CommandNetwork):
    def __init__(self):
        super().__init__()
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()

    def ejecute(self):
        data = self.getData()
        print("mi data" + str(data))
        id =data['user']['id']
        pos =data['user']['pos']
        gr =data['user']['gr']
        for player in self.__context.getPartidaContext()["players"]:
            if (player.get_id() == str(id)):
                player.set_position((pos[0], pos[1]))
                player.set_gr(gr)
                break

class updateDisparos(CommandNetwork):
    def __init__(self):
        super().__init__()
        from client.globalContext import GlobalContext
        self.__context = GlobalContext()

    def ejecute(self):
        data = self.getData()
        print("mi data" + str(data))
        id= data["playerId"]
        for player in self.__context.getPartidaContext()["players"]:
            if (player.get_id() == str(id)):
                player.addShoot(data["gr"], data["pos"])

