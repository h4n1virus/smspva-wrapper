class BalanceSIMContainer(object):
    """Immutable high level container for balance_sim query"""

    def __init__(self, data: dict):
        self._data = data

    @property
    def data(self) -> dict:
        return self._data

    @property
    def response(self) -> int:
        return int(self._data.get('response'))

    @property
    def balance(self) -> float:
        return float(self._data.get('amount'))
