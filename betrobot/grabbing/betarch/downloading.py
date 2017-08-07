from betrobot.util.requests_util import requests_get


def betarch_get(*args, **kwargs):
    response = requests_get('betarch.ru', *args, **kwargs)
    if response is None:
        return None

    if 'You can use this only from our website' in response.text:
        raise RuntimeError('update headers!')

    return response.text
