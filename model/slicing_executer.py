from os import terminal_size
from pydub import AudioSegment

from album import Album
from file import File

Slicer = (int, str)
Slicers = list[Slicer]

TermintedSlicer = (int, int, str)
TermintedSlicers = list[TermintedSlicer]

class SlicingExecuter :

    def __init__(self, file: File, album: Album) :
        self._file = file
        self._album = album

        self._segment = AudioSegment.from_file(file.location, file.format)

    def slice(self, slicers: Slicers) :
        terminated_slicers = self._create_terminated_slicer(slicers)

        for terminated_slicer in terminated_slicers :
            self._export(terminated_slicer)

    def _create_terminated_slicer(self, slicers: Slicers) -> TermintedSlicers :
        file_end = len(self._segment)
        termintedSlicers = []
        
        for i in range(0, len(slicers)) :
            (start, name) = slicers[i]
            if i == len(slicers) - 1 :
                termintedSlicers.append((start * 1000, file_end, name))
            else :
                (next_start, _) = slicers[i + 1]
                termintedSlicers.append((start * 1000, next_start * 1000, name))

        return termintedSlicers

    def _export(self, terminated_slicer: TermintedSlicer) -> None:
        (start, end, name) = terminated_slicer
        format = "mp3"
        self._segment[start:end].export(f'{name}.{format}', format=format, tags=self._create_tag_structure())

    def _create_tag_structure(self) :
        return {'artist' : self._album._band, 'album' : self._album._name}