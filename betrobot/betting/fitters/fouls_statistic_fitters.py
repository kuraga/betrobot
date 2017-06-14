from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.util.sport_util import count_events_of_teams, is_foul, is_first_period, is_second_period
from betrobot.util.common_util import conjunction


class FoulsStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (fouls_home_count, fouls_away_count) = count_events_of_teams(is_foul, whoscored_match)

        match_statistic_data = {
            'events_home_count': fouls_home_count,
            'events_away_count': fouls_away_count
        }

        return match_statistic_data


class FoulsFirstPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (fouls_first_period_home_count, fouls_first_period_away_count) = count_events_of_teams(conjunction(is_foul, is_first_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': fouls_first_period_home_count,
            'events_away_count': fouls_first_period_away_count
        }

        return match_statistic_data


class FoulsSecondPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (fouls_second_period_home_count, fouls_second_period_away_count) = count_events_of_teams(conjunction(is_foul, is_second_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': fouls_second_period_home_count,
            'events_away_count': fouls_second_period_away_count
        }

        return match_statistic_data
