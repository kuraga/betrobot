from betrobot.betting.predictors.match_predictor_mixins import CornersMatchPredictorMixin
from betrobot.betting.predictors.probabilities_via_result_predictor import ProbabilitiesViaResultPredictor
from betrobot.betting.predictors.corners_attack_defense_result_predictors import CornersAttackDefenseResultPredictor, CornersViaPassesAttackDefenseResultPredictor


class CornersAttackDefenseProbabilitiesPredictor(CornersMatchPredictorMixin, ProbabilitiesViaResultPredictor):

    def __init__(self, *args, **kwargs):
       corners_attack_defense_result_predictor = CornersAttackDefenseResultPredictor(*args, **kwargs)

       super().__init__(corners_attack_defense_result_predictor)


class CornersViaPassesAttackDefenseProbabilitiesPredictor(CornersMatchPredictorMixin, ProbabilitiesViaResultPredictor):

    def __init__(self, *args, **kwargs):
       corners_via_passes_attack_defense_result_predictor = CornersViaPassesAttackDefenseResultPredictor(*args, **kwargs)

       super().__init__(corners_via_passes_attack_defense_result_predictor)
