from smspva_wrapper.types.countries import Countries, country_dict
from smspva_wrapper.types.services import Services, service_dict


class ServicePriceContainer:
    """Immutable high level container for get_service_price"""

    def __init__(self, data: dict):
        self._data = data

    @property
    def data(self) -> dict:
        return self._data

    @property
    def response(self) -> int:
        return int(self._data.get('response'))

    @property
    def country(self) -> Countries:
        return country_dict.get(self._data.get('country'))

    @property
    def service(self) -> Services:
        return service_dict.get(self._data.get('service'))

    @property
    def price(self) -> float:
        return float(self._data.get('price'))
