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
import fonts

class About(Menu):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(About, self).__init__()

        # ITEM SELECTED
        self.font_item_selected['font_name'] = 'Roboto'
        self.font_item_selected['color'] = (230,80,145,225)
        self.font_title['bold'] = True
        self.font_item_selected['font_size'] = 35

        items = []

        items.append(MenuItem('Назад', self.on_menu))
        items[0].y -= 250
        items[0].x += 10

        self.create_menu(items, shake(), shake_back())
    
    def on_menu(self):
        director.pop()

    def on_quit(self):
        director.pop()

class AboutScene(Scene):

    def __init__(self):
        super().__init__()
        bg = Sprite("res/keyboard/MyBG.jpg")
        bg.position = bg.width // 2, bg.height // 2
        self.add(bg)

        title = Label("Над грою працювали: ",font_name='Roboto', font_size = 40,bold = True, color = (230,80,145,225))
        title.position = (120, 450)
        self.add(title)

        y = Label("Кулик Юрій",font_name='Roboto', font_size = 35,bold = True, color = (230,80,145,225))
        y.position = (260, 380)
        self.add(y)

        o = Label("Андріїв Олег",font_name='Roboto', font_size = 35,bold = True, color = (230,80,145,225))
        o.position = (260, 310)
        self.add(o)

        i = Label("Перегінець Іван",font_name='Roboto', font_size = 35,bold = True, color = (230,80,145,225))
        i.position = (260, 240)
        self.add(i)

        
            
def get_about():
  
    scene = Scene()
    a_scene = AboutScene()
    about = About()

    scene.add(a_scene)
    scene.add(about)

    return scene