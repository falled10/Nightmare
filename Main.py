import cocos
import cocos.actions as ac
import pyglet
from collections import defaultdict
from pyglet.window import key


class HelloCocos(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super().__init__()

        img_r = pyglet.image.load('adventurer-run3-sword-Sheet.png')
        img_grid_r = pyglet.image.ImageGrid(img_r, 1, 6, item_width=50, item_height=37 )

        anim_r = pyglet.image.Animation.from_image_sequence(img_grid_r[0:], 0.1, loop=True)

        self.spriterunright = cocos.sprite.Sprite(anim_r)
        self.spriterunright.position = (100, 150)
        self.spriterunright.scale = 2   
        self.add(self.spriterunright)
        img_l = pyglet.image.load('runleft.png')
        img_grid_l = pyglet.image.ImageGrid(img_l, 1, 6, item_width=50, item_height=37)
        temp = img_grid_l[::-1]
        
        anim_l = pyglet.image.Animation.from_image_sequence(temp[0:], 0.1, loop=True)
        self.spriterunleft = cocos.sprite.Sprite(anim_l)
        self.spriterunleft.visible = False
        self.spriterunleft.scale = 2
        self.spriterunleft.position = (100, 150)
        self.add(self.spriterunleft)
        self.speed = 100.0
        self.pressed = defaultdict(int)
        self.schedule(self.update)


    def on_key_press(self, k, m):
        self.pressed[k] = 1
        if k == 65361:
            self.spriterunright.visible = False
            self.spriterunleft.visible = True
        if k == 65363:
            self.spriterunright.visible = True
            self.spriterunleft.visible = False

    def on_key_release(self, k, m):
        self.pressed[k] = 0


    def update(self, dt):
        x = self.pressed[key.RIGHT] - self.pressed[key.LEFT]
        pos_x = self.spriterunright.position
        if x != 0:
            pos = self.spriterunright.position
            new_x = pos[0] + self.speed * x * dt
            self.spriterunright.x = new_x
            self.spriterunleft.x = new_x


class Background(cocos.layer.Layer):

    def __init__(self):
        super().__init__()

        bg = cocos.sprite.Sprite('Map1.png')

        bg.position = (400,400)

        bg.scale = 1.25

        self.add(bg)

if __name__ == '__main__':
    cocos.director.director.init(width=800, height=800, caption='Nightmare')    

    layer = HelloCocos()
    bglayer = Background()
    test_scene = cocos.scene.Scene()
    test_scene.add(bglayer)
    test_scene.add(layer)

    cocos.director.director.run(test_scene)
