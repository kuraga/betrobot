import numpy as np
import pandas as pd
from betrobot.betting.refitter import Refitter
from betrobot.util.sport_util import tournaments, get_whoscored_teams_of_betcity_match
from betrobot.util.math_util import get_weights_array


class DiffsRefitter(Refitter):

    _pick = [ 'home_weights', 'away_weights', 'home', 'away', 'home_diffs_mean', 'away_diffs_mean' ]


    def __init__(self, home_weights=None, away_weights=None):
        super().__init__()

        self.home_weights = home_weights
        self.away_weights = away_weights


    def _clean(self):
        super()._clean()

        self.home = None
        self.away = None
        self.home_diffs_mean = None
        self.away_diffs_mean = None


    def _refit(self, betcity_match):
        statistic = self.previous_fitter.statistic
        if statistic.shape[0] == 0 or statistic.shape[0] == 0:
            return

        (self.home, self.away) = get_whoscored_teams_of_betcity_match(betcity_match)

        # Статистика матчей, где betcity_match['home'] тоже была хозяйкой
        home_data = statistic[ statistic['home'] == self.home ].sort_values('date', ascending=False)
        if home_data.shape[0] == 0:
            return
        # Статистика матчей, где betcity_match['away'] тоже была гостьей
        away_data = statistic[ statistic['away'] == self.away ].sort_values('date', ascending=False)
        if away_data.shape[0] == 0:
            return

        home_diffs = (home_data['events_home_count'] - home_data['events_away_count']).values
        away_diffs = (away_data['events_away_count'] - away_data['events_home_count']).values

        home_weights_full = get_weights_array(home_diffs.size, self.home_weights)
        away_weights_full = get_weights_array(away_diffs.size, self.away_weights)

        self.home_diffs_mean = np.sum(home_diffs * home_weights_full)
        self.away_diffs_mean = np.sum(away_diffs * away_weights_full)


    def _get_init_strs(self):
        result = []
        if self.home_weights is not None:
            strs.append( 'home_weights=[%s]' % (str(', '.join(map(str, self.home_weights))),) )
        if self.away_weights is not None:
            strs.append( 'away_weights=[%s]' % (str(', '.join(map(str, self.away_weights))),) )
        return result
