import datetime
from betrobot.betting.fitters.statistic_transformer_fitter import StatisticTransformerFitter
from betrobot.util.common_util import eve_datetime


class MatchPastStatisticTransformerFitter(StatisticTransformerFitter):

    _pick = [ 'betcity_match_date', 'last_datetime' ]


    def _clean(self):
        super()._clean()

        self.betcity_match_date = None
        self.last_datetime = None


    def _fit(self, statistic_fitter, betcity_match):
        self._prefit(statistic_fitter)

        self.betcity_match_date = datetime.datetime.strptime(betcity_match['date'], '%Y-%m-%d')
        self.last_datetime = eve_datetime(self.betcity_match_date)

        statistic = self.statistic_fitter.statistic
        transformed_statistic = statistic[ statistic['date'] <= self.last_datetime ]

        self.statistic = transformed_statistic


class MatchEveStatisticTransformerFitter(StatisticTransformerFitter):

    _pick = [ 'delta', 'betcity_match_date', 'last_datetime', 'first_datetime' ]


    def _clean(self):
        super()._clean()

        self.betcity_match_date = None
        self.last_datetime = None
        self.first_datetime = None


    def __init__(self, delta=None):
        super().__init__()

        if delta is not None:
           self.delta = delta
        else:
           self.delta = datetime.timedelta(days=100)


    def _fit(self, statistic_fitter, betcity_match):
        self._prefit(statistic_fitter)

        self.betcity_match_date = datetime.datetime.strptime(betcity_match['date'], '%Y-%m-%d')
        self.last_datetime = eve_datetime(self.betcity_match_date)
        self.first_datetime = eve_datetime(self.betcity_match_date - self.delta)

        statistic = self.statistic_fitter.statistic
        transformed_statistic = statistic[ (statistic['date'] >= self.first_datetime) & (statistic['date'] <= self.last_datetime) ]

        self.statistic = transformed_statistic
