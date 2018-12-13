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
from Level1_Monsters import *
from Level2_Monsters import *
from Level2_Monsters import *
import GameOver


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
        #-----------------------------------------------------------------------
        # second level monsters -------------------------------------------------

        #Nightmare
        self.nightmare_1 = Nightmare()
        self.nightmare_2 = Nightmare()

        #HellHound
        self.red_hound_1 = HellHound()
        self.red_hound_2 = HellHound()
        self.green_hound_1 = HellHound()
        self.green_hound_2 = HellHound()


        #HellBeast
        self.hell_beast = HellBeast()
        self.hell_fire_beast = HellFireBeast()
        self.ball = self.hell_beast.fire_ball
        self.ball_f = self.hell_fire_beast.fire_ball  
        #------------------------------------------------------------------------
        
        #Skeleton
        self.skeleton = GreenSkeleton()

        #FirstStack---------------------------------------------------------------

        self.green_hound_1.sprite.position = (550,400)
        self.green_hound_1.sprite.color = (0,255,0)
        self.green_hound_1.sprite.scale_x = -1
        self.green_hound_1.lifes = 3

        self.green_hound_2.sprite.position = (650,400)
        self.green_hound_2.sprite.color = (0,255,0)
        self.green_hound_2.lifes = 3

        self.hell_beast.sprite.position =  (1000,420)
        self.hell_beast.sprite.color = (0,255,0)
        self.hell_beast.fire_ball.color = (0,255,0)
    

        #SecondStack
        self.red_hound_1.sprite.position = (1350,400)
        self.red_hound_1.sprite.color = (255,0,0)
        self.red_hound_1.sprite.scale_x = -1
        self.red_hound_1.lifes = 3

        self.red_hound_2.sprite.position = (1450,400)
        self.red_hound_2.sprite.color = (255,0,0)
        self.red_hound_2.lifes = 3

        #third
        self.nightmare_1.sprite.position = (1700,420)
        self.nightmare_1.sprite.color = (255,0,0)
        self.hell_fire_beast.sprite.position = (1900,430)
        self.hell_fire_beast.sprite.color = (255,0,0)
        self.hell_fire_beast.fire_ball.color = (255,0,0)

        #fourth
        self.nightmare_2.sprite.position = (2150,420)
        self.nightmare_2.sprite.color = (0,255,0)

        self.skeleton.sprite.position = (2500, 420)
        self.skeleton.sprite.scale = 2
        self.skeleton.sprite.scale_x = -1
        self.skeleton.sprite.color = (255,0,0)
        

        #--------------------------------------------------------------------------
        self.skeleton_is_alive = True
        self.run_r = False
        self.run_l = False
        self.attacks = False
        self.run_r = False
        self.run_l = False
        self.life = 3
        self.sprite = Sprite(animations.anim_i)

        self.can_attack = True

        self.sprite.position = (100, 410)
        self.sprite.scale = 2
        self.sprite.scale_x = 1
        self.sprite.velocity = (0,0)
        self.attack = False
        self.flag = False
        self.x_y = 0
        

        self.mirror_sprite = Sprite(animations.anim_i)
        self.mirror_sprite.position = (100, 320)
        self.mirror_sprite.scale = -2
        self.mirror_sprite.scale_x = -1
        self.mirror_sprite.velocity = (0,0)
        self.mirror_sprite.color = (0, 0, 0)
        
        #FirstStack
        self.add(self.green_hound_1)
        self.add(self.green_hound_2)
        self.add(self.hell_beast)
        self.add(self.ball)
        self.ball.visible = False

        #SecondStack
        self.add(self.red_hound_1)
        self.add(self.red_hound_2)

        #ThirdStack
        self.add(self.nightmare_1)
        self.add(self.hell_fire_beast)
        self.add(self.ball_f)
        self.ball_f.visible = False

        #FourthStack
        self.add(self.nightmare_2)
        self.add(self.skeleton)
        #Hearts
        self.add(self.heart1)
        self.add(self.heart2)
        self.add(self.heart3)
        #-------------------------------------
        self.add(self.sprite)
        self.add(self.mirror_sprite)
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def get_fire(self, enemy,hp):
        if enemy.flag:
                if enemy.lifes != 0:
                    enemy.lifes -= hp
                    print('Enemy lifes: ',enemy.lifes)
                    
                else:
                    enemy.sprite.position = (10000, -1000)
                    enemy.visible = False
                    print('emeny`s dead')
                    self.flag = False
    
    def get_flag(self, enemy,hp):
        if enemy.flag:
                if enemy.lifes != 0:
                    enemy.lifes -= hp
                    print('Enemy lifes: ', enemy.lifes)
                    
                else:
                    enemy.sprite.position = (10000, -1000)
                    enemy.visible = False
                    print('emeny`s dead')

    def get_skeleton_flag(self, enemy,hp):
        if not enemy.first_death:
            if enemy.flag:
                    if enemy.lifes >= 0:
                        enemy.lifes -= hp
                        print('Enemy lifes: ', enemy.lifes)
                        
                    else:
                        self.skeleton_is_alive = False
                        self.remove(enemy)
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

                self.mirror_sprite.scale_x = 1
                self.mirror_sprite.image = animations.anim_r

        if k == key.B:
            if not self.is_dead:
                self.sprite.image = animations.anim_b


        if k == 65363:
            if not self.is_dead:
                self.run_r = True
                self.sprite.scale_x = 1
                self.sprite.image = animations.anim_r

                self.mirror_sprite.scale_x = -1
                self.mirror_sprite.image = animations.anim_r
        if k == key.B:
            if not self.is_dead:
                self.sprite.image = animations.anim_b   
                self.mirror_sprite.image = animations.anim_b

        if k == key.Z:
            if not self.is_dead:
                #FirstStack
                self.get_flag(self.green_hound_1,1)
                self.get_flag(self.green_hound_2,1)
                self.get_fire(self.hell_beast,1)

                #SecondStack
                self.get_flag(self.red_hound_1,1)
                self.get_flag(self.red_hound_2,1)
                
                #ThirdStack
                self.get_flag(self.nightmare_1,1)
                self.get_fire(self.hell_fire_beast,1)

                #FourthStack
                self.get_flag(self.nightmare_2,1)
                self.get_skeleton_flag(self.skeleton,1)
                '''
                get flag add logic for our hero`s hit, when our hero attacks enemy
                enemy lost his 1 or more lifes
                if enemy has 0 lifes his position equals (10000, -1000) and his visible = False
                '''
        if k == key.X:
            if not self.is_dead:
                #FirstStack
                self.get_flag(self.green_hound_1, 1.5)
                self.get_flag(self.green_hound_2,1.5)
                self.get_fire(self.hell_beast,1.5) 
                
                #SecondStack
                self.get_flag(self.red_hound_1,1.5)
                self.get_flag(self.red_hound_2,1.5)
                #ThirdStack
                self.get_flag(self.nightmare_1,1.5)
                self.get_fire(self.hell_fire_beast,1.5)

                #FourthStack
                self.get_flag(self.nightmare_2,1.5)
                self.get_skeleton_flag(self.skeleton,1.5)
                '''
                get flag add logic for our hero`s hit, when our hero attacks enemy
                enemy lost his 1 or more lifes
                if enemy has 0 lifes his position equals (10000, -1000) and his visible = False
                ''' 
    def on_key_release(self, k, m):
        if k == key.B:
            if not self.is_dead:
                self.sprite.image = animations.anim_b
                self.mirror_sprite.image = animations.anim_b
                self.run_l = False
                self.run_r = False
            
        if k == key.Z:
            if not self.is_dead:
                self.run_l = False
                self.run_r = False
                self.sprite.image = animations.anim_a1
                self.mirror_sprite.image = animations.anim_a1
        elif k == key.X:
            if not self.is_dead:
                self.run_l = False
                self.run_r = False
                self.sprite.image = animations.anim_a2
                self.mirror_sprite.image = animations.anim_a2
        else:
                self.sprite.image = animations.anim_i
                self.mirror_sprite.image = animations.anim_i
                self.run_l = False
                self.run_r = False

    def beast_action(self, position, enemy, fire_ball):
        
        x, y = self.sprite.position
        xm, ym = self.mirror_sprite.position
        b_x, b_y = enemy.sprite.position
        
        
        '''
        when our hero is in start of level then is dead = false
        and he can be attack
        '''
        if self.sprite.position[0] < 120:
            fire_ball.position = (b_x, b_y)
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
            self.mirror_sprite.position = xm-5, ym 
        if (b_x - x) < position:
            if (fire_ball.position[0]-x) < 10:
                if (self.sprite.image == animations.anim_a1 or self.sprite.image == animations.anim_a2) and self.sprite.scale_x == 1:
                    fire_ball.position = (b_x, b_y)
    
                elif self.can_attack:
                    self.can_attack = False
                    # logic for visible heart
                    if(self.life == 3):
                        self.sprite.do(FadeOut(2) + MoveTo((100, 410), 2) + FadeIn(1))
                        self.mirror_sprite.do(FadeOut(2) + MoveTo((100, 320), 2) + FadeIn(1))
                        self.heart1.sprite.visible = True
                        self.heart2.sprite.visible = True
                        self.heart3.sprite.visible = True
                        self.heart1.do(Show() + Delay(2) + Hide())
                        self.heart2.do(Show() + Delay(2) + Hide())
                        self.heart3.do(Show() + Blink(10,2))
                    elif(self.life == 2):
                        self.sprite.do(FadeOut(3) + MoveTo((100, 410), 2) + FadeIn(1))
                        self.mirror_sprite.do(FadeOut(2) + MoveTo((100, 320), 2) + FadeIn(1))
                        self.heart1.sprite.visible = True
                        self.heart2.sprite.visible = True
                        self.heart3.sprite.visible = True
                        self.heart1.do(Show() + Delay(2) + Hide())
                        self.heart2.do(Show() + Blink(10,2))
                    elif(self.life == 1):              
                        self.sprite.do(FadeOut(1) + MoveTo((100, 410), 1) + FadeIn(1))
                        self.mirror_sprite.do(FadeOut(2) + MoveTo((100, 320), 2) + FadeIn(1))
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
                fire_ball.do(MoveBy((-1,0), 0.6) + MoveBy((-550, 0), 1))
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
                    enemy.sprite._animation = enemy.get_run_animation()
                    enemy.sprite.scale_x = l     
                    enemy.sprite.position = (w_x - speed, w_y)
                elif (w_x-self.x_y) <= 0:
                    enemy.sprite.scale_x = r     
                    enemy.sprite.position = (w_x + speed, w_y)
                '''
                when our hero makes block, enemy move away from hero by 100px
                '''
                if self.sprite.image == animations.anim_b and (w_x - x) <= 40 and (w_x - x) >= 0:
                    enemy.sprite.position = (w_x+180, w_y)
                if self.sprite.image == animations.anim_b and (w_x - x) <= 0 and (w_x - x) >= -40:
                    enemy.sprite.position = (w_x-180, w_y)
            
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
                    self.sprite.do(FadeOut(2) + MoveTo((100, 410), 2) + FadeIn(1))
                    self.mirror_sprite.do(FadeOut(2) + MoveTo((100, 320), 2) + FadeIn(1))
                    self.heart1.sprite.visible = True
                    self.heart2.sprite.visible = True
                    self.heart3.sprite.visible = True
                    self.heart1.do(Show() + Delay(2) + Hide())
                    self.heart2.do(Show() + Delay(2) + Hide())
                    self.heart3.do(Show() + Blink(10,2))
                elif(self.life == 2):
                    self.sprite.do(FadeOut(3) + MoveTo((100, 410), 2) + FadeIn(1))
                    self.mirror_sprite.do(FadeOut(2) + MoveTo((100, 320), 2) + FadeIn(1))
                    self.heart1.sprite.visible = True
                    self.heart2.sprite.visible = True
                    self.heart3.sprite.visible = True
                    self.heart1.do(Show() + Delay(2) + Hide())
                    self.heart2.do(Show() + Blink(10,2))
                elif(self.life == 1):
                    self.sprite.do(FadeOut(1) + MoveTo((100, 410), 1) + FadeIn(1))
                    self.mirror_sprite.do(FadeOut(2) + MoveTo((100, 320), 2) + FadeIn(1))
                    print("dead 0")
                self.is_dead = True
                self.life -= 1
                    
                print(self.life)
    def skeleton_action(self, position, enemy, speed, l, r):
        
        x, y = self.sprite.position
        
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
    

        if enemy.lifes < 4:
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
                if(self.life == 3):
                    self.sprite.do(FadeOut(2) + MoveTo((100, 410), 2) + FadeIn(1))
                    self.mirror_sprite.do(FadeOut(2) + MoveTo((100, 320), 2) + FadeIn(1))
                    self.heart1.sprite.visible = True
                    self.heart2.sprite.visible = True
                    self.heart3.sprite.visible = True
                    self.heart1.do(Show() + Delay(2) + Hide())
                    self.heart2.do(Show() + Delay(2) + Hide())
                    self.heart3.do(Show() + Blink(10,2))
                elif(self.life == 2):
                    self.sprite.do(FadeOut(3) + MoveTo((100, 410), 2) + FadeIn(1))
                    self.mirror_sprite.do(FadeOut(2) + MoveTo((100, 320), 2) + FadeIn(1))
                    self.heart1.sprite.visible = True
                    self.heart2.sprite.visible = True
                    self.heart3.sprite.visible = True
                    self.heart1.do(Show() + Delay(2) + Hide())
                    self.heart2.do(Show() + Blink(10,2))
                elif(self.life == 1):
                    self.sprite.do(FadeOut(1) + MoveTo((100, 410), 1) + FadeIn(1))
                    self.mirror_sprite.do(FadeOut(2) + MoveTo((100, 320), 2) + FadeIn(1))
                    print("dead 0")
                self.is_dead = True
                self.life -= 1
                    
                print(self.life)

            if not self.is_dead:
                if (w_x - x) < position and (w_x - x) >= 0:
                    if (w_x-x) < 50 and (w_x - x) >= 0:
                        
                        enemy.flag = True
                        enemy.sprite._animation = enemy.get_attack()
                        enemy.sprite.do(Delay(0.8) + MoveTo((w_x, w_y+1), 0))
                        
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
                        enemy.sprite.do(Delay(0.8) + MoveTo((w_x, w_y+1), 0))
                    else:
                        enemy.sprite.scale_x = 1
                        enemy.sprite._animation = enemy.get_walk()
                        enemy.sprite.scale = 2
                        enemy.sprite.position = (w_x + speed, 390)
                    
                else:
                    enemy.flag = False
                    enemy.sprite.position = (w_x, 405)
                    enemy.sprite._animation = enemy.anim

    def update(self, dt):
        x,y = self.sprite.position
        xm, ym = self.mirror_sprite.position
        if(x <=20 ):
            self.run_l = False
            self.run_r = False
            self.sprite.position = (30,410)
            self.mirror_sprite.position = (30,320)
        if self.life == 0:
            self.life = 3
            director.push(ZoomTransition(GameOver.get_gameover(2)))
            self.kill()
        
       
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
        '''
        # first stack --------------------------------------------
        self.wolf_action(200, self.green_hound_1, 3, -1, 1)
        self.wolf_action(200, self.green_hound_2, 3, -1, 1)
        self.beast_action(300,self.hell_beast, self.ball)
        # second stack -------------------------------------------
        self.wolf_action(200, self.red_hound_1, 3, -1, 1)
        self.wolf_action(200, self.red_hound_2, 3, -1, 1)
        # third stack --------------------------------------------
        self.beast_action(300, self.hell_fire_beast, self.ball_f)
        self.wolf_action(200, self.nightmare_1, 2.5, -1, 1)

        #fourth --------------------------------------------------
        self.wolf_action(200, self.nightmare_2, 2.5, -1, 1) '''
        self.skeleton_action(300, self.skeleton, 2, -1, 1)
        

        if self.life == 0:
            import GameOver
            self.life = 3
            director.push(ZoomTransition(GameOver.get_gameover(2)))
            self.kill()
        if(self.sprite.position > (2755,y) and self.skeleton_is_alive == False):
            import Level3_Background
            director.push(SlideInTTransition(Level3_Background.get_newgame()))
        elif(x >= 2755):
            self.sprite.position = (2750,410)
            self.mirror_sprite.position = (2750,320)