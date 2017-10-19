import datetime
from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.util.common_util import eve_datetime
from betrobot.util.logging_util import get_logger


class AttainableMatchesFilterStatisticTransformerFitter(StatisticFitter):

    _pick = [ 'match_date', 'last_datetime', 'statistic' ]


    def _clean(self):
        super()._clean()

        self.match_date = None
        self.last_datetime = None
        self.statistic = None


    def _fit(self, match_header, **kwargs):
        statistic = self.previous_fitter.statistic.copy()
        if statistic.shape[0] == 0:
            self.statistic = statistic
            return

        self.match_date = match_header['date']
        self.last_datetime = eve_datetime(self.match_date)
        transformed_statistic = statistic[ statistic['date'] <= self.last_datetime ]

        self.statistic = transformed_statistic.copy()
        get_logger('prediction').info('Отобраны заголовки матчей, доступные на %s: %u штук', self.last_datetime.strftime('%Y-%m-%d %H:%M:%S'), self.statistic.shape[0])


    def _get_runtime_strs(self):
        result = []

        if self.is_fitted:
            result += [
                'match_date=%s' % (self.match_date.strftime('%Y-%m-%d'),),
                'last_datetime=%s' % (self.last_datetime.strftime('%Y-%m-%d %H:%M:%S'),),
                'statistic=<%u matches data>' % (self.statistic.shape[0],)
            ]

        return result
