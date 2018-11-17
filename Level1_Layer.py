import cocos
import pyglet
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer, ScrollableLayer, ScrollingManager
from cocos.sprite import Sprite
from cocos.actions import Move
from collections import defaultdict
from pyglet.window import key



class Level1_Layer(ScrollableLayer):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Level1_Layer, self).__init__()
    
        lvl1_bg = Sprite('map/level1.png')

        lvl1_bg.position = lvl1_bg.width // 2, lvl1_bg.height // 2

        self.px_width = lvl1_bg.width
        self.px_height = lvl1_bg.height

        self.add(lvl1_bg)
        
    

def get_newgame():
  
    scene = Scene()
    layer = MainHero()
    level1_layer = Level1_Layer

    scroller_1 = ScrollingManager()
    scroller_1.add(level1_layer)
    scroller_1.add(layer)

    scene.add(scroller_1)

    return scene

class MainHero(ScrollableLayer):   
    is_event_handler = True
    def __init__(self):
        super().__init__()
        #run right --------------------------------------------------
        self.img_r = pyglet.image.load('adventurer-run3-sword-Sheet.png')
        self.img_grid_r = pyglet.image.ImageGrid(self.img_r, 1, 6, item_width=50, item_height=37 )
        self.anim_r = pyglet.image.Animation.from_image_sequence(self.img_grid_r[0:], 0.1, loop=True)
        # ----------------------------------------------------------
        
        #attak1
        self.img_a1 = pyglet.image.load('attack1/Attacksheet.png')
        self.img_grid_a1 = pyglet.image.ImageGrid(self.img_a1, 1, 5, item_width=50, item_height=37 )

        self.anim_a1 = pyglet.image.Animation.from_image_sequence(self.img_grid_a1[0:], 0.1, loop=True)
        #_-----------------------------------------------------------------

        # idle
        self.img_i = pyglet.image.load('idle/idlesheet.png')
        self.img_grid_i = pyglet.image.ImageGrid(self.img_i, 1, 4, item_width=50, item_height=37 )

        self.anim_i = pyglet.image.Animation.from_image_sequence(self.img_grid_i[0:], 0.3, loop=True)
        #_-----------------------------------------------------------------


        self.sprite = Sprite(self.anim_i)
        self.sprite.position = (100, 180)
        self.sprite.scale = 2
        self.sprite.scale_x = 1
        self.sprite.velocity = (0,0)
        self.sprite.do(Mover())
        self.add(self.sprite)
        

        self.speed = 100.0
        self.pressed = defaultdict(int)
        self.schedule(self.update)
        #h

    def on_key_press(self, k, m):
        print(k)

        if k == 65361:
            self.sprite.scale_x = -1
            self.sprite._animation = self.anim_r

        if k == 65363:
            self.sprite.scale_x = 1
            self.sprite._animation = self.anim_r

        if k == 65362:
            self.sprite._animation = self.anim_a1


    def on_key_release(self, k, m):
        self.sprite._animation = self.anim_i


    def update(self, dt):
        pass

class Mover(Move):
    def step(self,dt):
        from Level1_Layer import get_newgame
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 180
        self.target.velocity = (vel_x, 0)
        scroller_1.set_focus(self.target.x, self.target.y)
        # scroller_2.set_focus(self.target.x, self.target.y)