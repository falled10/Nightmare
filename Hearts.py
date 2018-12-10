import cocos
from cocos.layer import ScrollableLayer
from cocos.sprite import Sprite

class Hearts(ScrollableLayer):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Hearts, self).__init__()

        self.sprite = Sprite('res/maps/heart.png')
        
        self.add(self.sprite)
        
        