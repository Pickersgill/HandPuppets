from view import View
from model import Model
from tkinter import  Tk

import sys

class Controller(Tk):
    def __init__(self, title="default"):
        Tk.__init__(self)
        self.title(title)
        self.resizable(False, False)
        self.model = Model(self)
        self.view = View(self, self.model)
        self.view.clear_canvas()
        self.mainloop()


