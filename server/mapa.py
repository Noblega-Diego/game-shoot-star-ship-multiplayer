class Map():
    def getMap(self) -> list[str]:
        pass

    def getPositions(self) -> list[tuple[int, int]]:
        pass


class MapBasic(Map):
    def __init__(self):
        super().__init__()
        self.__basicMap = ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      xxxxxxxxxxxx",
                           "x        x                 x                     x",
                           "x        x                 x                     x",
                           "x        x                 x                     x",
                           "x        x                              A        x",
                           "x                                                x",
                           "x                     A                          x",
                           "x     A                                          x",
                           "x                                                x",
                           "x           x              x                     x",
                           "x           x              x                     x",
                           "x           x              x                     x",
                           "xxxxx       xxxxxxxxx  xxxxxxxxxxxxxx       xxxxxx",
                           "                   xx                             ",
                           "                   xx                             ",
                           "                   xx                             ",
                           "          A        xx          A                  ",
                           "x                  xx                            x",
                           "x                  x                             x",
                           "x                  x                             x",
                           "x    xxxxxxxxx     x                 xxxx        x",
                           "x                  x                 xxxx        x",
                           "x                                    xxxx        x",
                           "x                           xxxxxxxxxxxxx        x",
                           "x                           xxxxxxxxxxxxx        x",
                           "x                                                x",
                           "x                  x                             x",
                           "x                  x                             x",
                           "x                  x                             x",
                           "x        A         x                             x",
                           "x                  x                             x",
                           "x                  x                A            x",
                           "x                  x                             x",
                           "x                  x                             x",
                           "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      xxxxxxxxxxxx"]

    def getMap(self) -> list[str]:
        return self.__basicMap

    def getPositions(self) -> list[tuple[int, int]]:
        posInitx = 12
        posInity = 12
        posY = posInity
        positions = []
        for f in self.__basicMap:
            posX = posInitx
            for x in f:
                if (x == "A"):
                    positions.append((posX, posY))
                posX += 24
            posY += 24
        return positions
