#!/usr/bin/env python3


import datetime
import os
import argparse
from betrobot.grabbing.betarch.downloading import betarch_get


def _parse_betarch_stage1(next_date, last_date):
  out_dir_path = os.path.join('tmp', 'update', 'betarch', 'datesHtml')
  os.makedirs(out_dir_path, exist_ok=True)

  current_date = next_date
  while current_date != last_date:
    url = 'http://betarch.ru/index.php?date=b%s' % (current_date.strftime('%Y-%m-%d'),)
    print(url)
    date_html = betarch_get(url)

    if date_html != 'File not exists':
      out_file_path = os.path.join(out_dir_path, '%s.html' % (current_date.strftime('%Y-%m-%d'),))
      with open(out_file_path, 'wt', encoding='utf-8') as f_out:
        f_out.write(date_html)

    current_date += datetime.timedelta(1)


if __name__ == '__main__':
    next_date_default = '2014-01-01'
    last_date_default = datetime.date.today().strftime('%Y-%m-%d')

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--next-date', default=next_date_default)
    argument_parser.add_argument('--last-date', default=last_date_default)
    args = argument_parser.parse_args()

    next_date = datetime.datetime.strptime(args.next_date, '%Y-%m-%d').date()
    last_date = datetime.datetime.strptime(args.last_date, '%Y-%m-%d').date()

    _parse_betarch_stage1(next_date, last_date)
