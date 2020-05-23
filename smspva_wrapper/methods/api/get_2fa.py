from ..raw_api import RawGet2FA
from smspva_wrapper.ext.containers import TwoFAContainer


class Get2FA(RawGet2FA):
    def get_2fa(self, secret: str):
        """Function for obtaining 2FA authorization code from Google, Microsoft, etc. by secret key

        Args:
            secret (str): "1234567890"

        Returns:
            TwoFAContainer

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
        """

        return TwoFAContainer(
            self.raw_get_2fa(
                secret=secret
            )
        )
