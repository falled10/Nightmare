import cocos
from cocos.layer import ScrollableLayer, ScrollingManager, MultiplexLayer, Layer
from cocos.sprite import Sprite
from cocos.actions import *
from cocos.scene import Scene
from Level1_Hero import Level1_Hero
from pyglet.window import key
from cocos.director import director
from cocos.scenes.transitions import *
from cocos.text import Label

import PauseScene
import Sound



scroller_1 = ScrollingManager()



class Level1_Background(ScrollableLayer):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Level1_Background, self).__init__()
        
        bg = Sprite('res/maps/Level1/level1.png')
        bg.position = bg.width // 2, bg.height // 2

        lvl1 = Sprite('res/maps/Level1/LVL1.png')
        lvl1.position = (420,500)
        lvl1.scale = 0.7
        blink = Blink(10,3)
        lvl1.do(blink)
        self.px_width = bg.width
        self.px_height = bg.height
        
        self.add(bg)
        self.add(lvl1)

    def on_key_press(self, k, m):
         if k == key.P:
            director.push(ZoomTransition(PauseScene.get_pause()))
            
         if k == key.M:
             Sound.on_off()
             
    



def get_newgame():

    scene = Scene()
    bg_layer = Level1_Background()
    hero = Level1_Hero()
    
    Sound.play("res/audio/Level1.mp3")

    scroller_1.add(bg_layer)
   
    scroller_1.add(hero)
    
    scene.add(scroller_1)

    return scene
