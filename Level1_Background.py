import cocos
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.sprite import Sprite
from cocos.scene import Scene
from Level1_Hero import Level1_Hero
from Level1_Monsters import WhiteWolf
from pyglet.window import key
from cocos.director import director
from cocos.scenes.transitions import *

import PauseScene
import Sound


scroller_1 = ScrollingManager()



class Level1_Background(ScrollableLayer):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Level1_Background, self).__init__()

        bg = Sprite('res/maps/level1.png')
        bg.position = bg.width // 2, bg.height // 2

        self.px_width = bg.width
        self.px_height = bg.height
        
        self.add(bg)

    def on_key_press(self, k, m):
         if k == key.P:
            director.push(ZoomTransition(PauseScene.get_pause()))

         if k == key.M:
             Sound.stop() 
        
    

def get_newgame():

    scene = Scene()
    bg_layer = Level1_Background()
    hero = Level1_Hero()
    wolf = WhiteWolf()
    
    Sound.play("res/audio/Level1.mp3")

    scroller_1.add(bg_layer)
    scroller_1.add(hero)
    
   
    scene.add(scroller_1)

    return scene
