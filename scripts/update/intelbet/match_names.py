#!/usr/bin/env python3


import re
import json
import datetime
import os
import tqdm
import glob
import argparse
from betrobot.util.common_util import get_identifier, is_value_valid
from betrobot.betting.sport_util import countries_data, tournaments_data
from betrobot.grabbing.intelbet.downloading import intelbet_get
from betrobot.grabbing.intelbet.parsing import handle_date
from betrobot.grabbing.intelbet.matching_names import match_names_automatically


def _parse_file(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f:
        data = handle_date(f)

    for item in data:
        (intelbet_country, intelbet_tournament, intelbet_home, intelbet_away, url, match_time_str) = item

        if not ( is_value_valid(countries_data, 'intelbetCountryName', intelbet_country) and \
          is_value_valid(tournaments_data, 'intelbetTournamentName', intelbet_tournament) ):
            continue

        print(url)
        match_names_automatically(url)


def _match_names():
    glob_path = os.path.join('tmp', 'update', 'intelbet', 'datesHtml', '*.html')
    file_paths = glob.glob(glob_path)

    bar = tqdm.tqdm(file_paths)
    for file_path in bar:
        bar.write('Processing file %s...' % (file_path,))
        _parse_file(file_path)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _match_names()
