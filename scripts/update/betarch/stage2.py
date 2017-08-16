#!/usr/bin/env python3


import os
import glob
import json
import datetime
import tqdm
import argparse
from betrobot.util.common_util import get_identifier, is_value_valid
from betrobot.betting.sport_util import tournaments_data
from betrobot.grabbing.betarch.parsing import handle


def _get_possible_tournament_names(full_tournament_name):
    result = []

    full_tournament_name_parts = full_tournament_name.split('. ')

    for i in range(1, len(full_tournament_name_parts)+1):
        item = '. '.join(full_tournament_name_parts[:i])
        if item[-1] == '.':
            item = item[:-1]
        result.append(item)

    return result


def _is_betarch_tournament_name_valid(betarch_tournament_name):
     possible_tournament_names = _get_possible_tournament_names(betarch_tournament_name)

     for possible_tournament_name in possible_tournament_names:
         if is_value_valid(tournaments_data, 'betarchTournamentName', possible_tournament_name):
             return True

     return False


def _parse_file(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f_in:
      for tournament_day_raw_match_data in handle(f_in):
        if not _is_betarch_tournament_name_valid(raw_match_data['tournament']):
            continue

        betarch_match_uuid = get_identifier()
        match_date_str = datetime.datetime.strptime(tournament_day_raw_match_data['date'], '%d.%m.%Y').strftime('%Y-%m-%d')

        match_data = {
          'uuid': betarch_match_uuid,
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
        out_file_path = os.path.join(out_dir_path, '%s.json' % (betarch_match_uuid,))
        with open(out_file_path, 'wt', encoding='utf-8') as f_out:
          json.dump(match_data, f_out, ensure_ascii=False)


def _parse_betarch_stage2():
    glob_path = os.path.join('tmp', 'update', 'betarch', 'datesHtml', '*.html')
    file_paths = glob.glob(glob_path)

    bar = tqdm.tqdm(file_paths)
    for file_path in bar:
        bar.write('Processing file %s...' % (file_path,))
        _parse_file(file_path)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    args = argument_parser.parse_args()

    _parse_betarch_stage2()
