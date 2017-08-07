#!/usr/bin/env python3


import os
import glob
import json
import tqdm
import argparse
from betrobot.util.database_util import db
from betrobot.betting.sport_util import get_extended_info, get_bets_match, get_match_uuid_by_betcity_match
from betrobot.betting.bets_checking import check_bet
from betrobot.grabbing.betcity.incorporating import transform_betcity_bets


def _update_with_betcity_match(match_uuid, betcity_match):
    bets_match = get_bets_match(match_uuid)
    whoscored_match = get_extended_info(match_uuid)['whoscored']

    bets_dict = { tuple(bet['pattern']): bet for bet in bets_match['bets'] }

    transformed_betcity_bets = transform_betcity_bets(betcity_match)
    for bet in transformed_betcity_bets:
        bet_pattern_tuple = tuple(bet['pattern'])

        if bet_pattern_tuple not in bets_dict:
            bets_dict[bet_pattern_tuple] = bet
        else:
            bets_dict[bet_pattern_tuple]['value'] = bet['value']
        bets_dict[bet_pattern_tuple]['match_uuid'] = match_uuid

        if bets_dict[bet_pattern_tuple]['ground_truth'] is None:
            bets_dict[bet_pattern_tuple]['ground_truth'] = check_bet(bet, whoscored_match=whoscored_match)

    bets = list(bets_dict.values())

    bets_collection = db['bets']
    bets_collection.update_one({ 'match_uuid': match_uuid }, { '$set': { 'bets': bets } }, upsert=True)


def _incorporate_betcity_files():
    betcity_glob_path = os.path.join('tmp', 'update', 'betcity', 'matchesJson', '*', '*.json')
    betcity_file_paths = glob.glob(betcity_glob_path)

    bar = tqdm.tqdm(betcity_file_paths)
    for betcity_file_path in bar:
        bar.write('Processing file %s...' % (betcity_file_path,))

        with open(betcity_file_path, 'rt', encoding='utf-8') as f:
            betcity_match = json.load(f)

        match_uuid = get_match_uuid_by_betcity_match(betcity_match)
        if match_uuid is not None:
            _update_with_betcity_match(match_uuid, betcity_match)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _incorporate_betcity_files()
