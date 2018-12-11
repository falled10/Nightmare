import cocos
from cocos.scene import Scene
from cocos.sprite import Sprite


class MainScene(Scene):
    def __init__(self):
        super().__init__()
        menu_bg = Sprite('res/maps/MoonBG.jpg')

        menu_bg.position = menu_bg.width // 2, menu_bg.height // 2

        self.add(menu_bg)