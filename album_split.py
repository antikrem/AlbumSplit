from model.file import File
from model.album import Album

from actors.spliter import Splitter

from view.gui import GUI
import tkinter as tk

root = tk.Tk()

wrappedApplication = GUI(root)
wrappedApplication.mainloop()