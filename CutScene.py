import cocos
from cocos.actions import *
import pyglet
from pyglet import image
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.scenes.transitions import *
from cocos.director import director
from cocos.text import Label
from cocos.actions import *
from pyglet.window import key


class MainLayer(Layer):
    def __init__(self):
        super(MainLayer, self).__init__()
        skip = Label("Натисніть ПРОБІЛ, щоб пропустити", position = (100,550), color = (255,0,0, 255), font_size = 25, bold = True)
        skip.do(Blink (20,20))
        self.add(skip)
        self.img_h = pyglet.image.load('res/animation/level1_monsters/hell_hound/hell-hound-run.png')
        self.img_grid_h = pyglet.image.ImageGrid(self.img_h, 1, 5, item_width=67, item_height=31)
        self.anim_h = pyglet.image.Animation.from_image_sequence(self.img_grid_h[0:], 0.2, loop=True)
        
        self.hell_hound = cocos.sprite.Sprite(self.anim_h)

        self.hell_hound.position = (-100, 180)
        self.hell_hound.scale = 2
        self.hell_hound.scale_x = -1
        self.add(self.hell_hound)

        self.portal = cocos.sprite.Sprite('res/animation/catscene/portal.png')
        self.portal.position = (500, 500)
        self.portal.scale = 0.3
        self.add(self.portal)

        self.img = pyglet.image.load('res/animation/catscene/Character_03/Idle/idle_sheet.png')
        self.img_grid = pyglet.image.ImageGrid(self.img, 1, 13, item_width=64, item_height=64 )
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[0:], 0.1, loop=True)

        self.hero_1 = cocos.sprite.Sprite(self.anim)
        self.hero_1.scale = 2.2
        self.hero_1.position = (300, 180)
        self.add(self.hero_1)

        self.img_1 = pyglet.image.load('res/animation/catscene/girl/Idle_Png/idle_sheet.png')
        self.img_grid_1 = pyglet.image.ImageGrid(self.img_1, 1, 5, item_width=128, item_height=128 )
        self.anim_1 = pyglet.image.Animation.from_image_sequence(self.img_grid_1[0:], 0.1, loop=True)

        self.hero_2 = cocos.sprite.Sprite(self.anim_1)
        self.hero_2.position = (200, 190)
        self.hero_2.scale = 1.6
        self.add(self.hero_2)


        self.img_2 = pyglet.image.load('res/animation/idle/idlesheet.png')
        self.img_grid_2 = pyglet.image.ImageGrid(self.img_2, 1, 4, item_width=50, item_height=37 )
        self.anim_2 = pyglet.image.Animation.from_image_sequence(self.img_grid_2[0:], 0.2, loop=True)

        self.hero_3 = cocos.sprite.Sprite(self.anim_2)
        self.hero_3.position = (100, 180)
        self.hero_3.scale = 2.2
        self.add(self.hero_3)


        self.img_3 = pyglet.image.load('res/animation/level3_monsters/demon boss/demon-idle.png')
        self.img_grid_3 = pyglet.image.ImageGrid(self.img_3, 1, 6, item_width=160, item_height=144 )
        self.anim_3 = pyglet.image.Animation.from_image_sequence(self.img_grid_3[0:], 0.1, loop=True)
        
        self.demon = cocos.sprite.Sprite(self.anim_3)
        self.demon.position = (400, 500)
        self.demon.scale = 1.4
        self.add(self.demon)

        self.hell_hound.do(MoveTo((1000, 180), 11))
        self.hero_3.do(MoveBy((170, 0), 3) + Delay(9.5) + MoveBy((1000, 0), 7.5))

        self.hero_1.do(MoveBy((100,0), 3) + Delay(8.5) + FadeOut(0.5))
        self.hero_2.do(MoveBy((250,0), 3) + Delay(8.5) + FadeOut(0.5))

        self.portal.do(FadeOut(0) + MoveTo((700, 300), 5) + FadeIn(1) + Delay(7.5) + FadeOut(0.5))
        self.demon.do(FadeOut(0) + MoveTo((700, 350), 5) + FadeIn(4) + Delay(1) + MoveTo((550, 250), 1) + Delay(2) + MoveTo((550, 1000), 1))

        self.schedule(self.update)

    def get_girl_walk(self):
        img_2 = pyglet.image.load('res/animation/catscene/girl/Walk_Png/walk_sheet.png')
        img_grid_2 = pyglet.image.ImageGrid(img_2, 1, 4, item_width=128, item_height=128 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid_2[0:], 0.1, loop=True)
        return anim


    def get_girl_attack(self):
        img_2 = pyglet.image.load('res/animation/catscene/girl/Action_Png/action_sheet.png')
        img_grid_2 = pyglet.image.ImageGrid(img_2, 10, 2, item_width=128, item_height=128 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid_2[::-1], 0.1, loop=True)
        return anim

    def get_walk(self):
        img_2 = pyglet.image.load('res/animation/catscene/Character_03/Walk/walk_sheet.png')
        img_grid_2 = pyglet.image.ImageGrid(img_2, 1, 12, item_width=64, item_height=64 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid_2[0:], 0.1, loop=True)
        return anim


    def get_attack(self):
        img_2 = pyglet.image.load('res/animation/catscene/Character_03/Attack_02/attack2_sheet.png')
        img_grid_2 = pyglet.image.ImageGrid(img_2, 1, 16, item_width=64, item_height=64 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid_2[0:], 0.1, loop=True)
        return anim


    def get_attack_hero(self):
        img_2 = pyglet.image.load('res/animation/attack1/attack1sheet.png')
        img_grid_2 = pyglet.image.ImageGrid(img_2, 6, 1, item_width=50, item_height=37 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid_2[::-1], 0.1, loop=True)
        return anim


    def get_attack_run(self):
        img_2 = pyglet.image.load('res/animation/run/adventurer-run3-sword-Sheet.png')
        img_grid_2 = pyglet.image.ImageGrid(img_2, 1, 6, item_width=50, item_height=37 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid_2[0:], 0.1, loop=True)
        return anim


    def get_attack_demon(self):
        img = pyglet.image.load('res/animation/level3_monsters/demon boss/demon-attack.png')
        img_grid = pyglet.image.ImageGrid(img, 1, 11, item_width=240, item_height=192 )
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1, loop=True)
        return anim


    def update(self, dt):
        x,y = self.hell_hound.position
        if( x > 800):
            import Level1_Background          
            director.push(SlideInTTransition(Level1_Background.get_newgame()))
        if self.hell_hound.position[0] > self.hero_3.position[0] - 10:
            self.hell_hound.position = (-100, 180)
            self.hell_hound.do(MoveTo((1000, 180), 6.7))
        if self.hero_3.position[0] > 100 and self.hero_3.position[0] < 270:
            self.hero_3._animation = self.get_attack_run()
        if self.hero_2.position[0] > 200 and self.hero_2.position[0] < 500:
            self.hero_2._animation = self.get_girl_walk()
        if self.hero_1.position[0] > 100 and self.hero_1.position[0] < 400:
            self.hero_1._animation = self.get_walk() 

        if self.hero_1.position[0] == 400:
            self.hero_1._animation = self.get_attack()
        if self.hero_2.position[0] == 450:
            self.hero_2._animation = self.get_girl_attack()
        if self.hero_3.position[0] == 270:
            self.hero_3.scale_x = -1
            self.hero_3._animation = self.get_attack_hero()

        if self.hero_3.position[0] > 270:
            self.hero_3.scale_x = 1
            self.hero_3._animation = self.get_attack_run()


        if self.portal.position == (700, 300):
            self.hero_1._animation = self.anim
            self.hero_2._animation = self.anim_1

        if self.demon.position == (550, 250):
            self.demon.position = (520, 250)
            self.demon.scale = 2
            self.demon._animation = self.get_attack_demon()
        
        if self.demon.position[1] > 250:
            self.demon._animation = self.anim_3
        



class BackgroundLayer(Layer):
    is_event_handler = True 
    def __init__(self):
        super(BackgroundLayer, self).__init__()
        bg = cocos.sprite.Sprite('res/maps/Level1/level1.png')
        bg.position = bg.width // 2, bg.height // 2
        self.add(bg)
    def on_key_press(self, k, m):
         if k == key.SPACE:
            import Level1_Background 
            director.push(SlideInTTransition(Level1_Background.get_newgame()))

         if k == key.M:
             import Sound
             Sound.mute_volume(0)
        


def get_cut_scene():

    scene = Scene()
    layer = MainLayer()
    bgLayer = BackgroundLayer()
    scene.add(bgLayer)
    scene.add(layer)   
    return scene
