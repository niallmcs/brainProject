"""
Basic GUI Demonstatiopn

http://zetcode.com/gui/tkinter/layout/ - qutie useful
"""

from tkinter import Tk, Frame, BOTH, filedialog, W, N, E, S
from tkinter.ttk import Button, Style, Label

import matplotlib.pyplot as plt
import numpy as np
from nilearn import image
from nilearn import plotting


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        self.initUI()

        self.addButtons()
        self.addMainContent()
        
    
    def initUI(self):
      
        self.parent.title("Brain GUI")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        # style
        self.style = Style()
        self.style.theme_use("default")

        # Style().configure("TButton", padding=(0, 5, 0, 5), 
        #     font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)


    def centerWindow(self):
      
        w = 500
        h = 300

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def addButtons(self):
        anatomyButton = Button(self, text="Open Anatomy",
            command=self.openAnatomy)
        anatomyButton.grid(row=0, column=0)

        boldButton = Button(self, text="Open Bold",
            command=self.openBold)
        boldButton.grid(row=1, column=0)

        quitButton = Button(self, text="Quit",
            command=self.quit)
        quitButton.grid(row=2, column=0)

    def addMainContent(self):
        anatomy_label = Label(self, text="Anatomy")
        anatomy_label.grid(row=0, column=1)

        bold_labal = Label(self, text="BOLD")
        bold_labal.grid(row=1, column=1)


    def onOpen(self, types):
      
        ftypes = types
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        
        if fl != '':
            return fl

    def openAnatomy(self):
        file = self.onOpen([('NIFTI files', '*.nii.gz'), ('All files', '*')])
        print("anatomy file: " + file)
        plotting.plot_anat(file, title='Anatomy')
        plt.show()

    def openBold(self):
        file = self.onOpen([('NIFTI files', '*.nii.gz'), ('All files', '*')])
        print("anatomy file: " + file)

        bold = image.index_img(file, 0)

        plotting.plot_glass_brain(bold, title='glass_brain',
    black_bg=True, display_mode='ortho')
        plt.show()
        

def main():
  
    root = Tk()
    # root.geometry("500x400+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()