from smspva_wrapper.sync.caller import Caller
from .helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


class RawGetNumber(Caller):
    def raw_get_number(self, api_base: str, service: str, country: str) -> dict:
        """Low level function to receive a phone number for a certain service.

        Args:
            api_base (str): "http://smspva.com/priemnik.php?apikey=DSWAFvdedrE4"
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

        q = f"{api_base}&metod=get_number&service={service}&country={country}"
        r = self.call(q)
        c = responce_hack(r)

        if check_errors(c) is True:
            return c
        elif c['response'] == '2':
            raise Errors.NumberAlreadyTakenError(c)
        else:
            raise Errors.UnknownAPIError(c)
