from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_teams_by_match_uuid, is_goal, is_first_period, is_second_period
from betrobot.util.common_util import conjunct


class GoalsStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (goals_home_count, goals_away_count) = count_events_of_teams_by_match_uuid(is_goal, match_header['uuid'])

        match_statistic_data = {
            'events_home_count': goals_home_count,
            'events_away_count': goals_away_count
        }

        return match_statistic_data


class GoalsFirstPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (goals_first_period_home_count, goals_first_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_goal, is_first_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': goals_first_period_home_count,
            'events_away_count': goals_first_period_away_count
        }

        return match_statistic_data


class GoalsSecondPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (goals_second_period_home_count, goals_second_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_goal, is_second_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': goals_second_period_home_count,
            'events_away_count': goals_second_period_away_count
        }

        return match_statistic_data
