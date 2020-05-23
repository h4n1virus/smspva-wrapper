class RedirectContainer:
    """Immutable high level container for redirect"""

    def __init__(self, data: dict):
        self._data = data

    @property
    def data(self) -> dict:
        return self._data

    @property
    def response(self) -> int:
        return int(self._data.get('response'))

    def forwarding(self) -> str:
        return self._data.get('forwarding')
