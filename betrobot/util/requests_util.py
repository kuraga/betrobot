import time
import requests
import os
import json


def _get_headers(domain):
    headers_file_path = os.path.join('tmp', 'update', 'headers', '%s.json' % (domain,))
    if not os.path.exists(headers_file_path):
        return None

    with open(headers_file_path, 'rt') as headers_f:
        headers = json.load(headers_f)

    return headers


_sessions = {}


def _get_session(domain):
    if domain not in _sessions:
        _sessions[domain] = requests.Session()
        headers = _get_headers(domain)
        if headers is not None:
            _sessions[domain].headers = headers

    return _sessions[domain]


def requests_clear_session(domain):
    del _sessions[domain]


def requests_get(domain, *args, delay=1.5, **kwargs):
    session = _get_session(domain)

    for i in range(3):
        time.sleep(delay)

        try:
            response = session.get(*args, timeout=30, **kwargs)
        except Exception as e:
            print('Internet error: ', e)
            continue

        if response.status_code not in (200, 403):
            print('Bad response, code: %d' % (response.status_code,))

            if response.status_code == 404:
                return None
            else:
                continue

        break

    return response
