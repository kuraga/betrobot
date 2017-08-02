import datetime
import math
import time
import requests
import os
import json
from betrobot.util.common_util import recursive_sub


def get_week(target):
  jan4_week_start = datetime.date(target.year, 1, 4)
  while jan4_week_start.weekday() != 0:
    jan4_week_start = datetime.date.fromordinal(jan4_week_start.toordinal() - 1)
  day_diff = (target - jan4_week_start).days
  return 1 + math.floor(max(day_diff, 0) // 7)


def fix_dirtyjson(string):
  return recursive_sub(r',(\n*)(,|}|])', r',null\1\2', string)


def _get_headers():
    headers_file_path = os.path.join('tmp', 'update', 'whoscoredHeaders.json')
    if not os.path.exists(headers_file_path):
        return None

    with open(headers_file_path, 'rt') as headers_f:
        headers = json.load(headers_f)

    return headers


whoscored_s = requests.Session()


def whoscored_get(*args, delay=1.5, **kwargs):
  global whoscored_s

  headers = _get_headers()
  if headers is None:
    raise RuntimeError('update headers!')
  whoscored_s.headers = headers

  for i in range(3):
    time.sleep(delay)

    try:
      response = whoscored_s.get(*args, timeout=30, **kwargs)
    except Exception as e:
      print('Internet error: ', e)
      continue

    if response.status_code not in (200, 403):
      print('Bad response, code: %d' % (response.status_code,))
      continue

    if ('The page you requested does not exist' in response.text or 'Request unsuccessful. Incapsula incident ID:' in response.text or """<META NAME="robots" CONTENT="noindex,nofollow">""" in response.text or """<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">""" in response.text or '403 - Forbidden: Access is denied.' in response.text) or response.status_code == 403:
      raise RuntimeError('update headers!')

    break

  if response.status_code == 200:
    return response
  else:
    return None
