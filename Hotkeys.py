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
import fonts



class Hotkeys(Menu):
    is_event_handler = True  #: enable director.window events

    def __init__(self):
        super(Hotkeys, self).__init__()

        # ITEM SELECTED
        self.font_item_selected['font_name'] = 'Motion Control'
        self.font_item_selected['color'] = (215, 100, 55, 255)
        self.font_title['bold'] = True
        self.font_item_selected['font_size'] = 25

        items = []

        items.append(MenuItem('Назад', self.on_back))
        
        items[0].y -= 280
        items[0].x += 30

        self.create_menu(items, shake(), shake_back())
    
    def on_back(self):
        director.pop()

    def on_quit(self):
        director.pop()

    

class HotkeyScene(Scene):
    def __init__(self):
        super().__init__()
        bg = Sprite("res/keyboard/HorrorBack.png")
        bg.position = bg.width // 2, bg.height // 2
        self.add(bg)
        manage = Label("Загальні", font_name = 'KreepTown', font_size = 30, bold = True, color = (10, 165, 85, 255))
        manage.position = (60,560)
        self.add(manage)
        # ESC ==========================================================
        key_ESC = Sprite('res/keyboard/key_ESC.png')
        key_ESC.position = (30,510)
        self.add(key_ESC)

        esc = Label("Вихід/Назад", font_size = 20, bold = True, color = (10, 165, 85, 255))
        esc.position = (60,500)
        self.add(esc)
        
        # Pause ========================================================
        key_P = Sprite('res/keyboard/key_P.png')
        key_P.position = (30,450)
        
        self.add(key_P)

        p = Label("Пауза", font_size = 20, bold = True, color = (10, 165, 85, 255))
        p.position = (60,440)
        self.add(p)
       
        # Mute =========================================================
        key_M = Sprite('res/keyboard/key_M.png')
        key_M.position = (30,390)
        self.add(key_M)

        m = Label("Вимкнути/Увімкнути звук", font_size = 20, bold = True, color = (10, 165, 85, 255))
        m.position = (60,380)
        self.add(m)
        #===============================================================

        movement = Label("Дії", font_name = 'Foul Fiend', font_size = 30, bold = True, color = (200, 150, 80, 255))
        movement.position = (650,560)
        self.add(movement)
        # Move Right ===================================================
        right_arrow = Sprite('res/keyboard/right_arrow.png')
        right_arrow.position = (580,510)
        self.add(right_arrow)
        
        r_a = Label("Рух вправо", font_size = 20, bold = True, color = (220,150,80, 255))
        r_a.position = (620,505)
        self.add(r_a)

        # Move Left ====================================================
        left_arrow = Sprite('res/keyboard/left_arrow.png')
        left_arrow.position = (580,450)
        self.add(left_arrow)
        
        l_a = Label("Рух вліво", font_size = 20, bold = True, color = (220,150,80, 255))
        l_a.position = (620,445)
        self.add(l_a)

        # Jump =========================================================
        key_B = Sprite('res/keyboard/key_B.png')
        key_B.position = (580,390)
        self.add(key_B)
        
        b = Label("Блок", font_size = 20, bold = True, color = (220,150,80, 255))
        b.position = (620,380)
        self.add(b)

        
        #==============================================================
        
        attack = Label("Атака", font_size = 30, bold = True, color = (255, 65, 65, 255))
        attack.position = (360,270)
        self.add(attack)

        # Attack_1======================================================
        key_Z = Sprite('res/keyboard/key_Z.png')
        key_Z.position = (170,220)
        self.add(key_Z)

        a1 = Label("Атака мечем (Доступно на 1 рівні)", font_size = 20, bold = True, color = (255, 65, 65, 255))
        a1.position = (200,215)
        self.add(a1)

        # Attack_2======================================================
        key_X = Sprite('res/keyboard/key_X.png')
        key_X.position = (170,160)
        self.add(key_X)

        a2 = Label("Атака мечем (Доступно на 2 рівні)", font_size = 20, bold = True, color = (255, 65, 65, 255))
        a2.position = (200,155)
        self.add(a2)

        # Attack_3======================================================
        key_C = Sprite('res/keyboard/key_C.png')
        key_C.position = (170,100)
        self.add(key_C)

        a3 = Label("Атака мечем (Доступно на 3 рівні)", font_size = 20, bold = True, color = (255, 65, 65, 255))
        a3.position = (200,95)
        self.add(a3)
        #===============================================================
  
    
def get_hotkeys():
  
    scene = Scene()
    h_scene = HotkeyScene()
    hotkey = Hotkeys()
    scene.add(h_scene)
    scene.add(hotkey)

    return scene