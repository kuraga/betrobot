from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_players_by_match_uuid, is_corner, is_first_period, is_second_period
from betrobot.util.common_util import conjunct


class CornersPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        return count_events_of_players_by_match_uuid(is_corner, match_header['uuid'])


class CornersFirstPeriodPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        return count_events_of_players_by_match_uuid(conjunct(is_corner, is_first_period), match_header['uuid'])


class CornersSecondPeriodPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        return count_events_of_players_by_match_uuid(conjunct(is_corner, is_second_period), match_header['uuid'])
