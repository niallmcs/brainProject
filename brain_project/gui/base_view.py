import tkinter as tk
from tkinter import StringVar

class BaseView(tk.Frame):

    TITLE_FONT = ("Helvetica", 18, "bold")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.grid()
        self.create_widgets()
        self.setup_window_details()

        

    def create_widgets(self):
        """Create the widgets for the frame."""
        raise NotImplementedError

    def setup_window_details(self):
        raise NotImplementedError

    def center(self):

        toplevel = self.controller

        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))