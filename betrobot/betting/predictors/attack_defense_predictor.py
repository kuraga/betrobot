import scipy
import scipy.stats
import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.util.sport_util import get_whoscored_tournament_id_of_betcity_match, get_whoscored_teams_of_betcity_match


class AttackDefensePredictor(Predictor):

    def _predict(self, betcity_match):
        (whoscored_home, whoscored_away) = get_whoscored_teams_of_betcity_match(betcity_match)
        if whoscored_home != self.fitter.home or whoscored_away != self.fitter.away:
            return None

        mu_home = self.fitter.home_attack * self.fitter.away_defense * self.fitter.events_home_mean
        mu_away = self.fitter.away_attack * self.fitter.home_defense * self.fitter.events_away_mean

        # TODO: Подумать, какие границы у `x`
        x = np.arange(0, 20)
        pmf_home = scipy.stats.poisson(mu_home).pmf(x)
        pmf_away = scipy.stats.poisson(mu_away).pmf(x)
        prediction = np.outer(pmf_home, pmf_away)

        return prediction
