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


class AxeSkeleton(ScrollableLayer):
    def __init__(self):
        super(AxeSkeleton, self).__init__()
        #animation
        self.img = pyglet.image.load('res/animation/level3_monsters/Skeleton/Sprite Sheets/Skeleton Idle.png')
        self.img_grid = pyglet.image.ImageGrid(self.img, 1, 11, item_width=24, item_height=31)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[0:], 0.1, loop=True)
        self.lifes = 7
        self.l = 7
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
        img = pyglet.image.load('res/animation/level3_monsters/Skeleton/Sprite Sheets/Skeleton Walk.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 13, item_width=22, item_height=33 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1, loop=True)
        return anim


    def get_attack(self):
        img = pyglet.image.load('res/animation/level3_monsters/Skeleton/Sprite Sheets/Skeleton Attack.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 18, item_width=43, item_height=37 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.05, loop=True)
        return anim

    
    def get_death(self):
        img = pyglet.image.load('res/animation/level3_monsters/Skeleton/Sprite Sheets/Skeleton Dead.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 13, item_width=33, item_height=31 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid[12:13], 0.2, loop=True)
        return anim



class Ghost(ScrollableLayer):
    def __init__(self):
        super(Ghost, self).__init__()

        #animation
        self.img = pyglet.image.load('res/animation/level3_monsters/ghost/ghost-idle.png')
        self.img_grid = pyglet.image.ImageGrid(self.img, 1, 7, item_width=64, item_height=80)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[0:], 0.2, loop=True)
        self.lifes = 5 
        self.l = 5
        self.flag = False
        self.sprite = Sprite(self.anim)
        self.sprite.scale = 1.4
        self.x = 0
        self.can_attack = False
        self.can_action = True
        self.add(self.sprite)

    def get_appears(self):
        img = pyglet.image.load('res/animation/level3_monsters/ghost/ghost-appears.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 6, item_width=64, item_height=80 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.2, loop=True)
        return anim


    def get_vanish(self):
        img = pyglet.image.load('res/animation/level3_monsters/ghost/ghost-vanish.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 6, item_width=64, item_height=64 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.2, loop=True)
        return anim

    
    def get_shriek(self):
        img = pyglet.image.load('res/animation/level3_monsters/ghost/ghost-shriek.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 4, item_width=64, item_height=80 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.2, loop=True)
        return anim


class DemonBoss(ScrollableLayer):
    def __init__(self):
        super(DemonBoss, self).__init__()
        self.img = pyglet.image.load('res/animation/level3_monsters/demon boss/demon-idle.png')
        self.img_grid = pyglet.image.ImageGrid(self.img, 1, 6, item_width=160, item_height=144)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[0:], 0.1, loop=True)
        self.lifes = 24 
        self.flag = False
        self.sprite = Sprite(self.anim)
        self.sprite.scale = 1.4
        self.x = 0
        self.can_attack = False
        self.can_action = True
        self.add(self.sprite)


    def get_attack(self):
        img = pyglet.image.load('res/animation/level3_monsters/demon boss/demon-attack.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 11, item_width=240, item_height=192 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1, loop=True)
        return anim