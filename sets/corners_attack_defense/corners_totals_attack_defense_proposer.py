import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./sets/attack_defense')
sys.path.append('./sets/corners_attack_defense')

import numpy as np
from common_util import safe_get
from sport_util import get_bet, is_betarch_match_corner
from check_util import check_bet
from teams_pair_and_tournament_based_proposer import TeamsPairAndTournamentBasedProposer
from betting_session import BettingSession


class CornersTotalsAttackDefenseProposer(TeamsPairAndTournamentBasedProposer):

    def __init__(self, betting_sessions=None, model_name_pattern='corners-attack_defense-%d'):
        if betting_sessions is None:
            betting_sessions = [ BettingSession(name='Бол'), BettingSession(name='Мен') ]

        TeamsPairAndTournamentBasedProposer.__init__(self, betting_sessions, model_name_pattern)


    def propose(self, betcity_match, whoscored_match=None, tresholds=None):
        if not is_betarch_match_corner(betcity_match):
            return

        prediction = self._predict(betcity_match)
        if prediction is None:
            return
        # Наиболее вероятные индивидуальные тоталы
        (corners_predicted_home, corners_predicted_away) = prediction 
        corners_predicted = corners_predicted_home + corners_predicted_away
    
        # Делаем ставки "Тотал угловых больше `j`", где `j = corners_predicted_total+1..+np.inf`
        for j in np.arange(0.5, corners_predicted-1+0.5, 0.5):
            bet_pattern = ('УГЛ', 'Тотал', '', 'Бол', j)
            bet = get_bet(bet_pattern, betcity_match)
            if bet is None:
                bet_pattern = ('УГЛ', 'Дополнительные тоталы', '', 'Бол', j)
                bet = get_bet(bet_pattern, betcity_match)
            ground_truth = check_bet(bet, 'УГЛ', whoscored_match)
            self._propose(bet, ground_truth, betcity_match, session_key='Бол', treshold=safe_get(tresholds, 'Бол'))
    
        # Делаем ставки "Тотал угловых меньше `j`", где `j = 0..corners_predicted_total-1`
        for j in np.arange(corners_predicted+1, 20.5, 0.5):
            bet_pattern = ('УГЛ', 'Тотал', '', 'Мен', j)
            bet = get_bet(bet_pattern, betcity_match)
            if bet is None:
                bet_pattern = ('УГЛ', 'Дополнительные тоталы', '', 'Мен', j)
                bet = get_bet(bet_pattern, betcity_match)
            ground_truth = check_bet(bet, 'УГЛ', whoscored_match)
            self._propose(bet, ground_truth, betcity_match, session_key='Мен', treshold=safe_get(tresholds, 'Мен'))
