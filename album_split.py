from model.file import File
from model.album import Album
from actors.slicing_executer import SlicingExecuter

album = Album('', '')
file = File('', '')
slicers = [
    ]

SlicingExecuter(file, album).slice(slicers)
