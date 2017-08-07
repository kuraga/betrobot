#!/usr/bin/env python3


import os
import glob
import json
import tqdm
import argparse
from betrobot.util.database_util import db
from betrobot.util.common_util import get_value
from betrobot.betting.sport_util import players_data, get_match_uuid_by_intelbet_match


def _get_additional_info_of_intelbet_match(intelbet_match):
    additional_info = {}

    if intelbet_match.get('homePlayerNames') is not None:
      additional_info['homePlayers'] = []
      for intelbet_player_name in intelbet_match['homePlayerNames']:
          player_name = get_value(players_data, 'intelbetPlayerName', intelbet_player_name, 'whoscoredPlayerName')
          player_id = get_value(players_data, 'intelbetPlayerName', intelbet_player_name, 'whoscoredPlayerId')
          additional_info['homePlayers'].append({
              'playerId': int(player_id) if player_id is not None else None, # FIXME
              'playerName': player_name,
              'isFirstEleven': True
          })

    if intelbet_match.get('awayPlayerNames') is not None:
      additional_info['awayPlayers'] = []
      for intelbet_player_name in intelbet_match['awayPlayerNames']:
          player_name = get_value(players_data, 'intelbetPlayerName', intelbet_player_name, 'whoscoredPlayerName')
          player_id = get_value(players_data, 'intelbetPlayerName', intelbet_player_name, 'whoscoredPlayerId')
          additional_info['awayPlayers'].append({
              'playerId': int(player_id) if player_id is not None else None, # FIXME
              'playerName': player_name,
              'isFirstEleven': True
          })

    return additional_info


def _update_with_intelbet_match(match_uuid, intelbet_match):
    additional_info_collection = db['additional_info']
    new_additional_info = _get_additional_info_of_intelbet_match(intelbet_match)
    if len(new_additional_info) > 0:
        additional_info_collection.update_one({ 'match_uuid': match_uuid }, { '$set': new_additional_info })


def _incorporate_intelbet_files():
    intelbet_glob_path = os.path.join('tmp', 'update', 'intelbet', 'matchesJson', '*', '*.json')
    intelbet_file_paths = glob.glob(intelbet_glob_path)

    bar = tqdm.tqdm(intelbet_file_paths)
    for intelbet_file_path in bar:
        bar.write('Processing file %s...' % (intelbet_file_path,))

        with open(intelbet_file_path, 'rt', encoding='utf-8') as f:
            intelbet_match = json.load(f)

        match_uuid = get_match_uuid_by_intelbet_match(intelbet_match)
        if match_uuid is not None:
            _update_with_intelbet_match(match_uuid, intelbet_match)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _incorporate_intelbet_files()
