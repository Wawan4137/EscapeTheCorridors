from kivy.uix.image import Image
from kivy.core.window import Window

class Coin(Image):
    imagesrc = 'assets/coin.png'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)