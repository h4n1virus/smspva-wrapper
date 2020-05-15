from smspva_wrapper.caller import caller
from smspva_wrapper.methods.helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


def redirect(api_base: str, service: str, _id: str, number_redirect: str) -> dict:
    """Low level function for number forwarding
    This method works only for avito+forwarding service.

    Note:
        Indicate the number for forwarding in the parameter number_redirect!

    Args:
        api_base (str): "http://smspva.com/priemnik.php?apikey=DSWAFvdedrE4"
        service (str): "opt59"
        _id (str): "25623"
        number_redirect (str): "9869788422"

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
        RedirectInvalidNumberFormat
        RedirectFailError
    """

    q = f"{api_base}&service={service}&id={_id}&number_redirect={number_redirect}"
    r = caller(q)
    c = responce_hack(r)

    if check_errors(c) is True:
        return c
    elif c['response'] == '2':
        raise Errors.RedirectInvalidNumberFormat(c['forwarding'], c)
    elif c['response'] == '3':
        raise Errors.RedirectFailError(c['forwarding'], c)
    else:
        raise Errors.UnknownAPIError(c)
