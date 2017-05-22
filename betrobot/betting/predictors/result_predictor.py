import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.util.sport_util import get_whoscored_tournament_id_of_betcity_match, get_whoscored_teams_of_betcity_match


class ResultPredictor(Predictor):

    def _predict(self, fitteds, betcity_match):
        [ results_fitted ] = fitteds

        (whoscored_home, whoscored_away) = get_whoscored_teams_of_betcity_match(betcity_match)
        if whoscored_home != results_fitted.home or whoscored_away != results_fitted.away:
            return None

        if results_fitted.events_home_counts_mean is None or results_fitted.events_away_counts_mean is None:
            return None

        result_prediction = (results_fitted.events_home_counts_mean, results_fitted.events_away_counts_mean)

        return result_prediction
