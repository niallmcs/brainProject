from numpy import *
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

root = Tk()
f1 = Figure()

canvas = FigureCanvasTkAgg(f1, master=root)
canvas.show()
canvas.get_tk_widget().pack(fill="x")
a = f1.add_subplot(111)
a.get_axes().set_frame_on(True)
ini = [[i] * 100 for i in range(100)]
cax = a.matshow(ini)

def redraw():
    mat = random.randint(0, 2**16-1, (1000, 1000))
    cax.set_data(mat)
    canvas.draw()
    root.after(100, redraw)

redraw()
root.mainloop()