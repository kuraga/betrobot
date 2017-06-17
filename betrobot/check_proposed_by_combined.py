import os
import json
import glob
import pymongo
import datetime
from betrobot.util.sport_util import get_teams_tournaments_countries_data
from betrobot.util.check_util import check_bet


client = pymongo.MongoClient()
db = client['betrobot']
proposed_collection = db['proposed']
matches_collection = db['matches']


# TODO: def check_bet(bet, proposed_collection):


unchecked_bets = proposed_collection.find({ 'ground_truth': None })

for bet in unchecked_bets:
    date_str = bet['date'].strftime('%Y-%m-%d')
    print('%s - %s vs %s' % (date_str, bet['home'], bet['away']))

    whoscored_home = get_teams_tournaments_countries_data('betcityName', bet['home'], 'whoscoredName')
    whoscored_away = get_teams_tournaments_countries_data('betcityName', bet['away'], 'whoscoredName')
    if whoscored_home is None or whoscored_away is None:
        return None

    match_data = matches_collection.find_one({ 'date': date_str, 'home': home_whoscored, 'away': away_whoscored })
    if match_data is None:
        continue
    whoscored_match = match_data['whoscored'][0]

    ground_truth = check_bet(bet['bet_pattern'], bet['match_special_word'], whoscored_match)
    if ground_truth is not None:
        proposed_collection.update_one({ '_id': bet['_id'] }, { '$set': { 'ground_truth': ground_truth }})

