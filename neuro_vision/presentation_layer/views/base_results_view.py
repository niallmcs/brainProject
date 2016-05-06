import tkinter as tk

from tkinter import Frame

import presentation_layer.views.base_view as bv

class BaseResultsView(bv.BaseView):

    results = None

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="white")

    def plot_results(self, *args):
        pass
