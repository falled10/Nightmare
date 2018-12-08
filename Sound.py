from pygame import mixer
from pygame.mixer import music
import pyglet
from pyglet.window import key
import time
import cocos

mixer.pre_init(44100, -16, 2, 1024)     
mixer.init()

# Make sure we exit the mixer when the application quits
cocos.director.event_loop.push_handlers(on_exit=mixer.quit)

def play(soundtrack):
    # music.load(bytes(os.path.join("assets", "music", soundtrack), 'utf-8'))
    music.load(soundtrack)
  
    music.play(loops=-1)

def actions_play(soundtrack):
    music.load(soundtrack)
    
    music.play(loops=1)
    
def pause():
    music.pause()

def mute_volume(m):
    music.set_volume(m)

def on_off():
    if(music.get_volume()==1):
        music.set_volume(0)
    elif(music.get_volume()==0):
        music.set_volume(1)

def resume():
    music.unpause()
      