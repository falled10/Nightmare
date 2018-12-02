import cocos
import cocos.actions as ac
import pyglet
import time
from cocos.director import director
from collections import defaultdict
from pyglet.window import key
from cocos.layer import ScrollableLayer
from cocos.scenes.transitions import *
from cocos.actions import Move
from cocos.sprite import Sprite
import Level1_Background
from cocos.scene import Scene
from cocos.scenes.transitions import *
from Level1_Monsters import WhiteWolf, BlueWolf
import Sound



director.window.pop_handlers()
keyboard = key.KeyStateHandler()
director.window.push_handlers(keyboard)

class Mover(Move):
    def step(self,dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 180
        self.target.velocity = (vel_x, 0)
        Level1_Background.scroller_1.set_focus(self.target.x, self.target.y)

class Level1_Hero(ScrollableLayer):
    is_event_handler = True

    def __init__(self):
        super().__init__()

        #hearts---------------------------------------------------------------------------

        heart1 = Sprite('res/maps/heart1.png')
        heart1.position = (25,570)
        self.add(heart1)
        heart2 = Sprite('res/maps/heart2.png')
        heart2.position = (70,570)
        self.add(heart2)
        heart3 = Sprite('res/maps/heart1.png')
        heart3.position = (115,570)
        self.add(heart3)

        #----------------------------------------------------------------------------------
        self.white_wolf = WhiteWolf()
        self.blue_wolf = BlueWolf()
        self.blue_wolf2 = BlueWolf()
        self.blue_wolf2.sprite.position = (1100, 160)
        #run right --------------------------------------------------
        self.img_r = pyglet.image.load('res/animation/run/adventurer-run3-sword-Sheet.png')
        self.img_grid_r = pyglet.image.ImageGrid(self.img_r, 1, 6, item_width=50, item_height=37 )
        self.anim_r = pyglet.image.Animation.from_image_sequence(self.img_grid_r[0:], 0.1, loop=True)
        # ----------------------------------------------------------
        
        #attack1
        self.img_a1 = pyglet.image.load('res/animation/attack1/Attacksheet.png')
        self.img_grid_a1 = pyglet.image.ImageGrid(self.img_a1, 1, 5, item_width=50, item_height=37 )

        self.anim_a1 = pyglet.image.Animation.from_image_sequence(self.img_grid_a1[0:], 0.05, loop=False)
        #------------------------------------------------------------------

        #attack2
        self.img_a2 = pyglet.image.load('res/animation/attack2/attack2sheet.png')
        self.img_grid_a2 = pyglet.image.ImageGrid(self.img_a2, 6, 1, item_width=50, item_height=37)
        self.anim_a2 = pyglet.image.Animation.from_image_sequence(self.img_grid_a2[::-1], 0.1, loop=True)
        #------------------------------------------------------------------

        #attack3
        self.img_a3 = pyglet.image.load('res/animation/attack3/attack3sheet.png')
        self.img_grid_a3 = pyglet.image.ImageGrid(self.img_a3, 6, 1, item_width=50, item_height=37)
        self.anim_a3 = pyglet.image.Animation.from_image_sequence(self.img_grid_a3[::-1], 0.1, loop=True)
        #-------------------------------------------------------------------

        # idle
        self.img_i = pyglet.image.load('res/animation/idle/idlesheet.png')
        self.img_grid_i = pyglet.image.ImageGrid(self.img_i, 1, 4, item_width=50, item_height=37 )

        self.anim_i = pyglet.image.Animation.from_image_sequence(self.img_grid_i[0:], 0.3, loop=True)
    
        #_-----------------------------------------------------------------

        # jump
        self.img_j = pyglet.image.load('res/animation/jump/jumpsheet.png')
        self.img_grid_j = pyglet.image.ImageGrid(self.img_j, 1, 4, item_width=50, item_height=37)

        self.anim_j = pyglet.image.Animation.from_image_sequence(self.img_grid_j[0:], 0.2, loop=True)
  
        #------------------------------------------------------------------

        # block
        self.img_b = pyglet.image.load('res/animation/block/blocksheet.png')
        self.img_grid_b = pyglet.image.ImageGrid(self.img_b, 3, 1, item_width=50, item_height=37)

        self.anim_b = pyglet.image.Animation.from_image_sequence(self.img_grid_b[0:], 0.3, loop=True)
  
        #------------------------------------------------------------------
    
       
        self.life = 3
        self.sprite = Sprite(self.anim_i)

        

        self.sprite.position = (100, 180)
        self.sprite.scale = 2
        self.sprite.scale_x = 1
        self.sprite.velocity = (0,0)
        self.flag = False
        
        self.sprite.do(Mover())
        self.add(self.blue_wolf)
        self.add(self.blue_wolf2)
        self.add(self.white_wolf)
        self.add(self.sprite)

        self.pressed = defaultdict(int)
        self.schedule(self.update)

   
    
    def get_flag(self, enemy):
        if enemy.flag:
                if enemy.lifes != 0:
                    enemy.lifes -= 1
                    
                else:
                    enemy.sprite.position = (-1000, 1000)
                    enemy.visible = False
                    print('emeny`s dead')

      

    def on_key_press(self, k, m):
        if k == 65361:
            self.sprite.scale_x = -1
            self.sprite.image = self.anim_r

        if k == 65363:
            self.sprite.scale_x = 1
            self.sprite.image = self.anim_r

        if k == 65362:
            x, y = self.sprite.position
            if self.sprite.scale_x == -1:
                if y == 180:
                    self.sprite.do(ac.JumpBy((-150, 0), 100, 1, 1))
                    self.sprite.image = self.anim_j
                    
            else:        
                if y == 180:

                    print(self.anim_j.get_duration())
                    self.sprite.do(ac.JumpBy((150, 0), 100, 1, 1))
                    self.sprite.image = self.anim_j
        if k == key.B:
            self.sprite.image = self.anim_b

        if k == key.Z:
            
            self.get_flag(self.white_wolf)
            self.get_flag(self.blue_wolf)
            self.get_flag(self.blue_wolf2)
            print(self.white_wolf.lifes)
            
        
    def on_key_release(self, k, m):
        if k == key.Z:
            self.sprite.image = self.anim_a1
        else:
            self.sprite.image = self.anim_i


    def wolf_action(self, position, enemy, speed):
        x, y = self.sprite.position
        w_x, w_y = enemy.sprite.position
        if enemy.sprite.visible  is not False:
            if (w_x-x) < position and (w_x-x) > 0:
                enemy.sprite._animation = enemy.get_idle_animation()
                enemy.sprite.scale_x = -1     
                enemy.sprite.position = (w_x-2, w_y)
            elif (w_x-x) < 0 and (w_x-x) > position:
                enemy.sprite.scale_x = 1     
                enemy.sprite.do(ac.MoveTo((x, w_y), speed))
                enemy.sprite.position = (w_x+2, w_y)
            if self.sprite.image == self.anim_b and (w_x - x) <= 40 and (w_x - x) >= 0:
                enemy.sprite.position = (w_x+80, w_y)
            if self.sprite.image == self.anim_b and (w_x - x) <= 0 and (w_x - x) >= -40:
                enemy.sprite.position = (w_x-80, w_y)
            if (w_x - x) <= 80 and (w_x - x) >= -80:
                enemy.flag = True
                if y <= 200 and (w_x - x) <= 30 and (w_x - x) >= -30:
     
                    if enemy.sprite.visible is True:
                        if self.life == 0:
                            import GameOver
                            director.push(ZoomTransition(GameOver.get_gameover(1)))
                            self.life = 3
                            self.sprite.position = (100, 180)            
                        else:
                            self.life -= 1
                            enemy.sprite.image = enemy.anim
                            self.sprite.position = (100, 180)
            elif (w_x - x) > 80 or (w_x - x) < -80:
                enemy.flag = False
        


    def update(self, dt):
        self.wolf_action(200, self.white_wolf, 0.7)
        self.wolf_action(200, self.blue_wolf, 0.5)
        self.wolf_action(200, self.blue_wolf2, 0.5)    


        
        
