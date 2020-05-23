from smspva_wrapper.sync.caller import Caller
from .helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


class RawGetProverka(Caller):
    def raw_get_proverka(self, api_base: str, service: str, number: str) -> dict:
        """Low level function for checking the numbers for multiple SMS
        In this method, number parameter specifies the number that you want to check.

        Note:
            Following the successful check of a number, send a request for getting the number - get_number ALSO with number parameter.\
             To check SMS send a request for SMS get_sms according to conditions


        Args:
            api_base (str): "http://smspva.com/priemnik.php?apikey=DSWAFvdedrE4"
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

        q = f"{api_base}&metod=get_proverka&service={service}&id={number}"
        r = self.call(q)
        c = responce_hack(r)

        if check_errors(c) is True:
            return c
        else:
            e_msg = c['error_msg']
            if e_msg == 'Number shall consist of 10 digits!':
                raise Errors.ProverkaNumberForServiceError(c)
            elif e_msg == 'Such a number you did not order for the service':
                raise Errors.ProverkaNumberForServiceError(c)
            elif e_msg == 'The modem is busy, try to order in 5 minutes':
                raise Errors.ProverkaGSMBusyError(c)
            elif 'not_number' in c:
                if c['not_number'] == 'This number is no longer in the system':
                    raise Errors.ProverkaNumberError(c)
            else:
                raise Errors.UnknownAPIError(c)
