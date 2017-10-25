import numpy as np
import pandas as pd
from collections import Counter
from betrobot.betting.predictor import Predictor
from betrobot.betting.predictors.attack_defense_results_result_predictor import AttackDefenseResultsResultPredictor
from betrobot.betting.sport_util import get_bets_match, get_substatistic, filter_bets


# TODO: Сделать универсальным
class StohasticProcessPredictor(Predictor):

    def __init__(self, **kwargs):
        super().__init__()

        self._corners_first_period_while_home_winning_results_result_predictor = AttackDefenseResultsResultPredictor(**kwargs)
        self._corners_first_period_while_away_winning_results_result_predictor = AttackDefenseResultsResultPredictor(**kwargs)
        self._corners_first_period_while_draw_results_result_predictor = AttackDefenseResultsResultPredictor(**kwargs)


    def _predict(self, fitteds, match_header, **kwargs):
        [ corners_first_period_while_home_winning_statistic_fitted, tournament_first_period_while_home_winning_counts_means_fitted, corners_first_period_while_away_winning_statistic_fitted, tournament_first_period_while_away_winning_counts_means_fitted, corners_first_period_while_draw_statistic_fitted, tournament_first_period_while_draw_counts_means_fitted, goals_game_situation_durations_statistic_fitted, goals_frequencies_by_tournament_and_minute_data_fitted ] = fitteds


        match_uuid = match_header['uuid']
        bets = get_bets_match(match_uuid)['bets']

        first_period_result_1_pattern = (None, 'Исход', '1-й тайм', '1')
        first_period_result_1_bets = filter_bets([ first_period_result_1_pattern ], bets)
        if len(first_period_result_1_bets) == 0:
            return None
        first_period_result_1_bet = first_period_result_1_bets[0]
        first_period_result_1_value = first_period_result_1_bet['value']

        first_period_result_2_pattern = (None, 'Исход', '1-й тайм', '2')
        first_period_result_2_bets = filter_bets([ first_period_result_2_pattern ], bets)
        if len(first_period_result_2_bets) == 0:
            return None
        first_period_result_2_bet = first_period_result_2_bets[0]
        first_period_result_2_value = first_period_result_2_bet['value']

        first_period_result_X_pattern = (None, 'Исход', '1-й тайм', 'X')
        first_period_result_X_bets = filter_bets([ first_period_result_X_pattern ], bets)
        if len(first_period_result_X_bets) == 0:
            return None
        first_period_result_X_bet = first_period_result_X_bets[0]
        first_period_result_X_value = first_period_result_X_bet['value']

        probabilities_sum = 1 / first_period_result_1_value + 1 / first_period_result_2_value + 1 / first_period_result_X_value
        normed_first_period_result_1_probability = 1 / first_period_result_1_value / probabilities_sum
        normed_first_period_result_2_probability = 1 / first_period_result_2_value / probabilities_sum
        normed_first_period_result_X_probability = 1 / first_period_result_X_value / probabilities_sum

        result_probabilities = np.array([ normed_first_period_result_1_probability, normed_first_period_result_2_probability, normed_first_period_result_X_probability ])


        corners_first_period_while_home_winning_prediction = self._corners_first_period_while_home_winning_results_result_predictor.predict([ corners_first_period_while_home_winning_statistic_fitted, tournament_first_period_while_home_winning_counts_means_fitted ], match_header, **kwargs)
        if corners_first_period_while_home_winning_prediction is None:
            return None
        corners_first_period_while_away_winning_prediction = self._corners_first_period_while_away_winning_results_result_predictor.predict([ corners_first_period_while_away_winning_statistic_fitted, tournament_first_period_while_away_winning_counts_means_fitted ], match_header, **kwargs)
        if corners_first_period_while_away_winning_prediction is None:
            return None
        corners_first_period_while_draw_prediction = self._corners_first_period_while_draw_results_result_predictor.predict([ corners_first_period_while_draw_statistic_fitted, tournament_first_period_while_draw_counts_means_fitted ], match_header, **kwargs)
        if corners_first_period_while_draw_prediction is None:
            return None


        tournament_id = match_header['tournamentId']

        home_corners_counts = np.zeros(100)
        away_corners_counts = np.zeros(100)
        for i in range(100):

            game_situation = 2
            for minute in range(45):
                if game_situation == 2 and (tournament_id, minute) in goals_frequencies_by_tournament_and_minute_data_fitted.data.index.tolist():
                    minute_probabilities = np.array([
                        goals_frequencies_by_tournament_and_minute_data_fitted.data.at[(tournament_id, minute), 'home_frequency'],
                        goals_frequencies_by_tournament_and_minute_data_fitted.data.at[(tournament_id, minute), 'away_frequency'],
                        1 - (goals_frequencies_by_tournament_and_minute_data_fitted.data.at[(tournament_id, minute), 'home_frequency'] + goals_frequencies_by_tournament_and_minute_data_fitted.data.at[(tournament_id, minute), 'away_frequency'])
                    ])
                    probabilities = result_probabilities * minute_probabilities
                    probabilities /= probabilities.sum()

                    game_situation = np.random.choice((0, 1, 2), p=probabilities)

                if game_situation == 0:
                    home_corners_counts[i] += corners_first_period_while_home_winning_prediction[0] / goals_game_situation_durations_statistic_fitted.statistic['home_winning_duration'].mean()
                    away_corners_counts[i] += corners_first_period_while_home_winning_prediction[1] / goals_game_situation_durations_statistic_fitted.statistic['home_winning_duration'].mean()
                elif game_situation == 1:
                    home_corners_counts[i] += corners_first_period_while_away_winning_prediction[0] / goals_game_situation_durations_statistic_fitted.statistic['away_winning_duration'].mean()
                    away_corners_counts[i] += corners_first_period_while_away_winning_prediction[1] / goals_game_situation_durations_statistic_fitted.statistic['away_winning_duration'].mean()
                elif game_situation == 2:
                    home_corners_counts[i] += corners_first_period_while_draw_prediction[0] / goals_game_situation_durations_statistic_fitted.statistic['draw_duration'].mean()
                    away_corners_counts[i] += corners_first_period_while_draw_prediction[1] / goals_game_situation_durations_statistic_fitted.statistic['draw_duration'].mean()

        home_corners_prediction = home_corners_counts.mean()
        away_corners_prediction = away_corners_counts.mean()
        prediction = (home_corners_prediction, away_corners_prediction)

        return prediction


    def _get_runtime_strs(self):
        return [
            '_corners_first_period_while_home_winning_results_result_predictor=%s' % (str(self._corners_first_period_while_home_winning_results_result_predictor),),
            '_corners_first_period_while_away_winning_results_result_predictor=%s' % (str(self._corners_first_period_while_away_winning_results_result_predictor),),
            '_corners_first_period_while_draw_results_result_predictor=%s' % (str(self._corners_first_period_while_draw_results_result_predictor),),
        ]
