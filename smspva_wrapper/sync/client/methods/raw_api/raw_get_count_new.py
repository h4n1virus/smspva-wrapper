from smspva_wrapper.sync.caller import Caller
from .helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


class RawGetCountNew(Caller):
    def raw_get_count_new(self, api_base: str, service: str, country: str) -> dict:
        """Low level function to request for the amount of free activations for a certain service

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
        """

        q = f"{api_base}&metod=get_count_new&service={service}&country={country}"
        r = self.call(q)
        c = responce_hack(r)

        if check_errors(c) is True:
            return c
        else:
            raise Errors.UnknownAPIError(c)
