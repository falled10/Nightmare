import cocos
import cocos.actions as ac
import pyglet
from cocos.director import director
from collections import defaultdict
from pyglet.window import key
from cocos.layer import ScrollableLayer
from cocos.actions import Move
from cocos.sprite import Sprite
from cocos.scenes.transitions import *
import Level1_Background
from cocos.scene import Scene



director.window.pop_handlers()
keyboard = key.KeyStateHandler()
director.window.push_handlers(keyboard)

class Mover(Move):
    def step(self,dt):
         
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 180
        
        dx = vel_x * dt

        last = self.target.get_rect()
        new = last.copy()
        new.x != dx
        self.target.velocity = self.target.collide_map(last, new, vel_X)
        self.target.position = new.center

        
        Level1_Background.scroller_1.set_focus(*new.center)

class MainHero(ScrollableLayer):
    is_event_handler = True

    def __init__(self, collision_handler):
        super().__init__()
        #run right --------------------------------------------------
        self.img_r = pyglet.image.load('res/animation/run/adventurer-run3-sword-Sheet.png')
        self.img_grid_r = pyglet.image.ImageGrid(self.img_r, 1, 6, item_width=50, item_height=37 )
        self.anim_r = pyglet.image.Animation.from_image_sequence(self.img_grid_r[0:], 0.1, loop=True)
        # ----------------------------------------------------------
        
        #attack1
        self.img_a1 = pyglet.image.load('res/animation/attack1/Attacksheet.png')
        self.img_grid_a1 = pyglet.image.ImageGrid(self.img_a1, 1, 5, item_width=50, item_height=37 )

        self.anim_a1 = pyglet.image.Animation.from_image_sequence(self.img_grid_a1[0:], 0.1, loop=True)
        #_-----------------------------------------------------------------

        # idle
        self.img_i = pyglet.image.load('res/animation/idle/idlesheet.png')
        self.img_grid_i = pyglet.image.ImageGrid(self.img_i, 1, 4, item_width=50, item_height=37 )

        self.anim_i = pyglet.image.Animation.from_image_sequence(self.img_grid_i[0:], 0.3, loop=True)
        #_-----------------------------------------------------------------


        self.sprite = Sprite(self.anim_i)
        self.sprite.position = (100, 75)
        self.sprite.scale = 2
        self.sprite.scale_x = 1
        self.sprite.velocity = (0,0)

        sprite.collide_map = collision_handler

        self.sprite.do(Mover())

        self.add(self.sprite)
        

        self.speed = 100.0
        self.pressed = defaultdict(int)
        self.schedule(self.update)

       

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
       
