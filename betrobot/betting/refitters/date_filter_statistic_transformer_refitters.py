import datetime
from betrobot.betting.refitter import Refitter
from betrobot.util.common_util import eve_datetime


class MatchPastStatisticTransformerRefitter(Refitter):

    _pick = [ 'statistic', 'betcity_match_date', 'last_datetime' ]


    def _clean(self):
        super()._clean()

        self.statistic = None
        self.betcity_match_date = None
        self.last_datetime = None


    def _refit(self, betcity_match):
        self.betcity_match_date = datetime.datetime.strptime(betcity_match['date'], '%Y-%m-%d')
        self.last_datetime = eve_datetime(self.betcity_match_date)

        statistic = self.previous_fitter.statistic

        transformed_statistic = statistic[ statistic['date'] <= self.last_datetime ]

        self.statistic = transformed_statistic


class MatchEveStatisticTransformerRefitter(Refitter):

    _pick = [ 'statistic', 'delta', 'betcity_match_date', 'last_datetime', 'first_datetime' ]


    def _clean(self):
        super()._clean()

        self.statistic = None
        self.betcity_match_date = None
        self.last_datetime = None
        self.first_datetime = None


    def __init__(self, delta=None):
        super().__init__()

        if delta is not None:
           self.delta = delta
        else:
           self.delta = datetime.timedelta(days=100)


    def _refit(self, betcity_match):
        self.betcity_match_date = datetime.datetime.strptime(betcity_match['date'], '%Y-%m-%d')
        self.last_datetime = eve_datetime(self.betcity_match_date)
        self.first_datetime = eve_datetime(self.betcity_match_date - self.delta)

        statistic = self.previous_fitter.statistic

        transformed_statistic = statistic[ (statistic['date'] >= self.first_datetime) & (statistic['date'] <= self.last_datetime) ]

        self.statistic = transformed_statistic
