from tkinter import StringVar, IntVar


class FileInputModel:

    def __init__(self, title, description, file_types, file_handler):

        self.title = title
        self.description = description
        self.file_types = file_types
        self.location = None
        self.location_text = StringVar()
        self.location_text.set("Nothing yet")
        self.file_handler = file_handler

    def open(self):
        return self.file_handler(self.location)