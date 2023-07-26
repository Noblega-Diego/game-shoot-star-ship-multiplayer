# template v1.0
import pygame.event

from client.network.multiplayer import PublicEvent
from client.network.network import Data


class NetworkEvents:
    EVENT_HANGUP = pygame.USEREVENT +1
    EVENT_NETWORK = pygame.USEREVENT +2



class PublicEventPygame(PublicEvent):
    def __init__(self):
        super().__init__()

    def public(self, type, data: Data):
        print("event public:" + type)
        print("data:" + str(data))
        event = pygame.event.Event(NetworkEvents.EVENT_NETWORK, data)
        pygame.event.post(event)


