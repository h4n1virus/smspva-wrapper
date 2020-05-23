from ..raw_api import RawGetUserinfo
from smspva_wrapper.ext.containers import UserInfoContainer


class GetUserInfo(RawGetUserinfo):
    def get_userinfo(self) -> UserInfoContainer:
        """Function to request user's balance and karma

        Returns:
            UserInfoContainer

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

        return UserInfoContainer(
            self.raw_get_userinfo()
        )
