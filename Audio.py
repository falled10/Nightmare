from cocos.scene import Scene
from cocos.layer import Layer
from cocos.director import director

from cocos.audio.pygame.mixer import Sound
from cocos.audio.pygame import mixer


class Audio(Sound):
    def __init__(self, audio_file):
        # As stated above, we initialize the super class with the audio file we passed in
        super(Audio, self).__init__(audio_file)

class AudioLayer(Layer):
    def __init__(self):
        super(AudioLayer, self).__init__()
        song = Audio("/res/audio/sound.ogg")
        song.play(-1)