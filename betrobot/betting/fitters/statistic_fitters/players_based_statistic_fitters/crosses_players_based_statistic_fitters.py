from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.betting.sport_util import count_events_of_players, is_cross, is_first_period, is_second_period
from betrobot.util.common_util import conjunction


class CrossesPlayersBasedStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        return count_events_of_players(is_cross, whoscored_match)


class CrossesFirstPeriodPlayersBasedStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        return count_events_of_players(conjunction(is_cross, is_first_period), whoscored_match)


class CrossesSecondPeriodPlayersBasedStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        return count_events_of_players(conjunction(is_cross, is_second_period), whoscored_match)
