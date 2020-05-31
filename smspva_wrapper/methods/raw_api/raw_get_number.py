from smspva_wrapper.caller import Caller
from .helpers import inconsistencies_hack, check_errors
from smspva_wrapper.errors import *


class RawGetNumber(Caller):
    def raw_get_number(self, service: str, country: str) -> dict:
        """Low level function to receive a phone number for a certain service.

        Args:
            service (str): "opt4"
            country (str): "ru"

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
            NumberAlreadyTakenError
        """

        q = f"metod=get_number&service={service}&country={country}"
        r = self.call(q)
        c = inconsistencies_hack(r)

        if check_errors(c) is True:
            return c
        elif c['response'] == '2':
            raise NumberAlreadyTakenError(c)
        else:
            raise UnknownAPIError(c)
