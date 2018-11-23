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
from cocos import mapcolliders


scroller = ScrollingManager()


class Level1_Layer():

    def __init__(self):
    
        lvl1_bg = cocos.tiles.load('map/level1.1.tmx')
        self.layer1 = lvl1_bg['Objects']

        
    

def get_newgame():
    bg_layer = Level1_Layer()
    scene = Scene()
    mapcollider = mapcolliders.TmxObjectMapCollider()
    mapcollider.on_bump_handler = mapcollider.on_bump_bounce
    collision_handler = mapcolliders.make_collision_handler(mapcollider, bg_layer.layer1)
    hero = MainHero(collision_handler)
   
    scroller.add(bg_layer.layer1)
    scroller.add(hero)

    scene.add(scroller)

    return scene
