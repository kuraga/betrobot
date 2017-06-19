import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.util.sport_util import get_teams_tournaments_countries_value
from betrobot.util.math_util import get_weights_array


class ResultPredictor(Predictor):

    _pick = [ 'home_weights', 'away_weights' ]

 
    def __init__(self, home_weights=None, away_weights=None):
        super().__init__()

        self.home_weights = home_weights
        self.away_weights = away_weights


    def _predict(self, fitteds, betcity_match):
        [ counts_fitted ] = fitteds

        if counts_fitted.home is None or counts_fitted.away is None or counts_fitted.events_home_counts is None or counts_fitted.events_away_counts is None:
            return None

        whoscored_home = get_teams_tournaments_countries_value('betcityName', betcity_match['home'], 'whoscoredName')
        whoscored_away = get_teams_tournaments_countries_value('betcityName', betcity_match['away'], 'whoscoredName')
        if whoscored_home is None or whoscored_away is None:
            return None

        if whoscored_home != counts_fitted.home or whoscored_away != counts_fitted.away:
            return None

        home_weights_full = get_weights_array(counts_fitted.events_home_counts.size, self.home_weights)
        events_home_counts_mean = np.sum(counts_fitted.events_home_counts * home_weights_full)

        away_weights_full = get_weights_array(counts_fitted.events_away_counts.size, self.away_weights)
        events_away_counts_mean = np.sum(counts_fitted.events_away_counts * away_weights_full)

        result_prediction = (events_home_counts_mean, events_away_counts_mean)

        return result_prediction


    def _get_init_strs(self):
        result = []
        if self.home_weights is not None:
            strs.append( 'home_weights=[%s]' % (str(', '.join(map(str, self.home_weights))),) )
        if self.away_weights is not None:
            strs.append( 'away_weights=[%s]' % (str(', '.join(map(str, self.away_weights))),) )
        return result
