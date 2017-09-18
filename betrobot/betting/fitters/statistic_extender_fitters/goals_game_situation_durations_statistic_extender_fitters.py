from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_game_situation_durations_by_match_uuid, is_goal, is_first_period, is_second_period
from betrobot.util.common_util import conjunct
from betrobot.util.logging_util import get_logger


class GoalsGameSituationDurationsStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация о продолжительности игровых ситуаций по голам (матч)')


    def _get_match_statistic_data(self, match_header):
        (home_winning_duration, away_winning_duration, draw_duration) = count_game_situation_durations_by_match_uuid(None, is_goal, match_header['uuid'])

        match_statistic_data = {
            'home_winning_duration': home_winning_duration,
            'away_winning_duration': away_winning_duration,
            'draw_duration': draw_duration
        }

        return match_statistic_data


class GoalsFirstPeriodGameSituationDurationsStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация о продолжительности игровых ситуаций по голам (1-й тайм)')


    def _get_match_statistic_data(self, match_header):
        (home_winning_duration, away_winning_duration, draw_duration) = count_game_situation_durations_by_match_uuid(is_first_period, is_goal, match_header['uuid'])

        match_statistic_data = {
            'home_winning_duration': home_winning_duration,
            'away_winning_duration': away_winning_duration,
            'draw_duration': draw_duration
        }

        return match_statistic_data


class GoalsSecondPeriodGameSituationDurationsStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация о продолжительности игровых ситуаций по голам (2-й тайм)')


    def _get_match_statistic_data(self, match_header):
        (home_winning_duration, away_winning_duration, draw_duration) = count_game_situation_durations_by_match_uuid(is_second_period, is_goal, match_header['uuid'])

        match_statistic_data = {
            'home_winning_duration': home_winning_duration,
            'away_winning_duration': away_winning_duration,
            'draw_duration': draw_duration
        }

        return match_statistic_data
