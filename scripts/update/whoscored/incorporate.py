#!/usr/bin/env python3


import os
import glob
import json
import uuid
import tqdm
import argparse
from betrobot.util.database_util import db
from betrobot.util.cache_util import cache_clear
from betrobot.betting.sport_util import get_extended_info, get_match_uuid_by_whoscored_match, dateize


def _clear_match_cache(match_uuid):
    cache_clear(namespace=match_uuid)


def _get_additional_info_of_whoscored_match(whoscored_match):
    additional_info = {}

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

    return additional_info


# WARNING: Необходимо создавать матч (с Whoscored-матчем) перед его дополнением
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
    additional_info.update( _get_additional_info_of_whoscored_match(whoscored_match) )
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
    _clear_match_cache(match_uuid)
    # FIXME: Пересчитывать исходы ставок

    matches_collection = db['matches']
    matches_collection.update_one({ 'match_uuid': match_uuid }, { '$set': { 'whoscored': whoscored_match } })

    new_additional_info = _get_additional_info_of_whoscored_match(whoscored_match)
    if len(new_additional_info) > 0:
        additional_info_collection = db['additional_info']
        additional_info_collection.update_one({ 'match_uuid': match_uuid }, { '$set': new_additional_info })


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


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _incorporate_whoscored_files()
