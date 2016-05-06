import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as backend

from matplotlib.figure import Figure


root = tk.Tk()
f1 = Figure()

canvas = backend.FigureCanvasTkAgg(f1, master=root)
canvas.show()
canvas.get_tk_widget().pack(fill="x")
a = f1.add_subplot(111)
a.get_axes().set_frame_on(True)
ini = [[i] * 100 for i in range(100)]
cax = a.matshow(ini)


def run():
    mat = np.random.randint(0, 2**16-1, (1000, 1000))
    cax.set_data(mat)
    canvas.draw()
    root.after(15, run)


run()
root.mainloop()