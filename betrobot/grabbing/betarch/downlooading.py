import requests
from betrobot.util.common_util import input_multiline


betarch_s = requests.Session()
betarch_s.headers.update({
  'Host': 'betarch.ru'
})


def betarch_get(*args, **kwargs):
  global betarch_s

  while True:
    try:
      response = betarch_s.get(*args, timeout=30, **kwargs)
    except Exception:
      print('Internet error!')
      continue

    if response.status_code not in (200, 403):
      print('Bad response! Code: %d' %(response.status_code,))
      continue

    if not ('You can use this only from our website' in response.text):
      return response

    print('Update headers!')
    for line in input_multiline():
      if line.strip() == '':
        continue
      (header, colon, value) = line.partition(':')
      betarch_s.headers[header.strip()] = value.strip()
    print('')
