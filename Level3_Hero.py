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
        
        self.add(self.ghost)
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

        if enemy.lifes == 0:
            enemy.sprite.position = (10000, -1000)
            enemy.visible = False

        if self.sprite.position[0] < 120:
            self.is_dead = False
            self.can_attack = True
        
        g_x, g_y = enemy.sprite.position
        x, y = self.sprite.position

        
        '''
        enemy start move when we are in radius of enemy vision front or behind us
        '''
        if not self.is_dead:
            if (g_x - x) < position and (g_x - x) > 0:
                if (g_x - x) < 40 and self.sprite.image == animations.anim_a1:
                    enemy.lifes -=1
                    print('Enemy lifes: ', enemy.lifes)
                    enemy.can_action = False
                    enemy.sprite._animation = enemy.get_vanish()
                    enemy.sprite.position = (g_x - 200, g_y)
                    enemy.flag = False
                elif (g_x - x) < 20:
                    enemy.sprite._animation = enemy.get_shriek()
                    self.life -= 1
                    self.is_dead = True
                    self.sprite.do(ac.FadeOut(1) + ac.MoveTo((100, 180), 1) + ac.FadeIn(1))
                    print(self.life)
                else:
                    enemy.sprite._animation = enemy.anim
                    enemy.sprite.scale_x = 1
                    enemy.sprite.position = (g_x - speed, g_y)
                
            elif (g_x - x) <= 0 and (g_x - x) > -position:
                if (g_x - x) > -40 and self.sprite.image == animations.anim_a1:
                    enemy.lifes -= 1
                    print('Enemy lifes: ', enemy.lifes)
                    enemy.sprite._animation = enemy.get_vanish()
                    enemy.sprite.position = (g_x + 200, g_y)
                    enemy.flag = False
                elif (g_x - x) > -20:
                    enemy.sprite._animation = enemy.get_shriek()   
                    self.life -= 1
                    self.is_dead = True
                    self.sprite.do(ac.FadeOut(1) + ac.MoveTo((100, 180), 1) + ac.FadeIn(1))
                    
                    print(self.life)
                else:
                    enemy.sprite._animation = enemy.anim
                    enemy.sprite.scale_x = -1
                    enemy.sprite.position = (g_x + speed, g_y)


        
        
        


    def update(self, dt):
        
        x, y = self.sprite.position
        self.ghost_action(200,self.ghost, 3)
        if self.run_l:
            self.sprite.position = (x - 3, y)
        elif self.run_r:
            self.sprite.position = (x + 3, y)
        Level3_Background.scroller_3.set_focus(self.sprite.position[0], self.sprite.position[1])
       
