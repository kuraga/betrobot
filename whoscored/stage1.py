import sys
sys.path.append('./')
sys.path.append('./util')

import datetime
import os
import dirtyjson
import json
from util import whoscored_get, fix_dirtyjson


last_file_path = os.path.join('data', 'whoscored', 'last.txt')
queue_file_path = os.path.join('data', 'whoscored', 'queue.txt')

with open(last_file_path, 'r', encoding='utf-8') as f_last:
  last_date_str = f_last.read()
last_date = datetime.datetime.strptime(last_date_str, '%Y-%m-%d')
today = datetime.datetime.today()

out_dir_path = os.path.join('data', 'whoscored', 'datesJson')
os.makedirs(out_dir_path, exist_ok=True)

files_queue = []
current_date = last_date
while current_date <= today:
  current_date += datetime.timedelta(1)

  url = 'https://www.whoscored.com/matchesfeed/?d=%s' % (current_date.strftime('%Y%m%d'),)
  print(url)

  date_broken_dirtyjson = whoscored_get(url).text
  date_dirtyjson = fix_dirtyjson(date_broken_dirtyjson)
  date_json = dirtyjson.loads(date_dirtyjson)

  out_file_path = os.path.join(out_dir_path, '%s.json' % (current_date.strftime('%Y-%m-%d'),))
  with open(out_file_path, 'w', encoding='utf-8') as f_out:
    json.dump(date_json, f_out, ensure_ascii=False)
  files_queue.append(out_file_path)

with open(last_file_path, 'w', encoding='utf-8') as f_last_out:
  f_last_out.write(current_date.strftime('%Y-%m-%d'))
with open(queue_file_path, 'w', encoding='utf-8') as f_queue_out:
  for file_queue in files_queue:
    f_queue_out.write(file_queue + '\n')
