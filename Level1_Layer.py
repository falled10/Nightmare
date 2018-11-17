import cocos
from cocos.director import director
from cocos.scene import Scene

from cocos.layer import Layer
from cocos.sprite import Sprite

__all__ = ['get_newgame']


class Level1_Layer(Layer):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Level1_Layer, self).__init__()
    
        lvl1_bg = Sprite('map/level1.png')

        lvl1_bg.position = lvl1_bg.width // 2, lvl1_bg.height // 2

        self.px_width = lvl1_bg.width
        self.px_height = lvl1_bg.height

        self.add(lvl1_bg)
        
    

def get_newgame():
    scene = Scene()
    scene.add(Level1_Layer())

    return scene
