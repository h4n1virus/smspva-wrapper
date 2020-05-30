class NumberContainer:
    """Immutable high level container for get_number query"""

    def __init__(self, data: dict, country: str, service: str):
        self._data = data
        self._country = country
        self._service = service

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

    @property
    def country(self) -> str:
        return self._country

    @property
    def service(self) -> str:
        return self._service
