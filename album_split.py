from file import File
from album import Album
from slicing_executer import SlicingExecuter

album = Album("Rings of Saturn", "GIDIM")
file = File("RINGS OF SATURN - GIDIM OFFICIAL FULL LENGTH ALBUM STREAM 2019.mp3", "mp3")
slicers = [(0, "Pustules"), (269, "Divine Authority"), (482, "Hypodermis Glitch")]

SlicingExecuter().slice(file, album, slicers)