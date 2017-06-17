import numpy as np
import pandas as pd
from betrobot.betting.refitter import Refitter
from betrobot.util.sport_util import get_teams_tournaments_countries_data
from betrobot.util.math_util import get_weights_array


class EventsMeanRefitter(Refitter):

    _pick = [ 'home_weights', 'away_weights', 'home', 'away', 'events_home_mean', 'events_away_mean' ]


    def __init__(self, home_weights=None, away_weights=None):
        super().__init__()

        self.home_weights = home_weights
        self.away_weights = away_weights


    def _clean(self):
        super()._clean()

        self.home = None
        self.away = None
        self.events_home_mean = None
        self.events_away_mean = None


    def _refit(self, betcity_match):
        statistic = self.previous_fitter.statistic
        if statistic.shape[0] == 0:
            return

        self.home = get_teams_tournaments_countries_data('betcityName', betcity_match['home'], 'whoscoredName')
        self.away = get_teams_tournaments_countries_data('betcityName', betcity_match['away'], 'whoscoredName')
        if self.home is None or self.away is None:
            return

        home_weights_full = get_weights_array(statistic.shape[0], self.home_weights)
        # Среднее количество голов, забиваемых хозяевами матчей
        self.events_home_mean = np.sum(statistic['events_home_count'] * home_weights_full)

        away_weights_full = get_weights_array(statistic.shape[0], self.away_weights)
        # Среднее количество голов, забиваемых гостями матчей
        self.events_away_mean = np.sum(statistic['events_away_count'] * away_weights_full)


    def _get_init_strs(self):
        result = []
        if self.home_weights is not None:
            strs.append( 'home_weights=[%s]' % (str(', '.join(map(str, self.home_weights))),) )
        if self.away_weights is not None:
            strs.append( 'away_weights=[%s]' % (str(', '.join(map(str, self.away_weights))),) )
        return result
