from cocos.menu import *
from cocos.director import director
from cocos.scenes.transitions import *
import pyglet
from cocos.scene import Scene
from Menu_Background import MainScene
import Sound
from pyglet import font
import fonts



class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__('Головне меню')

        # TITLE   
        self.font_title = {
            'font_name': 'Peace Sans',
            'font_size': 60,
            'color': (255, 69, 0, 255),
            'bold': True,
            'anchor_y': 'center',
            'anchor_x': 'center',
        }
        # ITEM
        self.font_item['font_name'] = 'Arial Black'
        self.font_item['color'] = (0, 150, 115, 255)
        self.font_item['bold'] = True
        self.font_item['font_size'] = 35

        # ITEM SELECTED
        self.font_item_selected['font_name'] = 'Arial Black'
        self.font_item_selected['color'] = (140, 0, 0, 255)
        self.font_item['bold'] = True
        self.font_item_selected['font_size'] = 35

        
        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER

        items = []

        items.append(MenuItem('Нова гра', self.on_new_game))
        items[0].x += 35
        items.append(MenuItem('Допомога', self.on_help))
        items[1].x += 35
        items.append(MenuItem('Про авторів', self.on_author))
        items[2].x += 35
        items.append(MenuItem('Вихід', self.on_quit))
        items[3].x += 35
        self.create_menu(items, shake(), shake_back())

    def on_new_game(self):
        import CutScene
        import Level3_Background
        director.push(SlideInTTransition(Level3_Background.get_newgame()))
        #director.push(SlideInTTransition(CutScene.get_cut_scene()))

    def on_help(self):
        import Help
        director.push(SlideInTTransition(Help.get_help()))  

    def on_author(self):
        import About
        director.push(SlideInTTransition(About.get_about()))  

    def on_quit(self):
        pyglet.app.exit()


def get_menu():
  
    menu = MainMenu()
    main_bg = MainScene()
    scene = Scene()
    Sound.music.set_volume(0.5)
    Sound.play("res/audio/Menu.mp3")

    scene.add(main_bg)
    scene.add(menu)

    return scene
