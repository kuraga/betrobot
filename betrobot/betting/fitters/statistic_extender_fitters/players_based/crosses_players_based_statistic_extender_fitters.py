from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_players_by_match_uuid, is_cross, is_first_period, is_second_period
from betrobot.util.common_util import conjunct


class CrossesPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        return count_events_of_players_by_match_uuid(is_cross, match_header['uuid'])


class CrossesFirstPeriodPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        return count_events_of_players_by_match_uuid(conjunct(is_cross, is_first_period), match_header['uuid'])


class CrossesSecondPeriodPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        return count_events_of_players_by_match_uuid(conjunct(is_cross, is_second_period), match_header['uuid'])
