import os
import glob
import json
import datetime
import uuid
from betrobot.grabbing.betarch.parsing import get_text, remove_colon_and_dash, get_and_remove_special_word, handle_tournament_day, handle_bets, get_bets_from_line, get_bets_from_table, handle_main_data, handle_table_data,


matches_metadata = []

glob_path = os.path.join('data', 'betarch', 'datesHtml', '*.html')
for file_path in glob.iglob(glob_path):
  print(file_path)

  with open(file_path, 'rt', encoding='utf-8') as f_in:
    for tournament_day_raw_match_data in handle(f_in):
      match_uuid_str = str(uuid.uuid4())
      match_date_str = datetime.datetime.strptime(tournament_day_raw_match_data['date'], '%d.%m.%Y').strftime('%Y-%m-%d')

      match_data = {
        'uuid': match_uuid_str,
        'tournament': tournament_day_raw_match_data['tournament'],
        'date': match_date_str,
        'time': tournament_day_raw_match_data['time'],
        'home': tournament_day_raw_match_data['home'],
        'away': tournament_day_raw_match_data['away'],
        'specialWord': tournament_day_raw_match_data['special_word'],
        'bets': tournament_day_raw_match_data['bets']
      }

      out_dir_path = os.path.join('tmp', 'update', 'betarch', 'matchesJson', match_date_str)
      os.makedirs(out_dir_path, exist_ok=True)
      out_file_path = os.path.join(out_dir_path, '%s.json' % (match_uuid_str,))
      with open(out_file_path, 'wt', encoding='utf-8') as f_out:
        json.dump(match_data, f_out, ensure_ascii=False)

      match_metadata = {
        'uuid': match_uuid_str,
        'tournament': match_data['tournament'],
        'date': match_data['date'],
        'home': match_data['home'],
        'away': match_data['away'],
        'specialWord': match_data['specialWord']
      }
      matches_metadata.append(match_metadata)

matches_metadata_out_file_path = os.path.join('tmp', 'update', 'betarch', 'matches_metadata.json')
with open(matches_metadata_out_file_path, 'wt', encoding='utf-8') as matches_metadata_f_out:
  json.dump(matches_metadata, matches_metadata_f_out, ensure_ascii=False)
