from smspva_wrapper.caller import caller
from smspva_wrapper.methods.helpers import responce_hack, check_errors
from smspva_wrapper.errors import Errors


def balance_sim(api_base: str, service: str, _id: str) -> dict:
    """Low level function to receive SIM card balance for avito+forwarding service.

    Args:
        api_base (str): "http://smspva.com/priemnik.php?apikey=DSWAFvdedrE4"
        service (str): "opt59"
        _id (str): "25623"

    Returns:
        dict: provides an API call dictionary

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
        BalanceSIMError
    """

    q = f"{api_base}&metod=balance_sim&service={service}&id={_id}"
    r = caller(q)
    c = responce_hack(r)

    if check_errors(c) is True:
        return c
    elif c['response'] == '2':
        raise Errors.BalanceSIMError(c['amount'], c)
    else:
        raise Errors.UnknownAPIError(c)
