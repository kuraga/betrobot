from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_teams_by_match_uuid, is_cross, is_first_period, is_second_period
from betrobot.util.common_util import conjunct


class CrossesStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (crosses_home_count, crosses_away_count) = count_events_of_teams_by_match_uuid(is_cross, match_header['uuid'])

        match_statistic_data = {
            'events_home_count': crosses_home_count,
            'events_away_count': crosses_away_count
        }

        return match_statistic_data


class CrossesFirstPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (crosses_first_period_home_count, crosses_first_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_cross, is_first_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': crosses_first_period_home_count,
            'events_away_count': crosses_first_period_away_count
        }

        return match_statistic_data


class CrossesSecondPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (crosses_second_period_home_count, crosses_second_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_cross, is_second_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': crosses_second_period_home_count,
            'events_away_count': crosses_second_period_away_count
        }

        return match_statistic_data
