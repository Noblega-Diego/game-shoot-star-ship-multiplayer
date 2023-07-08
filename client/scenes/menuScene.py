

from client.basicEventUI import ElementUI
from client.scene import Scene,SceneAppendListeiner
from client.uiElements.button import Button


class MenuScene(SceneAppendListeiner):
    
    def __init__(self):
        super().__init__()
        self.EButtonToLoby:Button = self.addObjectsEvents(Button(pos=[10,10], size=[200,40]))
        
    def start(self):
        pass

    def event(self, event):
        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, ElementUI)):
                elemts.event(event)

    def update(self):
        for elemts in self.getObjectsEvents():
            elemts.update()

    def draw(self, surface):
        for elemts in self.getObjectsEvents():
            if (isinstance(elemts, ElementUI)):
                elemts.draw(surface)

    def end(self):
        self.resetInit()

    