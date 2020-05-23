from smspva_wrapper.caller import Caller
from .helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


class RawGetBalance(Caller):
    def raw_get_balance(self) -> dict:
        """Low level function that returns balance of the account

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

        q = f"metod=get_balance"
        r = self.call(q)
        c = responce_hack(r)

        if check_errors(c) is True:
            return c
        elif c['response'] == 'error':
            raise Errors.UserInfoError(c['error_msg'], c)
        else:
            raise Errors.UnknownAPIError(c)
