from typing import Union

from ..raw_api import RawRedirect
from smspva_wrapper.ext.containers import RedirectContainer
from smspva_wrapper.types import Services


class Redirect(RawRedirect):
    def redirect(
        self,
        service: Union[Services, str],
        _id: str,
        number_redirect: str
    ) -> RedirectContainer:
        """Function for number forwarding
        This method works only for avito+forwarding service.

        Note:
            Indicate the number for forwarding in the parameter number_redirect!

        Args:
            service (Services or str): TELEGRAM or "opt59"
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

        return RedirectContainer(
            self.raw_redirect(
                service=str(service),
                _id=_id,
                number_redirect=number_redirect
            )
        )
