
class TimePoint :
    def __init__(self, param) :
        self._milliseconds = param * 1000

    @staticmethod
    def from_milliseconds(value) :
        return TimePoint(value / 1000.0)

    def _get_time(self) :
        return self._milliseconds

    time = property(_get_time)