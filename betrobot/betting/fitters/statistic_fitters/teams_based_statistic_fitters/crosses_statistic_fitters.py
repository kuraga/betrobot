from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.betting.sport_util import count_events_of_teams, is_cross, is_first_period, is_second_period
from betrobot.util.common_util import conjunction


class CrossesStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (crosses_home_count, crosses_away_count) = count_events_of_teams(is_cross, whoscored_match)

        match_statistic_data = {
            'events_home_count': crosses_home_count,
            'events_away_count': crosses_away_count
        }

        return match_statistic_data


class CrossesFirstPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (crosses_first_period_home_count, crosses_first_period_away_count) = count_events_of_teams(conjunction(is_cross, is_first_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': crosses_first_period_home_count,
            'events_away_count': crosses_first_period_away_count
        }

        return match_statistic_data


class CrossesSecondPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (crosses_second_period_home_count, crosses_second_period_away_count) = count_events_of_teams(conjunction(is_cross, is_second_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': crosses_second_period_home_count,
            'events_away_count': crosses_second_period_away_count
        }

        return match_statistic_data
