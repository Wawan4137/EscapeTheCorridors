from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, BooleanProperty
from kivy.metrics import dp
from kivy.parser import parse_color

from labyrinth.prefabs.wall import Wall
from labyrinth.prefabs.coin import Coin
from labyrinth.prefabs.empty import Empty
from labyrinth.prefabs.finish import Finish
from labyrinth.prefabs.floor import Floor
from labyrinth.prefabs.player import Player

from .tile import Tile

COLORS = ["#804515", "#D49A6A", "#FFD1AA"]

class Board(Widget):

    nrows = NumericProperty(16)
    ncols = NumericProperty(16)
    tsize = NumericProperty(0)
    hmargin = NumericProperty(dp(10))
    wmargin = NumericProperty(dp(10))
    tx = NumericProperty(0)
    ty = NumericProperty(0)
    tmargin = NumericProperty(dp(1))
    colors = ListProperty([parse_color(c) for c in COLORS])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matrix = None
        self.display()
        self.getLevel()
        print(self.matrix[1][0].prefab)

    def display(self):
        level = self.getLevel()
        if self.matrix:
            for r in self.matrix:
                for t in r:
                    self.remove_widget(t)
        self.matrix = [
            [Tile(i, j, self, level[i][j]) for j in range(self.ncols)]
            for i in range(self.nrows)
        ]


    def getLevel(self):
        level = open('labyrinth/levels/level3.txt','r')
        matrixPrefabs = [
            [None for j in range(self.ncols)]
            for i in range(self.nrows)
        ]
        j = 0
        for x in level:
            i = 0
            for y in x:
                if i <= 15:
                    matrixPrefabs[j][i] = self.getRealPrefab(y)
                i += 1
            j+=1
        print (matrixPrefabs)
        return matrixPrefabs
                  

    def getRealPrefab(self, char):
        if char == "w":
            return Wall()
        if char == "f":
            return Finish()
        if char == "e":
            return Empty()
        if char == "c":
            return Coin()
        if char == "p":
            return Player()
        if char == "s":
            return Floor()
            