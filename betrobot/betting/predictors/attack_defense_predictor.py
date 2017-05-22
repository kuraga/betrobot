import scipy
import scipy.stats
import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.util.sport_util import get_whoscored_tournament_id_of_betcity_match, get_whoscored_teams_of_betcity_match


class AttackDefensePredictor(Predictor):

    def _predict(self, fitteds, betcity_match):
        [ attack_defense_fitted ] = fitteds

        (whoscored_home, whoscored_away) = get_whoscored_teams_of_betcity_match(betcity_match)
        if whoscored_home != attack_defense_fitted.home or whoscored_away != attack_defense_fitted.away:
            return None

        if attack_defense_fitted.home_attack is None or attack_defense_fitted.away_defense is None or attack_defense_fitted.events_home_mean is None or attack_defense_fitted.away_attack is None or attack_defense_fitted.home_defense is None or attack_defense_fitted.events_away_mean is None:
            return None

        mu_home = attack_defense_fitted.home_attack * attack_defense_fitted.away_defense * attack_defense_fitted.events_home_mean
        mu_away = attack_defense_fitted.away_attack * attack_defense_fitted.home_defense * attack_defense_fitted.events_away_mean

        x = np.arange(0, 20)
        pmf_home = scipy.stats.poisson(mu_home).pmf(x)
        pmf_away = scipy.stats.poisson(mu_away).pmf(x)
        prediction = np.outer(pmf_home, pmf_away)

        return prediction
