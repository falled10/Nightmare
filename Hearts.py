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
from cocos.scene import Scene
from cocos.scenes.transitions import *
from Level1_Monsters import *
import Level1_Background
import Sound

keyboard = key.KeyStateHandler()

global heart1
heart1 = Sprite('res/maps/heart1.png')
global heart2
heart2 = Sprite('res/maps/heart2.png')
global heart3
heart3 = Sprite('res/maps/heart3.png')


class MoverForFirstHeart(Move):
    def step(self,dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 180
        self.target.velocity = (vel_x, 0)
        Level1_Background.scroller_1.set_focus(self.target.x, self.target.y)
class MoverForSecondHeart(Move):
    def step(self,dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 180
        self.target.velocity = (vel_x, 0)
        Level1_Background.scroller_1.set_focus(self.target.x, self.target.y)
class MoverForThirdHeart(Move):
    def step(self,dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 180
        self.target.velocity = (vel_x, 0)
        Level1_Background.scroller_1.set_focus(self.target.x, self.target.y) 

class HeartsIcons(ScrollableLayer):
    def __init__(self):
        super(HeartsIcons, self).__init__()     
        heart1.position = (25,570)
        self.add(heart1)
        heart2.position = (70,570)
        self.add(heart2) 
        heart3.position = (115,570)
        self.add(heart3)
        heart1.velocity = (0,0)
        heart2.velocity = (0,0)
        heart3.velocity = (0,0)
        heart1.do(MoverForFirstHeart())
        heart2.do(MoverForSecondHeart())
        heart3.do(MoverForThirdHeart())