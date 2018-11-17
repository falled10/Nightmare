
from cocos import director
from cocos.scene import Scene
from cocos.layer import MultiplexLayer
from Menu import MainMenu
from cocos.director import director


def main():
    director.init(width=800, height=600, caption="Match 3")

    scene = Scene()
    scene.add(MainMenu())

    director.run(scene)


if __name__ == '__main__':
    main()

    

   
  
