import pyglet
from cocos.layer import ScrollableLayer
from cocos.sprite import Sprite



class SimpleWolf(ScrollableLayer):
    def __init__(self):
        super(SimpleWolf, self).__init__()

        #animation
        self.img = pyglet.image.load('res/animation/level1_monsters/wolf1/wolf-runing-cycle.png')
        self.img_grid = pyglet.image.ImageGrid(self.img, 1, 4, item_width=54, item_height=31)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[3:4], 0.2, loop=True)
        self.lifes = 1  
        self.flag = False
        self.sprite = Sprite(self.anim)
        self.sprite.scale = 1.4
        self.sprite.position = (800, 160)
        self.x = 0
        self.can_attack = False
        self.add(self.sprite)


    def get_run_animation(self):
        img = pyglet.image.load('res/animation/level1_monsters/wolf1/wolf-runing-cycle.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 4, item_width=54, item_height=31)
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.2, loop=True)
        return anim


class MiddleWolf(ScrollableLayer):
    def __init__(self):
        super(MiddleWolf, self).__init__()

        #animation
        self.img = pyglet.image.load('res/animation/level1_monsters/wolf2/wolf-runing-cycle-skin.png')
        self.img_grid = pyglet.image.ImageGrid(self.img, 1, 4, item_width=54, item_height=31)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[1:2], 0.2, loop=True)
        self.lifes = 2
        self.flag = False
        self.sprite = Sprite(self.anim)
        self.sprite.scale = 1.4
        self.sprite.position = (1000, 160)
        self.x = 0
        
        self.add(self.sprite)


    def get_run_animation(self):
        img = pyglet.image.load('res/animation/level1_monsters/wolf2/wolf-runing-cycle-skin.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 4, item_width=54, item_height=31)
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.2, loop=True)
        return anim


class HellHound(ScrollableLayer):
    def __init__(self):
        super(HellHound, self).__init__()

        #animation_idle
        self.img_i = pyglet.image.load('res/animation/level1_monsters/hell_hound/hell-hound-idle.png')
        self.img_grid_i = pyglet.image.ImageGrid(self.img_i, 1, 6, item_width=64, item_height=31)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid_i[0:], 0.2, loop=True)
        self.lifes = 2
        self.flag = False
        self.sprite = Sprite(self.anim)
        self.sprite.scale = 1.8
        self.sprite.position = (1200, 160)
        self.x = 0

        self.add(self.sprite)


    def get_run_animation(self):
        img = pyglet.image.load('res/animation/level1_monsters/hell_hound/hell-hound-run.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 5, item_width=67, item_height=31)
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.2, loop=True)
        return anim


class HellBeast(ScrollableLayer):
    def __init__(self):
        super(HellBeast, self).__init__()
        #ball animation
        self.img_b = pyglet.image.load('res/animation/level1_monsters/hell_beast/fire-ball.png')
        self.img_grid_b = pyglet.image.ImageGrid(self.img_b, 1, 6, item_width=19, item_height=15)
        self.anim_b = pyglet.image.Animation.from_image_sequence(self.img_grid_b[0:], 0.1   , loop=True)
        self.fire_ball = Sprite(self.anim_b)
        self.fire_ball.scale = 2
        self.fire_ball.position = (500, 200)

        self.ball_action = False

        #animation idle
        self.img_i = pyglet.image.load('res/animation/level1_monsters/hell_beast/hell-beast-idle.png')
        self.img_grid_i = pyglet.image.ImageGrid(self.img_i, 1, 6, item_width=55, item_height=67)
        self.anim_i = pyglet.image.Animation.from_image_sequence(self.img_grid_i[0:], 0.2, loop=True)
        self.lifes = 3
        self.flag = False
        self.sprite = Sprite(self.anim_i)
        self.sprite.position = (1200, 200)
        self.sprite.scale = 1.8
        self.x = 0

        self.add(self.sprite)

    def get_burn_animation(self):
        img = pyglet.image.load('res/animation/level1_monsters/hell_beast/hell-beast-burn.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 6, item_width=74, item_height=160)
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.05, loop=False)
        return anim
    
    def get_attack_animation(self):
        img = pyglet.image.load('res/animation/level1_monsters/hell_beast/hell-beast-breath.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 4, item_width=64, item_height=63)
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.262, loop=True)
        return anim

    def get_idle(self):
        return self.anim_i

    

