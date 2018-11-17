
from cocos import director
from cocos.scene import Scene
from cocos.layer import MultiplexLayer
from Menu import MainMenu
from cocos.director import director

from pyglet.window import key

keyboard = key.KeyStateHandler()

def main():
    director.init(width=800, height=600, caption="Match 3")
    director.window.pop_handlers()
    director.window.push_handlers(keyboard)
    scene = Scene()
    scene.add(MainMenu())

    director.run(scene)


if __name__ == '__main__':
    main()

    

   
  
