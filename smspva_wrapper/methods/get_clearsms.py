from smspva_wrapper.caller import caller
from smspva_wrapper.methods.helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


def get_clearsms(api_base: str, service: str, _id: str) -> dict:
    """SIMSMS ONLY! Low level function to check the number to receive several SMS consecutively within one order
    In this method, the parameter id indicates the order number within which you need to receive another text.

    Args:
        api_base (str): "http://simsms.org/priemnik.php?apikey=DSWAFvdedrE4"
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
        ClearSMSError
    """

    q = f"{api_base}&metod=get_clearsms&service={service}&id={_id}"
    r = caller(q)
    c = responce_hack(r)

    if check_errors(c) is True:
        return c
    elif c['response'] == '2':
        raise Errors.ClearSMSError(c)
    else:
        raise Errors.UnknownAPIError(c)
