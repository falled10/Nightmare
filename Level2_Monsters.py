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