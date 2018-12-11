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


class Ghost(ScrollableLayer):
    def __init__(self):
        super(Ghost, self).__init__()

        #animation
        self.img = pyglet.image.load('res/animation/level3_monsters/ghost/ghost-idle.png')
        self.img_grid = pyglet.image.ImageGrid(self.img, 1, 7, item_width=64, item_height=80)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[0:], 0.2, loop=True)
        self.lifes = 1  
        self.flag = False
        self.sprite = Sprite(self.anim)
        self.sprite.scale = 1.4
        self.x = 0
        self.can_attack = False
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