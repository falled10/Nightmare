import cocos
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.sprite import Sprite
from cocos.scene import Scene
from Level3_Hero import Level3_Hero
from pyglet.window import key
from cocos.director import director
from cocos.scenes.transitions import *
import Sound
import PauseScene


scroller_3 = ScrollingManager()


class Level3_Background(ScrollableLayer):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Level3_Background, self).__init__()

        bg = Sprite('res/maps/level3.png')

        bg.position = bg.width // 2, bg.height // 2

        self.px_width = bg.width
        self.px_height = bg.height

        self.add(bg)
        
    def on_key_press(self, k, m):
        if k == key.P: 
            director.push(ZoomTransition(PauseScene.get_pause()))
    

def get_newgame():
    scene = Scene()
    bg_layer = Level3_Background()
    hero = Level3_Hero()
    
    Sound.play("res/audio/Level3.mp3")

    scroller_3.add(bg_layer)
    scroller_3.add(hero)   
   
    scene.add(scroller_3)
    return scene