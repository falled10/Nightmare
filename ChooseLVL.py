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




class ChooseLVL(Menu):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(ChooseLVL, self).__init__('Вибір рівня')

       # TITLE
        self.font_title['font_name'] = 'Motion Control'
        self.font_title['bold'] = True
        self.font_title['font_size'] = 60
        self.font_title['color'] = (0, 75, 0, 255)

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

        items.append(MenuItem('Рівень 1', self.on_lvl1))
        items[0].x += 35
        items.append(MenuItem('Рівень 2', self.on_lvl2))
        items[1].x += 35
        items.append(MenuItem('Рівень 3', self.on_lvl3))
        items[2].x += 35
        items.append(MenuItem('В меню', self.on_menu))
        items[3].x += 35
        items.append(MenuItem('Вихід', self.on_exit))
        items[4].x += 35

        self.create_menu(items, shake(), shake_back())

    def on_lvl1(self):
        import Level1_Background
        director.push(SlideInTTransition(Level1_Background.get_newgame()))

    def on_lvl2(self):
        import Level2_Background
        director.push(SlideInTTransition(Level2_Background.get_newgame()))    
    
    def on_lvl3(self):
        import Level3_Background
        director.push(SlideInTTransition(Level3_Background.get_newgame()))

    def on_menu(self):
        import Menu
        director.push(ZoomTransition(Menu.get_menu()))

    def on_quit(self):
        Sound.stop()
        pyglet.app.exit()
    
    
def get_choose():
  
    scene = Scene()
    main_bg = MainScene()
    lvl = ChooseLVL()

    scene.add(main_bg)
    scene.add(lvl)

    return scene