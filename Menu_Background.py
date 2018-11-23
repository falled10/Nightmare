import cocos
from cocos.scene import Scene
from cocos.sprite import Sprite


class MainScene(Scene):
    def __init__(self):
        super().__init__()
        menu_bg = Sprite('res/maps/MainMenu.png')
        menu_bg.position = menu_bg.width // 2, menu_bg.height // 2

        self.px_width = menu_bg.width 
        self.px_height = menu_bg.height
        self.add(menu_bg)