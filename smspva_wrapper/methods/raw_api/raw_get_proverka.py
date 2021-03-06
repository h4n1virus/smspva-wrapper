from smspva_wrapper.caller import Caller
from .helpers import inconsistencies_hack, check_errors
from smspva_wrapper.errors import *


class RawGetProverka(Caller):
    def raw_get_proverka(self, service: str, number: str) -> dict:
        """Low level function for checking the numbers for multiple SMS
        In this method, number parameter specifies the number that you want to check.

        Note:
            Following the successful check of a number, send a request for getting the number - get_number ALSO with number parameter.\
             To check SMS send a request for SMS get_sms according to conditions

        Args:
            service (str): "opt4"
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

        q = f"metod=get_proverka&service={service}&id={number}"
        r = self.call(q)
        c = inconsistencies_hack(r)

        if check_errors(c) is True:
            return c
        else:
            e_msg = c['error_msg']
            if e_msg == 'Number shall consist of 10 digits!':
                raise ProverkaNumberForServiceError(c)
            elif e_msg == 'Such a number you did not order for the service':
                raise ProverkaNumberForServiceError(c)
            elif e_msg == 'The modem is busy, try to order in 5 minutes':
                raise ProverkaGSMBusyError(c)
            elif 'not_number' in c:
                if c['not_number'] == 'This number is no longer in the system':
                    raise ProverkaNumberError(c)
            else:
                raise UnknownAPIError(c)
