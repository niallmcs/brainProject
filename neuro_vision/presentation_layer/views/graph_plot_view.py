import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


from tkinter import Frame, W, N, E, S, Button, Label, RIGHT, LEFT, BOTH, BOTTOM, ttk, Canvas, StringVar, filedialog
import numpy as np
import pickle

from .base_results_view import BaseResultsView

plt.style.use('ggplot')

class GraphPlotView(BaseResultsView):

    results = None

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="white")

        #self.figure = Figure(figsize=(4,5), dpi=100)
        self.figure = plt.figure(figsize=(4,5), dpi=100)

        self.ax1 = None
        self.ax2 = None

        self.ax1 = self.figure.add_subplot(211)
        # ax1.set_title('Original Trajectory')
        # ax1.plot([1,2,3,4,5],[5,6,7,8,9])

        self.ax2 = self.figure.add_subplot(212, sharex=self.ax1, sharey=self.ax1)
        # ax2.set_title('Predicted Trajectory')
        # ax2.plot([1,2,3,4,5],[5,6,7,8,9])

        plt.tight_layout()


        #if broke on windows - follow https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/xssOnleIPFw
        self.canvas = FigureCanvasTkAgg(self.figure, self)

        self.canvas.show()

        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.value = 10

        
        

        self.export_button = ttk.Button(self, text="Export Predicted Trajectory", state='disabled',
                            command=lambda: self.export_results())
        


        self.file_opt = options = {}
        options['filetypes'] = [('all files', '.*'), ('pickle files', '.pkl')]
        options['initialfile'] = 'results.pkl'
        options['parent'] = parent
        
        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    def plot_results(self, original, results):

        self.export_button.config(state='normal')
        self.results = results

        if self.ax1 is not None:
            self.ax1.clear()
        self.ax1 = self.figure.add_subplot(211)
        self.ax1.set_title('Original Trajectory')
        self.ax1.plot(original)

        if self.ax2 is not None:
            self.ax2.clear()
        self.ax2 = self.figure.add_subplot(212, sharex=self.ax1, sharey=self.ax1)
        self.ax2.set_title('Predicted Trajectory')
        self.value = self.value+1
        self.ax2.plot(results)
        self.canvas.draw()

        self.export_button.pack(side="right", padx=5, pady=5)

    def export_results(self):
        file_location = filedialog.asksaveasfilename(**self.file_opt)
        output = open(file_location, 'wb')
        pickle.dump(self.results, output)
        output.close()
