import pandas as pd
from betrobot.betting.fitter import Fitter
from betrobot.util.sport_util import tournaments


class AttackDefenseFitter(Fitter):

    _pick = [ 'statistic_fitter', 'home', 'away', 'events_home_mean', 'events_away_mean' ]


    def _clean(self):
        super()._clean()

        self.statistic_fitter = None
        self.home = None
        self.away = None
        self.events_home_mean = None
        self.events_away_mean = None


    def _fit(self, statistic_fitter, home, away):
        self.statistic_fitter = statistic_fitter
        self.home = home
        self.away = away

        statistic = self.statistic_fitter.statistic

        self.events_home_mean = statistic['events_home_count'].mean()
        self.events_away_mean = statistic['events_away_count'].mean()

        home_data = statistic[ statistic['home'] == home ]
        self.home_attack = home_data['events_home_count'].mean() / self.events_home_mean if self.events_home_mean > 0 else 0
        self.home_defense = home_data['events_away_count'].mean() / self.events_away_mean if self.events_away_mean > 0 else 0

        away_data = statistic[ statistic['away'] == away ]
        self.away_attack = away_data['events_away_count'].mean() / self.events_away_mean if self.events_away_mean > 0 else 0
        self.away_defense = away_data['events_home_count'].mean() / self.events_home_mean if self.events_home_mean > 0 else 0
