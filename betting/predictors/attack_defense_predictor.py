import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./betting/predictors')


import scipy
import scipy.stats
import numpy as np
from predictor import Predictor
from sport_util import get_whoscored_tournament_id_of_betcity_match, get_whoscored_team_ids_of_betcity_match


class AttackDefensePredictor(Predictor):
    def __init__(self):
        Predictor.__init__(self)


    def predict(self, betcity_match, fitted_data):
        tournament_id = get_whoscored_tournament_id_of_betcity_match(betcity_match)
        (whoscored_home, whoscored_away) = get_whoscored_team_ids_of_betcity_match(betcity_match)
        if tournament_id is None or whoscored_home is None or whoscored_away is None:
            return None

        teams_attack_defense, events_home_average, events_away_average = \
            fitted_data[tournament_id]['teams_attack_defense'], fitted_data[tournament_id]['events_home_average'], fitted_data[tournament_id]['events_away_average']

        teams = teams_attack_defense.index.values
        if whoscored_home not in teams or whoscored_away not in teams:
            return None

        mu_home = teams_attack_defense.loc[whoscored_home, 'home_attack'] * teams_attack_defense.loc[whoscored_away, 'away_defense'] * events_home_average
        median_home = scipy.stats.poisson.median(mu_home)
        predicted_home = int(median_home) if not np.isnan(median_home) else 0

        mu_away = teams_attack_defense.loc[whoscored_away, 'away_attack'] * teams_attack_defense.loc[whoscored_home, 'home_defense'] * events_away_average
        median_away = scipy.stats.poisson.median(mu_away)
        predicted_away = int(median_away) if not np.isnan(median_away) else 0

        return (predicted_home, predicted_away)
