import cocos
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.sprite import Sprite
from cocos.scene import Scene
from MainSprite import MainHero


from cocos import mapcolliders
from MainSprite import MainHero


scroller_1 = ScrollingManager()
scroller_2 = ScrollingManager()
scroller_3 = ScrollingManager()


class Level1_Background(ScrollableLayer):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Level1_Background, self).__init__()
    
        bg_1 = cocos.tiles.load("res/maps/level2.tmx")
        self.layer1 = bg_1["MainBg"] 
        self.layer2 = bg_1["TreesBg"]
        self.layer3 = bg_1["Bg stuff"]
        self.layer4 = bg_1["Ground"]
        self.colliders = bg_1["Ground_obj"]
        
    

def get_newgame():
    scene = Scene()
    
    bg_layer = Level1_Background()

    mapcollider = mapcolliders.TmxObjectMapCollider()
    mapcollider.on_bump_handler = mapcollider.on_bump_bounce
    collision_handler = mapcolliders.make_collision_handler(mapcollider, bg_layer.colliders )  

    hero = MainHero(collision_handler)
    scroller_1.add(bg_1.layer1)
    scroller_1.add(bg_1.layer2)
    scroller_1.add(bg_1.layer3)
    scroller_1.add(bg_1.layer4)
    scroller_1.add(hero)
   

    scene.add(scroller_1)
    return scene
