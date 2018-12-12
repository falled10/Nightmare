import cocos
from cocos.actions import *
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
from Level2_Monsters import *
from Level1_Monsters import *
import animations
import random


director.window.pop_handlers()
keyboard = key.KeyStateHandler()
director.window.push_handlers(keyboard)

class Level3_Hero(ScrollableLayer):
    is_event_handler = True

    def __init__(self):
        super().__init__()

        #FirstStack
        self.axe_skeleton_1 = AxeSkeleton()
        self.axe_skeleton_1.sprite.position = (500, 225)
        self.axe_skeleton_1.sprite.scale = 3
        self.axe_skeleton_1.sprite.scale_x = -1
        self.add(self.axe_skeleton_1)

        self.ghost_1 = Ghost()
        self.ghost_1.sprite.position = (700, 200)

        self.


        # boss monsters --------------------------------
        self.axe_skeleton_b = AxeSkeleton()
        self.axe_skeleton_b.sprite.visible = False
        self.axe_skeleton_b .sprite.scale = 3
        self.add(self.axe_skeleton_b )

        self.ghost_b = Ghost()
        self.ghost_b.sprite.visible = False
        self.add(self.ghost_b)

        self.blue_wolf_b = MiddleWolf()
        self.blue_wolf_b.sprite.visible = False
        self.add(self.blue_wolf_b)

        self.hell_hound_b = HellHound()
        self.hell_hound_b.sprite.visible = False
        self.add(self.hell_hound_b)

        self.green_hound_b = HellHound()
        self.green_hound_b.sprite.color = (0,255,0)
        self.green_hound_b.lifes = 3
        self.green_hound_b.l = 3
        self.green_hound_b.sprite.visible = False
        self.add(self.green_hound_b)

        self.red_hound_b = HellHound()
        self.red_hound_b.sprite.color = (255,0,0)
        self.red_hound_b.lifes = 3
        self.red_hound_b.l = 3
        self.red_hound_b.sprite.visible = False
        self.add(self.red_hound_b)

        self.nightmare_b = Nightmare()
        self.nightmare_b.sprite.visible = False
        self.add(self.nightmare_b)

        self.red_nightmare_b = Nightmare()
        self.red_nightmare_b.sprite.color = (255,0,0)
        self.red_nightmare_b.lifes = 4
        self.red_nightmare_b.l = 4
        self.red_nightmare_b.sprite.visible = False
        self.add(self.red_nightmare_b)

        self.green_nightmare_b = Nightmare()
        self.green_nightmare_b.sprite.color = (0, 255, 0)
        self.green_nightmare_b.lifes = 4
        self.green_nightmare_b.l = 4
        self.green_nightmare_b.sprite.visible = False
        self.add(self.green_nightmare_b)

        self.hell_beast_b = HellBeast()
        self.hell_beast_b.sprite.visible = False
        self.hell_ball_b = self.hell_beast_b.fire_ball
        self.hell_ball_b.visible = False
        self.add(self.hell_beast_b)
        self.add(self.hell_ball_b)

        self.green_hell_beast_b = HellBeast()
        self.green_hell_beast_b.sprite.color = (0, 255, 0)
        self.green_hell_beast_b.sprite.visible = False
        self.green_hell_beast_b.lifes = 3
        self.green_hell_ball_b = self.green_hell_beast_b.fire_ball
        self.green_hell_ball_b.color = (0, 255, 0)
        self.green_hell_ball_b.visible = False
        self.add(self.green_hell_beast_b)
        self.add(self.green_hell_ball_b)
        # --------------------------------------------------------------
    


        self.list_of_monsters = [     
            self.axe_skeleton_b,
            self.blue_wolf_b, 
            self.hell_hound_b,
            self.hell_beast_b,
            self.red_hound_b,
            self.green_hound_b,
            self.nightmare_b,
            self.red_nightmare_b,
            self.green_nightmare_b,
            self.green_hell_beast_b,
            self.ghost_b,
            ]

        
        self.boss = DemonBoss()
        self.boss.sprite.position = (1000, 200)
        

        self.is_dead = False
     
        self.run_r = False
        self.run_l = False
        
    
        
        
        self.life = 3
        self.sprite = Sprite(animations.anim_i)

        self.can_attack = True
        
        self.sprite.position = (100, 215)
        self.sprite.scale = 2
        self.sprite.scale_x = 1
        self.sprite.velocity = (0,0)
        self.attack = False
        self.flag = False
        self.x_y = 0

        #FirstStack
        self.add(self.axe_skeleton_1)
        self.add(self.ghost_1)

        #
        self.add(self.boss)
        

        #-------------------------------------
        self.add(self.sprite)
        self.boss_flag = False
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def get_skeleton_flag(self, enemy, hp):
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

    
    def get_fire(self, enemy,hp):
        if enemy.flag:
                if enemy.lifes >= 0:
                    enemy.lifes -= hp
                    print('beast lifes: ',enemy.lifes)
                    
                else:
                    enemy.sprite.position = (10000, -1000)
                    print('emeny`s dead')
                    self.flag = False
    
    
    def get_flag(self, enemy, hp):
        if enemy.flag:
                if enemy.lifes >= 0:
                    enemy.lifes -= hp
                    print('Enemy lifes: ', enemy.lifes)
                    
                else:
                    enemy.sprite.position = (10000, -1000)
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
                self.get_skeleton_flag(self.axe_skeleton_1,1)
                self.get_flag(self.ghost_1,1)
                #BOSS    
                self.get_flag(self.boss,1)
                self.get_skeleton_flag(self.axe_skeleton_b,1)
                self.get_flag(self.ghost_b,1)
                self.get_flag(self.blue_wolf_b,1)
                self.get_fire(self.hell_beast_b,1)  
                self.get_flag(self.hell_hound_b,1)
                self.get_flag(self.red_hound_b,1)
                self.get_flag(self.green_hound_b,1)
                self.get_flag(self.nightmare_b,1)
                self.get_flag(self.red_nightmare_b,1)
                self.get_flag(self.green_nightmare_b,1)
                self.get_fire(self.green_hell_beast_b,1)
               
                
                
                '''
                get flag add logic for our hero`s hit, when our hero attacks enemy
                enemy lost his 1 or more lifes
                if enemy has 0 lifes his position equals (10000, -1000) and his visible = False
                '''

        if k == key.X:
            if not self.is_dead:
                #FirstStack
                self.get_skeleton_flag(self.axe_skeleton_1,1)
                self.get_flag(self.ghost_1,1)
                #BOSS    
                self.get_flag(self.boss,1.5)
                self.get_skeleton_flag(self.axe_skeleton_b,1.5)
                self.get_flag(self.ghost_b,1.5)
                self.get_flag(self.blue_wolf_b,1.5)
                self.get_fire(self.hell_beast_b,1.5)  
                self.get_flag(self.hell_hound_b,1.5)
                self.get_flag(self.red_hound_b,1.5)
                self.get_flag(self.green_hound_b,1.5)
                self.get_flag(self.nightmare_b,1.5)
                self.get_flag(self.red_nightmare_b,1.5)
                self.get_flag(self.green_nightmare_b,1.5)
                self.get_fire(self.green_hell_beast_b,1.5)
        if k == key.C:
            if not self.is_dead:
                #FirstStack
                self.get_skeleton_flag(self.axe_skeleton_1,1)
                self.get_flag(self.ghost_1,1)
                #BOSS    
                self.get_flag(self.boss,2)
                self.get_skeleton_flag(self.axe_skeleton_b,2)
                self.get_flag(self.ghost_b,2)
                self.get_flag(self.blue_wolf_b,2)
                self.get_fire(self.hell_beast_b,2)  
                self.get_flag(self.hell_hound_b,2)
                self.get_flag(self.red_hound_b,2)
                self.get_flag(self.green_hound_b,2)
                self.get_flag(self.nightmare_b,2)
                self.get_flag(self.red_nightmare_b,2)
                self.get_flag(self.green_nightmare_b,2)
                self.get_fire(self.green_hell_beast_b,2)

        
               
        
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

        elif k == key.X:
            if not self.is_dead:
                self.run_l = False
                self.run_r = False
                self.sprite.image = animations.anim_a2
            
        elif k == key.C:
            if not self.is_dead:
                self.run_l = False
                self.run_r = False
                self.sprite.image = animations.anim_a3
        else:
            self.sprite.image = animations.anim_i
            self.run_l = False
            self.run_r = False

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
                self.sprite.do(FadeOut(2) + MoveTo((100, 180), 2) + FadeIn(1))
            elif(self.life == 2):
                self.sprite.do(FadeOut(3) + MoveTo((100, 180), 2) + FadeIn(1))
            elif(self.life == 1):
                self.sprite.do(FadeOut(1) + MoveTo((100, 180), 1) + FadeIn(1))
                print("dead 0")
            self.is_dead = True
            self.life -= 1
                
            print(self.life)

    def beast_action(self, position, enemy, fire_ball):
        
        x, y = self.sprite.position
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
        if (b_x - x) > position:
            self.flag = False

        '''
        when our flag = true we start move back from enemy until flag = false
        '''
        if self.flag:
            self.sprite.position = x - 5, y
        if (b_x - x) < position:
            if (fire_ball.position[0]-x) < 10:
                if (self.sprite.image == animations.anim_a1 or self.sprite.image == animations.anim_a2) and self.sprite.scale_x == 1:
                    fire_ball.position = (b_x, b_y)
    
                elif self.can_attack:
                    self.can_attack = False
                    # logic for visible heart
                    if(self.life == 3):
                        self.sprite.do(FadeOut(2) + MoveTo((100, 180), 2) + FadeIn(1))
                    elif(self.life == 2):
                        self.sprite.do(FadeOut(3) + MoveTo((100, 180), 2) + FadeIn(1))

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

    
    def boss_action(self, position, enemy):
        # get coords of hero and enemy
        x, y = self.sprite.position
        b_x, b_y = enemy.sprite.position

        '''
        if boss had breath he sumon some monster in random choice
        '''
        if (b_x - x) > position and self.boss_flag:
            
            monster = random.choice(self.list_of_monsters)
            monster.sprite.position = (b_x-200, b_y)
            self.hell_ball_b.position = self.hell_beast_b.sprite.position
            self.green_hell_ball_b.position = self.green_hell_beast_b.sprite.position
            monster.lifes = monster.l
            monster.sprite.visible = True
        
        '''
        if hero is too close to boss
        boss start breath and hero start to move away from boss
        while self.flag = true, and stops when self.flag = false
        '''
        if self.boss_flag:
            enemy.sprite.scale = 1.5
            enemy.sprite._animation = enemy.get_attack()
            self.sprite.position = (x - 5, y)
        elif not self.boss_flag:
            enemy.sprite.scale = 1.5
            enemy.sprite._animation = enemy.anim
        
        #check if hero is in radius view of boss
        if (b_x - x) < 80:
            enemy.flag = True

        if (b_x - x) > 120:
            enemy.flag = False
        if (b_x - x) < 80:
            
            self.boss_flag = True
            
        elif (b_x - x) > position:
            
            self.boss_flag = False
       




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
                    self.sprite.do(FadeOut(1) + MoveTo((100, 180), 1) + FadeIn(1))
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
                    self.sprite.do(FadeOut(1) + MoveTo((100, 180), 1) + FadeIn(1))
                    
                    print(self.life)
                else:
                    enemy.sprite._animation = enemy.anim
                    enemy.sprite.scale_x = -1
                    enemy.sprite.position = (g_x + speed, g_y)

    def skeleton_action(self, position, enemy, speed, l, r):
        
        x, y = self.sprite.position
        
        w_x, w_y = enemy.sprite.position
        if x <120:
            
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
            if w_y == 181 and enemy.lifes >= 0 and (w_x-x) < 50 and (w_x - x) >= -50 and not self.is_dead:
                self.is_dead = True
                if(self.life == 3):
                    self.sprite.do(FadeOut(2) + MoveTo((100, 180), 2) + FadeIn(1))
                elif(self.life == 2):
                    self.sprite.do(FadeOut(3) + MoveTo((100, 180), 2) + FadeIn(1))

                elif(self.life == 1):
                    self.sprite.do(FadeOut(1) + MoveTo((100, 180), 1) + FadeIn(1))
                    print("dead 0")
                self.is_dead = True
                self.life -= 1
                    
                print(self.life)

            if not self.is_dead:
                if (w_x - x) < position and (w_x - x) >= 0:
                    if (w_x-x) < 50 and (w_x - x) >= 0:
                        
                        enemy.flag = True
                        enemy.sprite.scale = 2.7
                        enemy.sprite._animation = enemy.get_attack()
                        enemy.sprite.do(Delay(0.8) + MoveTo((w_x, w_y+1), 0))
                        
                    else:
                        enemy.flag = False
                        enemy.sprite.scale_x = -1
                        enemy.sprite._animation = enemy.get_walk()
                        enemy.sprite.scale = 2.7
                        enemy.sprite.position = (w_x - speed, w_y)

                elif (w_x - x) <= 0 and (w_x - x) > -position:
                    if (w_x-x) > -50 and (w_x - x) <= 0:
                        enemy.flag = True
                        enemy.sprite.scale = 2.7
                        enemy.sprite._animation = enemy.get_attack()
                        enemy.sprite.do(Delay(0.8) + MoveTo((w_x, w_y+1), 0))
                    else:
                        enemy.sprite.scale_x = 1
                        enemy.sprite._animation = enemy.get_walk()
                        enemy.sprite.scale = 2.7
                        enemy.sprite.position = (w_x + speed, w_y)
                    
                else:
                    enemy.flag = False
                    enemy.sprite.position = (w_x, w_y)
                    enemy.sprite._animation = enemy.anim

    def update(self, dt):
        #BOSS
        if self.axe_skeleton_b.sprite.visible:
            self.skeleton_action(350, self.axe_skeleton_b, 1, -1, 1)
        if self.blue_wolf_b.sprite.visible:
            self.wolf_action(350, self.blue_wolf_b, 2, 1, -1)
        if self.hell_hound_b.sprite.visible:
            self.wolf_action(350, self.hell_hound_b, 2, 1, -1)
        if self.hell_beast_b.sprite.visible:
            self.beast_action(300, self.hell_beast_b, self.hell_ball_b)  
        if self.red_hound_b.sprite.visible:
            self.wolf_action(350, self.red_hound_b, 3, -1, 1)
        if self.green_hound_b.sprite.visible:
            self.wolf_action(350, self.green_hound_b, 3, -1, 1)
        if self.nightmare_b.sprite.visible:
            self.wolf_action(350, self.nightmare_b, 3, -1, 1)
        if self.red_nightmare_b.sprite.visible:
            self.wolf_action(350, self.red_nightmare_b, 3, -1, 1)
        if self.green_nightmare_b.sprite.visible:
            self.wolf_action(350, self.green_nightmare_b, 3, -1, 1)
        if self.green_hell_beast_b.sprite.visible:
            self.beast_action(300, self.green_hell_beast_b, self.green_hell_ball_b)
        if self.ghost_b.sprite.visible:
            self.ghost_action(350,self.ghost_b, 2)
        
        #first stack

        self.skeleton_action(100, self.axe_skeleton_1, 1, -1, 1)
        #self.boss_action(350, self.boss)
        #self.ghost_action(200,self.ghost, 3)

        x, y = self.sprite.position
        if(x <=20 ):
            self.run_l = False
            self.run_r = False
            self.sprite.position = (30,180)
       
        if self.run_l:
            self.sprite.position = (x - 3, y)
        elif self.run_r:
            self.sprite.position = (x + 3, y)
        Level3_Background.scroller_3.set_focus(self.sprite.position[0], self.sprite.position[1])
        if self.life == 0:
            import GameOver
            self.life = 3
            director.push(ZoomTransition(GameOver.get_gameover(3)))
            self.kill()
       
