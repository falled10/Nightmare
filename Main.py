import cocos
import cocos.actions as ac
import pyglet
from collections import defaultdict
from pyglet.window import key
from cocos.director import director



class Mover(cocos.actions.Move):
    def step(self,dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 500
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 500
        self.target.velocity = (vel_x, vel_y)
        scroller.set_focus(self.target.x, self.target.y)

class HelloCocos(cocos.layer.ScrollableLayer):
    is_event_handler = True
    def __init__(self):
        super().__init__()

        img_r = pyglet.image.load('adventurer-run3-sword-Sheet.png')
        img_grid_r = pyglet.image.ImageGrid(img_r, 1, 6, item_width=50, item_height=37 )

        anim_r = pyglet.image.Animation.from_image_sequence(img_grid_r[0:], 0.1, loop=True)

        self.spriterunright = cocos.sprite.Sprite(anim_r)
        self.spriterunright.position = (100, 150)
        self.spriterunright.scale = 2
        self.spriterunright.velocity = (0,0)
        
        self.spriterunright.do(Mover())

        self.add(self.spriterunright)

        """
        img_l = pyglet.image.load('runleft.png')
        img_grid_l = pyglet.image.ImageGrid(img_l, 1, 6, item_width=50, item_height=37)
        temp = img_grid_l[::-1]
        
        anim_l = pyglet.image.Animation.from_image_sequence(temp[0:], 0.1, loop=True)
        self.spriterunleft = cocos.sprite.Sprite(anim_l)
        self.spriterunleft.visible = False
        self.spriterunleft.scale = 2
        self.spriterunleft.position = (100, 150)
        self.add(self.spriterunleft)
    
        self.pressed = defaultdict(int)
       """

class BackgroundLayer(cocos.layer.ScrollableLayer):

    def __init__(self):
        super().__init__()

        bg = cocos.sprite.Sprite('level1.png')

        bg.position = bg.width // 2, bg.height // 2

        self.px_width = bg.width
        self.px_height = bg.height

        self.add(bg)

if __name__ == '__main__':
    director.init(width=800, height=600, caption='Nightmare')    

    director.window.pop_handlers()
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    layer = HelloCocos()
    bglayer = BackgroundLayer()

    scroller = cocos.layer.ScrollingManager()
    scroller.add(bglayer)
    scroller.add(layer)

    test_scene = cocos.scene.Scene()  
    test_scene.add(scroller)

    
    director.run(test_scene)
