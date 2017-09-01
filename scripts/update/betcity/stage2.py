#!/usr/bin/env python3


import re
import os
import glob
import json
import datetime
import re
import tqdm
import argparse
from betrobot.util.common_util import get_identifier, is_value_valid
from betrobot.betting.sport_util import tournaments_data, teams_data
from betrobot.grabbing.betcity.parsing import handle


_unknown_tournaments = set()
_unknown_teams = set()


def _get_possible_tournament_names(full_tournament_name):
    result = []

    full_tournament_name_parts = full_tournament_name.split('. ')

    for i in range(1, len(full_tournament_name_parts)+1):
        item = '. '.join(full_tournament_name_parts[:i])
        if item[-1] == '.':
            item = item[:-1]
        result.append(item)

    return result


def _is_betcity_tournament_name_valid(betcity_tournament_name):
     possible_tournament_names = _get_possible_tournament_names(betcity_tournament_name)

     for possible_tournament_name in possible_tournament_names:
         if is_value_valid(tournaments_data, 'betcityTournamentName', possible_tournament_name):
             return True

     return False


def _parse_file(file_path):
    m = re.search(r'(\d{4}-\d{2}-\d{2})\.html$', file_path)
    grab_date_str = m.group(1)

    grab_date = datetime.datetime.strptime(grab_date_str, '%Y-%m-%d').date()
    tomorrow_grab_date = grab_date + datetime.timedelta(days=1)

    with open(file_path, 'rt', encoding='utf-8') as f_in:
      for raw_match_data in handle(f_in):
        if not _is_betcity_tournament_name_valid(raw_match_data['tournament']):
            if raw_match_data['tournament'].startswith('Футбол.'):
                _unknown_tournaments.add(raw_match_data['tournament'])
            continue
        if 'Статистика игрового дня' in raw_match_data['tournament']:
            continue

        if not is_value_valid(teams_data, 'betcityName', raw_match_data['home']):
            _unknown_teams.add(raw_match_data['home'])
        if not is_value_valid(teams_data, 'betcityName', raw_match_data['away']):
            _unknown_teams.add(raw_match_data['away'])

        match_date = datetime.datetime.strptime(raw_match_data['date'], '%d.%m.%Y').date()
        if match_date != grab_date and match_date != tomorrow_grab_date:
            continue
        match_date_str = match_date.strftime('%Y-%m-%d')

        betcity_match_uuid = get_identifier()

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

    print('Unknown tournaments: %s' % (str(sorted(_unknown_tournaments)),))
    print('Unknown teams: %s' % (str(sorted(_unknown_teams)),))
