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
from betrobot.betting.sport_util import get_teams_tournaments_countries_value
from betrobot.grabbing.whoscored.downloading import fix_dirtyjson



def _extract1(match_html, match_data, r, key, flags=0):
  m = re.search(r, match_html, flags)
  if m is None:
    return

  dirtyjson_string = m.group(1)
  fixed_dirtyjson_string = fix_dirtyjson(dirtyjson_string)

  value = dirtyjson.loads(fixed_dirtyjson_string)
  if value is None:
    return

  match_data[key] = value


def _extract2(match_html, match_data, r, key, flags=0):
  m = re.search(r, match_html, flags)
  if m is None:
    return

  json_string = m.group(1)
  unescaper = codecs.getdecoder('unicode_escape')
  unescaped_json_string = unescaper(json_string)[0]

  value = json.loads(unescaped_json_string)
  if value is None:
    return

  match_data[key] = value


def _parse_file(whoscored_header_file_path):
    with open(whoscored_header_file_path, 'rt', encoding='utf-8') as f:
      whoscored_header = json.load(f)

    match_uuid_str = str(uuid.uuid4())
    match_date_str = '%s' % (whoscored_header['date'],)
    match_data = dict(whoscored_header)

    match_files_glob_path = re.sub(r'\.json$', '*.html', whoscored_header_file_path)
    match_file_paths = glob.glob(match_files_glob_path)
    for match_file_path in match_file_paths:
      with open(match_file_path, 'rt', encoding='utf-8') as f:
          match_html = f.read()

          # WARNING: Предполагается отсутствие символа ';' в репрезентации значении переменной
          _extract1(match_html, match_data, r'var matchCentreData = (.+?);', 'matchCentreData')
          # WARNING: В случае подключения других страниц (и необходимости):
          # _extract1(match_html, match_data, r'var matchCentreEventType = (.+?);', 'matchCentreEventType')
          # _extract1(match_html, match_data, r'var formationIdNameMappings = (.+?);', 'formationIdNameMappings')
          # _extract1(match_html, match_data, r'var matchStats = (.+?);', 'matchStats', re.MULTILINE | re.DOTALL)
          # _extract1(match_html, match_data, r'var initialMatchDataForScrappers = (.+?);', 'initialMatchDataForScrappers', re.MULTILINE | re.DOTALL)
          # _extract2(match_html, match_data, r'var matchHeaderJson = JSON.parse\(\'(.+?)\'\);', 'matchHeader', 0)
          # _extract2(match_html, match_data, r'var homePlayers = JSON.parse\(\'(.+?)\'\);', 'homePlayers', 0)
          # _extract2(match_html, match_data, r'var awayPlayers = JSON.parse\(\'(.+?)\'\);', 'awayPlayers', 0)

    out_dir_path = os.path.join('tmp', 'update', 'whoscored', 'matchesJson', match_date_str)
    os.makedirs(out_dir_path, exist_ok=True)
    out_file_path = os.path.join(out_dir_path, '%s.json' % (match_uuid_str,))
    with open(out_file_path, 'wt', encoding='utf-8') as f_out:
      json.dump(match_data, f_out, ensure_ascii=False)


def _parse_whoscored_stage3(glob_path):
    file_paths = glob.glob(glob_path)
    bar = tqdm.tqdm(file_paths)
    for file_path in bar:
        bar.write('Processing file %s...' % (file_path,))
        _parse_file(file_path)


if __name__ == '__main__':
    default_glob_path = os.path.join('tmp', 'update', 'whoscored', 'matchesHtml', '*', '*.json')

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('glob_path', nargs='?', default=default_glob_path)
    args = argument_parser.parse_args()

    _parse_whoscored_stage3(args.glob_path)
