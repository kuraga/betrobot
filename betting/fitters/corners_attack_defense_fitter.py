from betting.fitters.attack_defense_fitter import AttackDefenseFitter
from util.sport_util import is_corner


class CornersAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        corners_condition = is_corner
        AttackDefenseFitter.__init__(self, corners_condition)
