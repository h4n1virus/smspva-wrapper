class UserInfoContainer:
    """Immutable high level container for get_userinfo"""

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
        return float(self._data.get('balance'))

    @property
    def karma(self) -> float:
        return float(self._data.get('karma'))

    @property
    def name(self) -> str:
        return self._data.get('name')
