from kivy.uix.image import Image
from kivy.core.window import Window

class Floor(Image):
    imagesrc = 'assets/floor.png'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)