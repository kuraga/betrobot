from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_teams_by_match_uuid, is_shot, is_first_period, is_second_period
from betrobot.util.common_util import conjunct
from betrobot.util.logging_util import get_logger


class ShotsStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "удар" (матч)')


    def _get_match_statistic_data(self, match_header):
        (shots_home_count, shots_away_count) = count_events_of_teams_by_match_uuid(is_shot, match_header['uuid'])

        match_statistic_data = {
            'events_home_count': shots_home_count,
            'events_away_count': shots_away_count
        }

        return match_statistic_data


class ShotsFirstPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "удар" (1-й тайм)')


    def _get_match_statistic_data(self, match_header):
        (shots_first_period_home_count, shots_first_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_shot, is_first_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': shots_first_period_home_count,
            'events_away_count': shots_first_period_away_count
        }

        return match_statistic_data


class ShotsSecondPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "удар" (2-й тайм)')


    def _get_match_statistic_data(self, match_header):
        (shots_second_period_home_count, shots_second_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_shot, is_second_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': shots_second_period_home_count,
            'events_away_count': shots_second_period_away_count
        }

        return match_statistic_data
