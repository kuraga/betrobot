import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.betting.sport_util import get_teams_tournaments_countries_value
from betrobot.util.math_util import get_weights_array


class DiffsDiff2Predictor(Predictor):

    _pick = [ 'home_weights', 'away_weights', 'n', 'kappa', 'max_competitor_events_diff' ]

 
    def __init__(self, home_weights=None, away_weights=None, n=3, kappa=1.0, max_competitor_events_diff=3):
        super().__init__()

        self.home_weights = home_weights
        self.away_weights = away_weights
        self.n = n
        self.kappa = kappa
        self.max_competitor_events_diff = max_competitor_events_diff


    def _predict(self, fitteds, match_header, **kwargs):
        [ statistic_fitted ] = fitteds

        statistic = statistic_fitted.statistic
        if statistic.shape[0] == 0:
            return None

        whoscored_home = match_header['home']
        whoscored_away = match_header['away']
        if whoscored_home != statistic_fitted.home or whoscored_away != statistic_fitted.away:
            return None

        home_match_indices = []
        home_match_competitor_indices = []
        away_match_indices = []
        away_match_competitor_indices = []

        target_competitor_home = None
        target_competitor_away = None

        indices_for_home = None
        indices_for_away = None
        for i in range(statistic.shape[0]-1, 0-1, -1):
            if statistic.ix[i, 'home'] == whoscored_home:
                indices_for_home = i
                target_competitor_away = statistic.ix[i, 'away']
            elif target_competitor_away is not None and statistic.ix[i, 'away'] == target_competitor_away:
                if indices_for_home is not None:
                    home_match_indices.append(indices_for_home)
                    home_match_competitor_indices.append(i)
                target_competitor_away = None

            if statistic.ix[i, 'away'] == whoscored_away:
                indices_for_away = i
                target_competitor_home = statistic.ix[i, 'home']
            elif target_competitor_home is not None and statistic.ix[i, 'home'] == target_competitor_home:
                if indices_for_away is not None:
                    away_match_indices.append(indices_for_away)
                    away_match_competitor_indices.append(i)
                target_competitor_home = None

        home_last = statistic.iloc[home_match_indices, :]
        home_competitor_last = statistic.iloc[home_match_competitor_indices, :]
        away_last = statistic.iloc[away_match_indices, :]
        away_competitor_last = statistic.iloc[away_match_competitor_indices, :]

        events_home_diff = (home_last['events_home_count'] - home_last['events_away_count']).values[:self.n]
        events_home_competitor_diff = (home_competitor_last['events_home_count'] - home_competitor_last['events_away_count']).values[:self.n]
        normed_events_home_competitor_diff = np.fmin(np.fmax(-self.max_competitor_events_diff, events_home_competitor_diff), self.max_competitor_events_diff)
        events_away_diff = (away_last['events_home_count'] - away_last['events_away_count']).values[:self.n]
        events_away_competitor_diff = (away_competitor_last['events_home_count'] - away_competitor_last['events_away_count']).values[:self.n]
        normed_events_away_competitor_diff = np.fmin(np.fmax(-self.max_competitor_events_diff, events_away_competitor_diff), self.max_competitor_events_diff)

        home_weights_full = get_weights_array(min(events_home_diff.size, self.n), self.home_weights)
        away_weights_full = get_weights_array(min(events_away_diff.size, self.n), self.away_weights)

        events_home_diffs_diff2 = np.sum(((1 - self.kappa) * events_home_diff - self.kappa * normed_events_home_competitor_diff) * home_weights_full)
        events_away_diffs_diff2 = np.sum(((1 - self.kappa) * events_away_diff - self.kappa * normed_events_away_competitor_diff) * away_weights_full)

        diffs_diff2_prediction = events_home_diffs_diff2 + events_away_diffs_diff2

        return diffs_diff2_prediction


    def _get_init_strs(self):
        result = []
        if self.home_weights is not None:
            result.append( 'home_weights=[%s]' % (str(', '.join(map(str, self.home_weights))),) )
        if self.away_weights is not None:
            result.append( 'away_weights=[%s]' % (str(', '.join(map(str, self.away_weights))),) )
        result += [
            'n=%u' % (self.n,),
            'kappa=%.2f' % (self.kappa,),
            'max_competitor_events_diff=%u' % (self.max_competitor_events_diff,)
        ]
        return result
