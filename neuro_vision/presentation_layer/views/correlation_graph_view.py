import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from presentation_layer.util.brain_correlation_plotter import plot_lightbox
from presentation_layer.views.base_results_view import BaseResultsView

plt.style.use('ggplot')

class CorrelationGraphView(BaseResultsView):

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

        

        
        

    def plot_results(self, overlay_data, mri_args):
        plot_lightbox(overlay=overlay_data, vlim=(-1.0, 1.0), do_stretch_colors=True, fig=self.figure, **mri_args)

        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.canvas.draw()