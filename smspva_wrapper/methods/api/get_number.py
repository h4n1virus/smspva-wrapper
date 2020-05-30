from typing import Union

from ..raw_api import RawGetNumber
from smspva_wrapper.types import Services, Countries
from smspva_wrapper.ext.containers import NumberContainer


class GetNumber(RawGetNumber):
    def get_number(
        self,
        service: Union[Services, str],
        country: Union[Countries, str],
    ) -> NumberContainer:
        """Function to receive a phone number for a certain service.

        Args:
            service (Services or str): TELEGRAM or "opt59"
            country (Countries or str): KAZAKHSTAN or "KZ"

        Returns:
            NumberContainer

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
            NumberAlreadyTakenError
        """

        return NumberContainer(
            self.raw_get_number(
                service=str(service),
                country=str(country)
            ),
            country=str(country),
            service=str(service)
        )
