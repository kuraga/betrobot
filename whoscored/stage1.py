import sys
sys.path.append('./')
sys.path.append('./util')

import datetime
import os
import dirtyjson
import json
from util import whoscored_get, fix_dirtyjson


out_dir_path = os.path.join('data', 'whoscored', 'datesJson')
os.makedirs(out_dir_path, exist_ok=True)

current_date = datetime.date.today()
while current_date.year >= 2016 and current_date.month >= 9 and current_date.day >= 21:
  url = 'https://www.whoscored.com/matchesfeed/?d=%s' % (current_date.strftime('%Y%m%d'),)
  print(url)

  date_broken_dirtyjson = whoscored_get(url).text
  date_dirtyjson = fix_dirtyjson(date_broken_dirtyjson)
  date_json = dirtyjson.loads(date_dirtyjson)

  out_file_path = os.path.join(out_dir_path, '%s.json' % (current_date.strftime('%Y-%m-%d'),))
  with open(out_file_path, 'w', encoding='utf-8') as f_out:
    json.dump(date_json, f_out, ensure_ascii=False)

  current_date -= datetime.timedelta(1)
