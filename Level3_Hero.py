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

        self.is_dead = False
     
        self.run_r = False
        self.run_l = False
        
    
        
        
        self.life = 3
        self.sprite = Sprite(animations.anim_i)

        self.can_attack = True

        self.sprite.position = (100, 180)
        self.sprite.scale = 2
        self.sprite.scale_x = 1
        self.sprite.velocity = (0,0)
        self.attack = False
        self.flag = False
        self.x_y = 0
        
        self.add(self.sprite)
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    
    
    def get_flag(self, enemy):
        if enemy.flag:
                if enemy.lifes != 0:
                    enemy.lifes -= 1
                    print('Enemy lifes: ', enemy.lifes)
                    
                else:
                    enemy.sprite.position = (10000, -1000)
                    enemy.visible = False
                    print('emeny`s dead')

    '''
    we can`t attack or block and run in the same time 
    '''
    def on_key_press(self, k, m):
        if k == 65361:
            if not self.is_dead:
                self.run_l = True
                self.sprite.scale_x = -1
                self.sprite.image = animations.anim_r

        if k == 65363:
            if not self.is_dead:
                self.run_r = True
                self.sprite.scale_x = 1
                self.sprite.image = animations.anim_r

        if k == key.B:
            if not self.is_dead:
                self.sprite.image = animations.anim_b

        if k == key.Z:
            if not self.is_dead:
                pass
                '''
                get flag add logic for our hero`s hit, when our hero attacks enemy
                enemy lost his 1 or more lifes
                if enemy has 0 lifes his position equals (10000, -1000) and his visible = False
                '''
               
        
    def on_key_release(self, k, m):
        if k == key.B:
            if not self.is_dead:
                self.sprite.image = animations.anim_b
                self.run_l = False
                self.run_r = False

        if k == key.Z:
            if not self.is_dead:
                self.run_l = False
                self.run_r = False
                self.sprite.image = animations.anim_a1
        else:
            self.sprite.image = animations.anim_i
            self.run_l = False
            self.run_r = False


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
       
