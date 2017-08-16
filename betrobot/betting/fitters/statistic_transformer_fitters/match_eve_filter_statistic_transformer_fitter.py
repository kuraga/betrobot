import datetime
from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.util.common_util import eve_datetime


class MatchEveFilterStatisticTransformerFitter(StatisticFitter):

    _pick = [ 'delta', 'match_date', 'last_datetime', 'first_datetime' ]


    def _clean(self):
        super()._clean()

        self.statistic = None
        self.match_date = None
        self.last_datetime = None
        self.first_datetime = None


    def __init__(self, days=100):
        super().__init__()

        self.delta = datetime.timedelta(days=days)


    def _fit(self, match_header, **kwargs):
        statistic = self.previous_fitter.statistic.copy()
        if statistic.shape[0] == 0:
            self.statistic = statistic
            return

        self.match_date = match_header['date']
        self.last_datetime = eve_datetime(self.match_date)
        self.first_datetime = eve_datetime(self.match_date - self.delta)

        transformed_statistic = statistic[ (statistic['date'] >= self.first_datetime) & (statistic['date'] <= self.last_datetime) ]

        self.statistic = transformed_statistic.copy()


    def _get_init_strs(self):
        return [
            'delta=%s' % (str(self.delta),)
        ]
