#!/usr/bin/env python3


import re
import os
import glob
import json
import datetime
import tqdm
import argparse
from betrobot.util.common_util import get_identifier, is_value_valid
from betrobot.betting.sport_util import tournaments_data
from betrobot.grabbing.betcity.parsing import handle


def _parse_file(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f_in:
      for raw_match_data in handle(f_in):
        if not is_value_valid(tournaments_data, 'betcityTournamentName', raw_match_data['tournament']):
            continue

        betcity_match_uuid = get_identifier()
        match_date_str = datetime.datetime.strptime(raw_match_data['date'], '%d.%m.%Y').strftime('%Y-%m-%d')

        match_data = {
          'uuid': betcity_match_uuid,
          'tournament': raw_match_data['tournament'],
          'date': match_date_str,
          'time': raw_match_data['time'],
          'home': raw_match_data['home'],
          'away': raw_match_data['away'],
          'specialWord': raw_match_data['special_word'],
          'bets': raw_match_data['bets']
        }

        out_dir_path = os.path.join('tmp', 'update', 'betcity', 'matchesJson', match_date_str)
        os.makedirs(out_dir_path, exist_ok=True)
        out_file_path = os.path.join(out_dir_path, '%s.json' % (betcity_match_uuid,))
        with open(out_file_path, 'wt', encoding='utf-8') as f_out:
          json.dump(match_data, f_out, ensure_ascii=False)


def _parse_betcity_stage2():
    glob_path = os.path.join('tmp', 'update', 'betcity', 'datesHtml', '*.html')
    file_paths = glob.glob(glob_path)

    bar = tqdm.tqdm(file_paths)
    for file_path in bar:
        bar.write('Processing file %s...' % (file_path,))
        _parse_file(file_path)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    args = argument_parser.parse_args()

    _parse_betcity_stage2()
