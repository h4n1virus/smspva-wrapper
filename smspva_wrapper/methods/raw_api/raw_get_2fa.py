from smspva_wrapper.caller import Caller
from .helpers import responce_hack, check_errors
from smspva_wrapper.errors import *


class RawGet2FA(Caller):
    def raw_get_2fa(self, secret: str) -> dict:
        """Low level function for obtaining 2FA authorization code from Google, Microsoft, etc. by secret key

        Args:
            secret (str): "1234567890"

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

        q = f"metod=get_2fa&secret={secret}"
        r = self.call(q)
        c = responce_hack(r)

        if check_errors(c) is True:
            return c
        else:
            raise UnknownAPIError(c)
