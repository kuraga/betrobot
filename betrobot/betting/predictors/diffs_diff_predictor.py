import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.util.sport_util import get_whoscored_tournament_id_of_betcity_match, get_whoscored_teams_of_betcity_match
from betrobot.util.math_util import get_weights_array


class DiffsDiffPredictor(Predictor):

    _pick = [ 'home_weights', 'away_weights' ]

 
    def __init__(self, home_weights=None, away_weights=None):
        super().__init__()

        self.home_weights = home_weights
        self.away_weights = away_weights


    def _predict(self, fitteds, betcity_match):
        [ diffs_fitted ] = fitteds

        if diffs_fitted.home is None or diffs_fitted.away is None or diffs_fitted.events_home_diffs is None or diffs_fitted.events_away_diffs is None:
            return None

        (whoscored_home, whoscored_away) = get_whoscored_teams_of_betcity_match(betcity_match)
        if whoscored_home != diffs_fitted.home or whoscored_away != diffs_fitted.away:
            return None

        home_weights_full = get_weights_array(diffs_fitted.events_home_diffs.size, self.home_weights)
        events_home_diffs_mean = np.sum(diffs_fitted.events_home_diffs * home_weights_full)

        away_weights_full = get_weights_array(diffs_fitted.events_away_diffs.size, self.away_weights)
        events_away_diffs_mean = np.sum(diffs_fitted.events_away_diffs * away_weights_full)

        diff_prediction = events_home_diffs_mean + events_away_diffs_mean

        return diff_prediction


    def _get_init_strs(self):
        result = []
        if self.home_weights is not None:
            strs.append( 'home_weights=[%s]' % (str(', '.join(map(str, self.home_weights))),) )
        if self.away_weights is not None:
            strs.append( 'away_weights=[%s]' % (str(', '.join(map(str, self.away_weights))),) )
        return result
