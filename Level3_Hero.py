import cocos
import cocos.actions as ac
import pyglet
from cocos.director import director
from collections import defaultdict
from pyglet.window import key
from cocos.layer import ScrollableLayer
from pyglet import image
from cocos.actions import Move
from cocos.sprite import Sprite
import Level3_Background
from cocos.scene import Scene
from cocos.scenes.transitions import *
from Level3_Monsters import *
import animations


director.window.pop_handlers()
keyboard = key.KeyStateHandler()
director.window.push_handlers(keyboard)

class Mover(Move):
    def step(self,dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 180
        self.target.velocity = (vel_x, 0)
        Level3_Background.scroller_3.set_focus(self.target.x, self.target.y)

class Level3_Hero(ScrollableLayer):
    is_event_handler = True

    def __init__(self):
        super().__init__()
        self.ghost = Ghost()

        self.ghost.sprite.position = (500, 200)
        self.sprite = Sprite(animations.anim_i)
        self.sprite.position = (100, 180)
        self.sprite.scale = 2
        self.sprite.scale_x = 1
        self.sprite.velocity = (0,0)
        self.sprite.do(Mover())
        
        self.add(self.sprite)
        self.add(self.ghost)
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def on_key_press(self, k, m):
        print(k)

        if k == 65361:
            self.sprite.scale_x = -1
            self.sprite._animation = animations.anim_r

        if k == 65363:
            self.sprite.scale_x = 1
            self.sprite._animation = animations.anim_r

        if k == key.Z:
            self.sprite._animation = animations.anim_a1
            
    def on_key_release(self, k, m):
        self.sprite._animation = animations.anim_i


    def ghost_action(self, position, enemy, speed):
        g_x, g_y = enemy.sprite.position
        x, y = self.sprite.position

        if (g_x - x) < position and (g_x - x) > 0:
            enemy.sprite.position = (g_x - speed, g_y)
        elif (g_x - x) <= 0:
            self.sprite.scale_x = -1
            enemy.sprite.position = (g_x + speed, g_y)


    def update(self, dt):
        self.ghost_action(300,self.ghost, 3)
       
