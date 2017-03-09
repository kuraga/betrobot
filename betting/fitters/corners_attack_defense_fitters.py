from betting.fitters.attack_defense_fitter import AttackDefenseFitter
from util.sport_util import is_corner, is_first_period, is_second_period


class CornersAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self, **kwargs):
        corners_condition = is_corner
        AttackDefenseFitter.__init__(self, corners_condition, **kwargs)


class CornersFirstPeriodAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self, **kwargs):
        corners_condition = lambda event: is_corner(event) and is_first_period(event)
        AttackDefenseFitter.__init__(self, corners_condition, **kwargs)


class CornersSecondPeriodAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self, **kwargs):
        corners_condition = lambda event: is_corner(event) and is_second_period(event)
        AttackDefenseFitter.__init__(self, corners_condition, **kwargs)
