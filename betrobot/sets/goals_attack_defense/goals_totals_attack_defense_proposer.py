import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./sets/attack_defense')
sys.path.append('./sets/goals_attack_defense')

from common_util import safe_get
from sport_util import get_bet, is_betarch_match_main
from check_util import check_bet
from teams_pair_and_tournament_based_proposer import TeamsPairAndTournamentBasedProposer
from betting_session import BettingSession
import numpy as np


class GoalsTotalsAttackDefenseProposer(TeamsPairAndTournamentBasedProposer):

    def __init__(self, betting_sessions=None, model_name_pattern='goals-attack_defense-%d'):
        if betting_sessions is None:
            betting_sessions = [ BettingSession(name='Бол'), BettingSession(name='Мен') ]

        TeamsPairAndTournamentBasedProposer.__init__(self, betting_sessions, model_name_pattern)


    def propose(self, betcity_match, whoscored_match=None, tresholds=None):
        if not is_betarch_match_main(betcity_match):
            return

        prediction = self._predict(betcity_match)
        if prediction is None:
            return
        # Наиболее вероятные индивидуальные тоталы
        (goals_predicted_home, goals_predicted_away) = prediction 
        goals_predicted = goals_predicted_home + goals_predicted_away
    
        # Делаем ставки "Тотал угловых больше `j`", где `j = goals_predicted_total+2..+np.inf`
        for j in np.arange(0.5, goals_predicted-2+0.5, 0.5):
            bet_pattern = (None, 'Тотал', None, 'Бол', j)
            bet = get_bet(bet_pattern, betcity_match)
            if bet is None:
                bet_pattern = (None, 'Дополнительные тоталы', None, 'Бол', j)
                bet = get_bet(bet_pattern, betcity_match)
            ground_truth = check_bet(bet_pattern, None, whoscored_match)
            self._propose(bet, ground_truth, betcity_match, session_key='Бол', treshold=safe_get(tresholds, 'Бол'))
    
        # Делаем ставки "Тотал угловых меньше `j`", где `j = 0..goals_predicted_total-2`
        for j in np.arange(goals_predicted+2, 10.5, 0.5):
            bet_pattern = (None, 'Тотал', None, 'Мен', j)
            bet = get_bet(bet_pattern, betcity_match)
            if bet is None:
                bet_pattern = (None, 'Дополнительные тоталы', None, 'Мен', j)
                bet = get_bet(bet_pattern, betcity_match)
            ground_truth = check_bet(bet_pattern, None, whoscored_match)
            self._propose(bet, ground_truth, betcity_match, session_key='Мен', treshold=safe_get(tresholds, 'Мен'))
