import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./check')

import os
import json
import glob2
from check_util import check_bet


def check_data(data):
    for betcity_match in data['betarch']:
        match_special_word = betcity_match['specialWord']
        whoscored_match = data['whoscored'][0]

        for bet in betcity_match['bets']:
            ground_truth = check_bet(bet, match_special_word, whoscored_match)
            if ground_truth is not None:
                 print(bet, ground_truth)


glob_path = os.path.join('data', 'combine', 'matchesJson', '**', '*.json')
for file_path, (path, filename) in glob2.iglob(glob_path, with_matches=True):
    print(file_path)

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    check_data(data)
