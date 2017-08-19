from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_teams_by_match_uuid, is_foul, is_first_period, is_second_period
from betrobot.util.common_util import conjunct
from betrobot.util.logging_util import get_logger


class FoulsStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "фол" (матч)')


    def _get_match_statistic_data(self, match_header):
        (fouls_home_count, fouls_away_count) = count_events_of_teams_by_match_uuid(is_foul, match_header['uuid'])

        match_statistic_data = {
            'events_home_count': fouls_home_count,
            'events_away_count': fouls_away_count
        }

        return match_statistic_data


class FoulsFirstPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "фол" (1-й тайм)')


    def _get_match_statistic_data(self, match_header):
        (fouls_first_period_home_count, fouls_first_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_foul, is_first_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': fouls_first_period_home_count,
            'events_away_count': fouls_first_period_away_count
        }

        return match_statistic_data


class FoulsSecondPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "фол" (2-й тайм)')


    def _get_match_statistic_data(self, match_header):
        (fouls_second_period_home_count, fouls_second_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_foul, is_second_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': fouls_second_period_home_count,
            'events_away_count': fouls_second_period_away_count
        }

        return match_statistic_data
