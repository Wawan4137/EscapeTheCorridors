from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, BooleanProperty, ObjectProperty
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
        self.player = None
        self.totalCoins = 0
        self.nbCoins = 0
        self.display()
        self.getLevel()
        self.findPlayer()

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

    def findPlayer(self):
        if self.matrix:
            for r in self.matrix:
                for t in r:
                    if isinstance(t.prefab, Player):
                        self.player = t
                        return

    def getLevel(self):
        level = open('labyrinth/levels/level4.txt','r')
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
        return matrixPrefabs
                  

    def getRealPrefab(self, char):
        if char == "w":
            return Wall()
        if char == "f":
            return Finish()
        if char == "e":
            return Empty()
        if char == "c":
            self.totalCoins += 1
            return Coin()
        if char == "p":
            return Player()
        if char == "s":
            return Floor()

    #Event click on move button
    #Action = "up","down","left","right"
    def movePlayer(self, action):
        iPlayer = self.player.row
        jPlayer = self.player.col
        actionDone = False
        if action == "up":
            if not (isinstance(self.matrix[iPlayer+1][jPlayer].prefab, Wall) or isinstance(self.matrix[iPlayer+1][jPlayer].prefab, Empty)):
                self.player.row = iPlayer+1
                self.checkCoin()
                self.matrix[self.player.row][jPlayer] = self.player
                actionDone = True
        if action == "down":
            if not (isinstance(self.matrix[iPlayer-1][jPlayer].prefab, Wall) or isinstance(self.matrix[iPlayer-1][jPlayer].prefab, Empty)):
                self.player.row = iPlayer-1
                self.checkCoin()
                self.matrix[self.player.row][jPlayer] = self.player
                actionDone = True
        if action == "left":
            if not (isinstance(self.matrix[iPlayer][jPlayer-1].prefab, Wall) or isinstance(self.matrix[iPlayer][jPlayer-1].prefab, Empty)):
                self.player.col = jPlayer-1
                self.checkCoin()
                self.matrix[iPlayer][self.player.col] = self.player
                actionDone = True
        if action == "right":
            if not (isinstance(self.matrix[iPlayer][jPlayer+1].prefab, Wall) or isinstance(self.matrix[iPlayer][jPlayer+1].prefab, Empty)):
                self.player.col = jPlayer+1
                self.checkCoin()
                self.matrix[iPlayer][self.player.col] = self.player
                actionDone = True       
        if actionDone:         
            tmpTile = Tile(iPlayer,jPlayer, self, Empty())
            self.matrix[iPlayer][jPlayer] = tmpTile
        
    
    def checkCoin(self):
        if isinstance(self.matrix[self.player.row][self.player.col].prefab, Coin):
            self.nbCoins += 1
            print(self.nbCoins)
        if self.nbCoins*2 >= self.totalCoins:
            if isinstance(self.matrix[self.player.row][self.player.col].prefab, Finish):
                print("gg")

            
 

            