import scipy
import scipy.stats
import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.util.sport_util import get_whoscored_tournament_id_of_betcity_match, get_whoscored_team_ids_of_betcity_match


class AttackDefensePredictor(Predictor):

    # FIXME: Подумать, какие границы у `x`
    def _predict(self, betcity_match, fitted_data, x=np.arange(0, 20)):
        tournament_id = get_whoscored_tournament_id_of_betcity_match(betcity_match)
        (whoscored_home, whoscored_away) = get_whoscored_team_ids_of_betcity_match(betcity_match)
        if tournament_id is None or whoscored_home is None or whoscored_away is None:
            return None

        teams_attack_defense, events_home_mean, events_away_mean = \
            fitted_data[tournament_id]['teams_attack_defense'], fitted_data[tournament_id]['events_home_mean'], fitted_data[tournament_id]['events_away_mean']

        teams = teams_attack_defense.index.values
        if whoscored_home not in teams or whoscored_away not in teams:
            return None

        mu_home = teams_attack_defense.loc[whoscored_home, 'home_attack'] * teams_attack_defense.loc[whoscored_away, 'away_defense'] * events_home_mean
        mu_away = teams_attack_defense.loc[whoscored_away, 'away_attack'] * teams_attack_defense.loc[whoscored_home, 'home_defense'] * events_away_mean

        pmf_home = scipy.stats.poisson(mu_home).pmf(x)
        pmf_away = scipy.stats.poisson(mu_away).pmf(x)
        prediction = np.outer(pmf_home, pmf_away)

        return prediction
