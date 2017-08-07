import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.betting.sport_util import get_additional_info, get_substatistic
from betrobot.util.math_util import get_weights_array


class PlayerCountsResultPredictor(Predictor):

    _pick = [ 'n', 'weights', 'min_n' ]

 
    def __init__(self, n=None, weights=None, min_n=None):
        super().__init__()

        self.n = n
        self.weights = weights
        self.min_n = n


    def _predict(self, fitteds, match_header, **kwargs):
        [ statistic_fitted ] = fitteds

        statistic = statistic_fitted.statistic
        if statistic.shape[0] == 0:
            return None

        additional_info = get_additional_info(match_header['uuid'])
        if additional_info is None:
            return None
        if 'homePlayers' not in additional_info or 'awayPlayers' not in additional_info:
            return None

        home_player_names = [ player['playerName'] for player in additional_info['homePlayers'] if player['isFirstEleven'] ]
        away_player_names = [ player['playerName'] for player in additional_info['awayPlayers'] if player['isFirstEleven'] ]

        events_home_counts_mean = 0
        for player_name in (frozenset(statistic_fitted.statistic.columns.values) & frozenset(home_player_names)):
            events_player_counts = get_substatistic(statistic, n=self.n, sort_by='date', ascending=False, which=player_name, notnull=player_name)
            if events_player_counts is None:
                continue

            weights_full = get_weights_array(events_player_counts.shape[0], self.weights)
            events_home_counts_mean += np.sum(events_player_counts * weights_full)

        events_away_counts_mean = 0
        for player_name in (frozenset(statistic_fitted.statistic.columns.values) & frozenset(away_player_names)):
            events_player_counts = get_substatistic(statistic, n=self.n, sort_by='date', ascending=False, which=player_name, notnull=player_name)
            if events_player_counts is None:
                continue

            weights_full = get_weights_array(events_player_counts.shape[0], self.weights)
            events_away_counts_mean += np.sum(events_player_counts * weights_full)

        result_prediction = (events_home_counts_mean, events_away_counts_mean)

        return result_prediction


    def _get_init_strs(self):
        result = []

        if self.n is not None:
            result.append( 'n=[%u]' % (n,) )
        if self.weights is not None:
            result.append( 'weights=[%s]' % (str(', '.join(map(str, self.weights))),) )
        if self.min_n is not None:
            result.append( 'min_n=[%u]' % (min_n,) )

        return result
