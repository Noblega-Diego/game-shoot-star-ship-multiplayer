# template v1.0

class MShip():

    def __init__(self):
        self.__position = (0, 0)
        self.__id = None
        self.__velocity = 1

    def set_id(self, id:str):
        self.__id = id
        return self

    def get_id(self):
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