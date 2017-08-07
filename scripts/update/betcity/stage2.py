#!/usr/bin/env python3


import os
import glob
import json
import datetime
import tqdm
import argparse
from betrobot.util.common_util import get_identifier
from betrobot.grabbing.betcity.parsing import handle


def _parse_file(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f_in:
      for tournament_raw_match_data in handle(f_in):
        betcity_match_uuid = get_identifier()
        match_date_str = datetime.datetime.strptime(tournament_raw_match_data['date'], '%d.%m.%Y').strftime('%Y-%m-%d')

        match_data = {
          'betcityMatcUuid': betcity_match_uuid,
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
        out_file_path = os.path.join(out_dir_path, '%s.json' % (betcity_match_uuid,))
        with open(out_file_path, 'wt', encoding='utf-8') as f_out:
          json.dump(match_data, f_out, ensure_ascii=False)


def _parse_betcity_stage2():
    default_glob_path = os.path.join('tmp', 'update', 'betcity', 'datesHtml', '*.html')
    file_paths = glob.glob(glob_path)

    bar = tqdm.tqdm(file_paths)
    for file_path in bar:
        bar.write('Processing file %s...' % (file_path,))
        _parse_file(file_path)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    args = argument_parser.parse_args()

    _parse_betcity_stage2()
