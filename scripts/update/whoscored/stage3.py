#!/usr/bin/env python3


import re
import json
import glob
import os
import datetime
import tqdm
import argparse
from betrobot.grabbing.whoscored.parsing import handle_match


def _parse_file(whoscored_header_file_path):
    with open(whoscored_header_file_path, 'rt', encoding='utf-8') as f:
      whoscored_header = json.load(f)

    match_date_str = '%s' % (whoscored_header['date'],)

    match_files_glob_path = re.sub(r'\.json$', '*.html', whoscored_header_file_path)
    match_file_paths = glob.glob(match_files_glob_path)
    for match_file_path in match_file_paths:
      with open(match_file_path, 'rt', encoding='utf-8') as f:
          match_data = handle_match(f)
          match_data.update(whoscored_header)

    out_dir_path = os.path.join('tmp', 'update', 'whoscored', 'matchesJson', match_date_str)
    os.makedirs(out_dir_path, exist_ok=True)
    out_file_path = os.path.join(out_dir_path, '%s.json' % (whoscored_header['uuid'],))
    with open(out_file_path, 'wt', encoding='utf-8') as f_out:
      json.dump(match_data, f_out, ensure_ascii=False)


def _parse_whoscored_stage3():
    glob_path = os.path.join('tmp', 'update', 'whoscored', 'matchesHtml', '*', '*.json')
    file_paths = glob.glob(glob_path)

    bar = tqdm.tqdm(file_paths)
    for file_path in bar:
        bar.write('Processing file %s...' % (file_path,))
        _parse_file(file_path)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    args = argument_parser.parse_args()

    _parse_whoscored_stage3()
