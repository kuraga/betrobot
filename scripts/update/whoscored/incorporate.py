#!/usr/bin/env python3


import os
import glob
import json
import pandas as pd
import tqdm
import argparse
from betrobot.util.common_util import get_identifier, get_value
from betrobot.util.database_util import db
from betrobot.util.cache_util import cache_clear
from betrobot.betting.bets_checking import check_bet
from betrobot.betting.sport_util import get_extended_info, get_match_uuid_by_whoscored_match, dateize, players_data, save_players_data, get_match_header, get_bets_match, teams_data


def _clear_match_cache(match_uuid):
    cache_clear(namespace=match_uuid)


def _create_player_if_neccessary(whoscored_player_id, whoscored_player_name, team):
    if whoscored_player_id not in players_data['whoscoredPlayerId'].values:
      print('Creating player %u (%s)...' % (whoscored_player_id, whoscored_player_name))

      players_data.loc[whoscored_player_id] = pd.Series({
        'whoscoredPlayerId': whoscored_player_id,
        'whoscoredPlayerName': whoscored_player_name,
        'intelbetPlayerName': None,
        'whoscoredName': team,
        'whoscoredId': get_value(teams_data, 'whoscoredName', team, 'whoscoredId')
      })

      save_players_data()


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


def _create_players_with_additional_info(match_uuid, additional_info):
    match_header = get_match_header(match_uuid)

    if 'homePlayers' in additional_info:
       for home_player_data in additional_info['homePlayers']:
         _create_player_if_neccessary(home_player_data['playerId'], home_player_data['playerName'], match_header['home'])
    if 'awayPlayers' in additional_info:
       for away_player_data in additional_info['awayPlayers']:
         _create_player_if_neccessary(away_player_data['playerId'], away_player_data['playerName'], match_header['away'])


def _update_bets_whoscored_match(match_uuid, whoscored_match):
    if 'matchCentreData' not in whoscored_match:
        return

    bets_match = get_bets_match(match_uuid)

    for i in range(len(bets_match['bets'])):
        bets_match['bets'][i]['ground_truth'] = check_bet(bets_match['bets'][i], whoscored_match=whoscored_match)

    bets_collection = db['bets']
    bets_collection.update_one({ 'match_uuid': match_uuid }, { '$set': { 'bets': bets_match['bets'] } })


# WARNING: Необходимо создавать матч (с Whoscored-матчем) перед его дополнением
def _create_match(whoscored_match):
    match_uuid = get_identifier()

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


    _create_players_with_additional_info(match_uuid, additional_info)


def _update_with_whoscored_match(match_uuid, whoscored_match):
    _clear_match_cache(match_uuid)

    matches_collection = db['matches']
    matches_collection.update_one({ 'match_uuid': match_uuid }, { '$set': { 'whoscored': whoscored_match } })

    _update_bets_whoscored_match(match_uuid, whoscored_match)

    new_additional_info = _get_additional_info_of_whoscored_match(whoscored_match)
    if len(new_additional_info) > 0:
        additional_info_collection = db['additional_info']
        additional_info_collection.update_one({ 'match_uuid': match_uuid }, { '$set': new_additional_info })

    _create_players_with_additional_info(match_uuid, new_additional_info)


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
