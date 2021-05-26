from os.path import exists

class File :
    def __init__(self, location: str, format: str) :

        if not exists(location) :
            raise FileNotFoundError(f'Could not find file "{location}"')

        self._location = location
        self._format = format

    def _get_location(self) -> str :
        return self._location

    def _get_format(self) -> str :
        return self._format

    location = property(_get_location)
    format = property(_get_format)