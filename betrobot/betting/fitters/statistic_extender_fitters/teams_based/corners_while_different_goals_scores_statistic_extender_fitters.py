from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_teams_by_match_uuid, is_corner, is_first_period, is_second_period, is_goals_score_1, is_goals_score_2, is_goals_score_X
from betrobot.util.common_util import conjunct
from betrobot.util.logging_util import get_logger


class CornersWhileHomeWinningByGoalsStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (матч, только периоды, пока хозяева побеждают)')


    def _get_match_statistic_data(self, match_header):
        (corners_home_count, corners_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_goals_score_1), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_home_count,
            'events_away_count': corners_away_count
        }

        return match_statistic_data


class CornersWhileHomeWinningByGoalsFirstPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (1-й тайм, пока хозяева побеждают)')


    def _get_match_statistic_data(self, match_header):
        (corners_first_period_home_count, corners_first_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_first_period, is_goals_score_1), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_first_period_home_count,
            'events_away_count': corners_first_period_away_count
        }

        return match_statistic_data


class CornersWhileHomeWinningByGoalsSecondPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (2-й тайм, пока хозяева побеждают)')


    def _get_match_statistic_data(self, match_header):
        (corners_second_period_home_count, corners_second_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_second_period, is_goals_score_1), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_second_period_home_count,
            'events_away_count': corners_second_period_away_count
        }

        return match_statistic_data


class CornersWhileAwayWinningByGoalsStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (матч, только периоды, пока гости побеждают)')


    def _get_match_statistic_data(self, match_header):
        (corners_home_count, corners_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_goals_score_2), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_home_count,
            'events_away_count': corners_away_count
        }

        return match_statistic_data


class CornersWhileAwayWinningByGoalsFirstPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (1-й тайм, пока гости побеждают)')


    def _get_match_statistic_data(self, match_header):
        (corners_first_period_home_count, corners_first_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_first_period, is_goals_score_2), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_first_period_home_count,
            'events_away_count': corners_first_period_away_count
        }

        return match_statistic_data


class CornersWhileAwayWinningByGoalsSecondPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (2-й тайм, пока гости побеждают)')


    def _get_match_statistic_data(self, match_header):
        (corners_second_period_home_count, corners_second_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_second_period, is_goals_score_2), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_second_period_home_count,
            'events_away_count': corners_second_period_away_count
        }

        return match_statistic_data


class CornersWhileDrawByGoalsStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (матч, только периоды, пока ничья)')


    def _get_match_statistic_data(self, match_header):
        (corners_home_count, corners_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_goals_score_X), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_home_count,
            'events_away_count': corners_away_count
        }

        return match_statistic_data


class CornersWhileDrawByGoalsFirstPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (1-й тайм, пока ничья)')


    def _get_match_statistic_data(self, match_header):
        (corners_first_period_home_count, corners_first_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_first_period, is_goals_score_X), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_first_period_home_count,
            'events_away_count': corners_first_period_away_count
        }

        return match_statistic_data


class CornersWhileDrawByGoalsSecondPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _fit(self, **kwargs):
        super()._fit(**kwargs)

        get_logger('prediction').info('Добавлена информация (по каждой команде) о количестве событий "угловой" (2-й тайм, пока ничья)')


    def _get_match_statistic_data(self, match_header):
        (corners_second_period_home_count, corners_second_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_second_period, is_goals_score_X), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': corners_second_period_home_count,
            'events_away_count': corners_second_period_away_count
        }

        return match_statistic_data
