from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, BooleanProperty
<<<<<<< HEAD
from .tile import Tile
from kivy.metrics import dp
from kivy.parser import parse_color
from random import randint
from kivy.clock import Clock
=======
from kivy.metrics import dp
from kivy.parser import parse_color
from .tile import Tile
>>>>>>> main

COLORS = ["#804515", "#D49A6A", "#FFD1AA"]

class Board(Widget):

<<<<<<< HEAD
    nrows = NumericProperty(8)
    ncols = NumericProperty(8)
    tsize = NumericProperty(0)
    tmargin = NumericProperty(dp(10))
    tx = NumericProperty(0)
    ty = NumericProperty(0)
    margin = NumericProperty(dp(1))
=======
    nrows = NumericProperty(16)
    ncols = NumericProperty(16)
    tsize = NumericProperty(0)
    hmargin = NumericProperty(dp(10))
    wmargin = NumericProperty(dp(10))
    tx = NumericProperty(0)
    ty = NumericProperty(0)
    tmargin = NumericProperty(dp(1))
>>>>>>> main
    colors = ListProperty([parse_color(c) for c in COLORS])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matrix = None
<<<<<<< HEAD
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
=======
        self.display()
        self.getLevel()

    def display(self):
        if self.matrix:
            for r in self.matrix:
                for t in r:
                    self.remove_widget(t)
        self.matrix = [
            [Tile(i, j, self) for j in range(self.ncols)]
            for i in range(self.nrows)
        ]


    def getLevel(self):
        level = open('labyrinth/levels/level1.txt','r')
        for x in level:
            for y in x:
                print('a')       

    def get(self, i, j):
        if i >= 0 and i < self.nrows and j >= 0 and j < self.ncols:
            return self.matrix[i][j]
        else:
            return None
            
>>>>>>> main
