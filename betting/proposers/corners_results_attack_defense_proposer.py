import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./betting/proposers')


from proposer import Proposer
from betting_session import BettingSession
from sport_util import is_betarch_match_corner


# TODO: Необходим класс CornersResultsProposer?
class CornersResultsAttackDefenseProposer(Proposer):
    def __init__(self, thresholds=None):
        betting_sessions = [ BettingSession(name='1'), BettingSession(name='1X'), BettingSession(name='X2'), BettingSession(name='2') ]
        Proposer.__init__(self, betting_sessions, thresholds)


    # TODO: Изменить (т.к. вероятность)
    def handle(self, betcity_match, prediction, whoscored_match=None):
        if prediction is None:
            return

        if not is_betarch_match_corner(betcity_match):
            return

        (corners_predicted_home, corners_predicted_away) = prediction

        # Делаем ставку на победу на победу хозяев, если предсказанный тотал хозяев превышает предсказанный тотал гостей хотя бы на 2
        if corners_predicted_home - corners_predicted_away >= 2:
            bet_pattern = ('УГЛ', 'Исход', '', '1', None)
            self._propose(bet_pattern, betcity_match, session_key='1', whoscored_match=whoscored_match)

        # Делаем ставку на победу на победу хозяев или ничью, если предсказанный тотал хозяев превышает предсказанный тотал гостей хотя бы на 1
        if corners_predicted_home - corners_predicted_away >= 1:
            bet_pattern = ('УГЛ', 'Исход', '', '1X', None)
            self._propose(bet_pattern, betcity_match, session_key='1X', whoscored_match=whoscored_match)

        # Делаем ставку на победу на победу гостей или ничью, если предсказанный тотал гостей превышает предсказанный тотал хозяев хотя бы на 1
        if corners_predicted_home - corners_predicted_away <= -1:
            bet_pattern = ('УГЛ', 'Исход', '', 'X2', None)
            self._propose(bet_pattern, betcity_match, session_key='X2', whoscored_match=whoscored_match)

        # Делаем ставку на победу на победу гостей, если предсказанный тотал гостей превышает предсказанный тотал хозяев хотя бы на 2
        if corners_predicted_home - corners_predicted_away <= -2:
            bet_pattern = ('УГЛ', 'Исход', '', '2', None)
            self._propose(bet_pattern, betcity_match, session_key='2', whoscored_match=whoscored_match)
