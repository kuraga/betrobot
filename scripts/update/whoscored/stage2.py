#!/usr/bin/env python3


import re
import json
import os
import glob
import datetime
import tqdm
import argparse
from betrobot.util.common_util import get_identifier, is_value_valid
from betrobot.betting.sport_util import tournaments_data
from betrobot.grabbing.whoscored.downloading import whoscored_get


def _parse_file(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f:
      data = json.load(f)

    m = re.search('(\d{4}-\d{2}-\d{2})\.json$', file_path)
    if m is None:
        raise RuntimeError('invalid file name')
    match_date_str = m.group(1)

    (main_data, raw_tournaments_data, raw_matches_data) = data

    stages_data = {}
    for raw_stage_data in raw_tournaments_data:
      if not is_value_valid(tournaments_data, 'whoscoredTournamentId', raw_stage_data[4]):
          continue

      stage_id = raw_stage_data[0]
      stages_data[stage_id] = {
        'region_id': int(raw_stage_data[1]),
        'region_name': raw_stage_data[3],
        'tournament_id': raw_stage_data[4],
        'tournament_name': raw_stage_data[7],
        'season_id': raw_stage_data[6],
        'stage_id': raw_stage_data[0],
      }

    for raw_match_data in raw_matches_data:
      stage_id = raw_match_data[0]
      if stage_id not in stages_data:
          continue
      stage_data = stages_data[stage_id]

      whoscored_match_uuid = get_identifier()

      match_id = raw_match_data[1]
      whoscored_header = {
        'uuid': whoscored_match_uuid,
        'matchId': match_id,
        'date': match_date_str,
        'home': raw_match_data[5],
        'homeId': raw_match_data[4],
        'away': raw_match_data[9],
        'awayId': raw_match_data[8],
        'regionId': stage_data['region_id'],
        'tournamentId': stage_data['tournament_id'],
        'seasonId': stage_data['season_id'],
        'stageId': stage_data['stage_id']
      }

      # WARNNING: Бывают и другие страницы
      url = 'https://www.whoscored.com/Matches/%d/Live' % (match_id,)
      print(url)
      match_html = whoscored_get(url, delay=0.5)

      out_dir_path = os.path.join('tmp', 'update', 'whoscored', 'matchesHtml', match_date_str)
      os.makedirs(out_dir_path, exist_ok=True)

      whoscored_header_out_file_path = os.path.join(out_dir_path, '%s.json' % (whoscored_match_uuid,))
      with open(whoscored_header_out_file_path, 'wt', encoding='utf-8') as whoscored_header_f_out:
        json.dump(whoscored_header, whoscored_header_f_out, ensure_ascii=False)

      html_out_file_path = os.path.join(out_dir_path, '%s.html' % (whoscored_match_uuid,))
      with open(html_out_file_path, 'wt', encoding='utf-8') as html_f_out:
        html_f_out.write(match_html)


def _parse_whoscored_stage2():
    glob_path = os.path.join('tmp', 'update', 'whoscored', 'datesJson', '*.json')
    file_paths = glob.glob(glob_path)

    bar = tqdm.tqdm(file_paths)
    for file_path in bar:
        bar.write('Processing file %s...' % (file_path,))
        _parse_file(file_path)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    args = argument_parser.parse_args()

    _parse_whoscored_stage2()
