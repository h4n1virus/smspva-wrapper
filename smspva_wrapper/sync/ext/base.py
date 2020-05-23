from smspva_wrapper.errors import Errors


class Base:
    def __init__(
        self,
        api_key: str,
        backend: str = 'smspva',
    ):
        self.api_key = api_key
        self.backend = self._get_backend(backend)
        self._api_base = self.api_base

    @property
    def api_base(self):
        return f'{self.backend}apikey={self.api_key}'

    @staticmethod
    def _get_backend(backend) -> str:
        if 'smspva' == backend.lower():
            return 'http://smspva.com/priemnik.php?'
        elif 'simsms' == backend.lower():
            return 'https://simsms.org/priemnik.php?'
        else:
            raise Errors.UnrecognizableBackEndError
