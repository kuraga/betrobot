from betrobot.betting.predictors.match_predictors import MainMatchPredictor
from betrobot.betting.predictors.attack_defense_predictor import AttackDefensePredictor


class GoalsResultProbabilitiesAttackDefensePredictor(MainMatchPredictor):

    _pick = [ '_goals_attack_defense_predictor' ]


    def __init__(self):
        super.__init__()

        self._goals_attack_defense_predictor = AttackDefensePredictor()


    def _predict(self, betcity_match, fitted_datas, **kwargs):
        # fitted_datas содержит один элемент - данные по голам
        # Для каждого элемента fitted_datas будет получено свое предсказание
        predictions = self._goals_attack_defense_predictor.predict(betcity_match, fitted_datas, **kwargs)

        return predictions[0]
