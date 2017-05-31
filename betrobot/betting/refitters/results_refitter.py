import numpy as np
import pandas as pd
from betrobot.betting.refitter import Refitter
from betrobot.util.sport_util import tournaments, get_whoscored_teams_of_betcity_match
from betrobot.util.math_util import get_weights_array


class ResultsRefitter(Refitter):

    _pick = [ 'home_weights', 'away_weights', 'home', 'away', 'events_home_counts_mean', 'events_away_counts_mean' ]


    def __init__(self, home_weights=None, away_weights=None):
        super().__init__()

        self.home_weights = home_weights
        self.away_weights = away_weights


    def _clean(self):
        super()._clean()

        self.home = None
        self.away = None
        self.events_home_counts_mean = None
        self.events_away_counts_mean = None


    def _refit(self, betcity_match):
        statistic = self.previous_fitter.statistic
        if statistic.shape[0] == 0:
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

        events_home_counts = home_data['events_home_count'].values
        events_away_counts = away_data['events_away_count'].values

        home_weights_full = get_weights_array(events_home_counts.size, self.home_weights)
        away_weights_full = get_weights_array(events_away_counts.size, self.away_weights)

        self.events_home_counts_mean = np.sum(events_home_counts * home_weights_full)
        self.events_away_counts_mean = np.sum(events_away_counts * away_weights_full)


    def _get_init_strs(self):
        result = []
        if self.home_weights is not None:
            strs.append( 'home_weights=[%s]' % (str(', '.join(map(str, self.home_weights))),) )
        if self.away_weights is not None:
            strs.append( 'away_weights=[%s]' % (str(', '.join(map(str, self.away_weights))),) )
        return result
