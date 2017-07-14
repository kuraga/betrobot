from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_players_by_match_uuid, is_shot, is_first_period, is_second_period
from betrobot.util.common_util import conjunct


class ShotsPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        return count_events_of_players_by_match_uuid(is_shot, match_header['uuid'])


class ShotsFirstPeriodPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        return count_events_of_players_by_match_uuid(conjunct(is_shot, is_first_period), match_header['uuid'])


class ShotsSecondPeriodPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        return count_events_of_players_by_match_uuid(conjunct(is_shot, is_second_period), match_header['uuid'])
