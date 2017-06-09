import datetime
import pandas as pd
from betrobot.betting.refitter import Refitter
from betrobot.util.sport_util import get_whoscored_teams_of_betcity_match


# TODO: Переименовать в LastMatchesFilterStatisticTransformerRefitter
class LastMatchesStatisticTransformerRefitter(Refitter):

    _pick = [ 'n', 'statistic', 'home', 'away' ]


    def __init__(self, n=3):
        super().__init__()

        self.n = n


    def _clean(self):
        super()._clean()

        self.statistic = None
        self.home = None
        self.away = None


    def _refit(self, betcity_match):
        (self.home, self.away) = get_whoscored_teams_of_betcity_match(betcity_match)

        statistic = self.previous_fitter.statistic

        last_home_statistic = statistic[ statistic['home'] == self.home ].sort_values('date', ascending=False)[:self.n]
        last_away_statistic = statistic[ statistic['away'] == self.away ].sort_values('date', ascending=False)[:self.n]

        transformed_statistic = pd.concat([last_home_statistic, last_away_statistic]).drop_duplicates('uuid')

        self.statistic = transformed_statistic


    def _get_init_strs(self):
        return [
            'n=%s' % (str(self.n),)
        ]
