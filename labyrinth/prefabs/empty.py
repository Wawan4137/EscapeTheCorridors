from kivy.uix.image import Image
from kivy.core.window import Window

class Empty(Image):
    imagesrc = 'assets/empty.png'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)