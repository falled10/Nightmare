import cocos
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.sprite import Sprite
from cocos.scene import Scene



class PauseScene(ColorLayer):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Level1_Background, self).__init__()
    
        lvl1_bg = Sprite('res/maps/level1.png')

        lvl1_bg.position = lvl1_bg.width // 2, lvl1_bg.height // 2

        self.px_width = lvl1_bg.width
        self.px_height = lvl1_bg.height

        self.add(lvl1_bg)
        
    

def get_newgame():
  
    scene = Scene()
    hero = MainHero()
   
    scroller_1.add(Level1_Background())
    scroller_1.add(hero)

    scene.add(scroller_1)

    return scene