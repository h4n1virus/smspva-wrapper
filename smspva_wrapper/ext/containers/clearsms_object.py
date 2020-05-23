class ClearSMSContainer:
    """Immutable high level container for clearsms query"""

    def __init__(self, data: dict):
        self._data = data

    @property
    def data(self) -> dict:
        return self._data

    @property
    def response(self) -> int:
        return int(self._data.get('number'))

    @property
    def clearsms(self) -> str:
        return self._data.get('clearsms')
