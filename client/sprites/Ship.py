from pygame import Surface
from .basicSpriteGame import BasicSpriteGame


class Ship(BasicSpriteGame):
    def __init__(self):
        super().__init__()
        self.changeImageDraw('client/assets/sprite_nave.png')\
            .setPos((0,0))

    def event(self, event):
        super().event(event)

    def update(self):
        pass

    def draw(self, surface: Surface):
        super().draw(surface)
