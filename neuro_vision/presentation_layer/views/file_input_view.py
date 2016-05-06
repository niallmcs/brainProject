import tkinter as tk

import presentation_layer.views.base_view as bv

from tkinter import Frame, W, N, E, S, Button, Label, RIGHT, LEFT, BOTH, ttk, Canvas, filedialog, StringVar

class FileInputView(bv.BaseView):

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

        title_label = ttk.Label(title_button_frame, text=self.model.title, font=self.TITLE_FONT)
        title_label.pack(side=LEFT, padx=5, pady=5)

        load_button = ttk.Button(title_button_frame, text="SELECT", command=self.openFile)
        load_button.pack(side=RIGHT, padx=5, pady=5)


        if self.model.location is None:
            filename_text = "No file selected"
        else:
            filename_text = self.model.location

        filename_label = Label(file_load_frame, textvariable=self.model.location_text)
        filename_label.pack(side=LEFT, padx=5, pady=5)


    def openFile(self):
        file = self.onOpen(self.model.file_types)
        if file is not None:
            self.model.location = file
            text = file.split('/')
            self.model.location_text.set(text[len(text)-1])

        print(self.model.location)


    def onOpen(self, types):
      
        ftypes = types
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        
        if fl != '':
            return fl