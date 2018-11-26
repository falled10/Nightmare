import cocos
import cocos.actions as ac
import pyglet
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
from Level1_Monsters import WhiteWolf


flag = 10

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
        self.white_wolf = WhiteWolf()
        #run right --------------------------------------------------
        self.img_r = pyglet.image.load('res/animation/run/adventurer-run3-sword-Sheet.png')
        self.img_grid_r = pyglet.image.ImageGrid(self.img_r, 1, 6, item_width=50, item_height=37 )
        self.anim_r = pyglet.image.Animation.from_image_sequence(self.img_grid_r[0:], 0.1, loop=True)
        # ----------------------------------------------------------
        
        #attack1
        self.img_a1 = pyglet.image.load('res/animation/attack1/Attacksheet.png')
        self.img_grid_a1 = pyglet.image.ImageGrid(self.img_a1, 1, 5, item_width=50, item_height=37 )

        self.anim_a1 = pyglet.image.Animation.from_image_sequence(self.img_grid_a1[0:], 0.1, loop=True)
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
        self.img_j = pyglet.image.load('jump/jumpsheet.png')
        self.img_grid_j = pyglet.image.ImageGrid(self.img_j, 1, 4, item_width=50, item_height=37)

        self.anim_j = pyglet.image.Animation.from_image_sequence(self.img_grid_j[0:], 0.2, loop=True)
        #------------------------------------------------------------------

        self.life = 3
        self.sprite = Sprite(self.anim_i)
        self.sprite.position = (100, 180)
        self.sprite.scale = 2
        self.sprite.scale_x = 1
        self.sprite.velocity = (0,0)
        
        self.sprite.do(Mover())
        self.add(self.white_wolf)
        self.add(self.sprite)
        
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def on_key_press(self, k, m):
        print(k)
        if k == 65361:
            self.sprite.scale_x = -1
            self.sprite._animation = self.anim_r

        if k == 65363:
            self.sprite.scale_x = 1
            self.sprite._animation = self.anim_r

        if k == 65362:
            x, y = self.sprite.position
            if self.sprite.scale_x == -1:
                if y == 180:
                    self.sprite.do(ac.JumpBy((-100, 0), 100, 1, 1))
                    self.sprite._animation = self.anim_j
            else:        
                if y == 180:
                    self.sprite.do(ac.JumpBy((100, 0), 100, 1, 1))
                    self.sprite._animation = self.anim_j


        if k == key.Z:
            self.sprite._animation = self.anim_a1

        if k == key.X:
            self.sprite._animation = self.anim_a2

        if k == key.C:
            self.sprite._animation = self.anim_a3

      

    def on_key_release(self, k, m):
        self.sprite._animation = self.anim_i

    def wolf_action(self):
        x, y = self.sprite.position
        w_x, w_y = self.white_wolf.sprite.position
        if (w_x-x) < 200:
            if w_x <= x:
                w_x += 0
                self.white_wolf.sprite.position = w_x, w_y
                return
            self.white_wolf.sprite.scale_x = -1
            w_x -= 4
            self.white_wolf.sprite.position = w_x, w_y

        if (w_x - x) < 20:
            if self.sprite._animation == self.anim_a1:
                self.white_wolf.sprite.visible = False
                print('wolf dead')
            else:
                if self.white_wolf.sprite.visible == True:
                    if self.life == 0:
                        import GameOver
                        flag = True
                        director.push(ZoomTransition(GameOver.get_gameover()))
                        self.life = 3
                        self.sprite.position = (100, 180)
                        
                    else:
                        self.life -= 1
                        self.sprite.position = (100, 180)
                    


    def update(self, dt):
        self.wolf_action()
        



        
