from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.util.sport_util import count_events_of_teams, is_corner, is_first_period, is_second_period
from betrobot.util.common_util import conjunction


class CornersStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

        match_statistic_data = {
            'events_home_count': corners_home_count,
            'events_away_count': corners_away_count
        }

        return match_statistic_data


class CornersFirstPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (corners_first_period_home_count, corners_first_period_away_count) = count_events_of_teams(conjunction(is_corner, is_first_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': corners_first_period_home_count,
            'events_away_count': corners_first_period_away_count
        }

        return match_statistic_data


class CornersSecondPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (corners_second_period_home_count, corners_second_period_away_count) = count_events_of_teams(conjunction(is_corner, is_second_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': corners_second_period_home_count,
            'events_away_count': corners_second_period_away_count
        }

        return match_statistic_data
