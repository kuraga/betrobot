import json
import os
import glob
import datetime
from betrobot.whoscored.util import whoscored_get


glob_path = os.path.join('tmp', 'update', 'whoscored', 'datesJson', '*.json')
file_paths = glob.iglob(glob_path)

out_dir_path = os.path.join('tmp', 'update', 'whoscored', 'matchesHtml')
os.makedirs(out_dir_path, exist_ok=True)

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

    if raw_match_data[15] != 1:
      continue

    if tournament_data['country_name'] not in ('England', 'France', 'Germany', 'Spain', 'Italy', 'Russia', 'Portugal'):
      continue

    url = 'https://www.whoscored.com/Matches/%d/Live' % (match_id,)
    match_html = whoscored_get(url).text
    print(url)

    out_file_path = os.path.join(out_dir_path, '%d.html' % (match_id,))
    with open(out_file_path, 'w', encoding='utf-8') as f_out:
      f_out.write(match_html)
