import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.util.sport_util import get_whoscored_tournament_id_of_betcity_match, get_whoscored_teams_of_betcity_match


class DiffsDiffPredictor(Predictor):

    def _predict(self, fitteds, betcity_match):
        [ diffs_fitted ] = fitteds

        (whoscored_home, whoscored_away) = get_whoscored_teams_of_betcity_match(betcity_match)
        if whoscored_home != diffs_fitted.home or whoscored_away != diffs_fitted.away:
            return None

        if diffs_fitted.home_diffs_mean is None or diffs_fitted.away_diffs_mean is None:
            return None

        prediction = diffs_fitted.home_diffs_mean - diffs_fitted.away_diffs_mean

        return prediction
