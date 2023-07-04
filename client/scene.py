
from abc import ABC,abstractmethod
class Scene(ABC):

    @abstractmethod
    def event(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, surface):
        pass