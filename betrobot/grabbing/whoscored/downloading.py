from betrobot.util.requests_util import requests_get


def whoscored_get(*args, **kwargs):
    response = requests_get('www.whoscored.com', *args, **kwargs)
    if response is None:
        return None

    if response.status_code == 403 or ( \
      'The page you requested does not exist' in response.text or \
      'Request unsuccessful. Incapsula incident ID:' in response.text or \
      '<META NAME="robots" CONTENT="noindex,nofollow">' in response.text or \
      '<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">' in response.text or \
      '403 - Forbidden: Access is denied.' in response.text \
      ) :
        raise RuntimeError('update headers!')

    return response.text
