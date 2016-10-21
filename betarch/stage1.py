import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betarch')

import datetime
import os
from util import betarch_get


today_date = datetime.date.today()
out_dir_path = os.path.join('data', 'betarch', 'betcityDatesHtml')
os.makedirs(out_dir_path, exist_ok=True)

current_date = datetime.date(2014, 1, 1)
while current_date != today_date:
  url = 'http://betarch.ru/index.php?date=b%s' % (current_date.strftime('%Y-%m-%d'),)
  print(url)
  date_html = betarch_get(url).text

  if date_html == 'File not exists':
    current_date += datetime.timedelta(1)
    continue

  out_file_path = os.path.join(out_dir_path, '%s.html' % (current_date.strftime('%Y-%m-%d'),))
  with open(out_file_path, 'w', encoding='utf-8') as f_out:
    f_out.write(date_html)

  current_date += datetime.timedelta(1)
