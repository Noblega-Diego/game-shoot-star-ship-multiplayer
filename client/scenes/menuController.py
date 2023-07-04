from client.basicEventUI import ListeinerEventUI, EventUI
from client.scene import SceneAppendListeiner;

class MenuController(ListeinerEventUI):

    def __init__(self, menu:SceneAppendListeiner, context) -> None:
        super().__init__()
        menu.set_listeinerEvent(self)

    def handlee_event(self, event: EventUI):
        pass