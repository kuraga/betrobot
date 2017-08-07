#!/usr/bin/env python3


import datetime
import os
import argparse
from betrobot.grabbing.intelbet.downloading import intelbet_get


def _download_intelbet_stage1():
    out_dir_path = os.path.join('tmp', 'update', 'intelbet', 'datesHtml')
    os.makedirs(out_dir_path, exist_ok=True)

    today = datetime.datetime.today()

    url = 'http://www.intelbet.ru/match-center/today/'
    print(url)
    today_html = intelbet_get(url)

    out_file_path = os.path.join(out_dir_path, '%s.html' % (today.strftime('%Y-%m-%d'),))
    with open(out_file_path, 'wt', encoding='utf-8') as f_out:
        f_out.write(today_html)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _download_intelbet_stage1()
