import datetime
import math
import time
import requests
import re
from betrobot.util.common_util import input_multiline


def get_week(target):
  jan4_week_start = datetime.date(target.year, 1, 4)
  while jan4_week_start.weekday() != 0:
    jan4_week_start = datetime.date.fromordinal(jan4_week_start.toordinal() - 1)
  day_diff = (target - jan4_week_start).days
  return 1 + math.floor(max(day_diff, 0) // 7)


whoscored_s = requests.Session()
whoscored_s.headers.update({
  'Host': 'www.whoscored.com'
})
whoscored_s.proxies.update({
  'http': 'socks5://127.0.0.1:9050',
  'https': 'socks5://127.0.0.1:9050'
})


def whoscored_get(*args, **kwargs):
  global whoscored_s

  while True:
    try:
      # TODO: Когда загружается HTML-страница, то пауза не нужна
      time.sleep(1.5)
      response = whoscored_s.get(*args, timeout=30, **kwargs)
    except Exception:
      print('Internet error!')
      continue

    if response.status_code not in (200, 403):
      raise ValueError('Bad response! Code: %d' % (response.status_code,))

    if not (('The page you requested does not exist' in response.text or 'Request unsuccessful. Incapsula incident ID:' in response.text or """<META NAME="robots" CONTENT="noindex,nofollow">""" in response.text or """<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">""" in response.text or '403 - Forbidden: Access is denied.' in response.text) or response.status_code == 403):
      return response

    # TODO: Автоматизировать получение заголовков
    print('Update headers!')
    for line in input_multiline():
      if line.strip() == '':
        continue
      (header, colon, value) = line.partition(':')
      whoscored_s.headers[header.strip()] = value.strip()
    print('')


def recursive_sub(pattern, repl, string, *args, **kwargs):
    n = 1
    while n > 0:
      (string, n) = re.subn(pattern, repl, string, *args, **kwargs)
    return string


def fix_dirtyjson(string):
  return recursive_sub(r',(\n*)(,|}|])', r',null\1\2', string)
