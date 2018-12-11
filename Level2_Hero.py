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
from Level2_Monsters import *
import GameOver


director.window.pop_handlers()
keyboard = key.KeyStateHandler()
director.window.push_handlers(keyboard)



class Level2_Hero(ScrollableLayer):
    is_event_handler = True

    def __init__(self):
        super().__init__()
        self.skeleton = GreenSkeleton()
        self.skeleton.sprite.position = (400, 420)
        self.skeleton.sprite.scale = 2
        self.skeleton.sprite.scale_x = -1
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
        self.some = 1
        self.run_r = False
        self.run_l = False
        self.attacks = False
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
        self.add(self.skeleton)
        self.add(self.sprite)
        self.add(self.mirror_sprite)
        self.add(self.heart1)
        self.add(self.heart2)
        self.add(self.heart3)
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def get_flag(self, enemy, hp):
        if not enemy.first_death:
            if enemy.flag:
                    if enemy.lifes >= 0:
                        enemy.lifes -= hp
                        print('Enemy lifes: ', enemy.lifes)
                        
                    else:
                        enemy.sprite.position = (10000, -1000)
                        enemy.visible = False
                        print('emeny`s dead')


    def on_key_press(self, k, m):
        print(k)
        if k == 65361:
            self.run_l = True
            self.sprite.scale_x = -1
            self.sprite.image = animations.anim_r

            self.mirror_sprite.scale_x = 1
            self.mirror_sprite.image = animations.anim_r

        if k == key.B:
            if not self.is_dead:
                self.sprite.image = animations.anim_b


        if k == 65363:
            self.run_r = True
            self.sprite.scale_x = 1
            self.sprite.image = animations.anim_r

            self.mirror_sprite.scale_x = -1
            self.mirror_sprite.image = animations.anim_r
                    
        if k == key.Z:
            if not self.is_dead:
                self.get_flag(self.skeleton, 1)


        if k == key.X:
            if not self.is_dead:
                self.get_flag(self.skeleton, 2)




        
    def on_key_release(self, k, m):
        if k == key.B:
            if not self.is_dead:
                self.sprite.image = animations.anim_b
                self.run_l = False
                self.run_r = False

        if k == key.Z:
            self.run_l = False
            self.run_r = False
            self.sprite.image = animations.anim_a1

            self.mirror_sprite.image = animations.anim_a1
        elif k == key.X:
            self.run_l = False
            self.run_r = False
            self.sprite.image = animations.anim_a2
            self.mirror_sprite.image = animations.anim_a2
        else:
            self.sprite.image = animations.anim_i
            self.mirror_sprite.image = animations.anim_i
            self.run_l = False
            self.run_r = False


    def skeleton_action(self, position, enemy, speed, l, r):
        
        x, y = self.sprite.position
        asdf = x
        w_x, w_y = enemy.sprite.position
        if x <120:
            w_y = 390
            self.is_dead = False
        
        if self.sprite.image == animations.anim_b and (w_x - x) <= 40 and (w_x - x) >= 0:
            enemy.sprite.position = (w_x+180, w_y)
            w_x += 180


        if self.sprite.image == animations.anim_b and (w_x - x) <= 0 and (w_x - x) >= -40:
            enemy.sprite.position = (w_x-180, w_y)
            w_x -= 180
    

        if enemy.lifes < 3:
            enemy.first_death = True
            enemy.sprite._animation = enemy.get_death()
            if (w_x - x) > 200 or (w_x - x) < -200:
                enemy.can_reinc = True
                
        if enemy.can_reinc:
            enemy.first_death = False
            enemy.sprite._animation = enemy.anim   

        if not enemy.first_death:
            if w_y == 391 and enemy.lifes >= 0 and (w_x-x) < 50 and (w_x - x) >= -50 and not self.is_dead:
                self.is_dead = True
                self.sprite.do(FadeOut(1) + MoveTo((100, 410), 1) + FadeIn(1))
                self.mirror_sprite.do(FadeOut(1) + MoveTo((100, 320), 1) + FadeIn(1))
                self.life -= 2
                print(self.life)

            if not self.is_dead:
                if (w_x - x) < position and (w_x - x) >= 0:
                    if (w_x-x) < 50 and (w_x - x) >= 0:
                        
                        enemy.flag = True
                        enemy.sprite._animation = enemy.get_attack()
                        enemy.sprite.do(ac.Delay(0.8) + ac.MoveTo((w_x, w_y+1), 0))
                        
                    else:
                        enemy.flag = False
                        enemy.sprite.scale_x = -1
                        enemy.sprite._animation = enemy.get_walk()
                        enemy.sprite.scale = 2
                        enemy.sprite.position = (w_x - speed, 390)

                elif (w_x - x) <= 0 and (w_x - x) > -position:
                    if (w_x-x) > -50 and (w_x - x) <= 0:
                        enemy.flag = True
                        enemy.sprite._animation = enemy.get_attack()
                        enemy.sprite.do(ac.Delay(0.8) + ac.MoveTo((w_x, w_y+1), 0))
                    else:
                        enemy.sprite.scale_x = 1
                        enemy.sprite._animation = enemy.get_walk()
                        enemy.sprite.scale = 2
                        enemy.sprite.position = (w_x + speed, 390)
                    
                else:
                    enemy.flag = False
                    enemy.sprite.position = (w_x, 410)
                    enemy.sprite._animation = enemy.anim

                


    def update(self, dt):
        if self.life == 0:
            self.life = 3
            director.push(ZoomTransition(GameOver.get_gameover(2)))
            self.kill()
        self.skeleton_action(200, self.skeleton, 1, -1, 1)
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
       
