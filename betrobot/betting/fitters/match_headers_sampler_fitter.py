import pandas as pd
from betrobot.betting.fitter import Fitter
from betrobot.util.database_util import db
from betrobot.util.cache_util import cache_get_or_evaluate
from betrobot.util.common_util import hashize
from betrobot.util.logging_util import get_logger
from betrobot.betting.sport_util import get_match_headers


class MatchHeadersSamplerFitter(Fitter):

    _pick = [ 'match_headers', 'statistic' ]


    # TODO: Сделать механизм управления этим "кешем"
    _cached_match_headers = { }


    def _clean(self):
        super()._clean()

        self.match_headers = None
        self.statistic = None


    def _fit(self, sample_condition=None, **kwargs):
        if sample_condition is None:
           sample_condition = {}

        key = hashize(sample_condition)
        if key in self.__class__._cached_match_headers:
            get_logger('prediction').debug('Заголовки матчей будут загружены из кеша')
            self.match_headers = self.__class__._cached_match_headers[key]
        else:
            get_logger('prediction').debug('Заголовки матчей будут перегенерированы. Условие: %s', str(sample_condition))
            self.match_headers = self.__class__._cached_match_headers[key] = get_match_headers(sample_condition)

        get_logger('prediction').info('Получены заголовки матчей: %u штук', self.match_headers.shape[0])

        # FIXME: Выделить это в отдельный фиттер
        self.statistic = self.match_headers.copy()


    def _get_runtime_strs(self):
        result = []

        if self.is_fitted:
            result += [
                'match_headers=<%u match headers>' % (self.match_headers.shape[0],)
            ]

        return result
