from betting.predictors.match_predictors import CornersMatchPredictor
from betting.predictors.attack_defense_predictor import AttackDefensePredictor
from util.sport_util import is_betarch_match_corner


class CornersAttackDefensePredictor(CornersMatchPredictor, AttackDefensePredictor):
    pass


class CornersFirstPeriodAttackDefensePredictor(CornersMatchPredictor, AttackDefensePredictor):
    pass


class CornersSecondPeriodAttackDefensePredictor(CornersMatchPredictor, AttackDefensePredictor):
    pass
