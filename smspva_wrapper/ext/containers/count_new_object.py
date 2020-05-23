from smspva_wrapper.types.countries import Countries, country_dict
from smspva_wrapper.types.services import Services, service_dict


class CountNewContainer:
    """Immutable high level container for get_count_new query"""

    def __init__(self, data: dict):
        self._data = data

    @property
    def data(self) -> dict:
        return self._data

    @property
    def online(self) -> int:
        return int(self._data.get('online'))

    @property
    def total(self) -> int:
        return int(self._data.get('total'))

    @property
    def for_total(self) -> int:
        return int(self._data.get('forTotal'))

    @property
    def country(self) -> Countries:
        return country_dict.get(self._data.get('country'))

    @property
    def service(self) -> Services:
        return service_dict.get(self._data.get('Service'))
