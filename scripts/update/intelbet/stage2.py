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


def _parse_file(file_path):
    m = re.search(r'(\d{4}-\d{2}-\d{2})\.html$', file_path)
    date_str = m.group(1)

    with open(file_path, 'rt', encoding='utf-8') as f:
        data = handle_date(f)

    for item in data:
        (intelbet_country, intelbet_tournament, intelbet_home, intelbet_away, url, match_time_str) = item

        if not ( is_value_valid(countries_data, 'intelbetCountryName', intelbet_country) and \
          is_value_valid(tournaments_data, 'intelbetTournamentName', intelbet_tournament) ):
            continue

        intelbet_match_uuid = get_identifier()

        intelbet_match_header = {
            'uuid': intelbet_match_uuid,
            'date': date_str,
            'home': intelbet_home,
            'away': intelbet_away,
            'contry': intelbet_country,
            'tournament': intelbet_tournament,
            'url': url,
            'time': match_time_str
        }

        print(url)
        match_html = intelbet_get(url, delay=0.5)

        out_dir_path = os.path.join('tmp', 'update', 'intelbet', 'matchesHtml', date_str)
        os.makedirs(out_dir_path, exist_ok=True)

        header_out_file_path = os.path.join(out_dir_path, '%s.json' % (intelbet_match_uuid,))
        with open(header_out_file_path, 'wt', encoding='utf-8') as header_f_out:
            json.dump(intelbet_match_header, header_f_out, ensure_ascii=False)

        out_file_path = os.path.join(out_dir_path, '%s.html' % (intelbet_match_uuid,))
        with open(out_file_path, 'wt', encoding='utf-8') as f_out:
            f_out.write(match_html)


def _download_intelbet_stage2():
    glob_path = os.path.join('tmp', 'update', 'intelbet', 'datesHtml', '*.html')
    file_paths = glob.glob(glob_path)

    bar = tqdm.tqdm(file_paths)
    for file_path in bar:
        bar.write('Processing file %s...' % (file_path,))
        _parse_file(file_path)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _download_intelbet_stage2()
