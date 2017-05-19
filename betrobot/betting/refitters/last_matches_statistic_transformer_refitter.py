import datetime
import pandas as pd
from betrobot.betting.refitter import Refitter
from betrobot.util.sport_util import get_whoscored_teams_of_betcity_match


class LastMatchesStatisticTransformerRefitter(Refitter):

    _pick = [ 'n', 'statistic', 'home', 'away' ]


    def _clean(self):
        super()._clean()

        self.statistic = None
        self.home = None
        self.away = None


    def __init__(self, n=3):
        super().__init__()

        self.n = n


    def _refit(self, betcity_match):
        (self.home, self.away) = get_whoscored_teams_of_betcity_match(betcity_match)

        statistic = self.previous_fitter.statistic

        last_home_statistic = statistic[ statistic['home'] == self.home ].sort_values('date', ascending=False)[:3]
        last_away_statistic = statistic[ statistic['away'] == self.away ].sort_values('date', ascending=False)[:3]

        transformed_statistic = pd.concat([last_home_statistic, last_away_statistic])

        self.statistic = transformed_statistic
