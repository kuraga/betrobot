import numpy as np
import pandas as pd
from betrobot.betting.predictor import Predictor
from betrobot.betting.sport_util import count_events_of_teams_by_match_uuid
from betrobot.util.math_util import get_weights_array
from betrobot.util.logging_util import get_logger


class CombinedResultPredictor(Predictor):

    _favorites = [
        'Juventus', 'Roma', 'Lazio', 'Napoli',
        'Manchester City', 'Manchester United', 'Chelsea', 'Arsenal', 'Liverpool', 'Tottenham',
        'Paris Saint Germain', 'Monaco', 'Lyon', 'Marseille',
        'Real Madrid', 'Barcelona', 'Atletico Madrid',
        'CSKA Moscow', 'Zenit St. Petersburg', 'Spartak Moscow', 'Lokomotiv Moscow', 'FC Krasnodar',
        'Bayer Leverkusen', 'RasenBallsport Leipzig'
    ]


    def __init__(self):
        super().__init__()

        self._match_same_location_only = False


    @staticmethod
    def _get_match_value(match_uuid, crosses_first_period_statistic, shots_first_period_statistic):
        crosses_first_period_home_count = crosses_first_period_statistic.at[match_uuid, 'events_home_count']
        crosses_first_period_away_count = crosses_first_period_statistic.at[match_uuid, 'events_away_count']
        get_logger('betting').debug('Количество кроссов в 1-м тайме: %u : %u', crosses_first_period_home_count, crosses_first_period_away_count)

        shots_first_period_home_count = shots_first_period_statistic.at[match_uuid, 'events_home_count']
        shots_first_period_away_count = shots_first_period_statistic.at[match_uuid, 'events_away_count']
        get_logger('betting').debug('Количество ударов в 1-м тайме: %u : %u', shots_first_period_home_count, shots_first_period_away_count)

        match_value = ( (crosses_first_period_home_count - crosses_first_period_away_count) + (shots_first_period_home_count - shots_first_period_away_count) ) / 2
        get_logger('betting').debug('"Значение" предыдущего матча: %f', match_value)

        return match_value


    def _predict(self, fitteds, match_header, **kwargs):
        [ crosses_first_period_statistic_fitted, shots_first_period_statistic_fitted ] = fitteds

        crosses_first_period_statistic = crosses_first_period_statistic_fitted.statistic
        shots_first_period_statistic = shots_first_period_statistic_fitted.statistic

        crosses_first_period_match_uuids = set(crosses_first_period_statistic['uuid'].values)
        shots_first_period_match_uuids = set(shots_first_period_statistic['uuid'].values)
        if crosses_first_period_match_uuids != shots_first_period_match_uuids:
            get_logger('betting').info('В собранных статистиках (кроссы, 1-й тайм; удары, 1-й тайм) - различные матчи!')
            raise RuntimeError('different matches in statistics!')

        statistic_match_headers = crosses_first_period_statistic[ ['date', 'home', 'away'] ].copy()

        get_logger('betting').info('В собранной статистике - %u матчей', statistic_match_headers.shape[0])
        if statistic_match_headers.shape[0] == 0:
            get_logger('betting').info('В собранной статистике нет матчей, не могу сделать предсказание')
            return None


        if not self._match_same_location_only:
            get_logger('betting').info('Выберем последний матч из статистики, где играла команда %s', match_header['home'])
            home_matches = statistic_match_headers[ (statistic_match_headers['home'] == match_header['home']) | (statistic_match_headers['away'] == match_header['home']) ]
        else:
            get_logger('betting').info('Выберем последний матч из статистики, где играла команда %s, причем так же дома', match_header['home'])
            home_matches = statistic_match_headers[ statistic_match_headers['home'] == match_header['home'] ]
        if home_matches.shape[0] == 0:
            get_logger('betting').info('Такого матча нет, не могу сделать предсказание')
            return None
        last_home_match_uuid = home_matches['date'].argmax()
        last_home_match = home_matches.loc[last_home_match_uuid]
        get_logger('betting').info('Предыдущий матч хозяев: %s - %s vs %s', last_home_match['date'].strftime('%Y-%m-%d'), last_home_match['home'], last_home_match['away'])

        was_last_home_match_home = match_header['home'] == last_home_match['home']
        if was_last_home_match_home:
            get_logger('betting').info('Хозяева так же играли дома в последнем матче')
            last_home_match_competitor = last_home_match['away']
        else:
            get_logger('betting').info('Хозяева играли в гостях в последнем матче')
            last_home_match_competitor = last_home_match['home']

        last_home_match_value = self._get_match_value(last_home_match_uuid, crosses_first_period_statistic, shots_first_period_statistic)
        get_logger('betting').info('"Значение" предыдущего матча хозяев: %f', last_home_match_value)
        home_number = last_home_match_value if was_last_home_match_home else -last_home_match_value
        get_logger('betting').info('"Число для хозяев": %f', home_number)

        corrected_home_number = home_number
        if not was_last_home_match_home:
            get_logger('betting').info('Последний матч хозяева играли в гостях, поэтому прибавляем 3')
            corrected_home_number += 3
        get_logger('betting').info('Ограничиваем "число для хозяев" отрезком [-7, 7]')
        corrected_home_number = np.clip(corrected_home_number, -7, 7)

        if last_home_match_competitor in self._favorites:
            return None

        get_logger('betting').info('"Число для хозяев", скорректированное: %f', corrected_home_number)


        if not self._match_same_location_only:
            get_logger('betting').info('Выберем последний матч из статистики, где играла команда %s', match_header['away'])
            away_matches = statistic_match_headers[ (statistic_match_headers['home'] == match_header['away']) | (statistic_match_headers['away'] == match_header['away']) ]
        else:
            get_logger('betting').info('Выберем последний матч из статистики, где играла команда %s, причем так же в гостях', match_header['away'])
            away_matches = statistic_match_headers[ statistic_match_headers['away'] == match_header['away'] ]
        if away_matches.shape[0] == 0:
            get_logger('betting').info('Такого матча нет, не могу сделать предсказание')
            return None
        last_away_match_uuid = away_matches['date'].argmax()
        last_away_match = away_matches.loc[last_away_match_uuid]
        get_logger('betting').info('Предыдущий матч гостей: %s - %s vs %s', last_away_match['date'].strftime('%Y-%m-%d'), last_away_match['home'], last_away_match['away'])

        was_last_away_match_away = match_header['away'] == last_away_match['away']
        if was_last_away_match_away:
            get_logger('betting').info('Гости так же играли в гостях в последнем матче')
            last_away_match_competitor = last_away_match['home']
        else:
            get_logger('betting').info('Гости играли дома в последнем матче')
            last_away_match_competitor = last_away_match['away']

        last_away_match_value = self._get_match_value(last_away_match_uuid, crosses_first_period_statistic, shots_first_period_statistic)
        get_logger('betting').info('"Значение" предыдущего матча гостей: %f', last_away_match_value)
        away_number = -last_away_match_value if was_last_away_match_away else last_away_match_value
        get_logger('betting').info('"Число для гостей": %f', away_number)

        corrected_away_number = away_number
        if not was_last_away_match_away:
            get_logger('betting').info('Последний матч гостей играли дома, поэтому отнимаем 3')
            corrected_away_number -= 3
        get_logger('betting').info('Ограничиваем "число для гостей" отрезком [-7, 7]')
        corrected_away_number = np.clip(corrected_away_number, -7, 7)

        if last_away_match_competitor in self._favorites:
            return None

        get_logger('betting').info('"Число для хозяев", скорректированное: %f', corrected_away_number)


        return (corrected_home_number, corrected_away_number)


    def _get_init_strs(self):
        result = []

        return result
