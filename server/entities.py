from typing import Tuple


class Player():
    def __init__(self):
        self.__pos = None
        self.__id = None
        self.__color = None
        self.__gr = None
        self.__vida = 100

    def set_Pos(self, pos: Tuple[int, int]):
        self.__pos = pos
        return self

    def set_Id(self, id: str):
        self.__id = id
        return self

    def get_pos(self):
        return self.__pos

    def get_id(self):
        return self.__id

    def set_gr(self, gr):
        self.__gr = gr
        return self

    def get_gr(self):
        return self.__gr

    def set_vida(self, vida):
        self.__vida = vida
        return self

    def get_vida(self):
        return self.__vida
