#!/usr/bin/env python3


import datetime
import os
import dirtyjson
import json
import argparse
from betrobot.grabbing.whoscored.downloading import whoscored_get
from betrobot.grabbing.whoscored.parsing import fix_dirtyjson


def _parse_whoscored_stage1(next_date, last_date):
  out_dir_path = os.path.join('tmp', 'update', 'whoscored', 'datesJson')
  os.makedirs(out_dir_path, exist_ok=True)

  current_date = next_date + datetime.timedelta(0)
  while current_date <= last_date:
    url = 'https://www.whoscored.com/matchesfeed/?d=%s' % (current_date.strftime('%Y%m%d'),)
    print(url)

    date_broken_dirtyjson = whoscored_get(url)
    date_dirtyjson = fix_dirtyjson(date_broken_dirtyjson)
    date_json = dirtyjson.loads(date_dirtyjson)

    out_file_path = os.path.join(out_dir_path, '%s.json' % (current_date.strftime('%Y-%m-%d'),))
    with open(out_file_path, 'wt', encoding='utf-8') as f_out:
      json.dump(date_json, f_out, ensure_ascii=False)

    current_date += datetime.timedelta(1)


if __name__ == '__main__':
    next_date_default = datetime.date.today().strftime('%Y-%m-%d')
    last_date_default = datetime.date.today().strftime('%Y-%m-%d')

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--next-date', default=next_date_default)
    argument_parser.add_argument('--last-date', default=last_date_default)
    args = argument_parser.parse_args()

    next_date = datetime.datetime.strptime(args.next_date, '%Y-%m-%d').date()
    last_date = datetime.datetime.strptime(args.last_date, '%Y-%m-%d').date()

    _parse_whoscored_stage1(next_date, last_date)
