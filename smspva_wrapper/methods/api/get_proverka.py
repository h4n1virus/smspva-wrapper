from typing import Union

from ..raw_api import RawGetProverka
from smspva_wrapper.types import Services
from smspva_wrapper.ext.containers import ProverkaContainer


class GetProverka(RawGetProverka):
    def get_proverka(
        self,
        service: Union[Services, str],
        number: str
    ) -> ProverkaContainer:
        """Low level function for checking the numbers for multiple SMS
        In this method, number parameter specifies the number that you want to check.

        Note:
            Following the successful check of a number, send a request for getting the number - get_number ALSO with number parameter.\
             To check SMS send a request for SMS get_sms according to conditions

        Args:
            service (Services or str): TELEGRAM or "opt59"
            number (str): "9685156912"

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
            ProverkaGSMModuleBusyError
            ProverkaNoOrderForNumberForServiceError
            ProverkaNoSuchNumberError
        """

        return ProverkaContainer(
            self.raw_get_proverka(
                service=str(service),
                number=number
            )
        )
