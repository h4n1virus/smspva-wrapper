from smspva_wrapper.errors import Errors


class Base(object):
    def __init__(self, api_key: str = None, backend: str = 'smspva'):
        self._api_key = api_key
        self._backend = self._get_backend(backend)
        self._api_base = f'{self._backend}apikey={self._api_key}'

    @property
    def api_base(self):
        return self._api_base

    @staticmethod
    def _get_backend(backend) -> str:
        if 'smspva' == backend.lower():
            return 'http://smspva.com/priemnik.php?'
        elif 'simsms' == backend.lower():
            return 'https://simsms.org/priemnik.php?'
        else:
            raise Errors.UnsupportedBackendError
