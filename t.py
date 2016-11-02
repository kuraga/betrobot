import sys
sys.path.append('./')
sys.path.append('./util')


from sport_util import bet_satisfy
import pymongo


client = pymongo.MongoClient()
db = client['betrobot']
proposed = db['proposed']


proposed.remove({ 'express': True })

corners_first_period_result_1_bets = []
for proposed_bet_data in proposed.find():
    if proposed_bet_data['match_special_word'] != 'УГЛ': continue
    bet_pattern = (None, 'Исходы по таймам (1-й тайм)', '', '1', None)
    if bet_satisfy(bet_pattern, proposed_bet_data['bet_pattern']):
        corners_first_period_result_1_bets.append(proposed_bet_data)

goals_second_period_result_X2_bets = []
for proposed_bet_data in proposed.find():
    if proposed_bet_data['match_special_word'] is not None: continue
    bet_pattern = (None, 'Исходы по таймам (2-й тайм)', '', 'X2', None)
    if bet_satisfy(bet_pattern, proposed_bet_data['bet_pattern']):
        goals_second_period_result_X2_bets.append(proposed_bet_data)

new_bets_data = []
for bet_data in corners_first_period_result_1_bets:
    for another_bet_data in goals_second_period_result_X2_bets:
        if bet_data['date'] == another_bet_data['date'] and bet_data['home'] == another_bet_data['home'] and bet_data['away'] == another_bet_data['away']:
            new_bet_data = {
                'express': True,
                'match_uuid': bet_data['match_uuid'],
                'match_uuid_2': another_bet_data['match_uuid'],
                'tournament': bet_data['tournament'],
                'tournament_2': another_bet_data['tournament'],
                'date': bet_data['date'],
                'home': bet_data['home'],
                'away': bet_data['away'],
                'match_special_word': bet_data['match_special_word'],
                'match_special_word_2': another_bet_data['match_special_word'],
                'bet_pattern': bet_data['bet_pattern'],
                'bet_pattern_2': another_bet_data['bet_pattern'],
                'bet_value': bet_data['bet_value'],
                'bet_value_2': another_bet_data['bet_value'],
                'ground_truth': bet_data['ground_truth'],
                'ground_truth_2': another_bet_data['ground_truth']
            }
            new_bets_data.append(new_bet_data)

proposed.insert(new_bets_data)
