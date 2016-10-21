import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./sets/attack_defense')
sys.path.append('./sets/goals_periods_attack_defense')

from common_util import safe_get
from sport_util import is_betarch_match_main, count_events_of_teams, is_goal, is_first_period
from teams_pair_and_tournament_based_proposer import TeamsPairAndTournnamentBasedProposer
from betting_session import BettingSession


class GoalsFirstPeriodResultAttackDefenseProposer(TeamsPairAndTournnamentBasedProposer):

    def __init__(self, betting_sessions=None, model_name_pattern='goals_first_period-attack_defense-%d'):
        if betting_sessions is None:
            betting_sessions = [ BettingSession(name='1'), BettingSession(name='1X'), BettingSession(name='X2'), BettingSession(name='2') ]

        TeamsPairAndTournnamentBasedProposer.__init__(self, betting_sessions, model_name_pattern)


    def propose(self, betcity_match, whoscored_match=None, tresholds=None):
        if not is_betarch_match_main(betcity_match):
            return

        prediction = self._predict(betcity_match)
        if prediction is None:
            return
        # Наиболее вероятные индивидуальные тоталы в первом тайме
        (goals_first_period_predicted_home, goals_first_period_predicted_away) = prediction 
    
        # Делаем ставку на победу на победу хозяев в первом тайме, если предсказанный тотал хозяева превышает предсказанный тотал гостя хотя бы на 1
        if goals_first_period_predicted_home - goals_first_period_predicted_away >= 1:
            if whoscored_match is not None:
                (goals_first_period_home_count, goals_first_period_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_first_period(event), whoscored_match)
                ground_truth = goals_first_period_home_count > goals_first_period_away_count
            else:
                ground_truth = None

            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', '', '1', None)
            self._propose_pattern(bet_pattern, betcity_match, ground_truth, session_key='1', treshold=safe_get(tresholds, '1'))

        # Делаем ставку на победу на победу хозяев или ничью в первом тайме, если предсказанный тотал хозяев хотя бы равен предсказанному тоталу гостей
        if goals_first_period_predicted_home - goals_first_period_predicted_away >= 0:
            if whoscored_match is not None:
                (goals_first_period_home_count, goals_first_period_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_first_period(event), whoscored_match)
                ground_truth = goals_first_period_home_count >= goals_first_period_away_count
            else:
                ground_truth = None

            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', '', '1X', None)
            self._propose_pattern(bet_pattern, betcity_match, ground_truth, session_key='1X', treshold=safe_get(tresholds, '1X'))

        # Делаем ставку на победу на победу гостей или ничью в первом тайме, если предсказанный тотал гостей хотя бы равен предсказанному тоталу хозяев
        if goals_first_period_predicted_home - goals_first_period_predicted_away <= 0:
            if whoscored_match is not None:
                (goals_first_period_home_count, goals_first_period_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_first_period(event), whoscored_match)
                ground_truth = goals_first_period_home_count <= goals_first_period_away_count
            else:
                ground_truth = None

            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', '', 'X2', None)
            self._propose_pattern(bet_pattern, betcity_match, ground_truth, session_key='X2', treshold=safe_get(tresholds, 'X2'))

        # Делаем ставку на победу на победу гостей в первом тайме, если предсказанный тотал гостей превышает предсказанный тотал хозяев хотя бы на 1
        if goals_first_period_predicted_home - goals_first_period_predicted_away <= -1:
            if whoscored_match is not None:
                (goals_first_period_home_count, goals_first_period_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_first_period(event), whoscored_match)
                ground_truth = goals_first_period_home_count < goals_first_period_away_count
            else:
                ground_truth = None

            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', '', '2', None)
            self._propose_pattern(bet_pattern, betcity_match, ground_truth, session_key='2', treshold=safe_get(tresholds, '2'))
