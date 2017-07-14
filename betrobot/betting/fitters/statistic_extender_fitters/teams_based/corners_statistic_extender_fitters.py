from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_teams_by_match_uuid, is_corner, is_first_period, is_second_period
from betrobot.util.common_util import conjunct


class CornersStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (corners_home_count, corners_away_count) = count_events_of_teams_by_match_uuid(is_corner, match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_home_count,
            'events_away_count': corners_away_count
        }

        return match_statistic_data


class CornersFirstPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (corners_first_period_home_count, corners_first_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_first_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_first_period_home_count,
            'events_away_count': corners_first_period_away_count
        }

        return match_statistic_data


class CornersSecondPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (corners_second_period_home_count, corners_second_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_second_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_second_period_home_count,
            'events_away_count': corners_second_period_away_count
        }

        return match_statistic_data
