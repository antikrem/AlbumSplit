from model.file import File
from model.album import Album

from actors.spliter import Splitter


album = Album('', '')
file = File('', '')
slicers = [
    ]


splitter = Splitter(file, album)
splitter.slice(slicers)

