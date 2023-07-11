


from client.basicEventUI import EventUI, ListeinerEventUI
from client.scenes.lobyScene import LobyScene


class LobyController(ListeinerEventUI):

    def __init__(self, scene:LobyScene) -> None:
        super().__init__()

    def handlee_event(self, event: EventUI):
        pass

    def getScene(self):
        pass

    