import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./sets/attack_defense')
sys.path.append('./sets/corners_attack_defense')

import numpy as np
from common_util import safe_get
from sport_util import is_betarch_match_corner, count_events_of_teams, is_corner
from teams_pair_and_tournament_based_proposer import TeamsPairAndTournnamentBasedProposer
from betting_session import BettingSession


class CornersTotalsAttackDefenseProposer(TeamsPairAndTournnamentBasedProposer):

    def __init__(self, betting_sessions=None, model_name_pattern='corners-attack_defense-%d'):
        if betting_sessions is None:
            betting_sessions = [ BettingSession(name='Бол'), BettingSession(name='Мен') ]

        TeamsPairAndTournnamentBasedProposer.__init__(self, betting_sessions, model_name_pattern)


    def propose(self, betcity_match, whoscored_match=None, tresholds=None):
        if not is_betarch_match_corner(betcity_match):
            return

        prediction = self._predict(betcity_match)
        if prediction is None:
            return
        # Наиболее вероятные индивидуальные тоталы
        (corners_predicted_home, corners_predicted_away) = prediction 
        corners_predicted = corners_predicted_home + corners_predicted_away
    
        if whoscored_match is not None:
            (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
            corners_count = corners_home_count + corners_away_count

        # Делаем ставки "Тотал угловых меньше `j`", где `j = 0..corners_predicted_total-1`
        for j in np.arange(0.5, corners_predicted-1+0.5, 0.5):
            if whoscored_match is not None:
                ground_truth = corners_count > j
            else:
                ground_truth = None
    
            bet_pattern = (None, 'Тотал', None, 'Бол', j)
            self._propose_pattern(bet_pattern, betcity_match, ground_truth, session_key='Бол', treshold=safe_get(tresholds, 'Бол'))
            
            bet_pattern = (None, 'Дополнительные тоталы', None, 'Бол', j)
            self._propose_pattern(bet_pattern, betcity_match, ground_truth, session_key='Бол', treshold=safe_get(tresholds, 'Бол'))
    
        # Делаем ставки "Тотал угловых больше `j`", где `j = corners_predicted_total+1..+np.inf`
        for j in np.arange(corners_predicted+1, 20.5, 0.5):
            if whoscored_match is not None:
                ground_truth = corners_count < j
            else:
                ground_truth = None
    
            bet_pattern = (None, 'Тотал', None, 'Мен', j)
            self._propose_pattern(bet_pattern, betcity_match, ground_truth, session_key='Мен', treshold=safe_get(tresholds, 'Мен'))
            
            bet_pattern = (None, 'Дополнительные тоталы', None, 'Мен', j)
            self._propose_pattern(bet_pattern, betcity_match, ground_truth, session_key='Мен', treshold=safe_get(tresholds, 'Мен'))
