from smspva_wrapper.caller import caller
from smspva_wrapper.methods.helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


def get_balance(api_base: str) -> dict:
    """Low level function that returns balance of the account

    Args:
        api_base (str): "http://smspva.com/priemnik.php?apikey=DSWAFvdedrE4"

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
        UserInfoError
    """

    q = f"{api_base}&metod=get_balance"
    r = caller(q)
    c = responce_hack(r)

    if check_errors(c) is True:
        return c
    elif c['response'] == 'error':
        raise Errors.UserInfoError(c['error_msg'], c)
    else:
        raise Errors.UnknownAPIError(c)
