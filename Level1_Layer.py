import cocos
import pyglet
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer, ScrollableLayer, ScrollingManager
from cocos.sprite import Sprite
from cocos.actions import Move
from collections import defaultdict
from pyglet.window import key
from MainSprite import MainHero


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
