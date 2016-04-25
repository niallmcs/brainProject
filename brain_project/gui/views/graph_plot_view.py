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

        figure = Figure(figsize=(4,5), dpi=100)
        #figure = plt.figure(figsize=(4,5), dpi=100)

        ax1 = figure.add_subplot(211)
        ax1.set_title('Original Trajectory')
        ax1.plot([1,2,3,4,5],[5,6,7,8,9])

        ax2 = figure.add_subplot(212, sharex=ax1, sharey=ax1)
        ax2.set_title('Predicted Trajectory')
        ax2.plot([1,2,3,4,5],[5,6,7,8,9])

        #plt.tight_layout()


        #if broke on windows - follow https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/xssOnleIPFw
        canvas = FigureCanvasTkAgg(figure, self)

        canvas.show()

        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        

        #toolbar = NavigationToolbar2TkAgg(canvas, self)
        #toolbar.update()
        #canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)