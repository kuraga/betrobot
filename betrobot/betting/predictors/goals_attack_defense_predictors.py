from betrobot.betting.predictors.match_predictors import GoalsMatchPredictor
from betrobot.betting.predictors.attack_defense_predictor import AttackDefensePredictor


class GoalsResultProbabilitiesAttackDefensePredictor(GoalsMatchPredictor):

    _pick = [ '_goals_attack_defense_predictor' ]


    def __init__(self):
         super().__init__()

         self._goals_attack_defense_predictor = AttackDefensePredictor()


    def _predict(self, fitteds, betcity_match):
         return self._goals_attack_defense_predictor._predict(fitteds, betcity_match)
