import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.betting.sport_util import get_substatistic
from betrobot.util.common_util import get_weights_array
from betrobot.util.logging_util import get_logger


class AttackDefenseResultsResultPredictor(Predictor):

    _pick = [ 'n', 'home_weights', 'away_weights', 'min_n' ]

 
    def __init__(self, n=3, home_weights=None, away_weights=None, min_n=2, **kwargs):
        super().__init__(**kwargs)

        self.n = n
        self.home_weights = home_weights
        self.away_weights = away_weights
        self.min_n = min_n


    def _predict(self, fitteds, match_header, **kwargs):
        [ statistic_fitted, tournament_event_counts_means_fitted ] = fitteds

        statistic = statistic_fitted.statistic
        get_logger('prediction').info('В собранной статистике %u матчей', statistic.shape[0])

        if statistic.shape[0] == 0:
            get_logger('prediction').info('В собранной статистике нет матчей, не могу сделать предсказание')
            return None


        tournament_id = match_header['tournamentId']

        # Среднее количество голов, забиваемых хозяевами матчей в турнире
        tournament_events_home_counts_mean = tournament_event_counts_means_fitted.tournament_event_home_counts_means[tournament_id]
        # Среднее количество голов, забиваемых гостями матчей в турнире
        tournament_events_away_counts_mean = tournament_event_counts_means_fitted.tournament_event_away_counts_means[tournament_id]

        if tournament_events_home_counts_mean == 0 or tournament_events_away_counts_mean == 0:
            return None


        get_logger('prediction').info('Выберем %u последних матчей из статистики, где команда %s тоже была хозяйкой', self.n, match_header['home'])
        # Статистика матчей, где match_header['home'] тоже была хозяйкой
        home_events_counts = get_substatistic(statistic, notnull='events_home_count', by='home', value=match_header['home'], n=self.n, min_n=self.min_n, sort_by='date', ascending=False, which='events_home_count')

        if home_events_counts is None:
            get_logger('prediction').info('Матчей оказалось меньше порога в %u матча', self.min_n)
            return None
        get_logger('prediction').info('Количество событий: %s', str(home_events_counts))

        home_weights_full = get_weights_array(home_events_counts.size, self.home_weights)
        get_logger('prediction').info('Веса: %s', str(home_weights_full))


        get_logger('prediction').info('Выберем %u последних матчей из статистики, где команда %s тоже была гостьей', self.n, match_header['away'])
        # Статистика матчей, где match_header['away'] тоже была гостьей
        away_events_counts = get_substatistic(statistic, notnull='events_away_count', by='away', value=match_header['away'], n=self.n, min_n=self.min_n, sort_by='date', ascending=False, which='events_away_count')

        if away_events_counts is None:
            get_logger('prediction').info('Матчей оказалось меньше порога в %u матча', self.min_n)
            return None
        get_logger('prediction').info('Количество событий: %s', str(away_events_counts))

        away_weights_full = get_weights_array(away_events_counts.size, self.away_weights)
        get_logger('prediction').info('Веса: %s', str(away_weights_full))


        # Во сколько раз превышает среднее по турниру число голов, забитых match_header['home'] в домашних матчах?
        home_attack = np.sum(home_events_counts * home_weights_full) / tournament_events_home_counts_mean
        # Во сколько раз превышает среднее по турниру число голов, пропущенных match_header['away'] в гостевых матчах?
        away_defense = np.sum(home_events_counts * home_weights_full) / tournament_events_home_counts_mean
        # Во сколько раз превышает среднее по турниру число голов, пропущенных match_header['home'] в домашних матчах?
        home_defense = np.sum(away_events_counts * away_weights_full) / tournament_events_away_counts_mean
        # Во сколько раз превышает среднее по турниру число голов, забитых match_header['away'] в гостевых матчах?
        away_attack = np.sum(away_events_counts * away_weights_full) / tournament_events_away_counts_mean

        home_events_count_prediction = home_attack * away_defense * tournament_events_home_counts_mean
        away_events_count_prediction = away_attack * home_defense * tournament_events_away_counts_mean


        result_prediction = (home_events_count_prediction, away_events_count_prediction)
        get_logger('prediction').info('Итого, предсказание: %.1f:%.1f', result_prediction[0], result_prediction[1])

        return result_prediction


    def _get_init_strs(self):
        result = []

        result.append( 'n=%u' % (self.n,) )
        if self.home_weights is not None:
            result.append( 'home_weights=[%s]' % (str(', '.join(map(str, self.home_weights))),) )
        if self.away_weights is not None:
            result.append( 'away_weights=[%s]' % (str(', '.join(map(str, self.away_weights))),) )
        result.append( 'min_n=%u' % (self.min_n,) )

        return result
