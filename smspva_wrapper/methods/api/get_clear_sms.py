from typing import Union

from ..raw_api import RawGetClearSMS
from smspva_wrapper.types import Services
from smspva_wrapper.ext.containers import ClearSMSContainer


class GetClearSMS(RawGetClearSMS):
    def get_clear_sms(
        self,
        service: Union[Services, str],
        _id: str
    ) -> ClearSMSContainer:
        """SIMSMS ONLY! Function to check the number to receive several SMS consecutively within one order
        In this method, the parameter id indicates the order number within which you need to receive another text.

        Args:
            service (Services or str): TELEGRAM or "opt59"
            _id (str): "25623"

        Returns:
            ClearSMSContainer

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
            ClearSMSError
        """

        return ClearSMSContainer(
            self.raw_get_clearsms(
                service=str(service),
                _id=_id
            )
        )
