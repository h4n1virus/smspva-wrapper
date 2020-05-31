from smspva_wrapper.caller import Caller
from .helpers import inconsistencies_hack, check_errors
from smspva_wrapper.errors import *


class RawDenial(Caller):
    def raw_denial(self, service: str, country: str, _id: str) -> dict:
        """Low level function to cancel the order to number you got
        In this method id parameter is indicated from the response to request for phone number get_number

        Args:
            service (str): "opt4"
            country (str): "ru"
            _id (str): "25623"

        Returns:
            dict: API call dictionary

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

        q = f"metod=denial&service={service}&country={country}&id={_id}"
        r = self.call(q)
        c = inconsistencies_hack(r)

        if check_errors(c) is True:
            return c
        elif c['response'] == '2':
            raise DenialFailedError(c)
        else:
            raise UnknownAPIError(c)
