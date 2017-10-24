import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.betting.sport_util import get_substatistic
from betrobot.util.common_util import get_weights_array
from betrobot.util.logging_util import get_logger


class DiffsDiffPredictor(Predictor):

    _pick = [ 'n', 'home_weights', 'away_weights', 'min_n' ]

 
    def __init__(self, n=3, home_weights=None, away_weights=None, min_n=2, **kwargs):
        super().__init__(**kwargs)

        self.n = n
        self.home_weights = home_weights
        self.away_weights = away_weights
        self.min_n = min_n


    def _predict(self, fitteds, match_header, **kwargs):
        [ statistic_fitted ] = fitteds

        statistic = statistic_fitted.statistic
        get_logger('prediction').info('В собранной статистике %u матчей', statistic.shape[0])

        if statistic.shape[0] == 0:
            get_logger('prediction').info('В собранной статистике нет матчей, не могу сделать предсказание')
            return None

        get_logger('prediction').info('Выберем %u последних матчей из статистики, где команда %s тоже была хозяйкой', self.n, match_header['home'])
        # Статистика матчей, где match_header['home'] тоже была хозяйкой
        events_home_counts = get_substatistic(statistic, notnull=['events_home_count', 'events_away_count'], by='home', value=match_header['home'], n=self.n, min_n=self.min_n, sort_by='date', ascending=False, which=['events_home_count', 'events_away_count'])

        if events_home_counts is None:
            get_logger('prediction').info('Матчей оказалось меньше порога в %u матча', self.min_n)
            return None
        get_logger('prediction').info('Количество колинеств событий: %s', str(events_home_counts))

        events_home_diffs = events_home_counts[:, 0] - events_home_counts[:, 1]
        get_logger('prediction').info('Разницы событий: %s', str(events_home_diffs))

        home_weights_full = get_weights_array(events_home_diffs.size, self.home_weights)
        get_logger('prediction').info('Веса: %s', str(home_weights_full))
        events_home_diffs_mean = np.sum(events_home_diffs * home_weights_full)
        get_logger('prediction').info('Взвешанное среднее: %f', events_home_diffs_mean)

        get_logger('prediction').info('Выберем %u последних матчей из статистики, где команда %s тоже была гостьей', self.n, match_header['away'])
        # Статистика матчей, где match_header['away'] тоже была гостьей
        events_away_counts = get_substatistic(statistic, notnull=['events_home_count', 'events_away_count'], by='away', value=match_header['away'], n=self.n, min_n=self.min_n, sort_by='date', ascending=False, which=['events_home_count', 'events_away_count'])

        if events_away_counts is None:
            get_logger('prediction').info('Матчей оказалось меньше порога в %u матча', self.min_n)
            return None
        get_logger('prediction').info('Количество событий: %s', str(events_away_counts))

        events_away_diffs = events_away_counts[:, 0] - events_away_counts[:, 1]
        get_logger('prediction').info('Разницы количеств событий: %s', str(events_away_diffs))

        away_weights_full = get_weights_array(events_away_diffs.size, self.away_weights)
        get_logger('prediction').info('Веса: %s', str(away_weights_full))
        events_away_diffs_mean = np.sum(events_away_diffs * away_weights_full)
        get_logger('prediction').info('Взвешанное среднее: %f', events_away_diffs_mean)

        # FIXME: Проверить, так ли было раньше (посмотреть историю репозитория)
        diffs_diff_prediction = events_home_diffs_mean + events_away_diffs_mean
        get_logger('prediction').info('Итого, предсказание разницы разниц: %.1f', diffs_diff_prediction)

        return diffs_diff_prediction


    def _get_init_strs(self):
        result = []

        result.append( 'n=%u' % (self.n,) )
        if self.home_weights is not None:
            result.append( 'home_weights=[%s]' % (str(', '.join(map(str, self.home_weights))),) )
        if self.away_weights is not None:
            result.append( 'away_weights=[%s]' % (str(', '.join(map(str, self.away_weights))),) )
        result.append( 'min_n=%u' % (self.min_n,) )

        return result
