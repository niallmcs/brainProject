import tkinter as tk
import base_view as bv
from PIL import Image, ImageTk

from tkinter import Frame, W, N, E, S, Button, Label, RIGHT, LEFT, BOTH, BOTTOM, ttk, Canvas

class StartPage(bv.BaseView):

    def create_widgets(self):

        logo_image = ImageTk.PhotoImage(Image.open("NeuroVision1024.png").resize((341, 256), Image.ANTIALIAS))

        logo_label = Label(self, image=logo_image)
        logo_label.image = logo_image
        logo_label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Find Correlation between story and fMRI data",
                            command=lambda: self.controller.show_frame("CorrelationTaskView"), borderwidth=0)
        button2 = tk.Button(self, text="Predict emotional response using Classification",
                            command=lambda: self.controller.show_frame("ClassificationTaskView"), borderwidth=0)
        button1.pack(padx=5, pady=5)
        regression_button = tk.Button(self, text="Predict emotional response using Regression",
                            command=lambda: self.controller.show_frame("RegressionTaskView"), borderwidth=0)
        button1.pack(padx=5, pady=5)
        button2.pack(padx=5, pady=5)
        regression_button.pack(padx=5, pady=5)

        about_button = tk.Button(self, text="About",
                            command=lambda: self.controller.show_frame("AboutPage"), borderwidth=0)
        about_button.pack(side="right", padx=5, pady=5)


    def setup_window_details(self):
        self.controller.title("Welcome Screen")
        self.controller.geometry("400x400")
        self.center()