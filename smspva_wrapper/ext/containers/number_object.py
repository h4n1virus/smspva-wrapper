class NumberContainer:
    """Immutable high level container for get_number query"""

    def __init__(self, data: dict):
        self._data = data

    @property
    def data(self) -> dict:
        return self._data

    @property
    def response(self) -> int:
        return int(self._data.get('response'))

    @property
    def country_code(self) -> str:
        return self._data.get('CountryCode')

    @property
    def number(self) -> str:
        return self._data.get('number')

    @property
    def full_number(self) -> str:
        return f"{self.country_code}{self.number}"

    @property
    def id(self) -> str:
        return self._data.get('id')
