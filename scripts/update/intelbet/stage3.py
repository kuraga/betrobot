#!/usr/bin/env python3


import re
import json
import dirtyjson
import codecs
import glob
import os
import datetime
import uuid
import tqdm
import argparse
from betrobot.grabbing.intelbet.parsing import handle_match


def _parse_file(intelbet_header_file_path):
    with open(intelbet_header_file_path, 'rt', encoding='utf-8') as f:
      intelbet_header = json.load(f)

    match_data = dict(intelbet_header)

    match_files_glob_path = re.sub(r'\.json$', '*.html', intelbet_header_file_path)
    match_file_paths = glob.glob(match_files_glob_path)
    for match_file_path in match_file_paths:
        with open(match_file_path, 'rt', encoding='utf-8') as f:
            (home_player_names, away_player_names) = handle_match(f)
        match_data.update({
            'homePlayerNames': home_player_names,
            'awayPlayerNames': away_player_names
        })

    out_dir_path = os.path.join('tmp', 'update', 'intelbet', 'matchesJson', intelbet_header['date'])
    os.makedirs(out_dir_path, exist_ok=True)
    out_file_path = os.path.join(out_dir_path, '%s.json' % (intelbet_header['uuid'],))
    with open(out_file_path, 'wt', encoding='utf-8') as f_out:
      json.dump(match_data, f_out, ensure_ascii=False)


def _parse_intelbet_stage3():
    glob_path = os.path.join('tmp', 'update', 'intelbet', 'matchesHtml', '*', '*.json')
    file_paths = glob.glob(glob_path)

    bar = tqdm.tqdm(file_paths)
    for file_path in bar:
        bar.write('Processing file %s...' % (file_path,))
        _parse_file(file_path)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _parse_intelbet_stage3()
