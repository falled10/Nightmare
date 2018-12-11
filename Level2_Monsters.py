import pyglet
from cocos.layer import ScrollableLayer
from cocos.sprite import Sprite


class HellFireBeast(ScrollableLayer):
    def __init__(self):
        super(HellFireBeast, self).__init__()
        #ball animation
        self.img_b = pyglet.image.load('res/animation/level2_monsters/hell_fire_beast/fire-ball.png')
        self.img_grid_b = pyglet.image.ImageGrid(self.img_b, 1, 6, item_width=19, item_height=15)
        self.anim_b = pyglet.image.Animation.from_image_sequence(self.img_grid_b[0:], 0.1   , loop=True)
        self.fire_ball = Sprite(self.anim_b)
        self.fire_ball.scale = 2
        

        self.ball_action = False

        #animation idle
        self.img_i = pyglet.image.load('res/animation/level2_monsters/hell_fire_beast/hell-beast-idle.png')
        self.img_grid_i = pyglet.image.ImageGrid(self.img_i, 1, 6, item_width=55, item_height=67)
        self.anim_i = pyglet.image.Animation.from_image_sequence(self.img_grid_i[0:], 0.2, loop=True)
        self.lifes = 2
        self.flag = False
        self.sprite = Sprite(self.anim_i)
        self.sprite.position = (1200, 200)
        self.sprite.scale = 1.8
        self.x = 0

        self.add(self.sprite)

    def get_burn_animation(self):
        img = pyglet.image.load('res/animation/level2_monsters/hell_fire_beast/hell-beast-burn.png')
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

class Nightmare(ScrollableLayer):
    def __init__(self):
        super(Nightmare, self).__init__()

        #animation_idle
        self.img_i = pyglet.image.load('res/animation/level2_monsters/nightmare/nightmare-idle.png')
        self.img_grid_i = pyglet.image.ImageGrid(self.img_i, 1, 4, item_width=128, item_height=96)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid_i[0:], 0.2, loop=True)
        self.lifes = 3
        self.flag = False
        self.sprite = Sprite(self.anim)
        self.sprite.scale = 1
        self.sprite.position = (1200, 160)
        self.x = 0

        self.add(self.sprite)


    def get_run_animation(self):
        img = pyglet.image.load('res/animation/level2_monsters/nightmare/nightmare-galloping.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 4, item_width=144, item_height=96)
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.2, loop=True)

class GreenSkeleton(ScrollableLayer):
    def __init__(self):
        super(GreenSkeleton, self).__init__()

        #animation
        self.img = pyglet.image.load('res/animation/level2_monsters/Undead Sprite Pack/SHEETS/undead_idle_sheet.png')
        self.img_grid = pyglet.image.ImageGrid(self.img, 1, 18, item_width=48, item_height=32)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[0:], 0.1, loop=True)
        self.lifes = 5
        self.first_death = False
        self.can_reinc = False
        self.flag = False
        self.sprite = Sprite(self.anim)
        self.sprite.scale = 1.4
        self.x = 0
        self.can_attack = False
        self.can_action = True
        self.add(self.sprite)

    def get_walk(self):
        img = pyglet.image.load('res/animation/level2_monsters/Undead Sprite Pack/SHEETS/undead_walk_sheet.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 20, item_width=56, item_height=48 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1, loop=True)
        return anim


    def get_attack(self):
        img = pyglet.image.load('res/animation/level2_monsters/Undead Sprite Pack/SHEETS/undead_attack_sheet.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 20, item_width=56, item_height=48 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.05, loop=True)
        return anim

    
    def get_death(self):
        img = pyglet.image.load('res/animation/level2_monsters/Undead Sprite Pack/SHEETS/undead_death_sheet.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 13, item_width=72, item_height=32 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid[12:13], 0.2, loop=True)
        return anim