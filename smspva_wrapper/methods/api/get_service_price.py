from typing import Union

from ..raw_api import RawGetServicePrice
from smspva_wrapper.types import Services, Countries
from smspva_wrapper.ext.containers import ServicePriceContainer


class GetServicePrice(RawGetServicePrice):
    def get_service_price(
        self,
        service: Union[Services, str],
        country: Union[Countries, str],
    ) -> ServicePriceContainer:
        """Function to request current price sms for country and service

        Args:
            service (Services or str): TELEGRAM or "opt59"
            country (Countries or str): KAZAKHSTAN or "KZ"

        Returns:
            ServicePriceContainer

        Raises:
            InvalidAPIKeyError
            InsufficientFundsError
            TooShortIntervalError
            RepeatRequestLaterError
            RequestSyntaxError
            UnknownAPIError
            NetworkingError
            MaxRequestsPerMinuteError
            NegativeKarmaError
            MaxConcurrentStreamsError
        """

        return ServicePriceContainer(
            self.raw_get_service_price(
                service=str(service),
                country=str(country)
            )
        )
