import cocos
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.sprite import Sprite
from cocos.scene import Scene
from Level2_Hero import Level2_Hero
from pyglet.window import key
from cocos.director import director
from cocos.scenes.transitions import *
import Sound
import PauseScene


scroller_2 = ScrollingManager()

class Level2_Background(ScrollableLayer):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Level2_Background, self).__init__()

        bg = Sprite('res/maps/level2.png')

        bg.position = bg.width // 2, bg.height // 2

        self.px_width = bg.width
        self.px_height = bg.height

        self.add(bg)
        
    def on_key_press(self, k, m):
        if k == key.P: 
            director.push(ZoomTransition(PauseScene.get_pause()))

def get_newgame():
    scene = Scene()
    bg_layer = Level2_Background()
    hero = Level2_Hero()
    
    Sound.play("res/audio/Level2.mp3")

    scroller_2.add(bg_layer)
    scroller_2.add(hero)   
   
    scene.add(scroller_2)
    return scene