import tkinter as tk
from tkinter import Frame, W, N, E, S, Button, Label, RIGHT, LEFT, BOTH, ttk, Canvas

class FileInputView(tk.Frame):

    TITLE_FONT = ("Helvetica", 18, "bold")

    def __init__(self, parent, model):
        tk.Frame.__init__(self, parent)

        self.pack(padx=20, pady=10)

        self.parent = parent
        self.model = model

        file_load_frame = Frame(self) #, bg="gold"
        file_load_frame.pack(fill=BOTH)

        title_button_frame = Frame(file_load_frame) #, bg="purple"
        title_button_frame.pack(fill=BOTH)

        bold_label = ttk.Label(title_button_frame, text=self.model.title, font=self.TITLE_FONT)
        bold_label.pack(side=LEFT, padx=5, pady=5)

        load_button = ttk.Button(title_button_frame, text="LOAD")
        load_button.pack(side=RIGHT, padx=5, pady=5)


        if self.model.location is None:
            filename_text = "No file selected"
        else:
            filename_text = self.model.location

        filename_label = Label(file_load_frame, text=filename_text)
        filename_label.pack(side=LEFT, padx=5, pady=5)