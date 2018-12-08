import cocos
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.sprite import Sprite
from cocos.scene import Scene
from cocos.actions import *
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

        lvl2 = Sprite('res/maps/LVL2.png')
        lvl2.position = (420,500)
        lvl2.scale = 0.7
        blink = Blink(10,5)
        lvl2.do(blink)
        self.add(bg)
        self.add(lvl2)
        
    def on_key_press(self, k, m):
        if k == key.P: 
            director.push(ZoomTransition(PauseScene.get_pause()))

        if k == key.M:
             Sound.on_off()
        #це можна видалити, я просто тестив геймовер, цю штуку треба буде поставити коли життів 0 буде в Level2_Hero
        """if k == key.SPACE:
            import GameOver
            director.push(ZoomTransition(GameOver.get_gameover(2)))"""
    

def get_newgame():
    scene = Scene()
    bg_layer = Level2_Background()
    hero = Level2_Hero()
    
    Sound.play("res/audio/Level2.mp3")

    scroller_2.add(bg_layer)
    scroller_2.add(hero)   
   
    scene.add(scroller_2)
    return scene
