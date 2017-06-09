from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.util.sport_util import count_events_of_teams, is_shot, is_first_period, is_second_period
from betrobot.util.common_util import conjunction


class ShotsStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (shots_home_count, shots_away_count) = count_events_of_teams(is_shot, whoscored_match)

        match_statistic_data = {
            'events_home_count': shots_home_count,
            'events_away_count': shots_away_count
        }

        return match_statistic_data


class ShotsFirstPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (shots_first_period_home_count, shots_first_period_away_count) = count_events_of_teams(conjunction(is_shot, is_first_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': shots_first_period_home_count,
            'events_away_count': shots_first_period_away_count
        }

        return match_statistic_data


class ShotsSecondPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (shots_second_period_home_count, shots_second_period_away_count) = count_events_of_teams(conjunction(is_shot, is_second_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': shots_second_period_home_count,
            'events_away_count': shots_second_period_away_count
        }

        return match_statistic_data
