import cocos
from cocos.layer import ScrollableLayer, ScrollingManager
from cocos.sprite import Sprite
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.text import Label
from cocos.director import director
from pyglet.window import key
from cocos.menu import *
from cocos.scenes.transitions import *
from cocos.text import *
import Sound
from cocos.actions import *
from pyglet.window import key



class About(Menu):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(About, self).__init__()

        # ITEM SELECTED
        self.font_item_selected['font_name'] = 'Motion Control'
        self.font_item_selected['color'] = (0, 100, 0, 255)
        self.font_title['bold'] = True
        self.font_item_selected['font_size'] = 35

        items = []

        items.append(MenuItem('Повернутись в меню', self.on_menu))
        items[0].y -= 250

        self.create_menu(items, shake(), shake_back())
    
    def on_menu(self):
        import Menu
        director.push(ZoomTransition(Menu.get_menu()))

    def on_quit(self):
        import Help
        director.push(ZoomTransition(Help.get_help()))

    

class AboutScene(Scene):

    def __init__(self):
        super().__init__()
        bg = Sprite("res/keyboard/bg.jpg")
        bg.position = bg.width // 2, bg.height // 2
        self.add(bg)
    
      
def get_about():
  
    scene = Scene()
    a_scene = AboutScene()
    about = About()

    scene.add(a_scene)
    scene.add(about)

    return scene