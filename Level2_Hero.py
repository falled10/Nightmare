import cocos
from cocos.actions import *
import pyglet
from pyglet import image
from cocos.director import director
from collections import defaultdict
from pyglet.window import key
from cocos.layer import ScrollableLayer
from cocos.actions import Move
from cocos.sprite import Sprite
import Level2_Background
from cocos.scene import Scene
from cocos.scenes.transitions import *
from Hearts import Hearts
import animations


director.window.pop_handlers()
keyboard = key.KeyStateHandler()
director.window.push_handlers(keyboard)



class Level2_Hero(ScrollableLayer):
    is_event_handler = True

    def __init__(self):
        super().__init__()
         #Hearts---------------------------------------------------------------
        self.is_dead = False
        self.heart1 = Hearts()
        self.heart2 = Hearts()
        self.heart3 = Hearts()
        self.heart1.scale = 0.5
        self.heart2.scale = 0.5
        self.heart3.scale = 0.5
        self.heart1.visible = False
        self.heart2.visible = False
        self.heart3.visible = False

        self.run_r = False
        self.run_l = False

        self.run_r = False
        self.run_l = False
        self.life = 3
        self.sprite = Sprite(animations.anim_i)
        self.sprite.position = (100, 410)
        self.sprite.scale = 2
        self.sprite.scale_x = 1
        self.sprite.velocity = (0,0)

        self.mirror_sprite = Sprite(animations.anim_i)
        self.mirror_sprite.position = (100, 320)
        self.mirror_sprite.scale = -2
        self.mirror_sprite.scale_x = -1
        self.mirror_sprite.velocity = (0,0)
        
        self.add(self.sprite)
        self.add(self.mirror_sprite)
        self.add(self.heart1)
        self.add(self.heart2)
        self.add(self.heart3)
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def on_key_press(self, k, m):
        print(k)
        if k == 65361:
            self.run_l = True
            self.sprite.scale_x = -1
            self.sprite.image = animations.anim_r

            self.mirror_sprite.scale_x = 1
            self.mirror_sprite._animation = animations.anim_r

        if k == 65363:
            self.run_r = True
            self.sprite.scale_x = 1
            self.sprite.image = animations.anim_r

            self.mirror_sprite.scale_x = -1
            self.mirror_sprite._animation = animations.anim_r
                    
        if k == key.Z:
            print("z")

        if k == key.X:
            self.sprite._animation = animations.anim_a2

            self.mirror_sprite._animation = animations.anim_a2

        
    def on_key_release(self, k, m):
        if k == key.Z:
            if not self.is_dead:
                self.run_l = False
                self.run_r = False
                self.sprite.image = animations.anim_a1
        else:
            self.sprite.image = animations.anim_i
            self.run_l = False
            self.run_r = False
        self.sprite._animation = animations.anim_i

        self.mirror_sprite._animation = animations.anim_i


    def update(self, dt):
        x,y = self.sprite.position
        xm, ym = self.mirror_sprite.position
        self.heart1.position = (x-20, y+40)
        self.heart2.position = (x, y+40)
        self.heart3.position = (x+20, y+40)
        if self.run_l:
            self.sprite.position = (x - 3, y)
            self.mirror_sprite.position = (xm-3, ym)
        elif self.run_r:
            self.sprite.position = (x + 3, y)
            self.mirror_sprite.position = (xm +3, ym)

        Level2_Background.scroller_2.set_focus(self.sprite.position[0], self.sprite.position[1])
       
