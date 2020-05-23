from smspva_wrapper.caller import Caller
from .helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


class RawGetServicePrice(Caller):
    def raw_get_service_price(self, service: str, country: str) -> dict:
        """Low level function to request current price sms for country and service

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

        q = f"metod=get_service_price&service={service}&country={country}"
        r = self.call(q)
        c = responce_hack(r)

        if check_errors(c) is True:
            return c
        else:
            raise Errors.UnknownAPIError(c)
