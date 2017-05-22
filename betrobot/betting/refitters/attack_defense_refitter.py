import numpy as np
import pandas as pd
from betrobot.betting.refitter import Refitter
from betrobot.util.sport_util import tournaments, get_whoscored_teams_of_betcity_match
from betrobot.util.math_util import get_weights_array


class AttackDefenseRefitter(Refitter):

    _pick = [ 'home_weights', 'away_weights', 'home', 'away', 'events_home_mean', 'events_away_mean', 'home_attack', 'home_defense', 'away_attack', 'away_defense' ]


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
        self.home_attack = None
        self.home_defense = None
        self.away_attack = None
        self.away_defense = None


    def _refit(self, betcity_match):
        statistic = self.previous_fitter.statistic
        if statistic.shape[0] == 0 or statistic.shape[0] == 0:
            return

        (self.home, self.away) = get_whoscored_teams_of_betcity_match(betcity_match)

        # Среднее количество голов, забиваемых хозяевами матчей
        self.events_home_mean = statistic['events_home_count'].mean()
        # Среднее количество голов, забиваемых гостями матчей
        self.events_away_mean = statistic['events_away_count'].mean()

        # Статистика матчей, где betcity_match['home'] тоже была хозяйкой
        home_data = statistic[ statistic['home'] == self.home ].sort_values('date', ascending=False)
        if home_data.shape[0] == 0:
            return
        # Статистика матчей, где betcity_match['away'] тоже была гостьей
        away_data = statistic[ statistic['away'] == self.away ].sort_values('date', ascending=False)
        if away_data.shape[0] == 0:
            return

        home_weights_full = get_weights_array(home_data['events_home_count'].size, self.home_weights)
        away_weights_full = get_weights_array(away_data['events_away_count'].size, self.away_weights)

        if self.events_home_mean > 0:
            # Во сколько раз превышает среднее по турниру число голов, забитых betcity_match['home'] в домашних матчах?
            self.home_attack = np.sum(home_data['events_home_count'].values * home_weights_full) / self.events_home_mean
            # Во сколько раз превышает среднее по турниру число голов, пропущенных betcity_match['away'] в гостевых матчах?
            self.away_defense = np.sum(away_data['events_home_count'].values * away_weights_full) / self.events_home_mean
        if self.events_away_mean > 0:
            # Во сколько раз превышает среднее по турниру число голов, пропущенных betcity_match['home'] в домашних матчах?
            self.home_defense = np.sum(home_data['events_away_count'].values * home_weights_full) / self.events_away_mean
            # Во сколько раз превышает среднее по турниру число голов, забитых betcity_match['away'] в гостевых матчах?
            self.away_attack = np.sum(away_data['events_away_count'].values * away_weights_full) / self.events_away_mean


    def __str__(self):
        return '%s(home_weights=%s, away_weights=%s)[is_fitted=%s]' % (self.__class__.__name__, str(self.home_weights), str(self.away_weights), str(self.is_fitted))
