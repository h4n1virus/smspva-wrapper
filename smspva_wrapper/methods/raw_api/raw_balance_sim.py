from smspva_wrapper.caller import Caller
from .helpers import inconsistencies_hack, check_errors
from smspva_wrapper.errors import *


class RawBalanceSim(Caller):
    def raw_balance_sim(self, service: str, _id: str) -> dict:
        """Low level function to receive SIM card balance for avito+forwarding service.

        Args:
            service (str): "opt59"
            _id (str): "25623"

        Returns:
            dict: provides an API call dictionary

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
            BalanceSIMError
        """

        q = f"metod=balance_sim&service={service}&id={_id}"
        r = self.call(q)
        c = inconsistencies_hack(r)

        if check_errors(c) is True:
            return c
        elif c['response'] == '2':
            raise BalanceSIMError(c['amount'], c)
        else:
            raise UnknownAPIError(c)
