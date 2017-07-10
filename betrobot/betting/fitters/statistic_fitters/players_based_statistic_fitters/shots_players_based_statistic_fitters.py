from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.betting.sport_util import count_events_of_players, is_shot, is_first_period, is_second_period
from betrobot.util.common_util import conjunction


class ShotsPlayersBasedStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        return count_events_of_players(is_shot, whoscored_match)


class ShotsFirstPeriodPlayersBasedStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        return count_events_of_players(conjunction(is_shot, is_first_period), whoscored_match)


class ShotsSecondPeriodPlayersBasedStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        return count_events_of_players(conjunction(is_shot, is_second_period), whoscored_match)
