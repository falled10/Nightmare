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
import pyglet




class GameOver(Menu):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(GameOver, self).__init__('Кінець гри')

       # TITLE
        self.font_title['font_name'] = 'Motion Control'
        self.font_title['bold'] = True
        self.font_title['font_size'] = 60
        self.font_title['color'] = (255, 69, 0, 255)

        # ITEM
        self.font_item['font_name'] = 'Motion Control'
        self.font_item['color'] = (0, 150, 115, 255)
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
        items.append(MenuItem('Допомога', self.on_help))
        items[1].x += 35
        items.append(MenuItem('Про авторів', self.on_author))
        items[2].x += 35
        items.append(MenuItem('В меню', self.on_menu))
        items[3].x += 35
        items.append(MenuItem('Вихід', self.on_quit))
        items[4].x += 35

        self.create_menu(items, shake(), shake_back())

    def on_retry(self):
        if(game_over_flag == 1):
            import Level1_Background
            Sound.stop()
            director.push(SlideInTTransition(Level1_Background.get_newgame()))
        if(game_over_flag == 2):
            import Level2_Background
            Sound.stop()
            director.push(SlideInTTransition(Level2_Background.get_newgame()))
        if(game_over_flag == 3):
            import Level3_Background
            Sound.stop()
            director.push(SlideInTTransition(Level3_Background.get_newgame()))
       
    def on_help(self):
        import Help
        director.push(SlideInTTransition(Help.get_help()))  

    def on_author(self):
        import About
        director.push(SlideInTTransition(About.get_about()))  

    def on_menu(self):
        Sound.on_off()
        import Menu
        director.push(ZoomTransition(Menu.get_menu()))

    def on_quit(self):
        pyglet.app.exit()
    

def get_gameover(flag):

    global game_over_flag
    game_over_flag = flag

    scene = Scene()
    main_bg = MainScene()
    over = GameOver()

    Sound.play("res/audio/GameOver.mp3")

    scene.add(main_bg)
    scene.add(over)

    return scene