from smspva_wrapper.caller import Caller
from .helpers import responce_hack, check_errors
from smspva_wrapper.errors import *


class RawGetCountNew(Caller):
    def raw_get_count_new(self, service: str, country: str) -> dict:
        """Low level function to request for the amount of free activations for a certain service

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
        """

        q = f"metod=get_count_new&service={service}&country={country}"
        r = self.call(q)
        c = responce_hack(r)

        if check_errors(c) is True:
            return c
        elif c.get('Service') == service:
            return c
        elif c.get('service') == service:
            return c
        else:
            raise UnknownAPIError(c)
