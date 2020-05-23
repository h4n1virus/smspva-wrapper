from typing import Union

from ..raw_api import RawGetCountNew
from smspva_wrapper.types import Services, Countries
from smspva_wrapper.ext.containers import CountNewContainer


class GetCountNew(RawGetCountNew):
    def get_count_new(
        self,
        service: Union[Services, str],
        country: Union[Countries, str],
    ) -> CountNewContainer:
        """Function to request for the amount of free activations for a certain service

        Args:
            service (Services or str): TELEGRAM or "opt59"
            country (Countries or str): KAZAKHSTAN or "KZ"

        Returns:
            CountNewContainer

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

        return CountNewContainer(
            self.raw_get_count_new(
                service=str(service),
                country=str(country)
            )
        )
