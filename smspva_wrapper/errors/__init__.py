class Errors:
    from .errors import GeneralError
    from .errors import NetworkingError
    from .errors import APIError
    from .errors import UnknownAPIError
    from .errors import MaxRequestsPerMinuteError
    from .errors import NegativeKarmaError
    from .errors import MaxConcurrentStreamsError
    from .errors import InvalidAPIKeyError
    from .errors import InsufficientFundsError
    from .errors import TooShortIntervalError
    from .errors import RepeatRequestLaterError
    from .errors import RequestSyntaxError
    from .errors import UserInfoError
    from .errors import NumberAlreadyTakenError
    from .errors import BanError
    from .errors import GetSMSError
    from .errors import DenialFailedError
    from .errors import ClearSMSError
    from .errors import BalanceSIMError
    from .errors import ProverkaNumberForServiceError
    from .errors import ProverkaGSMBusyError
    from .errors import ProverkaNumberError
    from .errors import RedirectFailError
    from .errors import RedirectInvalidNumberFormat
