import datetime
import os
import argparse
from betrobot.grabbing.betarch.downloading import betarch_get


def _parse_betarch_stage1():
  today_date = datetime.date.today()
  out_dir_path = os.path.join('tmp', 'update', 'betarch', 'datesHtml')
  os.makedirs(out_dir_path, exist_ok=True)

  current_date = datetime.date(2014, 1, 1)
  while current_date != today_date:
    url = 'http://betarch.ru/index.php?date=b%s' % (current_date.strftime('%Y-%m-%d'),)
    print(url)
    date_html = betarch_get(url).text

    if date_html != 'File not exists':
      out_file_path = os.path.join(out_dir_path, '%s.html' % (current_date.strftime('%Y-%m-%d'),))
      with open(out_file_path, 'wt', encoding='utf-8') as f_out:
        f_out.write(date_html)

    current_date += datetime.timedelta(1)


if __name__ == '__main__':
  argument_parser = argparse.ArgumentParser()
  argument_parser.parse_args()

  _parse_betarch_stage1()
