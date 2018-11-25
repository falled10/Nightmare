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
import Level1_Hero



class GameOver(Menu):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(GameOver, self).__init__('Кінець гри')

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

        items.append(MenuItem('Повторити', self.on_retry))
        items[0].x += 35
        items.append(MenuItem('В меню', self.on_menu))
        items[1].x += 35
        items.append(MenuItem('Вихід', self.on_quit))
        items[2].x += 35

        self.create_menu(items, shake(), shake_back())

    def on_retry(self):
        import Level_Background
        if(Level1_Hero.flag == True):
            director.push(SlideInTTransition(Level1_Background.get_newgame()))
        
    
    def on_menu(self):
        Sound.stop()
        import Menu
        director.push(ZoomTransition(Menu.get_menu()))

    def on_quit(self):
        Sound.stop()
        pyglet.app.exit()
    
    
def get_gameover():
  
    scene = Scene()
    main_bg = MainScene()
    over = GameOver()

    Sound.play("res/audio/GameOver.mp3")

    scene.add(main_bg)
    scene.add(over)

    return scene