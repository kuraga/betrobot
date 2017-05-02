import numpy as np
import pandas as pd
from betrobot.betting.refitter import Refitter
from betrobot.util.sport_util import tournaments, get_whoscored_teams_of_betcity_match


class AttackDefenseRefitter(Refitter):

    _pick = [ 'home', 'away', 'events_home_mean', 'events_away_mean' ]


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
        (self.home, self.away) = get_whoscored_teams_of_betcity_match(betcity_match)

        statistic = self.previous_fitter.statistic

        self.events_home_mean = statistic['events_home_count'].mean()
        self.events_away_mean = statistic['events_away_count'].mean()

        home_data = statistic[ statistic['home'] == self.home ]
        away_data = statistic[ statistic['away'] == self.away ]

        self.home_attack = home_data['events_home_count'].mean() / self.events_home_mean if self.events_home_mean > 0 else 0
        self.home_defense = home_data['events_away_count'].mean() / self.events_away_mean if self.events_away_mean > 0 else 0

        self.away_attack = away_data['events_away_count'].mean() / self.events_away_mean if self.events_away_mean > 0 else 0
        self.away_defense = away_data['events_home_count'].mean() / self.events_home_mean if self.events_home_mean > 0 else 0


    def __str__(self):
        return '%s()[is_fitted=%s]' % (self.__class__.__name__, str(self.is_fitted))
