from kivy.uix.image import Image
from kivy.core.window import Window

class Wall(Image):
    imagesrc = 'assets/wall.png'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)