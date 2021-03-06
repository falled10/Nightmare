import cocos
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.sprite import Sprite
from cocos.scene import Scene
from Level3_Hero import Level3_Hero
from pyglet.window import key
from cocos.actions import *
from cocos.director import director
from cocos.scenes.transitions import *
import Sound
import PauseScene


scroller_3 = ScrollingManager()


class Level3_Background(ScrollableLayer):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Level3_Background, self).__init__()

        bg = Sprite('res/maps/Level3/level3.png')

        bg.position = bg.width // 2, bg.height // 2

        self.px_width = bg.width
        self.px_height = bg.height

        self.add(bg)

        lvl3 = Sprite('res/maps/Level3/LVL3.png')
        lvl3.position = (420,500)
        lvl3.scale = 0.7
        blink = Blink(10,3)
        lvl3.do(blink)
        self.add(lvl3)
   
    def on_key_press(self, k, m):
        if k == key.P: 
            director.push(ZoomTransition(PauseScene.get_pause()))
        
        if k == key.M:
             Sound.on_off()

def get_newgame():
    scene = Scene()
    bg_layer = Level3_Background()
    hero = Level3_Hero()
    
    Sound.play("res/audio/Level3.mp3")

    scroller_3.add(bg_layer)
    scroller_3.add(hero)   
   
    scene.add(scroller_3)
    return scene
