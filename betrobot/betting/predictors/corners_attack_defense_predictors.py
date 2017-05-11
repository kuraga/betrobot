from betrobot.betting.predictors.match_predictors import CornersMatchPredictor
from betrobot.betting.predictors.attack_defense_predictor import AttackDefensePredictor


class CornersResultProbabilitiesAttackDefensePredictor(CornersMatchPredictor):

    _pick = [ '_corners_attack_defense_predictor' ]


    def __init__(self):
         super().__init__()

         self._corners_attack_defense_predictor = AttackDefensePredictor()


    def _predict(self, fitteds, betcity_match):
         return self._corners_attack_defense_predictor._predict(fitteds, betcity_match)
