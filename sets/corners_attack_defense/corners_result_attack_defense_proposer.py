import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./sets/attack_defense')
sys.path.append('./sets/corners_attack_defense')

from common_util import safe_get
from sport_util import get_bet, is_betarch_match_corner
from check_util import check_bet
from teams_pair_and_tournament_based_proposer import TeamsPairAndTournnamentBasedProposer
from betting_session import BettingSession


class CornersResultAttackDefenseProposer(TeamsPairAndTournnamentBasedProposer):

    def __init__(self, betting_sessions=None, model_name_pattern='corners-attack_defense-%d'):
        if betting_sessions is None:
            betting_sessions = [ BettingSession(name='1'), BettingSession(name='1X'), BettingSession(name='X2'), BettingSession(name='2') ]

        TeamsPairAndTournnamentBasedProposer.__init__(self, betting_sessions, model_name_pattern)


    def propose(self, betcity_match, whoscored_match=None, tresholds=None):
        if not is_betarch_match_corner(betcity_match):
            return

        prediction = self._predict(betcity_match)
        if prediction is None:
            return
        # Наиболее вероятные индивидуальные тоталы
        (corners_predicted_home, corners_predicted_away) = prediction 

        # Делаем ставку на победу на победу хозяев, если предсказанный тотал хозяев превышает предсказанный тотал гостей хотя бы на 2
        if corners_predicted_home - corners_predicted_away >= 2:
            bet_pattern = ('УГЛ', 'Исход', '', '1', None)
            bet = get_bet(bet_pattern, betcity_match)
            ground_truth = check_bet(bet, 'УГЛ', whoscored_match)
            self._propose(bet, ground_truth, betcity_match, session_key='1', treshold=safe_get(tresholds, '1'))

        # Делаем ставку на победу на победу хозяев или ничью, если предсказанный тотал хозяев превышает предсказанный тотал гостей хотя бы на 1
        if corners_predicted_home - corners_predicted_away >= 1:
            bet_pattern = ('УГЛ', 'Исход', '', '1X', None)
            bet = get_bet(bet_pattern, betcity_match)
            ground_truth = check_bet(bet, 'УГЛ', whoscored_match)
            self._propose(bet, ground_truth, betcity_match, session_key='1X', treshold=safe_get(tresholds, '1X'))

        # Делаем ставку на победу на победу гостей или ничью, если предсказанный тотал гостей превышает предсказанный тотал хозяев хотя бы на 1
        if corners_predicted_home - corners_predicted_away <= -1:
            bet_pattern = ('УГЛ', 'Исход', '', 'X2', None)
            bet = get_bet(bet_pattern, betcity_match)
            ground_truth = check_bet(bet, 'УГЛ', whoscored_match)
            self._propose(bet, ground_truth, betcity_match, session_key='X2', treshold=safe_get(tresholds, 'X2'))

        # Делаем ставку на победу на победу гостей, если предсказанный тотал гостей превышает предсказанный тотал хозяев хотя бы на 2
        if corners_predicted_home - corners_predicted_away <= -2:
            bet_pattern = ('УГЛ', 'Исход', '', '2', None)
            bet = get_bet(bet_pattern, betcity_match)
            ground_truth = check_bet(bet, 'УГЛ', whoscored_match)
            self._propose(bet, ground_truth, betcity_match, session_key='2', treshold=safe_get(tresholds, '2'))
