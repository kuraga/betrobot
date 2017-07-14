import datetime
from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.util.common_util import eve_datetime


class AttainableMatchesFilterStatisticTransformerFitter(StatisticFitter):

    _pick = [ 'match_date', 'last_datetime' ]


    def _clean(self):
        super()._clean()

        self.statistic = None
        self.match_date = None
        self.last_datetime = None


    def _fit(self, match_header, **kwargs):
        statistic = self.previous_fitter.statistic.copy()
        if statistic.shape[0] == 0:
            self.statistic = statistic
            return

        self.match_date = match_header['date']
        self.last_datetime = eve_datetime(self.match_date)
        transformed_statistic = statistic[ statistic['date'] <= self.last_datetime ]

        self.statistic = transformed_statistic
