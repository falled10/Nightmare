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
from Menu_Background import MainScene
import Sound



class Help(Menu):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Help, self).__init__('Допомога')

       # TITLE
        self.font_title['font_name'] = 'Motion Control'
        self.font_title['bold'] = True
        self.font_title['font_size'] = 60
        self.font_title['color'] = (255, 69, 0, 255)

        # ITEM
        self.font_item['font_name'] = 'Motion Control'
        self.font_item['color'] = (0, 0, 36, 255)
        self.font_title['bold'] = True
        self.font_item['font_size'] = 35

        # ITEM SELECTED
        self.font_item_selected['font_name'] = 'Motion Control'
        self.font_item_selected['color'] = (140, 0, 0, 255)
        self.font_title['bold'] = True
        self.font_item_selected['font_size'] = 35

        items = []

        items.append(MenuItem('Гарячі клавіші', self.on_hotkey))
        items[0].x += 35
        items.append(MenuItem('В меню', self.on_menu))
        items[1].x += 35
        

        self.create_menu(items, shake(), shake_back())

    def on_hotkey(self):
        import Hotkeys
        director.push(SlideInTTransition(Hotkeys.get_hotkeys()))
        
    
    def on_menu(self):
        Sound.stop()
        import Menu
        director.push(ZoomTransition(Menu.get_menu()))

    def on_quit(self):
        import Menu
        director.push(ZoomTransition(Menu.get_menu()))
    
    
def get_help():

    scene = Scene()
    main_bg = MainScene()
    help = Help()

    scene.add(main_bg)
    scene.add(help)

    return scene