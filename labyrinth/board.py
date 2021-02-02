from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, BooleanProperty
from .tile import Tile
from kivy.metrics import dp
from kivy.parser import parse_color
from random import randint
from kivy.clock import Clock

COLORS = ["#804515", "#D49A6A", "#FFD1AA"]

class Board(Widget):

    nrows = NumericProperty(8)
    ncols = NumericProperty(8)
    tsize = NumericProperty(0)
    tmargin = NumericProperty(dp(10))
    tx = NumericProperty(0)
    ty = NumericProperty(0)
    margin = NumericProperty(dp(1))
    colors = ListProperty([parse_color(c) for c in COLORS])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matrix = None
        self.create()
    
    def create(self):
        if self.matrix:
            for ligne in self.matrix:
                for tile in ligne:
                    self.remove_widget(tile)
        self.matrix = [
            [Tile(i, j, self) for j in range(self.ncols)]
            for i in range(self.nrows)
        ]