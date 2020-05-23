class TwoFAContainer:
    """Immutable high level container for get_two_fa"""

    def __init__(self, data: dict):
        self._data = data

    @property
    def data(self) -> dict:
        return self._data

    @property
    def response(self) -> int:
        return int(self._data.get('response'))

    @property
    def code_two_fa(self) -> str:
        return self._data.get('code2fa')

    @property
    def secret(self) -> str:
        return self._data.get('secret')

    @property
    def tonew(self) -> str:
        return self._data.get('tonew')
