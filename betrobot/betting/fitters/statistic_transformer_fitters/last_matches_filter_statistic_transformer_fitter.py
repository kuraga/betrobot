import datetime
import numpy as np
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

        last_home_uuids = statistic[ statistic['home'] == self.home ].index.values[:self.n]
        last_away_uuids = statistic[ statistic['away'] == self.away ].index.values[:self.n]
        last_uuids = np.unique(np.concatenate([last_home_uuids, last_away_uuids]))

        transformed_statistic = statistic.loc[last_uuids].sort_values('date', ascending=False)

        self.statistic = transformed_statistic


    def _get_init_strs(self):
        return [
            'n=%s' % (str(self.n),)
        ]
