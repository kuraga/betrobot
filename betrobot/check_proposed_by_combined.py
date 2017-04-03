import os
import json
import glob
import pymongo
import datetime
from betrobot.util.check_util import check_bet


client = pymongo.MongoClient()
db = client['betrobot']
proposed_collection = db['proposed']
matches_collection = db['matchesCleaned']


unchecked_bets = proposed_collection.find({ 'ground_truth': None })
for bet in unchecked_bets:
    date_str = bet['date'].strftime('%Y-%m-%d')
    print('%s - %s vs %s' % (date_str, bet['home'], bet['away']))

    match_data = matches_collection.find_one({ 'date': date_str, 'home': bet['home'], 'away': bet['away'] })
    if match_data is None:
        continue
    whoscord_match = match_data['whoscored'][0]

    ground_truth = check_bet(bet['bet_pattern'], bet['match_special_word'], whoscored_match)
    if ground_truth is not None:
        proposed_collection.update_one({ '_id': bet['_id'] }, { '$set': { 'ground_truth': ground_truth }})

