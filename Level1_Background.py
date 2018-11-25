import cocos
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.sprite import Sprite
from cocos.scene import Scene
from Level1_Hero import Level1_Hero
from Level1_Monsters import WhiteWolf



scroller_1 = ScrollingManager()
scroller_2 = ScrollingManager()
scroller_3 = ScrollingManager()


class Level1_Background(ScrollableLayer):
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
    bg_layer = Level1_Background()
    hero = Level1_Hero()
    wolf = WhiteWolf()
    
    scroller_1.add(bg_layer)
    scroller_1.add(hero)  
   
    scene.add(scroller_1)
    return scene
