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
from MainSprite import *


class MainScene(Scene):
    def __init__(self):
        super().__init__()
        menu_bg = Sprite('map/MainMenu.png')
        menu_bg.position = menu_bg.width // 2, menu_bg.height // 2

        self.px_width = menu_bg.width 
        self.px_height = menu_bg.height
        self.add(menu_bg)
       
class MainMenu(Menu):
    def __init__(self):
        super().__init__("Nightmare")

        items = []

        items.append(MenuItem("Нова гра", self.on_new_game))
        items[0].y = 40
        items[0].x = 40
        items.append(MenuItem("Вихід", self.on_exit))
        items[1].x = 40
        self.create_menu(items, cocos.menu.shake(), cocos.menu.shake_back())
        
    def on_new_game(self):
        director.init(width=800, height=600, caption='Nightmare')    
        director.window.pop_handlers()
        keyboard = key.KeyStateHandler()
        director.window.push_handlers(keyboard)
        director.window.close()
       
        director.run(Level1_Scene)
    
    def on_exit(self):
        director.window.close()

class Level1_Layer(ScrollableLayer):
   
    def __init__(self):
        super(Level1_Layer, self).__init__()

        lvl1_bg = Sprite('map/level1.png')

        lvl1_bg.position = lvl1_bg.width // 2, lvl1_bg.height // 2

        self.px_width = lvl1_bg.width
        self.px_height = lvl1_bg.height

        self.add(lvl1_bg)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.O:
            director.run(Level2_Scene)
    

class Level2_Layer(ScrollableLayer):
    is_event_handler = True
    def __init__(self):
        super(Level2_Layer,self).__init__()

        lvl2_bg = Sprite('map/level2.png')

        lvl2_bg.position = lvl2_bg.width // 2, lvl2_bg.height // 2

        self.px_width = lvl2_bg.width
        self.px_height = lvl2_bg.height

        self.add(lvl2_bg)
        self.add(SceneControlLayer())
    

class SceneControlLayer(Layer):
    is_event_handler = True
    active_scene = None
    def __init__(self):
        super().__init__()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.P:
            SceneControlLayer.active_scene = Scene(Level1_Scene)
            director.replace(FlipX3DTransition(SceneControlLayer.active_scene, duration = 2)) 
        if symbol == key.SPACE:
            SceneControlLayer.active_scene = Scene(Level2_Scene)
            director.replace(FlipX3DTransition(SceneControlLayer.active_scene, duration = 2))
        if symbol == key.O:
            SceneControlLayer.active_scene = Scene(Level2_Scene)
            director.replace(FlipX3DTransition(SceneControlLayer.active_scene, duration = 2))
            

if __name__ == '__main__':
    director.init(width=800, height=600, caption='Nightmare')    
    
    director.window.pop_handlers()
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    layer = MainHero()
    level1_layer = Level1_Layer()
    scroller_1 = ScrollingManager()
    scroller_1.add(level1_layer)
    scroller_1.add(layer)
    Level1_Scene = Scene()
    Level1_Scene.add(scroller_1)
    
    menu = MainMenu()  
    main = MainScene()
    
    
    level2_layer = Level2_Layer()
   
    
    scroller_2 = ScrollingManager()
    scroller_2.add(level2_layer)
    scroller_2.add(layer)
    

    MS = Scene()  
    
    Level2_Scene = Scene()
   
   
    MS.add(main)
    MS.add(menu)

   
    Level2_Scene.add(scroller_2)
    
    director.run(MS)   
    
    

   
  
