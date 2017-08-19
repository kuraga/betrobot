from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_teams_by_match_uuid, is_corner, is_first_period, is_second_period
from betrobot.util.common_util import conjunct
from betrobot.util.logging_util import get_logger


class CornersStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (матч)')


    def _get_match_statistic_data(self, match_header):
        (corners_home_count, corners_away_count) = count_events_of_teams_by_match_uuid(is_corner, match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_home_count,
            'events_away_count': corners_away_count
        }

        return match_statistic_data


class CornersFirstPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (1-й тайм)')


    def _get_match_statistic_data(self, match_header):
        (corners_first_period_home_count, corners_first_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_first_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_first_period_home_count,
            'events_away_count': corners_first_period_away_count
        }

        return match_statistic_data


class CornersSecondPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (2-й тайм)')


    def _get_match_statistic_data(self, match_header):
        (corners_second_period_home_count, corners_second_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_second_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_second_period_home_count,
            'events_away_count': corners_second_period_away_count
        }

        return match_statistic_data
