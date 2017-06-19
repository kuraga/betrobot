import datetime
from betrobot.util.common_util import eve_datetime
from betrobot.betting.refitter import Refitter


class InvalidMatchesFilterStatisticTransformerRefitter(Refitter):

    _pick = [ 'statistic' ]


    def _clean(self):
        super()._clean()

        self.statistic = None


    def _refit(self, betcity_match):
        betcity_match_date = datetime.datetime.strptime(betcity_match['date'], '%Y-%m-%d')
        last_datetime = eve_datetime(betcity_match_date)

        whole_statistic = self.previous_fitter.statistic

        self.statistic = whole_statistic[ whole_statistic['date'] <= last_datetime ]
