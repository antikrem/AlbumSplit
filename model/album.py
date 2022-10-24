class Album :

    def __init__(self, band: str, name: str, year: int, cover: str | None) :
        self._name = name
        self._band = band
        self._year = year
        self._cover = cover