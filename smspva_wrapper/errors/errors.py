class GeneralError(Exception):
    """Base class for exceptions in this module."""


class UnrecognizableBackEndError(GeneralError):
    """Unrecognizable backend"""


class NetworkingError(GeneralError):
    """Networking Error"""


# API errors
class APIError(GeneralError):
    """Base class for API error"""


class UnknownAPIError(APIError):
    """Unknown API error"""


# Return code errors
class MaxRequestsPerMinuteError(APIError):
    """You have exceeded the number of requests per minute"""


class NegativeKarmaError(APIError):
    """You will be banned for 10 minutes, because scored negative karma"""


class MaxConcurrentStreamsError(APIError):
    """You have exceeded the number of concurrent streams. SMS Wait from previous orders"""


class InvalidAPIKeyError(APIError):
    """Invalid API KEY has been entered"""


class InsufficientFundsError(APIError):
    """Insufficient funds"""


class TooShortIntervalError(APIError):
    """Set a longer interval between calls to API server"""


class RepeatRequestLaterError(APIError):
    """Try to repeat your request later."""


class RequestSyntaxError(APIError):
    """Check the request syntax and the list of parameters used (can be found on the page with method description)."""


# Method errors
# get_balance, get_userinfo
class UserInfoError(APIError):
    """Not ID or user balance"""


# get_number
class NumberAlreadyTakenError(APIError):
    """Number is already taken"""


# ban
class BanError(APIError):
    """RawBan request has failed"""


# get_sms
class GetSMSError(APIError):
    """No such SMS or invalid request ID or SMS waiting time has expired (no more than 10 minutes)"""


# denial
class DenialFailedError(APIError):
    """RawDenial request has failed"""


# clearsms
class ClearSMSError(APIError):
    """ClearSMS error"""


# balance_sim
class BalanceSIMError(APIError):
    """SIM card balance info hasn't been received"""


# get_proverka errors
class ProverkaNumberForServiceError(APIError):
    """You didn't order a number for this service"""


class ProverkaGSMBusyError(APIError):
    """GSM module is busy try to repeat your request 5 minutes later"""


class ProverkaNumberError(APIError):
    """There's no such number in the system any longer"""


# redirect errors
class RedirectFailError(APIError):
    """Redirecting failed"""


class RedirectInvalidNumberFormat(APIError):
    """Invalid number format for redirecting"""
