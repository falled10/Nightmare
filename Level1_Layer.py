import cocos
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.layer import Layer
from pyglet.window import key
from cocos.sprite import Sprite
from MainSprite import MainHero

__all__ = ['get_newgame']


scroller = ScrollingManager()





class Level1_Layer(ScrollableLayer):
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
    hero = MainHero()
   
    scroller.add(Level1_Layer())
    scroller.add(hero)

    scene.add(scroller)

    return scene
