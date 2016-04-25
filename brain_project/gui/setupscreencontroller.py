import setupscreen
from tkinter import Tk
from setupscreen import SetupScreen

def main():
    root = Tk()
    # root.geometry("500x400+300+300")
    app = SetupScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()