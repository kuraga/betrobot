import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.betting.sport_util import get_additional_info, get_substatistic
from betrobot.util.math_util import get_weights_array


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
        if statistic.shape[0] == 0:
            return None

        additional_info = get_additional_info(match_header['uuid'])
        if additional_info is None:
            return None
        if 'homePlayers' not in additional_info or 'awayPlayers' not in additional_info:
            return None

        home_player_names = [ player['playerName'] for player in additional_info['homePlayers'] if player['isFirstEleven'] ]
        away_player_names = [ player['playerName'] for player in additional_info['awayPlayers'] if player['isFirstEleven'] ]
        if len(home_player_names) != 11 or len(away_player_names) != 11:
            print('Bad players count in match %s' % (match_header['uuid'],))
            return None

        known_home_players_count = 0
        events_home_counts_mean = 0
        for player_name in (frozenset(statistic_fitted.statistic.columns.values) & frozenset(home_player_names)):
            events_player_counts = get_substatistic(statistic, n=self.n, sort_by='date', ascending=False, which=player_name, notnull=player_name)
            if events_player_counts is None:
                continue
            if len(events_player_counts) < self.min_n:
                continue
            known_home_players_count += 1

            weights_full = get_weights_array(events_player_counts.shape[0], self.weights)
            events_home_counts_mean += np.sum(events_player_counts * weights_full)
        if known_home_players_count < self.min_real_players:
            return None

        known_away_players_count = 0
        events_away_counts_mean = 0
        for player_name in (frozenset(statistic_fitted.statistic.columns.values) & frozenset(away_player_names)):
            events_player_counts = get_substatistic(statistic, n=self.n, sort_by='date', ascending=False, which=player_name, notnull=player_name)
            if events_player_counts is None:
                continue
            if len(events_player_counts) < self.min_n:
                continue
            known_away_players_count += 1

            weights_full = get_weights_array(events_player_counts.shape[0], self.weights)
            events_away_counts_mean += np.sum(events_player_counts * weights_full)
        if known_away_players_count < self.min_real_players:
            return None

        result_prediction = (events_home_counts_mean, events_away_counts_mean)

        return result_prediction


    def _get_init_strs(self):
        result = []

        if self.n is not None:
            result.append( 'n=[%u]' % (self.n,) )
        if self.weights is not None:
            result.append( 'weights=[%s]' % (str(', '.join(map(str, self.weights))),) )
        if self.min_n is not None:
            result.append( 'n=[%u]' % (self.min_n,) )
        if self.min_real_players is not None:
            result.append( 'n=[%u]' % (self.min_real_players,) )

        return result
