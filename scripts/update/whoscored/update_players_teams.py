#!/usr/bin/env python3


import pymongo
import tqdm
import pandas as pd
import datetime
import argparse
from betrobot.util.database_util import db
from betrobot.util.common_util import get_value, eve_datetime
from betrobot.betting.sport_util import teams_data, players_data, save_players_data


def _update_players_teams():
    global players_data

    players = {}

    sample = db['match_headers'].find({ 'date': { '$gte': datetime.datetime(2014, 1, 1) } }).sort([ ('date', pymongo.ASCENDING) ])
    for match_header in tqdm.tqdm(sample, total=sample.count()):
        home = match_header['home']
        home_id = get_value(teams_data, 'whoscoredName', home, 'whoscoredId')
        away = match_header['away']
        away_id = get_value(teams_data, 'whoscoredName', away, 'whoscoredId')

        additional_info = db['additional_info'].find_one({ 'match_uuid': match_header['uuid'] })
        if 'homePlayers' in additional_info:
           for player_data in additional_info['homePlayers']:
               player_id = player_data['playerId']
               players[player_id] = (home_id, home)

        if 'awayPlayers' in additional_info:
           for player_data in additional_info['awayPlayers']:
               player_id = player_data['playerId']
               players[player_id] = (away_id, away)

    for player_id in players:
        players_data.loc[player_id, 'whoscoredId'] = players[player_id][0]
        players_data.loc[player_id, 'whoscoredName'] = players[player_id][1]

    save_players_data()


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _update_players_teams()
