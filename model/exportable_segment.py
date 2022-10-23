from pydub import AudioSegment

class ExportableSegment :

    def __init__(self, segment: AudioSegment, name: str, track_number: int, tags: dict, cover: str | None) :
        self._segment = segment
        self._name = name
        self._track_number = track_number
        self._tags = tags 
        self._cover = cover

    def export(self, location: str, format: str) :
        self._segment.export(location, format=format, tags=self._tags, cover=self._cover)