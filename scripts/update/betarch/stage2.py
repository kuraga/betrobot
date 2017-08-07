#!/usr/bin/env python3


import os
import glob
import json
import datetime
import uuid
import tqdm
import argparse
from betrobot.grabbing.betarch.parsing import handle


def _parse_file(file_path):
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


def _parse_betarch_stage2(glob_path):
    file_paths = glob.glob(glob_path)
    bar = tqdm.tqdm(file_paths)
    for file_path in bar:
        bar.write('Processing file %s...' % (file_path,))
        _parse_file(file_path)


if __name__ == '__main__':
    default_glob_path = os.path.join('tmp', 'update', 'betarch', 'datesHtml', '*.html')

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('glob_path', nargs='?', default=default_glob_path)
    args = argument_parser.parse_args()

    _parse_betarch_stage2(args.glob_path)
