import sys
sys.path.append('./')
sys.path.append('./util')

import json
import os
import glob
import datetime
from util import whoscored_get


out_dir_path = os.path.join('data', 'whoscored', 'matchesHtml')
os.makedirs(out_dir_path, exist_ok=True)

queue_file_path = os.path.join('data', 'whoscored', 'queue.txt')
if os.path.exists(queue_file_path):
  with open(queue_file_path, 'r', encoding='utf-8') as f_queue:
    file_paths = [ file_path for file_path in f_queue.read().split('\n') if len(file_path) > 0 ]
else:
  glob_path = os.path.join('data', 'whoscored', 'datesJson', '*.json')
  file_paths = glob.iglob(glob_path)

files_queue = []
for file_path in file_paths:
  with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

  (main_data, raw_tournaments_data, raw_matches_data) = data

  current_date_str = datetime.datetime.strptime(main_data[3], '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d')

  tournaments_data = {}
  for raw_tournament_data in raw_tournaments_data:
    stage_id = raw_tournament_data[0]
    tournaments_data[stage_id] = {
      'country_id': int(raw_tournament_data[1]),
      'country_name': raw_tournament_data[3],
      'tournament_id': raw_tournament_data[4],
      'tournament_name': raw_tournament_data[7],
      'season_id': raw_tournament_data[6],
      'stage_id': raw_tournament_data[0],
    }

  matches_metadata = {}
  for raw_match_data in raw_matches_data:
    match_id = raw_match_data[1]
    stage_id = raw_match_data[0]
    tournament_data = tournaments_data[stage_id]

    if tournament_data['country_name'] not in ('England', 'France', 'Germany', 'Spain', 'Italy', 'Russia', 'Portugal') or raw_match_data[15] != 1:
      continue

    url = 'https://www.whoscored.com/Matches/%d/Live' % (match_id,)
    match_html = whoscored_get(url).text
    print(url)

    out_file_path = os.path.join(out_dir_path, '%d.html' % (match_id,))
    with open(out_file_path, 'w', encoding='utf-8') as f_out:
      f_out.write(match_html)
    files_queue.append(out_file_path)

with open(queue_file_path, 'w', encoding='utf-8') as f_queue_out:
  for file_queue in files_queue:
    f_queue_out.write(file_queue + '\n')
