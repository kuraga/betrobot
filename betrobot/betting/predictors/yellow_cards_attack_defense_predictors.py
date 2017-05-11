from betrobot.betting.predictors.match_predictors import YellowCardsMatchPredictor
from betrobot.betting.predictors.attack_defense_predictor import AttackDefensePredictor


class YellowCardsResultProbabilitiesAttackDefensePredictor(YellowCardsMatchPredictor):

    _pick = [ '_yellow_cards_attack_defense_predictor' ]


    def __init__(self):
         super().__init__()

         self._yellow_cards_attack_defense_predictor = AttackDefensePredictor()


    def _predict(self, fitteds, betcity_match):
         return self._yellow_cards_attack_defense_predictor._predict(fitteds, betcity_match)
