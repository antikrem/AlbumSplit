class TimePoint :

    def __init__(self, param) :
        self._milliseconds = TimePoint.MATCH[type(param)](param)

    @staticmethod
    def from_milliseconds(value) :
        return TimePoint(value / 1000.0)

    def time_from_string(x) :
        mins = int(x[:x.find(':')])
        secs = int(x[x.find(':') + 1:])
        return 1000 * (mins * 60 + secs)

    MATCH = {
        int: lambda x: x * 1000,
        str: time_from_string
    }

    def _get_time(self) :
        return self._milliseconds

    time = property(_get_time)