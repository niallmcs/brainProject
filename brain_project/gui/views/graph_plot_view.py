import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

plt.style.use('ggplot')

class GraphPlotView(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.figure = Figure(figsize=(4,5), dpi=100)
        #figure = plt.figure(figsize=(4,5), dpi=100)

        # ax1 = self.figure.add_subplot(211)
        # ax1.set_title('Original Trajectory')
        # ax1.plot([1,2,3,4,5],[5,6,7,8,9])

        # ax2 = self.figure.add_subplot(212, sharex=ax1, sharey=ax1)
        # ax2.set_title('Predicted Trajectory')
        # ax2.plot([1,2,3,4,5],[5,6,7,8,9])

        #plt.tight_layout()


        #if broke on windows - follow https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/xssOnleIPFw
        self.canvas = FigureCanvasTkAgg(self.figure, self)

        self.canvas.show()

        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.value = 10

        
        self.ax1 = None
        self.ax2 = None

        

        #toolbar = NavigationToolbar2TkAgg(canvas, self)
        #toolbar.update()
        #canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def plot_results(self, results):


        print("got this far")
        if self.ax1 is not None:
            self.ax1.clear()
        self.ax1 = self.figure.add_subplot(211)
        self.ax1.set_title('Original Trajectory')
        self.ax1.plot(results)

        if self.ax2 is not None:
            self.ax2.clear()
        self.ax2 = self.figure.add_subplot(212, sharex=self.ax1, sharey=self.ax1)
        self.ax2.set_title('Predicted Trajectory')
        self.value = self.value+1
        self.ax2.plot([1,2,3,4,5],[5,6,7,8,self.value])
        self.canvas.draw()