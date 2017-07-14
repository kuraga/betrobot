import datetime
import pandas as pd
from betrobot.betting.fitters.statistic_fitter import StatisticFitter


class LastMatchesFilterStatisticTransformerFitter(StatisticFitter):

    _pick = [ 'n', 'home', 'away' ]


    def __init__(self, n=3):
        super().__init__()

        self.n = n


    def _clean(self):
        super()._clean()

        self.statistic = None
        self.home = None
        self.away = None


    def _fit(self, match_header, **kwargs):
        statistic = self.previous_fitter.statistic.copy()
        if statistic.shape[0] == 0:
            self.statistic = statistic
            return

        self.home = match_header['home']
        self.away = match_header['away']

        last_home_statistic = statistic[ statistic['home'] == self.home ].sort_values('date', ascending=False)[:self.n]
        last_away_statistic = statistic[ statistic['away'] == self.away ].sort_values('date', ascending=False)[:self.n]

        transformed_statistic = pd.concat([last_home_statistic, last_away_statistic]).drop_duplicates('uuid')

        self.statistic = transformed_statistic


    def _get_init_strs(self):
        return [
            'n=%s' % (str(self.n),)
        ]
