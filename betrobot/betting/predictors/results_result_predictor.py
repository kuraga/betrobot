import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.betting.sport_util import get_substatistic
from betrobot.util.math_util import get_weights_array


class ResultsResultPredictor(Predictor):

    _pick = [ 'home_weights', 'away_weights' ]

 
    def __init__(self, home_weights=None, away_weights=None):
        super().__init__()

        self.home_weights = home_weights
        self.away_weights = away_weights


    def _predict(self, fitteds, match_header, **kwargs):
        [ statistic_fitted ] = fitteds

        statistic = statistic_fitted.statistic
        if statistic.shape[0] == 0:
            return None

        # Статистика матчей, где match_header['home'] тоже была хозяйкой
        events_home_counts = get_substatistic(statistic, notnull='events_home_count', by='home', value=match_header['home'], n=3, sort_by='date', ascending=False, which='events_home_count')
        if events_home_counts is None:
            return None
        # Статистика матчей, где match_header['away'] тоже была гостьей
        events_away_counts = get_substatistic(statistic, notnull='events_away_count', by='away', value=match_header['away'], n=3, sort_by='date', ascending=False, which='events_away_count')
        if events_away_counts is None:
            return None

        home_weights_full = get_weights_array(events_home_counts.size, self.home_weights)
        events_home_counts_mean = np.sum(events_home_counts * home_weights_full)
        away_weights_full = get_weights_array(events_away_counts.size, self.away_weights)
        events_away_counts_mean = np.sum(events_away_counts * away_weights_full)

        result_prediction = (events_home_counts_mean, events_away_counts_mean)

        return result_prediction


    def _get_init_strs(self):
        result = []

        if self.home_weights is not None:
            strs.append( 'home_weights=[%s]' % (str(', '.join(map(str, self.home_weights))),) )
        if self.away_weights is not None:
            strs.append( 'away_weights=[%s]' % (str(', '.join(map(str, self.away_weights))),) )

        return result
