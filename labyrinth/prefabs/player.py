from kivy.uix.image import Image
from kivy.core.window import Window

class Player(Image):
    imagesrc = 'assets/player.png'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)