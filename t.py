import sys
sys.path.append('./')
sys.path.append('./util')


from sport_util import bet_satisfy
import pymongo
import numpy as np


client = pymongo.MongoClient()
db = client['betrobot']
proposed = db['proposed']


proposed.remove({ 'express': True })

corners_first_period_result_1_bets = []
for proposed_bet_data in proposed.find():
    if proposed_bet_data['match_special_word'] != 'УГЛ': continue
    bet_pattern = (None, 'Исходы по таймам (1-й тайм)', '', '1', None)
    if bet_satisfy(bet_pattern, proposed_bet_data['bet']):
        corners_first_period_result_1_bets.append(proposed_bet_data)

goals_second_period_result_X2_bets = []
for proposed_bet_data in proposed.find():
    if proposed_bet_data['match_special_word'] is not None: continue
    bet_pattern = (None, 'Исходы по таймам (2-й тайм)', '', 'X2', None)
    if bet_satisfy(bet_pattern, proposed_bet_data['bet']):
        goals_second_period_result_X2_bets.append(proposed_bet_data)

new_bets_data = []
for bet_data in corners_first_period_result_1_bets:
    for another_bet_data in goals_second_period_result_X2_bets:
        if bet_data['date'] == another_bet_data['date'] and bet_data['home'] == another_bet_data['home'] and bet_data['away'] == another_bet_data['away']:
            new_bet_data = {
                'match_uuid': '%s & %s' % (bet_data['match_uuid'], another_bet_data['match_uuid']),
                'tournament': '%s & %s' % (bet_data['tournament'], another_bet_data['tournament']),
                'date': bet_data['date'],
                'home': bet_data['home'],
                'away': bet_data['away'],
                'match_special_word': '%s & %s' % (bet_data['match_special_word'], another_bet_data['match_special_word']),
                'bet': (bet_data['bet'], another_bet_data['bet']),
                'bet_value': np.round(bet_data['bet_value'] * another_bet_data['bet_value'], 2),
                'ground_truth': bet_data['ground_truth'] & another_bet_data['ground_truth'] if bet_data['ground_truth'] is not None and another_bet_data['ground_truth'] is not None else None,
                'express': True
            }
            new_bets_data.append(new_bet_data)

proposed.insert(new_bets_data)
