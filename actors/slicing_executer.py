from os import terminal_size
from pydub import AudioSegment

from model.time_point import TimePoint
from model.album import Album
from model.file import File
from model.publishable_segment import PublishableSegment

Slicer = (int, str)
Slicers = list[Slicer]

TermintedSlicer = (int, int, int, str)
TermintedSlicers = list[TermintedSlicer]

class SlicingExecuter :

    def __init__(self, file: File, album: Album) :
        self._file = file
        self._album = album

        self._segment = AudioSegment.from_file(file.location, file.format)

    def slice(self, slicers: Slicers) -> list[PublishableSegment]:
        terminated_slicers = self._create_terminated_slicer(slicers)
        return map(terminated_slicers, self._export)

    def _create_terminated_slicer(self, slicers: Slicers) -> TermintedSlicers :
        file_end = len(self._segment)
        termintedSlicers = []
        
        for i in range(0, len(slicers)) :
            (start, name) = slicers[i]
            if i == len(slicers) - 1 :
                termintedSlicers.append((i, TimePoint(start), TimePoint.from_milliseconds(file_end), name))
            else :
                (next_start, _) = slicers[i + 1]
                termintedSlicers.append((i, TimePoint(start), TimePoint(next_start), name))

        return termintedSlicers

    def _export(self, terminated_slicer: TermintedSlicer) -> None:
        (_, start, end, _) = terminated_slicer
        return PublishableSegment(self._segment[start.time:end.time], self._create_tag_structure())

    def _create_tag_structure(self) :
        return {'artist' : self._album._band, 'album' : self._album._name}