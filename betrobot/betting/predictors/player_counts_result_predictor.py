import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.betting.sport_util import get_additional_info, get_substatistic
from betrobot.util.math_util import get_weights_array
from betrobot.util.logging_util import get_logger


class PlayerCountsResultPredictor(Predictor):

    _pick = [ 'n', 'weights', 'min_n', 'min_real_players' ]

 
    def __init__(self, n=None, weights=None, min_n=2,  min_real_players=8):
        super().__init__()

        self.n = n
        self.weights = weights
        self.min_n = min_n
        self.min_real_players = min_real_players


    def _predict(self, fitteds, match_header, **kwargs):
        [ statistic_fitted ] = fitteds

        statistic = statistic_fitted.statistic
        get_logger('prediction').info('В собранной статистике %u матчей', statistic.shape[0])

        if statistic.shape[0] == 0:
            get_logger('prediction').info('В собранной статистике нет матчей, не могу сделать предсказание')
            return None

        additional_info = get_additional_info(match_header['uuid'])
        if additional_info is None:
            return None
        if 'homePlayers' not in additional_info or 'awayPlayers' not in additional_info:
            get_logger('prediction').info('В матче не известен состав игроков, не могу сделать предсказание')
            return None

        home_player_names = [ player['playerName'] for player in additional_info['homePlayers'] if player['isFirstEleven'] ]
        get_logger('prediction').info('Игроки хозяев: %s', str(home_player_names))
        away_player_names = [ player['playerName'] for player in additional_info['awayPlayers'] if player['isFirstEleven'] ]
        get_logger('prediction').info('Игроки гостей: %s', str(away_player_names))
        if len(home_player_names) != 11 or len(away_player_names) != 11:
            print('Bad players count in match %s' % (match_header['uuid'],))
            get_logger('prediction').info('В матче неверное количество игроков (известны не все игроки?), не могу сделать предсказание')
            return None

        events_home_counts = []
        get_logger('prediction').info('Рассчитаем среднее по игрокам хозяев')
        for player_name in frozenset(statistic.columns.values) & frozenset(home_player_names):
            if self.n is not None:
                get_logger('prediction').info('Выберем %u последних матчей из статистики игрока %s', self.n, player_name)
            else:
                get_logger('prediction').info('Выберем всю статистику игрока %s', player_name)
            events_player_counts = get_substatistic(statistic, n=self.n, min_n=self.min_n, sort_by='date', ascending=False, which=player_name, notnull=player_name)
            if events_player_counts is None:
                get_logger('prediction').info('Матчей оказалось меньше порога в %u матча', self.min_n)
                continue

            weights_full = get_weights_array(events_player_counts.shape[0], self.weights)
            get_logger('prediction').info('Веса: %s', str(weights_full))
            events_player_counts_mean = np.sum(events_player_counts * weights_full)
            get_logger('prediction').info('Взвешанное среднее: %s', str(events_player_counts_mean))

            events_home_counts.append(events_player_counts_mean)

        get_logger('prediction').info('Получили следующие средние для игроков хозяев (%u значений): %s', len(events_home_counts), events_home_counts)
        if len(events_home_counts) < self.min_real_players:
            get_logger('prediction').info('Значений оказалось меньше порога в %u матча', self.min_real_players)
            return None
        events_home_counts_mean = np.mean(events_home_counts)
        get_logger('prediction').info('Среднее для хозяев: %f', events_home_counts_mean)

        events_away_counts = []
        get_logger('prediction').info('Рассчитаем среднее по игрокам гостей')
        for player_name in frozenset(statistic.columns.values) & frozenset(away_player_names):
            if self.n is not None:
                get_logger('prediction').info('Выберем %u последних матчей из статистики игрока %s', self.n, player_name)
            else:
                get_logger('prediction').info('Выберем всю статистику игрока %s', player_name)
            events_player_counts = get_substatistic(statistic, n=self.n, min_n=self.min_n, sort_by='date', ascending=False, which=player_name, notnull=player_name)
            if events_player_counts is None:
                get_logger('prediction').info('Матчей оказалось меньше порога в %u матча', self.min_n)
                continue

            weights_full = get_weights_array(events_player_counts.shape[0], self.weights)
            get_logger('prediction').info('Веса: %s', str(weights_full))
            events_player_counts_mean = np.sum(events_player_counts * weights_full)
            get_logger('prediction').info('Взвешанное среднее: %s', str(events_player_counts_mean))

            events_away_counts.append(events_player_counts_mean)

        get_logger('prediction').info('Получили следующие средние для игроков гостей (%u значений): %s', len(events_away_counts), events_away_counts)
        if len(events_away_counts) < self.min_real_players:
            get_logger('prediction').info('Значений оказалось меньше порога в %u матча', self.min_real_players)
            return None
        events_away_counts_mean = np.mean(events_away_counts)
        get_logger('prediction').info('Среднее для гостей: %f', events_away_counts_mean)

        result_prediction = (events_home_counts_mean, events_away_counts_mean)
        get_logger('prediction').info('Итого, предсказание: %.1f:%.1f', result_prediction[0], result_prediction[1])

        return result_prediction


    def _get_init_strs(self):
        result = []

        if self.n is not None:
            result.append( 'n=[%u]' % (self.n,) )
        if self.weights is not None:
            result.append( 'weights=[%s]' % (str(', '.join(map(str, self.weights))),) )
        if self.min_n is not None:
            result.append( 'min_n=%u' % (self.min_n,) )
        if self.min_real_players is not None:
            result.append( 'min_real_players=%u' % (self.min_real_players,) )

        return result
