from pygame import mixer
from pygame.mixer import music
import pyglet

import cocos

mixer.pre_init(44100, -16, 2, 1024)
mixer.init()

# Make sure we exit the mixer when the application quits
cocos.director.event_loop.push_handlers(on_exit=mixer.quit)

def play(soundtrack):
    # music.load(bytes(os.path.join("assets", "music", soundtrack), 'utf-8'))
    music.load(soundtrack)
    music
    music.set_volume(0.5)
    music.play(loops=-1)

def pause():
    music.pause()

def stop():
    music.stop()

def resume():
    music.unpause()
    

"""
def transition(soundtrack, time):
    music.fadeout(time * 1000)
    pyglet.clock.schedule_once(next_music, time, soundtrack)

def next_music(dt, soundtrack):
    play(soundtrack)
"""