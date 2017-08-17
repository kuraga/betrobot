import os
import re
import json
from betrobot.util.requests_util import requests_get, requests_clear_session


def _check_antispam(response):
    return response.status_code == 403 or ( \
      'The page you requested does not exist' in response.text or \
      'Request unsuccessful. Incapsula incident ID:' in response.text or \
      '<META NAME="robots" CONTENT="noindex,nofollow">' in response.text or \
      '<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">' in response.text or \
      '403 - Forbidden: Access is denied.' in response.text \
      )


def _try_to_update_headers():
    url = 'https://www.whoscored.com/Regions/252/Tournaments/2/England-Premier-League'

    model_last_mode_page_file_path = os.path.join('tmp', 'update', 'whoscoredPage.html')
    if os.path.exists(model_last_mode_page_file_path):
        with open(model_last_mode_page_file_path, 'rt', encoding='utf-8') as f:
            text = f.read()
    else:
        response = requests_get('www.whoscored.com', url)
        if response.status_code != 200:
            return False
        text = response.text

    m = re.search(r"'Model-last-Mode': '(.+?)'", text)
    if m is None:
        return False
    model_last_mode = m.group(1)
    print('Model-Last-Mode: %s' % (model_last_mode,))

    headers_file_path = os.path.join('tmp', 'update', 'headers', 'www.whoscored.com.json')
    with open(headers_file_path, 'rt') as headers_f:
        headers = json.load(headers_f)
    headers['model-last-mode'] = model_last_mode
    headers['referer'] = url
    headers['x-requested-with'] = 'XMLHttpRequest'

    with open(headers_file_path, 'wt') as headers_f:
        json.dump(headers, headers_f)
    requests_clear_session('www.whoscored.com')

    response = requests_get('www.whoscored.com', url)
    if response.status_code != 200:
        return False

    return not _check_antispam(response)


def whoscored_get(*args, **kwargs):
    response = requests_get('www.whoscored.com', *args, **kwargs)
    if response is None:
        return None

    if _check_antispam(response):
        print('Updating headers...')

        t = _try_to_update_headers()
        if not t:
            raise RuntimeError("Can't update headers for Whoscored!")

        response = requests_get('www.whoscored.com', *args, **kwargs)
        if response is None:
            return None

        if _check_antispam(response):
            raise RuntimeError("Can't update headers for Whoscored!")

    return response.text
