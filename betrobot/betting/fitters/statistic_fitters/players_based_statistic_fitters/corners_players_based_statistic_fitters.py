from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.betting.sport_util import count_events_of_players, is_corner, is_first_period, is_second_period
from betrobot.util.common_util import conjunction


class CornersPlayersBasedStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        return count_events_of_players(is_corner, whoscored_match)


class CornersFirstPeriodPlayersBasedStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        return count_events_of_players(conjunction(is_corner, is_first_period), whoscored_match)


class CornersSecondPeriodPlayersBasedStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        return count_events_of_players(conjunction(is_corner, is_second_period), whoscored_match)
