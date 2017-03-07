import os
import json
import glob
import pymongo
import datetime
from util.sport_util import get_betcity_teams_of_whoscored_match
from util.check_util import check_bet


client = pymongo.MongoClient()
db = client['betrobot']
proposed = db['proposed']


def check_whoscored_match(whoscored_match, proposed):
    whoscored_match_date = datetime.datetime.strptime(whoscored_match['date'], '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0)
    (home_betcity, away_betcity) = get_betcity_teams_of_whoscored_match(whoscored_match)
    if home_betcity is None or away_betcity is None:
        return

    bets = proposed.find({ 'date': whoscored_match_date, 'home': home_betcity, 'away': away_betcity, 'ground_truth': None })

    for bet in bets:
        ground_truth = check_bet(bet['bet_pattern'], bet['match_special_word'], whoscored_match)
        if ground_truth is not None:
            proposed.update_one({ '_id': bet['_id'] }, { '$set': { 'ground_truth': ground_truth }})

dates = set()

unchecked_bets = proposed.find({ 'ground_truth': None })
for bet in unchecked_bets:
    dates.add(bet['date'])

for date_ in dates:
    date_str = date_.strftime('%Y-%m-%d')
    glob_path = os.path.join('data', 'whoscored', 'matchesJson', date_str, '*.json')
    for file_path in glob.iglob(glob_path):
        print(file_path)

        with open(file_path, 'r', encoding='utf-8') as f:
            whoscored_match = json.load(f)

        check_whoscored_match(whoscored_match, proposed)
