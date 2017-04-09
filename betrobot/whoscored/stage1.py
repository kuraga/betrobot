import datetime
import os
import dirtyjson
import json
from betrobot.whoscored.util import whoscored_get, fix_dirtyjson


next_file_path = os.path.join('data', 'whoscored', 'next.txt')
if os.path.exists(next_file_path):
  with open(next_file_path, 'rt', encoding='utf-8') as f_next:
    next_date_str = f_next.read().rstrip()
  next_date = datetime.datetime.strptime(next_date_str, '%Y-%m-%d').date()
else:
  next_date = datetime.date(2014, 1, 1)

out_dir_path = os.path.join('tmp', 'update', 'whoscored', 'datesJson')
os.makedirs(out_dir_path, exist_ok=True)

today = datetime.date.today()
current_date = next_date + datetime.timedelta(0)
while current_date < today:
  url = 'https://www.whoscored.com/matchesfeed/?d=%s' % (current_date.strftime('%Y%m%d'),)
  print(url)

  date_broken_dirtyjson = whoscored_get(url).text
  date_dirtyjson = fix_dirtyjson(date_broken_dirtyjson)
  date_json = dirtyjson.loads(date_dirtyjson)

  out_file_path = os.path.join(out_dir_path, '%s.json' % (current_date.strftime('%Y-%m-%d'),))
  with open(out_file_path, 'wt', encoding='utf-8') as f_out:
    json.dump(date_json, f_out, ensure_ascii=False)

  current_date += datetime.timedelta(1)
new_next_date_str = current_date.strftime('%Y-%m-%d')

next_out_file_path = os.path.join('tmp', 'update', 'whoscored', 'next.txt')
with open(next_out_file_path, 'wt', encoding='utf-8') as f_next_out:
  f_next_out.write(new_next_date_str)
