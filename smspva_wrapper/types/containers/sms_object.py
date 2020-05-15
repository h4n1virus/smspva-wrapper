class SMS:
    """Immutable high level container for get_sms"""

    def __init__(self, data: dict):
        self._data = data

    @property
    def data(self) -> dict:
        return self._data

    @property
    def response(self) -> int:
        return int(self._data.get('response'))

    @property
    def number(self) -> str:
        return self._data.get('number')

    @property
    def sms(self) -> str:
        return self._data.get('sms')
