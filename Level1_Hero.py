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

        # first level monsters -------------------------------------------------
        self.run_r = False
        self.run_l = False
        #Simple Wolf
        self.white_wolf_1 = SimpleWolf()
        self.white_wolf_2 = SimpleWolf()
        self.white_wolf_3 = SimpleWolf()
        self.white_wolf_4 = SimpleWolf()
        self.gray_wolf_1 =  SimpleWolf()
        self.gray_wolf_2 =  SimpleWolf()
        self.gray_wolf_3 =  SimpleWolf()
        self.gray_wolf_4 =  SimpleWolf()
        

        #Middle Wolf
        self.blue_wolf_1 =  MiddleWolf()
        self.blue_wolf_2 =  MiddleWolf()
        self.blue_wolf_3 =  MiddleWolf()
        self.blue_wolf_3 =  MiddleWolf()
        self.black_wolf_1 = MiddleWolf()
        self.black_wolf_2 = MiddleWolf()
        self.black_wolf_3 = MiddleWolf()
        self.black_wolf_4 = MiddleWolf()

        #Hell Hound
        self.hell_hound_1 = HellHound()
        self.hell_hound_2 = HellHound()

        #Hell Beast
        self.hell_beast = HellBeast()
        self.ball = self.hell_beast.fire_ball

        self.hell_beast_1 = HellBeast()
        self.ball_1 = self.hell_beast_1.fire_ball
        
        #FirstStack
        self.white_wolf_1.sprite.position = (850,160)
        self.white_wolf_1.sprite.scale_x = -1     
        self.gray_wolf_1.sprite.position = (900,160)
        self.gray_wolf_1.sprite.color = (105,105,105)
        self.gray_wolf_1.sprite.scale_x = -1
        self.white_wolf_2.sprite.position = (950,160)

        #SecondStack
        self.blue_wolf_1.sprite.position = (1200,160)
        self.blue_wolf_2.sprite.position = (1250,160)

        self.black_wolf_1.sprite.position = (1450,180)
        self.black_wolf_1.lifes = 3
        self.black_wolf_1.sprite.color = (0,0,0)
        self.black_wolf_1.sprite.scale_x = -1
        self.black_wolf_1.sprite.scale = 2.5

        #ThirdStack
        self.hell_hound_1.sprite.position = (1600,160)

        self.hell_beast.sprite.position = (1700, 200)
        #----------------------------------------------------------------------
        

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
        #FirstStack
        self.add(self.white_wolf_1)
        self.add(self.white_wolf_2)
        self.add(self.gray_wolf_1)
        
        #SecondStack
        self.add(self.blue_wolf_1)
        self.add(self.blue_wolf_2)
        self.add(self.black_wolf_1)
        self.add(self.hell_hound_1)
        #Hell Beast
        self.add(self.hell_beast)
        self.add(self.ball)

        #Hearts
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
                #FirstStack
                self.get_flag(self.white_wolf_1)
                self.get_flag(self.white_wolf_2)
                self.get_flag(self.gray_wolf_1)

                #SecondStack
                self.get_flag(self.blue_wolf_1)
                self.get_flag(self.blue_wolf_2)
                self.get_flag(self.black_wolf_1)
                self.get_flag(self.hell_hound_1)

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

    
    def beast_action(self, position, enemy, fire_ball):
        x, y = self.sprite.position
        b_x, b_y = enemy.sprite.position
        
        '''
        when our hero is in start of level then is dead = false
        and he can be attack
        '''
        if self.sprite.position[0] < 120:
            self.is_dead = False
            self.can_attack = True

        # when fire ball is too far from enemy then he turn back to enemy
        if fire_ball.position[0] < (b_x - 400):
            fire_ball.position = (b_x, b_y)

            fire_ball.visible = False
        # if our hero is too far from enemy then flag = false
        if (b_x - x) > 300:
            self.flag = False

        '''
        when our flag = true we start move back from enemy until flag = false
        '''
        if self.flag:
            self.sprite.position = x - 5, y
        if (b_x - x) < position:
            if (fire_ball.position[0]-x) < 10:
                if self.sprite.image == animations.anim_a1 and self.sprite.scale_x == 1:
                    fire_ball.position = (b_x, b_y)

                elif self.can_attack:
                    self.can_attack = False
                    # logic for visible heart
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
                    '''
                    when enemy attacks our hero, our hero lost his 1 lifes and flag is_dead = True
                    is_dead needs for logic when we dead our enemies stop they actions
                    '''
                    self.is_dead = True
                    self.life -= 1
                    
                    print(self.life)
            '''
            when our hero is not in radius visible beast, beast`s ball is not visible
            when enemy starts attack fire ball is visible 
            '''       
            fire_ball.visible = True
            if fire_ball.position[0] == b_x:
                enemy.ball_action = True
                fire_ball.visible = False
            else: 
                enemy.ball_action = False
            
            '''
            ball action is true when our hero is in visible of enemy
            when ball action is true ball start move by 500 pixels in 1 seconds
            '''
            if enemy.ball_action:
                
                enemy.sprite.scale = 1.5
                enemy.sprite.image = enemy.get_attack_animation()
                fire_ball.do(MoveBy((-1,0), 0.6) + MoveBy((-500, 0), 1))
                fire_ball.visible = True
            '''
            when our hero is in visible of enemy and if our hero starts attack beast
            beast start burn and our hero move out of enemy
            self.flag means that we can attack our enemy
            '''
            if (b_x - x) < 300:
                if self.sprite.image == animations.anim_a1 and (b_x - x) < 100:
                    enemy.flag = True
                    if self.sprite.image == animations.anim_a1 and (b_x - x) < 100:
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
                
    def wolf_action(self, position, enemy, speed, r, l):
        self.x_y = self.sprite.position[0]
        x, y = self.sprite.position
        w_x, w_y = enemy.sprite.position
        '''
        when our hero is in start of level then is dead = false
        and he can be attack
        '''
        if self.sprite.position[0] < 120:
            self.is_dead = False
            self.can_attack = True

        '''
        if enemy`s visible is not false he can do his actions
        and if our hero is not dead
        enemy start move to our hero when he is in visible of enemy
        and stop moving and attack when our hero die
        '''
        if enemy.sprite.visible  is not False:
            if not self.is_dead:
                if (w_x-self.x_y) < position and (w_x-self.x_y) > 0:
                    enemy.sprite._animation = enemy.get_idle_animation()
                    enemy.sprite.scale_x = l     
                    enemy.sprite.position = (w_x - speed, w_y)
                elif (w_x-self.x_y) <= 0:
                    enemy.sprite.scale_x = r     
                    enemy.sprite.position = (w_x + speed, w_y)
                '''
                when our hero makes block, enemy move away from hero by 100px
                '''
                if self.sprite.image == animations.anim_b and (w_x - x) <= 40 and (w_x - x) >= 0:
                    enemy.sprite.position = (w_x+100, w_y)
                if self.sprite.image == animations.anim_b and (w_x - x) <= 0 and (w_x - x) >= -40:
                    enemy.sprite.position = (w_x-100, w_y)
            
            if (w_x - self.x_y) <= 80 and (w_x - self.x_y) >= -80:
                enemy.flag = True
            elif (w_x - self.x_y) > 80 or (w_x - self.x_y) < -80:
                enemy.flag = False
            '''
            if our hero can be attack and if enemy is too close to our hero
            then hero lost his 1 lifes and move to start level
            '''
            if (w_x - self.x_y) <= 10 and (w_x - self.x_y) >= 0 and self.can_attack:
                enemy.sprite.image = enemy.anim
                self.x_y = self.sprite.position[0]
                print(self.sprite.position[0], enemy.sprite.position[0])
                self.can_attack = False
                self.is_dead = True
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
                self.is_dead = True
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
        self.wolf_action(200, self.white_wolf_1, 2, 1, -1)
        self.wolf_action(200, self.white_wolf_2, 2, 1, -1)
        self.wolf_action(200, self.gray_wolf_1, 2, 1, -1)
        #---------------------------------------------------------
        # second stack -------------------------------------------
        self.wolf_action(200, self.blue_wolf_1, 3, 1, -1)
        self.wolf_action(200, self.blue_wolf_2, 3, 1, -1)
        self.wolf_action(300, self.black_wolf_1, 3.5, 1, -1)
        self.wolf_action(200, self.hell_hound_1, 4, -1, 1)
        # fourth stack--------------------------------------------
        self.beast_action(300, self.hell_beast, self.ball)
        #---------------------------------------------------------
        if self.life == 0:
            self.life = 3
            director.push(ZoomTransition(GameOver.get_gameover(1)))
            self.kill()

   
            
           
      
        


        
        



        
        
