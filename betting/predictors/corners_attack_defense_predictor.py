from betting.predictors.attack_defense_predictor import AttackDefensePredictor
from util.sport_util import is_betarch_match_corner


class CornersAttackDefensePredictor(AttackDefensePredictor):

    def predict(self, betcity_match, fitted_data):
        if not is_betarch_match_corner(betcity_match):
            return

        return super().predict(betcity_match, fitted_data)
