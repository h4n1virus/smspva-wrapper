from ..raw_api import RawGetBalance
from smspva_wrapper.ext.containers import BalanceContainer


class GetBalance(RawGetBalance):
    def get_balance(self) -> BalanceContainer:
        """Function that returns balance of the account

        Returns:
            BalanceContainer

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

        return BalanceContainer(
            self.raw_get_balance()
        )
