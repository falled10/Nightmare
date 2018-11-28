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


class WhiteWolf(ScrollableLayer):
    def __init__(self):
        super(WhiteWolf, self).__init__()

        #animation
        self.img = pyglet.image.load('res/animation/level1_monters/wolf1/wolf-runing-cycle.png')
        self.img_grid = pyglet.image.ImageGrid(self.img, 1, 4, item_width=54, item_height=31)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[1:2], 0.2, loop=True)
        self.lifes = 1
        self.flag = False
        self.sprite = Sprite(self.anim)
        self.sprite.scale = 1.4
        self.sprite.position = (800, 160)
        self.x = 0
        
        self.add(self.sprite)


    def get_idle_animation(self):
        img = pyglet.image.load('res/animation/level1_monters/wolf1/wolf-runing-cycle.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 4, item_width=54, item_height=31)
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.2, loop=True)
        return anim


class BlueWolf(ScrollableLayer):
    def __init__(self):
        super(BlueWolf, self).__init__()

        #animation
        self.img = pyglet.image.load('res/animation/level1_monters/wolf2/wolf-runing-cycle-skin.png')
        self.img_grid = pyglet.image.ImageGrid(self.img, 1, 4, item_width=54, item_height=31)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[1:2], 0.2, loop=True)

        self.sprite = Sprite(self.anim)
        self.sprite.scale = 1.4
        self.sprite.position = (1000, 160)
        self.x = 0
        
        self.add(self.sprite)


    def get_idle_animation(self):
        img = pyglet.image.load('res/animation/level1_monters/wolf2/wolf-runing-cycle-skin.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 4, item_width=54, item_height=31)
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.2, loop=True)
        return anim

    

