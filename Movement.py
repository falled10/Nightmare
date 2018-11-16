import cocos
import cocos.actions as ac
import pyglet
import math
from collections import defaultdict
from pyglet.window import key
from cocos.director import director
from cocos.sprite import Sprite
from cocos.scene import Scene
from cocos.menu import MenuItem, Menu
from cocos.layer import Layer
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.menu import Menu
from cocos.scenes.transitions import *
from cocos.scenes import *
import MainSprite
from Main import 


class Mover(cocos.actions.Move):
    def step(self,dt):
        keyboard = key.KeyStateHandler()
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 180
        self.target.velocity = (vel_x, 0)
        scroller_1.set_focus(self.target.x, self.target.y)