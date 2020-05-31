from smspva_wrapper.caller import Caller
from .helpers import inconsistencies_hack, check_errors
from smspva_wrapper.errors import *


class RawGetUserinfo(Caller):
    def raw_get_userinfo(self) -> dict:
        """Low level function to request user's balance and karma

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

        q = f"metod=get_userinfo"
        r = self.call(q)
        c = inconsistencies_hack(r)

        if check_errors(c) is True:
            return c
        elif c['response'] == 'error':
            raise UserInfoError(c['error_msg'], c)
        else:
            raise UnknownAPIError(c)
