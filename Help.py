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
import fonts



class Help(Menu):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Help, self).__init__('Допомога')

       # TITLE
        self.font_title['font_name'] = 'Peace Sans'
        self.font_title['bold'] = True
        self.font_title['font_size'] = 60
        self.font_title['color'] = (255, 69, 0, 255)

        # ITEM
        self.font_item['font_name'] = 'Vodafone Rg'
        self.font_item['color'] = (0, 150, 115, 255)
        self.font_title['bold'] = True
        self.font_item['font_size'] = 35

        # ITEM SELECTED
        self.font_item_selected['font_name'] = 'Vodafone Rg'
        self.font_item_selected['color'] = (140, 0, 0, 255)
        self.font_title['bold'] = True
        self.font_item_selected['font_size'] = 35

        items = []
        self.volumes = ['0', '2', '4', '6', '8', '10']
        
        items.append(MenuItem('Гарячі клавіші', self.on_hotkey))
        items[0].x += 35
        items.append(MultipleMenuItem('Гучність: ', self.on_switch, self.volumes, 3))
        items[1].x += 35
        items.append(ToggleMenuItem("Кадри за секунду: ", self.on_show_fps, False))
        items[2].x += 35
        items.append(MenuItem('В меню', self.on_menu))
        items[3].x += 35
        

        self.create_menu(items, shake(), shake_back())

    def on_hotkey(self):
        import Hotkeys
        director.push(SlideInTTransition(Hotkeys.get_hotkeys()))

    def on_switch(self, index):
        if(self.volumes[index] == '0'):
            Sound.mute_volume(0)
        elif(self.volumes[index] == '2'):
            Sound.mute_volume(0.1)
        elif(self.volumes[index] == '4'):
            Sound.mute_volume(0.3)
        elif(self.volumes[index] == '6'):
            Sound.mute_volume(0.5)
        elif(self.volumes[index] == '8'):
            Sound.mute_volume(0.7)
        elif(self.volumes[index] == '10'):
            Sound.mute_volume(0.9)
       

    def on_show_fps(self, show_fps):
        director.show_FPS = show_fps
        
    def on_menu(self):
        director.pop()

    def on_quit(self):
        director.pop()
    
    
def get_help():

    scene = Scene()
    main_bg = MainScene()
    help = Help()

    scene.add(main_bg)
    scene.add(help)

    return scene