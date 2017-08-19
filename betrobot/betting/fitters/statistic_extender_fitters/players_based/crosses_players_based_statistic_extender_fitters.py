from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_players_by_match_uuid, is_cross, is_first_period, is_second_period
from betrobot.util.common_util import conjunct
from betrobot.util.logging_util import get_logger


class CrossesPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждому игроку) о количестве событий "кросс" (матч)')


    def _get_match_statistic_data(self, match_header):
        match_statistic_data = count_events_of_players_by_match_uuid(is_cross, match_header['uuid'])

        return match_statistic_data


class CrossesFirstPeriodPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждому игроку) о количестве событий "кросс" (1-й тайм)')


    def _get_match_statistic_data(self, match_header):
        match_statistic_data = count_events_of_players_by_match_uuid(conjunct(is_cross, is_first_period), match_header['uuid'])

        return match_statistic_data


class CrossesSecondPeriodPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждому игроку) о количестве событий "кросс" (2-й тайм)')


    def _get_match_statistic_data(self, match_header):
        match_statistic_data = count_events_of_players_by_match_uuid(conjunct(is_cross, is_second_period), match_header['uuid'])

        return match_statistic_data
