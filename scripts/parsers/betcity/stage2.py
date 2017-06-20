import os
import glob
import json
import datetime
import uuid
from betrobot.grabbing.betcity.parsing import get_text, remove_colon_and_dash, get_and_remove_special_word, handle, handle_tournament, handle_bets, get_bets_from_line, get_bets_from_table, handle_main_data, handle_table_data
from betrobot.util.common_util import safe_read_json


matches_metadata_file_path = os.path.join('data', 'betcity', 'matches_metadata.json')
matches_metadata = safe_read_json(matches_metadata_file_path, [])

next_file_path = os.path.join('data', 'betcity', 'next.txt')
if os.path.exists(next_file_path):
  with open(next_file_path, 'rt', encoding='utf-8') as f_next:
    next_date_str = f_next.read().rstrip()
  next_date = datetime.datetime.strptime(next_date_str, '%Y-%m-%d').date()

  file_paths = []
  today = datetime.date.today()
  current_date = next_date + datetime.timedelta(0)
  while current_date <= today:
    file_name = '%s.html' % (current_date.strftime('%Y-%m-%d'),)
    file_path = os.path.join('data', 'betcity', 'datesHtml', file_name)
    file_paths.append(file_path)
    current_date += datetime.timedelta(1)
  new_next_date_str = current_date.strftime('%Y-%m-%d')

else:
  glob_path = os.path.join('data', 'betcity', 'datesHtml', '*.html')
  file_paths = glob.glob(glob_path)

for file_path in file_paths:
  print(file_path)
  if not os.path.exists(file_path):
    continue

  with open(file_path, 'rt', encoding='utf-8') as f_in:
    for tournament_raw_match_data in handle(f_in):
      match_uuid_str = str(uuid.uuid4())
      match_date_str = datetime.datetime.strptime(tournament_raw_match_data['date'], '%d.%m.%Y').strftime('%Y-%m-%d')

      match_data = {
        'uuid': match_uuid_str,
        'tournament': tournament_raw_match_data['tournament'],
        'date': match_date_str,
        'time': tournament_raw_match_data['time'],
        'home': tournament_raw_match_data['home'],
        'away': tournament_raw_match_data['away'],
        'specialWord': tournament_raw_match_data['special_word'],
        'bets': tournament_raw_match_data['bets']
      }

      out_dir_path = os.path.join('tmp', 'update', 'betcity', 'matchesJson', match_date_str)
      os.makedirs(out_dir_path, exist_ok=True)
      out_file_path = os.path.join(out_dir_path, '%s.json' % (match_uuid_str,))
      with open(out_file_path, 'wt', encoding='utf-8') as f_out:
        json.dump(match_data, f_out, ensure_ascii=False)

      match_metadata = {
        'uuid': match_uuid_str,
        'tournament': match_data['tournament'],
        'date': match_date_str,
        'home': match_data['home'],
        'away': match_data['away'],
        'specialWord': match_data['specialWord']
      }
      matches_metadata.append(match_metadata)


matches_metadata_out_file_path = os.path.join('tmp', 'update', 'betcity', 'matches_metadata.json')
with open(matches_metadata_out_file_path, 'wt', encoding='utf-8') as matches_metadata_f_out:
  json.dump(matches_metadata, matches_metadata_f_out, ensure_ascii=False)

next_out_file_path = os.path.join('tmp', 'update', 'betcity', 'next.txt')
with open(next_out_file_path, 'wt', encoding='utf-8') as f_next_out:
  f_next_out.write(new_next_date_str)
