
from cocos import director
from cocos.scene import Scene
from cocos.layer import MultiplexLayer
from Menu import MainMenu
from cocos.director import director
from cocos.layer import *
from Menu_Background import MainScene
from pyglet.window import key

def main():
    director.init(width=800, height=600, caption="Nightmare")
    director.window.pop_handlers()
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)
    
    menu = MainMenu()
    main_bg = MainScene()
    scene = Scene()

    scene.add(main_bg)
    scene.add(menu)
    

    director.run(scene)


if __name__ == '__main__':
    main()

    

   
  
