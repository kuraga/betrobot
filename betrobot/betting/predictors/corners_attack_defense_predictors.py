from betrobot.betting.predictors.match_predictors import CornersMatchPredictor
from betrobot.betting.predictors.attack_defense_predictor import AttackDefensePredictor


class CornersResultProbabilitiesAttackDefensePredictor(CornersMatchPredictor):

    _pick = [ '_corners_attack_defense_predictor' ]


    def __init__(self):
        super().__init__()

        self._corners_attack_defense_predictor = AttackDefensePredictor()


    def _predict(self, betcity_match, fitted_datas, **kwargs):
        # fitted_datas содержит один элемент - данные по угловым
        # Для каждого элемента fitted_datas будет получено свое предсказание
        predictions = self._corners_attack_defense_predictor.predict(betcity_match, fitted_datas, **kwargs)

        return predictions[0]
