from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_players_by_match_uuid, is_corner, is_first_period, is_second_period
from betrobot.util.common_util import conjunct
from betrobot.util.logging_util import get_logger


class CornersPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждому игроку) о количестве событий "угловой" (матч)')


    def _get_match_statistic_data(self, match_header):
        match_statistic_data = count_events_of_players_by_match_uuid(is_corner, match_header['uuid'])

        return match_statistic_data


class CornersFirstPeriodPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждому игроку) о количестве событий "угловой" (1-й тайм)')


    def _get_match_statistic_data(self, match_header):
        match_statistic_data = count_events_of_players_by_match_uuid(conjunct(is_corner, is_first_period), match_header['uuid'])

        return match_statistic_data


class CornersSecondPeriodPlayersBasedStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждому игроку) о количестве событий "угловой" (2-й тайм)')


    def _get_match_statistic_data(self, match_header):
        match_statistic_data = count_events_of_players_by_match_uuid(conjunct(is_corner, is_second_period), match_header['uuid'])

        return match_statistic_data
