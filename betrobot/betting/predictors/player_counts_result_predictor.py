import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.betting.sport_util import get_additional_info
from betrobot.util.math_util import get_weights_array


class PlayerCountsResultPredictor(Predictor):

    _pick = [ 'weights' ]


    def __init__(self, weights=None):
        super().__init__()

        self.weights = weights


    def _predict(self, fitteds, match_header, **kwargs):
        [ player_counts_fitted ] = fitteds

        additional_info = get_additional_info(match_header['uuid'])
        if additional_info is None:
            return None
        if 'homePlayers' not in additional_info or 'awayPlayers' not in additional_info:
            return None

        home_player_names = [ player['playerName'] for player in additional_info['homePlayers'] if player['isFirstEleven'] ]
        away_player_names = [ player['playerName'] for player in additional_info['awayPlayers'] if player['isFirstEleven'] ]

        events_home_counts_mean = 0
        for player_name in (frozenset(player_counts_fitted.statistic.columns.values) & frozenset(home_player_names)):
            player_statistic = player_counts_fitted.statistic.loc[ player_counts_fitted.statistic[player_name].notnull(), player_name ]
            weights_full = get_weights_array(player_statistic.shape[0], self.weights)
            events_home_counts_mean += np.sum(player_statistic * weights_full)

        events_away_counts_mean = 0
        for player_name in (frozenset(player_counts_fitted.statistic.columns.values) & frozenset(away_player_names)):
            player_statistic = player_counts_fitted.statistic.loc[ player_counts_fitted.statistic[player_name].notnull(), player_name ]
            weights_full = get_weights_array(player_statistic.shape[0], self.weights)
            events_away_counts_mean += np.sum(player_statistic * weights_full)

        result_prediction = (events_home_counts_mean, events_away_counts_mean)

        return result_prediction


    def _get_init_strs(self):
        result = []
        if self.weights is not None:
            strs.append( 'weights=[%s]' % (str(', '.join(map(str, self.weights))),) )
        return result
