from smspva_wrapper.caller import Caller
from .helpers import responce_hack, check_errors
from smspva_wrapper.errors import *


class RawRedirect(Caller):
    def raw_redirect(self, service: str, _id: str, number_redirect: str) -> dict:
        """Low level function for number forwarding
        This method works only for avito+forwarding service.

        Note:
            Indicate the number for forwarding in the parameter number_redirect!

        Args:
            service (str): "opt59"
            _id (str): "25623"
            number_redirect (str): "9869788422"

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
            RedirectInvalidNumberFormat
            RedirectFailError
        """

        q = f"metod=redirect&service={service}&id={_id}&number_redirect={number_redirect}"
        r = self.call(q)
        c = responce_hack(r)

        if check_errors(c) is True:
            return c
        elif c['response'] == '2':
            raise RedirectInvalidNumberFormat(c['forwarding'], c)
        elif c['response'] == '3':
            raise RedirectFailError(c['forwarding'], c)
        else:
            raise UnknownAPIError(c)
