from typing import Union

from ..raw_api import RawGetSMS
from smspva_wrapper.types import Services, Countries
from smspva_wrapper.ext.containers import SMSContainer


class GetSMS(RawGetSMS):
    def get_sms(
        self,
        service: Union[Services, str],
        country: Union[Countries, str],
        _id: str,
        sms: bool = False
    ) -> SMSContainer:
        """Function for receiving a SMS for a certain service
        In this method id parameter is indicated from the response to request for phone number get_number

        Note:
            If you get the response that a code from SMS hasn't been found yet, send request get_sms once again 20 seconds later.\
             Note, the server searches for SMS for 10 minutes. You need to send your request within 10 minutes each 20 seconds per one request.\
              That said, you receive a code from SMS or error message.
            If you want to get re-SMS without closing the order (Code Refinement), then set sms parameter to True \
               In this case, your order can not be closed and you may receive a re-SMS. Re-chargeable SMS. The cost is the cost of an ordinary SMS for this service.

        Args:
            service (Services or str): TELEGRAM or "opt59"
            country (Countries or str): KAZAKHSTAN or "KZ"
            _id (str): "25623"
            sms (bool): False

        Returns:
            SMSContainer

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
            GetSMSError
        """

        return SMSContainer(
            self.raw_get_sms(
                service=str(service),
                country=str(country),
                _id=_id,
                sms=sms
            )
        )
