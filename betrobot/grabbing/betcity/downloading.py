from betrobot.util.requests_util import requests_get


def betcity_get(*args, **kwargs):
    response = requests_get('betsbc.com', *args, **kwargs)
    if response is None:
        return None

    return response.text
