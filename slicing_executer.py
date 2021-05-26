from os import terminal_size
from pydub import AudioSegment

from album import Album
from file import File

Slicer = (int, str)
Slicers = list[Slicer]

TermintedSlicer = (int, int, str)
TermintedSlicers = list[TermintedSlicer]

class SlicingExecuter :

    def slice(self, file: File, album: Album, slicers: Slicers) :
        segment = AudioSegment.from_file(file.location, file.format)

        terminated_slicers = self._create_terminated_slicer(slicers, len(segment))

        for terminated_slicer in terminated_slicers :
            SlicingExecuter._export(segment, terminated_slicer, album)

    def _create_terminated_slicer(self, slicers: Slicers, file_end: int) -> TermintedSlicers :
        termintedSlicers = []
        
        for i in range(0, len(slicers)) :
            (start, name) = slicers[i]
            if i == len(slicers) - 1 :
                termintedSlicers.append((start * 1000, file_end, name))
            else :
                (next_start, _) = slicers[i + 1]
                termintedSlicers.append((start * 1000, next_start * 1000, name))

        return termintedSlicers

    @staticmethod
    def _export(segment: AudioSegment, terminated_slicer: TermintedSlicer, album: Album) -> None:
        (start, end, name) = terminated_slicer
        format = "mp3"
        segment[start:end].export(f'{name}.{format}', format=format, tags=SlicingExecuter._create_tag_structure(album))

    @staticmethod
    def _create_tag_structure(album: Album) :
        return {'artist' : album._band, 'album' : album._name}