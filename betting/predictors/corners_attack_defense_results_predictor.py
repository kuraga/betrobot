import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./betting/predictors')


from attack_defense_predictor import AttackDefensePredictor
from sport_util import is_betarch_match_corner


class CornersResultsAttackDefensePredictor(AttackDefensePredictor):
    def __init__(self):
        AttackDefensePredictor.__init__(self)


    def predict(self, betcity_match, fitted_data):
        if not is_betarch_match_corner(betcity_match):
            return

        return super().predict(betcity_match, fitted_data)
