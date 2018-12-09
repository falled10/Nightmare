import cocos
from cocos.actions import *
import pyglet
import time
from cocos.director import director
from collections import defaultdict
from pyglet import image
from pyglet.window import key
from cocos.layer import ScrollableLayer
from cocos.scenes.transitions import *
from cocos.actions import Move
from cocos.sprite import Sprite
import Level1_Background
from cocos.scene import Scene
from cocos.scenes.transitions import *
from Level1_Monsters import *
from Hearts import Hearts
import Sound
import GameOver
import animations


director.window.pop_handlers()
keyboard = key.KeyStateHandler()
director.window.push_handlers(keyboard)
        
class Level1_Hero(ScrollableLayer):
    is_event_handler = True

    def __init__(self):
        super().__init__()

        #Hearts---------------------------------------------------------------
        self.heart1 = Hearts()
        self.heart2 = Hearts()
        self.heart3 = Hearts()
        self.heart1.sprite.scale = 0.5
        self.heart2.sprite.scale = 0.5
        self.heart3.sprite.scale = 0.5

        # first level monsters -------------------------------------------------
        self.run_r = False
        self.run_l = False
        self.white_wolf = WhiteWolf()
        self.white_wolf2 = WhiteWolf()
        self.blue_wolf = BlueWolf()
        self.blue_wolf2 = BlueWolf()
        self.hell_hound = HellHound()
        self.blue_wolf3 = BlueWolf()
        self.hell_beast = HellBeast()
        self.ball = self.hell_beast.fire_ball
        self.hell_beast.sprite.position = (500, 200)
        self.blue_wolf3.sprite.position = (1350, 160)
        self.white_wolf2.sprite.position = (1300, 160)
        self.blue_wolf2.sprite.position = (1100, 160)
        #----------------------------------------------------------------------
        

        #SwordSound
        global SwordLoops, SwordAudio, PlayerForSwordSound
        SwordAudio = pyglet.media.load('res/audio/str1.wav')
        SwordLoops=pyglet.media.SourceGroup(SwordAudio.audio_format, None)
        PlayerForSwordSound=pyglet.media.Player()
        SwordLoops.queue(SwordAudio)
        SwordLoops.loop = True
        #------------------------------------------------------------------
        
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
        
        #first stack ------------------------------------------------
        self.ball.visible = False
        self.add(self.blue_wolf)
        self.add(self.blue_wolf2)
        self.add(self.white_wolf)
        self.add(self.hell_hound)
        self.add(self.white_wolf2)
        self.add(self.blue_wolf3)
        self.add(self.hell_beast)
        self.add(self.ball)
        self.add(self.heart1)
        self.add(self.heart2)
        self.add(self.heart3)
        #-----------------------------------------------------------
        self.add(self.sprite)
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def get_fire(self, enemy):
        if enemy.flag:
                if enemy.lifes != 0:
                    enemy.lifes -= 1
                    print('Enemy lifes: ',enemy.lifes)
                    
                else:
                    enemy.sprite.position = (10000, -1000)
                    enemy.visible = False
                    print('emeny`s dead')
                    self.flag = False
    
    def get_flag(self, enemy):
        if enemy.flag:
                if enemy.lifes != 0:
                    enemy.lifes -= 1
                    
                    
                else:
                    enemy.sprite.position = (10000, -1000)
                    enemy.visible = False
                    print('emeny`s dead')

    
    def on_key_press(self, k, m):
        if k == 65361:
            self.run_l = True
            self.sprite.scale_x = -1
            self.sprite.image = animations.anim_r

        if k == 65363:
            self.run_r = True
            self.sprite.scale_x = 1
            self.sprite.image = animations.anim_r

        if k == key.B:
            self.sprite.image = animations.anim_b

        if k == key.Z:
            #SwordSound
            SwordLoops.loop=True
            PlayerForSwordSound.queue(SwordLoops)
            # PlayerForSwordSound.play()
            
            
            #------------------------------------------------------------------ 
            self.get_flag(self.white_wolf)
            self.get_flag(self.blue_wolf)
            self.get_flag(self.blue_wolf2)
            self.get_flag(self.hell_hound)
            self.get_flag(self.white_wolf2)
            self.get_flag(self.blue_wolf3)
            self.get_fire(self.hell_beast)
        
    def on_key_release(self, k, m):
        if k == key.B:
            self.sprite.image = animations.anim_b
            self.run_l = False
            self.run_r = False

        if k == key.Z:
             #SwordSound
            SwordLoops.loop=False
            #------------------------------------------------------------------ 
            self.run_l = False
            self.run_r = False
            self.sprite.image = animations.anim_a1
        else:
            self.sprite.image = animations.anim_i
            self.run_l = False
            self.run_r = False

    
    def beast_action(self, position, enemy, fire_ball):
        x, y = self.sprite.position
        b_x, b_y = enemy.sprite.position
        
        if self.sprite.position[0] < 120:
            self.can_attack = True

        if fire_ball.position[0] < (b_x - 400):
            fire_ball.position = (b_x, b_y)

            fire_ball.visible = False
        if (b_x - x) > 300:
            self.flag = False

        
        if self.flag:
            self.sprite.position = x - 5, y
        if (b_x - x) < position:
            if (fire_ball.position[0]-x) < 10:
                if self.sprite.image == animations.anim_a1:
                    fire_ball.position = (b_x, b_y)
                elif self.can_attack:
                    self.can_attack = False
                    if(self.life == 3):
                        self.sprite.do(FadeOut(2) + MoveTo((100, 180), 2) + FadeIn(1))
                        self.heart1.sprite.visible = True
                        self.heart2.sprite.visible = True
                        self.heart3.sprite.visible = True
                        self.heart1.do(Show() + Delay(2) + Hide())
                        self.heart2.do(Show() + Delay(2) + Hide())
                        self.heart3.do(Show() + Blink(10,2))
                    elif(self.life == 2):
                        self.sprite.do(FadeOut(3) + MoveTo((100, 180), 2) + FadeIn(1))
                        self.heart1.sprite.visible = True
                        self.heart2.sprite.visible = True
                        self.heart3.sprite.visible = True
                        self.heart1.do(Show() + Delay(2) + Hide())
                        self.heart2.do(Show() + Blink(10,2))
                    elif(self.life == 1):
                        self.sprite.do(FadeOut(1) + MoveTo((100, 180), 1) + FadeIn(1))
                        print("dead 0")
                    
                    self.life -= 1
                    
                    print(self.life)
                    
            fire_ball.visible = True
            if fire_ball.position[0] == b_x:
                enemy.ball_action = True
                fire_ball.visible = False
            

            else: 
                enemy.ball_action = False
            

            if enemy.ball_action:
                
                enemy.sprite.scale = 1.5
                enemy.sprite.image = enemy.get_attack_animation()
                fire_ball.do(MoveBy((-1,0), 0.6) + MoveBy((-500, 0), 1))
                fire_ball.visible = True
            if (b_x - x) < 300:
                if self.sprite.image == animations.anim_a1 and (b_x - x) < 100:
                    
                    enemy.flag = True
                    if self.sprite.image == animations.anim_a1 and (b_x - x) < 95:
                        self.flag = True
                        enemy.sprite.scale = 1.5
                        enemy.sprite.image = enemy.get_burn_animation()
                else:
                    enemy.flag = False
            else:
                enemy.sprite.scale = 1.5
                enemy.sprite.image = enemy.get_attack_animation()
                self.flag = False
              
        else:
            enemy.sprite.scale = 1.5
            enemy.sprite._animation = enemy.anim_i
            self.heart1.visible = False
            self.heart2.visible = False
            self.heart3.visible = False
              

        
        
            
    def wolf_action(self, position, enemy, speed, r, l):
        self.x_y = self.sprite.position[0]
        x, y = self.sprite.position
        w_x, w_y = enemy.sprite.position
        if self.sprite.position[0] < 120:
            self.can_attack = True
        if enemy.sprite.visible  is not False:
            if (w_x-self.x_y) < position and (w_x-self.x_y) > 0:
                enemy.sprite._animation = enemy.get_idle_animation()
                enemy.sprite.scale_x = l     
                enemy.sprite.position = (w_x - speed, w_y)
            elif (w_x-self.x_y) <= 0:
                enemy.sprite.scale_x = r     
                enemy.sprite.position = (w_x + speed, w_y)
            if self.sprite.image == animations.anim_b and (w_x - x) <= 40 and (w_x - x) >= 0:
                enemy.sprite.position = (w_x+100, w_y)
            if self.sprite.image == animations.anim_b and (w_x - x) <= 0 and (w_x - x) >= -40:
                enemy.sprite.position = (w_x-100, w_y)

            if (w_x - self.x_y) <= 80 and (w_x - self.x_y) >= -80:
                enemy.flag = True
            elif (w_x - self.x_y) > 80 or (w_x - self.x_y) < -80:
                enemy.flag = False
            if (w_x - self.x_y) <= 10 and (w_x - self.x_y) >= 0 and self.can_attack:
                enemy.sprite.image = enemy.anim
                self.x_y = self.sprite.position[0]
                print(self.sprite.position[0], enemy.sprite.position[0])
                self.can_attack = False
                self.sprite.do(FadeOut(1) +MoveTo((100, 180), 1) + FadeIn(1))
                self.life -= 1
                
                print(self.life)


    def update(self, dt):
        x, y = self.sprite.position
        self.heart1.position = (x-20, y+40)
        self.heart2.position = (x, y+40)
        self.heart3.position = (x+20, y+40)

        if self.run_l:
            self.sprite.position = (x - 3, y)
        elif self.run_r:
            self.sprite.position = (x + 3, y)
        Level1_Background.scroller_1.set_focus(self.sprite.position[0], self.sprite.position[1])
        # first stack --------------------------------------------
        self.wolf_action(200, self.white_wolf, 2, 1, -1)
        self.wolf_action(200, self.blue_wolf, 3, 1, -1)
        self.wolf_action(300, self.blue_wolf2, 3, 1, -1)
        #---------------------------------------------------------
        # second stack--------------------------------------------
        self.wolf_action(300, self.hell_hound, 4, -1, 1)
        self.wolf_action(200, self.white_wolf2, 2, 1, -1)
        self.wolf_action(200, self.blue_wolf3, 3, 1, -1)
        self.beast_action(300, self.hell_beast, self.ball)
        #---------------------------------------------------------
        if self.life == 0:
            self.life = 3
            director.push(ZoomTransition(GameOver.get_gameover(1)))
            self.kill()

"""
    def SwordSoundMute():
        if(PlayerForSwordSound.volume==1.0):
            PlayerForSwordSound.volume=0.0
        elif(PlayerForSwordSound.volume==0.0):
            PlayerForSwordSound.volume=1.0
"""        
            
           
      
        


        
        



        
        
