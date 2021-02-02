from kivy.app import App
from .board import Board

class LabyrinthApp(App):

    def on_pause(self):
        return True
