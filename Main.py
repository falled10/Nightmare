import cocos
import cocos.actions as ac
import pyglet
import math
from collections import defaultdict
from pyglet.window import key
from cocos.director import director
from cocos.sprite import Sprite
from cocos.scene import Scene
from cocos.menu import MenuItem
from cocos.layer import Layer
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.menu import Menu
from cocos.scenes.transitions import *


class MainScene(Scene):
    def __init__(self):
        super().__init__()
        menu_bg = Sprite('map/MainMenu.png')
        menu_bg.position = menu_bg.width // 2, menu_bg.height // 2

        self.px_width = menu_bg.width 
        self.px_height = menu_bg.height

        
        self.add(menu_bg)
"""
class PauseScene(Scene):
    def __init__(self):
        super().__init__()
       
        self.add(SceneControlLayer())
    """  
       
class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super().__init__("Nightmare")

        items = []

        items.append(MenuItem("New Game", self.on_new_game))
        items[0].y = 40
        items[0].x = 40
        items.append(MenuItem("Exit", self.on_exit))
        self.create_menu(items, cocos.menu.shake(), cocos.menu.shake_back())
        
    def on_new_game(self):
        director

    def on_exit(self):
        director.window.close()



class Mover(cocos.actions.Move):
    def step(self,dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 180
        self.target.velocity = (vel_x, 0)
        scroller_1.set_focus(self.target.x, self.target.y)


class HelloCocos(ScrollableLayer):   
    is_event_handler = True
    def __init__(self):
        super().__init__()
        #run right --------------------------------------------------
        self.img_r = pyglet.image.load('adventurer-run3-sword-Sheet.png')
        self.img_grid_r = pyglet.image.ImageGrid(self.img_r, 1, 6, item_width=50, item_height=37 )
        self.anim_r = pyglet.image.Animation.from_image_sequence(self.img_grid_r[0:], 0.1, loop=True)
        # ----------------------------------------------------------
        
        #attak1
        self.img_a1 = pyglet.image.load('attack1/Attacksheet.png')
        self.img_grid_a1 = pyglet.image.ImageGrid(self.img_a1, 1, 5, item_width=50, item_height=37 )

        self.anim_a1 = pyglet.image.Animation.from_image_sequence(self.img_grid_a1[0:], 0.1, loop=True)
        #_-----------------------------------------------------------------

        # idle
        self.img_i = pyglet.image.load('idle/idlesheet.png')
        self.img_grid_i = pyglet.image.ImageGrid(self.img_i, 1, 4, item_width=50, item_height=37 )

        self.anim_i = pyglet.image.Animation.from_image_sequence(self.img_grid_i[0:], 0.3, loop=True)
        #_-----------------------------------------------------------------


        self.sprite = Sprite(self.anim_i)
        self.sprite.position = (100, 180)
        self.sprite.scale = 2
        self.sprite.scale_x = 1
        self.sprite.velocity = (0,0)
        self.sprite.do(Mover())
        self.add(self.sprite)
        

        self.speed = 100.0
        self.pressed = defaultdict(int)
        self.schedule(self.update)
        #h

    def on_key_press(self, k, m):
        print(k)
        if k == 65361:
            self.sprite.scale_x = -1
            self.sprite._animation = self.anim_r
        if k == 65363:
            self.sprite.scale_x = 1
            self.sprite._animation = self.anim_r

        if k == 65362:
            self.sprite._animation = self.anim_a1


    def on_key_release(self, k, m):
        
            self.sprite._animation = self.anim_i


    def update(self, dt):
        pass


class Level1_Layer(ScrollableLayer):
   
    def __init__(self):
        super().__init__()

        lvl1_bg = Sprite('map/level1.png')

        lvl1_bg.position = lvl1_bg.width // 2, lvl1_bg.height // 2

        self.px_width = lvl1_bg.width
        self.px_height = lvl1_bg.height

        self.add(lvl1_bg)

class Level2_Layer(ScrollableLayer):

    def __init__(self):
        super().__init__()

        lvl2_bg = Sprite('map/level2.png')

        lvl2_bg.position = lvl2_bg.width // 2, lvl2_bg.height // 2

        self.px_width = lvl2_bg.width
        self.px_height = lvl2_bg.height

        self.add(lvl2_bg)
"""
class SceneControlLayer(Layer):
    is_event_handler = True
    active_scene = None
    def __init__(self):
        super().__init__()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.P:
            SceneControlLayer.active_scene = IntroScene()
            director.replace(FlipX3DTransition(SceneControlLayer.active_scene, duration = 2)) 
        if symbol == key.SPACE:
            SceneControlLayer.active_scene = TestScene1()
            director.replace(FlipX3DTransition(SceneControlLayer.active_scene, duration = 2))  """




   
    
if __name__ == '__main__':
    director.init(width=800, height=600, caption='Nightmare')    

    director.window.pop_handlers()
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

   #SceneControlLayer.active_scene = PauseScene()
    
    menu = MainMenu()  
    main = MainScene()
    layer = HelloCocos()
    level1_layer = Level1_Layer()
    level2_layer = Level2_Layer()
   
  

    scroller_1 = ScrollingManager()
    scroller_1.add(level1_layer)
    scroller_1.add(layer)

    scroller_2 = ScrollingManager()
    scroller_2.add(level2_layer)
    scroller_2.add(layer)
    

    Main_Scene = Scene()  
    Level1_Scene = Scene()
    Level2_Scene = Scene()
   
   
    Main_Scene.add(main)

    Main_Scene.add(menu)
    Level1_Scene.add(scroller_1)
    Level2_Scene.add(scroller_2)
    director.push(Level1_Scene)
    

    director.run(Main_Scene)
   
  
