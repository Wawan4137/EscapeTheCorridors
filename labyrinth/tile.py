from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from labyrinth.prefabs.default import Default

class Tile(Widget):
    row = NumericProperty(0)
    col = NumericProperty(0)
    board = ObjectProperty(None)
    #1 Wall/ 2 Sol/ 3 Sol cassé/ 4 Coin/ 5 Personnage/ 6 Fin
    state = NumericProperty(0)
    prefab = ObjectProperty(None)
    rgba = ObjectProperty((1,1,1,1))



    def __init__(self, i, j, board, prefab):
        self.row = i
        self.col = j
        self.board = board
        self.prefab = prefab
        super().__init__()
        self.rgba = self.board.colors[0]
        self.board.add_widget(self)
        #self.prefab = prefab
        #self.state = state

    def addPrefab(self, prefab):
        self.prefab = prefab
