#!/usr/bin/env python3


import os
import glob
import json
import uuid
import tqdm
import argparse
from betrobot.util.database_util import db
from betrobot.betting.sport_util import get_match_header, get_extended_info, get_bets_match, get_match_uuid_by_whoscored_match, get_match_uuid_by_betarch_match, get_match_uuid_by_betcity_match, dateize
from betrobot.betting.bets_checking import check_bet
from betrobot.grabbing.betarch.incorporating import transform_betarch_bets
from betrobot.grabbing.betcity.incorporating import transform_betcity_bets


def _create_match(whoscored_match):
    match_uuid = str(uuid.uuid4())

    match_headers_collection = db['match_headers']
    match_header = {
      'uuid': match_uuid,
      'date': dateize(whoscored_match['date']),
      'home': whoscored_match['home'],
      'away': whoscored_match['away'],
      'regionId': whoscored_match['regionId'],
      'tournamentId': whoscored_match['tournamentId'],
      'seasonId': whoscored_match['seasonId'],
      'stageId': whoscored_match['stageId']
    }
    match_headers_collection.insert_one(match_header)


    additional_info_collection = db['additional_info']
    additional_info = {
      'match_uuid': match_uuid
    }

    if 'matchCentreData' in whoscored_match:
      additional_info['homePlayers'] = []
      for home_player_data in whoscored_match['matchCentreData']['home']['players']:
        additional_info['homePlayers'].append({
          'playerId': home_player_data['playerId'],
          'playerName': home_player_data['name'],
          'isFirstEleven': home_player_data.get('isFirstEleven', False)
        })
      additional_info['awayPlayers'] = []
      for away_player_data in whoscored_match['matchCentreData']['away']['players']:
        additional_info['awayPlayers'].append({
          'playerId': away_player_data['playerId'],
          'playerName': away_player_data['name'],
          'isFirstEleven': away_player_data.get('isFirstEleven', False)
        })

    additional_info_collection.insert_one(additional_info)


    matches_collection = db['matches']
    match = {
      'match_uuid': match_uuid,
      'whoscored': whoscored_match
    }
    matches_collection.insert_one(match)


    bets_collection = db['bets']
    bets_match = {
      'match_uuid': match_uuid,
      'bets': []
    }
    bets_collection.insert_one(bets_match)


def _update_with_whoscored_match(match_uuid, whoscored_match):
    matches_collection = db['matches']
    matches_collection.update_one({ 'match_uuid': match_uuid }, { '$set': { 'whoscored': whoscored_match } }, upsert=True)


def _update_with_betarch_or_betcity_match(match_uuid, betcity_match):
    match_header = get_match_header(match_uuid)
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
            bets_dict[bet_pattern_tuple]['ground_truth'] = check_bet(bet, whoscored_match=whoscored_match, match_uuid=match_uuid)

    bets = list(bets_dict.values())

    bets_collection = db['bets']
    bets_collection.update_one({ 'match_uuid': match_uuid }, { '$set': { 'bets': bets } }, upsert=True)


def _incorporate_whoscored_files():
    whoscored_glob_path = os.path.join('tmp', 'update', 'whoscored', 'matchesJson', '*', '*.json')
    whoscored_file_paths = glob.glob(whoscored_glob_path)

    bar = tqdm.tqdm(whoscored_file_paths)
    for whoscored_file_path in bar:
        bar.write('Processing file %s...' % (whoscored_file_path,))

        with open(whoscored_file_path, 'rt', encoding='utf-8') as f:
            whoscored_match = json.load(f)

        match_uuid = get_match_uuid_by_whoscored_match(whoscored_match)
        if match_uuid is not None:
            _update_with_whoscored_match(match_uuid, whoscored_match)
        else:
            _create_match(whoscored_match)


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
            _update_with_betarch_or_betcity_match(match_uuid, betcity_match)


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
            _update_with_betarch_or_betcity_match(match_uuid, betarch_match)


def _incorporate():
    _incorporate_whoscored_files()
    _incorporate_betarch_files()
    _incorporate_betcity_files()


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _incorporate()
