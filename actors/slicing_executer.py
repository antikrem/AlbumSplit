from os import terminal_size
from pydub import AudioSegment

from model.time_point import TimePoint
from model.album import Album
from model.file import File
from model.exportable_segment import ExportableSegment

Slicer = (int, str)
Slicers = list[Slicer]

TermintedSlicer = (int, int, int, str)
TermintedSlicers = list[TermintedSlicer]

class SlicingExecuter :

    def __init__(self, file: File, album: Album) :
        self._file = file
        self._album = album

        self._segment = AudioSegment.from_file(file.location, file.format)

    def slice(self, slicers: Slicers) -> list[ExportableSegment]:
        terminated_slicers = self._create_terminated_slicer(slicers)
        return [self._export(index, slicer) for index, slicer in enumerate(terminated_slicers)]

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

    def _export(self, trackNumber: int, terminated_slicer: TermintedSlicer) -> None:
        (track, start, end, name) = terminated_slicer
        return ExportableSegment(self._segment[start.time:end.time], name, track, self._create_tag_structure(trackNumber))

    def _create_tag_structure(self, trackNumber: int) :
        return {'artist' : self._album._band, 'album' : self._album._name, 'track' : trackNumber + 1}