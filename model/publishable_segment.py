from pydub import AudioSegment

class PublishableSegment :
    def __init__(self, segment: AudioSegment, tags: dict) :

        self._segment = segment
        self._tags = tags 