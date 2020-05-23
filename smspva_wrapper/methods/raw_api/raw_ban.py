from smspva_wrapper.caller import Caller
from .helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


class RawBan(Caller):
    def raw_ban(self, service: str, _id: str) -> dict:
        """Low level function to report to the server that the number is already used
        In this method id parameter is indicated from the response to request for phone number get_number

        Args:
            service (str): "opt4"
            _id (str): "25623"

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
            BanFailedError
        """

        q = f"metod=ban&service={service}&id={_id}"
        r = self.call(q)
        c = responce_hack(r)

        if check_errors(c) is True:
            return c
        elif c['response'] == '2':
            raise Errors.BanError(c)
        else:
            raise Errors.UnknownAPIError(c)
