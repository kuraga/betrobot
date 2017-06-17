import os
import json
import glob
import pymongo
import datetime
from betrobot.util.sport_util import get_betcity_teams_of_whoscored_match
from betrobot.util.check_util import check_bet


client = pymongo.MongoClient()
db = client['betrobot']
proposed_collection = db['proposed']


def check_whoscored_match(whoscored_match, proposed_collection):
    whoscored_match_date = datetime.datetime.strptime(whoscored_match['date'], '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0)

    home_betcity = get_teams_tournaments_countries_data('whoscoredName', whoscored_match['home'], 'betcityName')
    away_betcity = get_teams_tournaments_countries_data('whoscoredName', whoscored_match['away'], 'betcityName')
    if home_betcity is None or away_betcity is None:
        return

    bets = proposed_collection.find({ 'date': whoscored_match_date, 'home': home_betcity, 'away': away_betcity, 'ground_truth': None })

    for bet in bets:
        ground_truth = check_bet(bet['bet_pattern'], bet['match_special_word'], whoscored_match)
        if ground_truth is not None:
            proposed_collection.update_one({ '_id': bet['_id'] }, { '$set': { 'ground_truth': ground_truth }})


unchecked_bets = proposed_collection.find({ 'ground_truth': None })
dates = set([ bet['date'] for bet in unchecked_bets ])

for date_ in dates:
    date_str = date_.strftime('%Y-%m-%d')
    glob_path = os.path.join('data', 'whoscored', 'matchesJson', date_str, '*.json')
    for file_path in glob.iglob(glob_path):
        print(file_path)

        with open(file_path, 'rt', encoding='utf-8') as f:
            whoscored_match = json.load(f)

        check_whoscored_match(whoscored_match, proposed_collection)
