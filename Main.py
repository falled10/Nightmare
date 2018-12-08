from cocos.director import director
import Menu


def main():
    director.init(width=800, height=600, caption="Nightmare")
   
    director.run(Menu.get_menu()) 

if __name__ == '__main__':
    main()