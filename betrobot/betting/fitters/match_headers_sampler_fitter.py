import pandas as pd
from betrobot.betting.fitter import Fitter
from betrobot.util.database_util import db
from betrobot.util.cache_util import cache_get_or_evaluate
from betrobot.util.common_util import hashize
from betrobot.util.logging_util import get_logger
from betrobot.betting.sport_util import get_match_headers


class MatchHeadersSamplerFitter(Fitter):

    _pick = [ 'sample_condition', 'match_headers', 'statistic' ]


    def __init__(self, sample_condition=None, **kwargs):
        super().__init__(**kwargs)

        if sample_condition is None:
           sample_condition = {}

        self.sample_condition = sample_condition


    def _clean(self):
        super()._clean()

        self.match_headers = None
        self.statistic = None


    def _fit(self, **kwargs):
        get_logger('prediction').info('Условие для получения заголовков: %s', str(self.sample_condition))
        self.match_headers = get_match_headers(self.sample_condition)
        get_logger('prediction').info('Получены заголовки матчей: %u штук', self.match_headers.shape[0])

        # FIXME: Решить, что с этим делать
        self.statistic = self.match_headers.copy()


    def _get_init_strs(self):
        return [
            'sample_condition=%s' % (str(self.sample_condition),)
        ]


    def _get_runtime_strs(self):
        result = []

        if self.is_fitted:
            result += [
                'match_headers=<%u match headers>' % (self.match_headers.shape[0],),
                'statistic=<%u match headers>' % (self.statistic.shape[0],)
            ]

        return result
