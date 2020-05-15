def responce_hack(d: dict) -> dict:
    """Shitty hack to fix inconsistencies in API responses

    Args:
        d (dict): takes in dictionary from API call

    Returns:
        d (dict):  returns fixed dictionary
    """
    if 'responce' in d:
        d['response'] = d.pop('responce')

    return d
