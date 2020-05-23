from typing import Union

from ..raw_api import RawDenial
from smspva_wrapper.types import Services, Countries
from smspva_wrapper.ext.containers import DenialContainer


class Denial(RawDenial):
    def denial(
        self,
        service: Union[Services, str],
        country: Union[Countries, str],
        _id: str
    ) -> DenialContainer:
        """Function to cancel the order to number you got
        In this method id parameter is indicated from the response to request for phone number get_number

        Args:
            service (Services or str): TELEGRAM or "opt59"
            country (Countries or str): KAZAKHSTAN or "KZ"
            _id (str): "25623"

        Returns:
            DenialContainer

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
            DenialFailedError
        """

        return DenialContainer(
            self.raw_denial(
                service=str(service),
                country=str(country),
                _id=_id
            )
        )
