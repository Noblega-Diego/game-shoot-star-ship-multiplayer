# template v1.0

class MShoot():
    def __init__(self, ship, gr: int, pos: tuple[int,int]):
        self.__gr = gr
        self.__pos = pos
        self.__ship = ship

    def get_pos(self):
        return self.__pos

    def get_gr(self):
        return self.__gr

    def get_ship(self):
        return self.__ship

class MShip():

    def __init__(self):
        self.__position = (0, 0)
        self.__id = None
        self.__velocity = 5
        self.__grados = 0
        self.__newShoots: list[MShoot] = []

    def set_id(self, id:str):
        self.__id = id
        return self

    def get_id(self)->str:
        return self.__id

    def set_position(self, position:tuple[int, int]):
        self.__position = position
        return self

    def get_pos(self) -> tuple[int, int]:
        return self.__position

    def set_velocity(self, velocity:int):
        self.__velocity = velocity
        return self

    def get_velocity(self):
        return self.__velocity

    def set_gr(self, grados):
        self.__grados = grados
        return self

    def get_gr(self):
        return self.__grados

    def addShoot(self, gr:int, pos:tuple[int,int]):
        self.__newShoots.append(MShoot(self,gr,pos))

    def getAllShoot(self):
        shoots = self.__newShoots
        self.__newShoots = []
        return shoots


