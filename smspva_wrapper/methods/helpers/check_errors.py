from smspva_wrapper.errors import Errors


def check_errors(d: dict) -> bool:
    """Checks for error codes in dict

    Args:
        d(dict): Takes in dictionary from API

    Returns:
        bool: True if no errors were found. False otherwise

    Raises:
        UnknownAPIError
        MaxRequestsPerMinuteError
        NegativeKarmaError
        MaxConcurrentStreamsError
    """

    response_code = d.get('response', '')
    if response_code == '1':
        return True
    if response_code == '2':
        return False
    elif response_code == '3':
        return False
    elif response_code == '4':
        raise Errors.UnknownAPIError(d)
    elif response_code == '5':
        raise Errors.MaxRequestsPerMinuteError(d)
    elif response_code == '6':
        raise Errors.NegativeKarmaError(d)
    elif response_code == '7':
        raise Errors.MaxConcurrentStreamsError(d)
    elif response_code == 'error':
        return False
    elif response_code == 'modem_busy':
        return False
    else:
        return False
