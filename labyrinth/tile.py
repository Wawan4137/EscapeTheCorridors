from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.animation import Animation

class Tile(Widget):

    row = NumericProperty(0)
    col = NumericProperty(0)
    board = ObjectProperty(None)
    state = NumericProperty(0)
    rgba = ObjectProperty((1,0,1,1))

    def __init__(self, ligne, colonne, board):
        self.row = ligne
        self.col = colonne
        self.board = board
        super().__init__()
        self.rgba = self.board.colors[0]
        self.board.add_widget(self)