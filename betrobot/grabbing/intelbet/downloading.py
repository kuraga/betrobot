import datetime
import math
import time
import requests
import os
import json
from betrobot.util.common_util import recursive_sub


def _get_headers():
    headers_file_path = os.path.join('tmp', 'update', 'intelbetHeaders.json')
    if not os.path.exists(headers_file_path):
        return None

    with open(headers_file_path, 'rt') as headers_f:
        headers = json.load(headers_f)

    return headers


intelbet_s = requests.Session()


def intelbet_get(*args, delay=1.5, **kwargs):
  global intelbet_s

  for i in range(3):
    time.sleep(delay)

    try:
      response = intelbet_s.get(*args, timeout=30, **kwargs)
    except Exception as e:
      print('Internet error: ', e)
      continue

    if response.status_code not in (200, 403):
      print('Bad response, code: %d' % (response.status_code,))
      continue

    break

  if response.status_code == 200:
    return response
  else:
    return None
