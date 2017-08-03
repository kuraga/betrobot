#!/usr/bin/env python3


import os
import glob
import json
import tqdm
import argparse
from betrobot.util.database_util import db
from betrobot.betting.sport_util import get_extended_info, get_bets_match, get_match_uuid_by_betarch_match
from betrobot.betting.bets_checking import check_bet
from betrobot.grabbing.betarch.incorporating import transform_betarch_bets


def _update_with_betarch_match(match_uuid, betarch_match):
    bets_match = get_bets_match(match_uuid)
    whoscored_match = get_extended_info(match_uuid)['whoscored']

    bets_dict = { tuple(bet['pattern']): bet for bet in bets_match['bets'] }

    transformed_betarch_bets = transform_betarch_bets(betarch_match)
    for bet in transformed_betarch_bets:
        bet_pattern_tuple = tuple(bet['pattern'])

        if bet_pattern_tuple not in bets_dict:
            bets_dict[bet_pattern_tuple] = bet
        else:
            bets_dict[bet_pattern_tuple]['value'] = bet['value']
        bets_dict[bet_pattern_tuple]['match_uuid'] = match_uuid

        if bets_dict[bet_pattern_tuple]['ground_truth'] is None:
            # FIXME: После пересборки базы можно убрать match_uuid
            bets_dict[bet_pattern_tuple]['ground_truth'] = check_bet(bet, whoscored_match=whoscored_match, match_uuid=match_uuid)

    bets = list(bets_dict.values())

    bets_collection = db['bets']
    bets_collection.update_one({ 'match_uuid': match_uuid }, { '$set': { 'bets': bets } }, upsert=True)


def _incorporate_betarch_files():
    betarch_glob_path = os.path.join('tmp', 'update', 'betarch', 'matchesJson', '*', '*.json')
    betarch_file_paths = glob.glob(betarch_glob_path)

    bar = tqdm.tqdm(betarch_file_paths)
    for betarch_file_path in bar:
        bar.write('Processing file %s...' % (betarch_file_path,))

        with open(betarch_file_path, 'rt', encoding='utf-8') as f:
            betarch_match = json.load(f)

        match_uuid = get_match_uuid_by_betarch_match(betarch_match)
        if match_uuid is not None:
            _update_with_betarch_match(match_uuid, betarch_match)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _incorporate_betarch_files()
