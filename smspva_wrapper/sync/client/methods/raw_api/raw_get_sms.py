from smspva_wrapper.sync.caller import Caller
from .helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


class RawGetSMS(Caller):
    def raw_get_sms(self, api_base: str, service: str, country: str, _id: str, sms: bool = False) -> dict:
        """Low level function for receiving a SMS for a certain service
        In this method id parameter is indicated from the response to request for phone number get_number

        Note:
            If you get the response that a code from SMS hasn't been found yet, send request get_sms once again 20 seconds later.\
             Note, the server searches for SMS for 10 minutes. You need to send your request within 10 minutes each 20 seconds per one request.\
              That said, you receive a code from SMS or error message.
            If you want to get re-SMS without closing the order (Code Refinement), then set sms parameter to True \
               In this case, your order can not be closed and you may receive a re-SMS. Re-chargeable SMS. The cost is the cost of an ordinary SMS for this service.

        Args:
            api_base (str): "http://smspva.com/priemnik.php?apikey=DSWAFvdedrE4"
            service (str): "opt4"
            country (str): "ru"
            _id (str): "25623"
            sms (bool): False

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
            GetSMSError
        """

        q = f"{api_base}&metod=get_sms&service={service}&country={country}&id={_id}"
        if sms:
            q = f"{q}&sms=sms"

        r = self.call(q)
        c = responce_hack(r)

        if check_errors(c) is True:
            return c
        elif c['response'] == '2':
            return c
        elif c['response'] == '3':
            raise Errors.GetSMSError(c)
        else:
            raise Errors.UnknownAPIError(c)
