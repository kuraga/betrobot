from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.util.sport_util import count_events_of_teams, is_goal, is_first_period, is_second_period
from betrobot.util.common_util import conjunction


class GoalsStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

        match_statistic_data = {
            'events_home_count': goals_home_count,
            'events_away_count': goals_away_count
        }

        return match_statistic_data


class GoalsFirstPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (goals_first_period_home_count, goals_first_period_away_count) = count_events_of_teams(conjunction(is_goal, is_first_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': goals_first_period_home_count,
            'events_away_count': goals_first_period_away_count
        }

        return match_statistic_data


class GoalsSecondPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (goals_second_period_home_count, goals_second_period_away_count) = count_events_of_teams(conjunction(is_goal, is_second_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': goals_second_period_home_count,
            'events_away_count': goals_second_period_away_count
        }

        return match_statistic_data
