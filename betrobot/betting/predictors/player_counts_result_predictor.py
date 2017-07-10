import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.betting.sport_util import get_teams_tournaments_countries_value
from betrobot.util.math_util import get_weights_array


class PlayerCountsResultPredictor(Predictor):

    _pick = [ 'weights' ]


    def __init__(self, weights=None):
        super().__init__()

        self.weights = weights


    def _predict(self, fitteds, betcity_match, whoscored_match, **kwargs):
        [ player_counts_fitted ] = fitteds

        home_player_names = [ player['name'] for player in whoscored_match['matchCentreData']['home']['players'] if player.get('isFirstEleven', False) ]
        away_player_names = [ player['name'] for player in whoscored_match['matchCentreData']['away']['players'] if player.get('isFirstEleven', False) ]

        events_home_counts_mean = 0
        for player_name in home_player_names:
            player_statistic = player_counts_fitted.statistic.loc[ player_counts_fitted.statistic[player_name].notnull() ]
            weights_full = get_weights_array(player_statistic.shape[0], self.weights)
            events_home_counts_mean += np.sum(player_statistic[player_name] * weights_full)

        events_away_counts_mean = 0
        for player_name in away_player_names:
            player_statistic = player_counts_fitted.statistic.loc[ player_counts_fitted.statistic[player_name].notnull() ]
            weights_full = get_weights_array(player_statistic.shape[0], self.weights)
            events_away_counts_mean += np.sum(player_statistic[player_name] * weights_full)

        result_prediction = (events_home_counts_mean, events_away_counts_mean)

        return result_prediction


    def _get_init_strs(self):
        result = []
        if self.weights is not None:
            strs.append( 'weights=[%s]' % (str(', '.join(map(str, self.weights))),) )
        return result
