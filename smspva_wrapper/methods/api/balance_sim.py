from typing import Union

from ..raw_api import RawBalanceSim
from smspva_wrapper.types import Services
from smspva_wrapper.ext.containers import BalanceSIMContainer


class BalanceSim(RawBalanceSim):
    def balance_sim(
        self,
        service: Union[Services, str],
        _id: str
    ) -> BalanceSIMContainer:
        """Function to receive SIM card balance for avito+forwarding service

        Args:
            service (obj::Services or str): TELEGRAM or "opt59"
            _id (str): "25623"

        Returns:
            BalanceSIMContainer

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

        return BalanceSIMContainer(
            self.raw_balance_sim(
                service=str(service),
                _id=_id
            )
        )
