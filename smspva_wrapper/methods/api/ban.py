from typing import Union

from ..raw_api import RawBan
from smspva_wrapper.types import Services
from smspva_wrapper.ext.containers import BanContainer


class Ban(RawBan):
    def ban(
        self,
        service: Union[Services, str],
        _id: str
    ) -> BanContainer:
        """Function to report to the server that the number is already used
        In this method id parameter is indicated from the response to request for phone number get_number

        Args:
            service (obj::Services or str): TELEGRAM or "opt59"
            _id (str): "25623"

        Returns:
            BanContainer

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
            BanFailedError
        """

        return BanContainer(
            self.raw_ban(
                service=str(service),
                _id=_id
            )
        )
