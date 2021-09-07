from pydub import AudioSegment

class PublishableSegment :

    def __init__(self, segment: AudioSegment, name: str, track_number: int, tags: dict) :
        self._segment = segment
        self._name = name
        self._track_number = track_number
        self._tags = tags 