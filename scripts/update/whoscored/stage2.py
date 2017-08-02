#!/usr/bin/env python3


import re
import json
import os
import glob2
import datetime
import tqdm
import argparse
from betrobot.betting.sport_util import teams_tournaments_countries_data
from betrobot.grabbing.whoscored.downloading import whoscored_get


_tournament_ids = frozenset(teams_tournaments_countries_data['whoscoredTournamentId'])
_teams = frozenset(teams_tournaments_countries_data['whoscoredName'])


def _parse_file(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f:
      data = json.load(f)

    m = re.search('(\d{4}-\d{2}-\d{2})\.json$', file_path)
    if m is None:
        raise RuntimeError('invalid file name')
    match_date_str = m.group(1)

    (main_data, raw_tournaments_data, raw_matches_data) = data

    tournaments_data = {}
    for raw_tournament_data in raw_tournaments_data:
      stage_id = raw_tournament_data[0]
      tournaments_data[stage_id] = {
        'region_id': int(raw_tournament_data[1]),
        'region_name': raw_tournament_data[3],
        'tournament_id': raw_tournament_data[4],
        'tournament_name': raw_tournament_data[7],
        'season_id': raw_tournament_data[6],
        'stage_id': raw_tournament_data[0],
      }

    for raw_match_data in raw_matches_data:
      match_id = raw_match_data[1]
      stage_id = raw_match_data[0]
      tournament_data = tournaments_data[stage_id]

      whoscored_header = {
        'matchId': match_id,
        'date': match_date_str,
        'home': raw_match_data[5],
        'homeId': raw_match_data[4],
        'away': raw_match_data[9],
        'awayId': raw_match_data[8],
        'regionId': tournament_data['region_id'],
        'tournamentId': tournament_data['tournament_id'],
        'seasonId': tournament_data['season_id'],
        'stageId': tournament_data['stage_id']
      }


      # FIXME: Принять решение, какие матчи сохранять
      if whoscored_header['tournamentId'] not in _tournament_ids or \
        (whoscored_header['home'] not in _teams and whoscored_header['away'] not in _teams):
          continue

      # WARNNING: Бывают и другие страницы
      url = 'https://www.whoscored.com/Matches/%d/Live' % (match_id,)
      print(url)
      match_html = whoscored_get(url, delay=0.5).text

      out_dir_path = os.path.join('tmp', 'update', 'whoscored', 'matchesHtml', match_date_str)
      os.makedirs(out_dir_path, exist_ok=True)

      whoscored_header_out_file_path = os.path.join(out_dir_path, '%d.json' % (match_id,))
      with open(whoscored_header_out_file_path, 'wt', encoding='utf-8') as whoscored_header_f_out:
        json.dump(whoscored_header, whoscored_header_f_out)

      html_out_file_path = os.path.join(out_dir_path, '%d.html' % (match_id,))
      with open(html_out_file_path, 'wt', encoding='utf-8') as html_f_out:
        html_f_out.write(match_html)


def _parse_whoscored_stage2(glob_path):
    file_paths = glob2.glob(glob_path)
    bar = tqdm.tqdm(file_paths)
    for file_path in bar:
        bar.write('Processing file %s...' % (file_path,))
        _parse_file(file_path)


if __name__ == '__main__':
    default_glob_path = os.path.join('tmp', 'update', 'whoscored', 'datesJson', '*.json')

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('glob_path', nargs='?', default=default_glob_path)
    args = argument_parser.parse_args()

    _parse_whoscored_stage2(args.glob_path)
