import tkinter as tk
import presentation_layer.views.base_view as bv
from tkinter import Frame, W, N, E, S, Button, Label, RIGHT, LEFT, BOTH, BOTTOM, ttk, Canvas, NW, TOP, YES


class AboutPage(bv.BaseView):

    def create_widgets(self):

        back_button = tk.Button(self, text="Back",
                            command=lambda: self.controller.show_frame("StartPage"), borderwidth=0)
        back_button.pack(side=TOP, padx=5, pady=5, anchor=NW)

        label = tk.Label(self, text="About NeuroVision", font=self.TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        neuro_vision_bio = "A tool used to analyse brain activity and an emotional trajectory. Using this data, the utility should be able to predict the current emotion using brain activity from a fMRI alone."

        main_body_label = tk.Label(self, text=neuro_vision_bio, wraplength=300)
        main_body_label.pack(side="top", pady=10)
        


    def setup_window_details(self):
        self.controller.title("Welcome Screen")
        self.controller.geometry("400x400")
        self.center()