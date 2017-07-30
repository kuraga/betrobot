import pandas as pd
from betrobot.betting.fitter import Fitter
from betrobot.util.database_util import db
from betrobot.util.cache_util import cache_get_or_evaluate
from betrobot.util.common_util import hashize


class MatchHeadersSamplerFitter(Fitter):

    _pick = [ 'match_headers' ]


    # TODO: Сделать механизм управления этим "кешем"
    _cached_match_headers = { }


    def _clean(self):
        super()._clean()

        self.match_headers = None


    def _fit(self, sample_condition=None, **kwargs):
        if sample_condition is None:
           sample_condition = {}

        key = hashize(sample_condition).decode('utf-8')
        if key in self.__class__._cached_match_headers:
            self.match_headers = self.__class__._cached_match_headers[key]
        else:
            self.match_headers = self.__class__._cached_match_headers[key] = self.__class__._get_match_headers(sample_condition)

        self.statistic = self.match_headers  # FIXME


    @classmethod
    def _get_match_headers(cls, sample_condition):
        match_headers_collection = db['match_headers']
        sample = match_headers_collection.find(sample_condition)

        data = []
        for match_header in sample:
            data.append({
                'uuid': match_header['uuid'],
                'region_id': match_header['regionId'],
                'tournament_id': match_header['tournamentId'],
                'date': match_header['date'],
                'home': match_header['home'],
                'away': match_header['away']
            })
        match_headers = pd.DataFrame(data, columns=['uuid', 'region_id', 'tournament_id', 'date', 'home', 'away']).set_index('uuid', drop=False)

        return match_headers


    def _get_runtime_strs(self):
        result = []

        if self.is_fitted:
            result += [
                'match_headers=<%u match headers>' % (self.match_headers.shape[0],)
            ]

        return result
