from cocos.menu import *
from cocos.director import director
from cocos.scenes.transitions import *
import pyglet
from cocos.scene import Scene
from Menu_Background import MainScene
import Sound



class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__('Головне меню')

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

        
        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER

        items = []

        items.append(MenuItem('Нова гра', self.on_new_game))
        items[0].x += 35
        items.append(MenuItem('Вибрати рівень', self.on_choose_lvl))
        items[1].x += 35
        items.append(MenuItem('Вихід', self.on_quit))
        items[2].x += 35
        self.create_menu(items, shake(), shake_back())

    def on_new_game(self):
        import Level3_Background
        director.push(SlideInTTransition(Level3_Background.get_newgame()))

    def on_choose_lvl(self):
        pass

    def on_quit(self):
        pyglet.app.exit()


def get_menu():
  
    menu = MainMenu()
    main_bg = MainScene()
    scene = Scene()
   
    Sound.play("res/audio/Menu.mp3")

    scene.add(main_bg)
    scene.add(menu)

    return scene
