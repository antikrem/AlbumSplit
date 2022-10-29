import tkinter as tk
from tkinter import filedialog as fd
from unicodedata import name
from model.album import Album

from model.file import File
from actors.spliter import Splitter


class GUI(tk.Frame) :
    
    _file = None
    _cover = None

    def __init__(self, parent: tk.Tk) :
        tk.Frame.__init__(self, parent)
        self.pack(side=tk.TOP)

        self._pickFileButton = tk.Button(self, text='Open music file', command=self._openFile)
        self._pickFileButton.pack(side=tk.TOP)

        tk.Label(self, text='Name').pack(side=tk.TOP)
        self._nameTextBox = tk.Entry(self)
        self._nameTextBox.pack(side=tk.TOP)

        tk.Label(self, text='Band').pack(side=tk.TOP)
        self._bandTextBox = tk.Entry(self)
        self._bandTextBox.pack(side=tk.TOP)

        tk.Label(self, text='Year').pack(side=tk.TOP)
        self._yearTextBox = tk.Entry(self)
        self._yearTextBox.pack(side=tk.TOP)

        self._pickCoverButton = tk.Button(self, text='Open cover file', command=self._openCover)
        self._pickCoverButton.pack(side=tk.TOP)

        tk.Label(self, text='Slicers').pack(side=tk.TOP)
        self._slicerText = tk.Text(self)
        self._slicerText.pack(side=tk.TOP)

        self._convertButton = tk.Button(self, text='Convert', command=self._convert)
        self._convertButton.pack(side=tk.TOP)

    def _openFile(self) :
        file = fd.askopenfile()
        if file is not None :
            self._loadFile(file.name)

    def _openCover(self) :
        file = fd.askopenfile()
        if file is not None :
            self._cover = file.name

    def _loadFile(self, filename: str) :
        self._file = File(filename, 'mp3')
        self._cover = None

    def _convert(self) :
        slicers = self._createSlicers(self._slicerText.get("1.0", 'end-1c'))
        album = Album(self._bandTextBox.get(), self._nameTextBox.get(), int(self._yearTextBox.get()), self._cover)
        spliter = Splitter(self._file, album)
        spliter.slice(slicers)

    def _createSlicers(self, text) -> str :
        lines = text.split('\n')
        return [self._createSlicer(line) for line in lines]

    def _createSlicer(self, text) -> str :
        return tuple(map(lambda x : x.strip(), text.split(';')))
