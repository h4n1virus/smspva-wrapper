class ProverkaContainer:
    """Immutable high level container for get_proverka"""

    def __init__(self, data: dict):
        self._data = data

    @property
    def data(self) -> dict:
        return self._data

    @property
    def number(self) -> str:
        return self._data.get('number')

    @property
    def sms(self) -> str:
        return self._data.get('sms')
