from smspva_wrapper.sync.caller import Caller
from .helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


class RawGetUserinfo(Caller):
    def raw_get_userinfo(self, api_base: str) -> dict:
        """Low level function to request user's balance and karma

        Args:
            api_base (str): "http://smspva.com/priemnik.php?apikey=DSWAFvdedrE4"

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
            UserInfoError
        """

        q = f"{api_base}&metod=get_userinfo"
        r = self.call(q)
        c = responce_hack(r)

        if check_errors(c) is True:
            return c
        elif c['response'] == 'error':
            raise Errors.UserInfoError(c['error_msg'], c)
        else:
            raise Errors.UnknownAPIError(c)
