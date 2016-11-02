import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')

import pymongo
import pandas as pd
from betting_session import BettingSession
from proposer import Proposer


exec(sys.argv[1])
if betting_session1 is None or betting_session2 is None:
    sys.exit()


# TODO: Выделить в метод
# TODO: Контролировать, не пусты ли части
betting_session_name = betting_session1.name + ' & ' + betting_session2.name
betting_session = BettingSession(betting_session_name)
bets = pd.merge(betting_session1.bets, betting_session2.bets, on=['date', 'home', 'away'], how='inner')
for (index, bet) in bets.iterrows():
    betting_session.append_bet(
        bet['match_uuid_x'],
        bet['tournament_x'],
        bet['date'],
        bet['home'],
        bet['away'],
        bet['match_special_word_x'],
        bet['bet_pattern_x'],
        bet['bet_value_x'] * bet['bet_value_y'],
        bet['ground_truth_x'] & bet['ground_truth_y'],
        True,
        bet['match_uuid_y'],
        bet['tournament_y'],
        bet['match_special_word_y'],
        bet['bet_pattern_y']
    )

proposer = Proposer(betting_session)


for betting_session in proposer.betting_sessions.values():
    betting_session.print_investigation()
    print()
    print()

if len(sys.argv) >= 3:
    proposer_file_path = sys.argv[2]
    proposer.save(proposer_file_path)
