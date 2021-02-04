from kivy.uix.image import Image
from kivy.core.window import Window

class Finish(Image):
    imagesrc = 'assets/finish.png'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)