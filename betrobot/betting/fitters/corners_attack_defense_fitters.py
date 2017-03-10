from betrobot.betting.fitters.attack_defense_fitter import AttackDefenseFitter
from betrobot.util.sport_util import is_corner, is_first_period, is_second_period


class CornersAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self, **kwargs):
        corners_condition = is_corner
        AttackDefenseFitter.__init__(self, corners_condition, **kwargs)


def _is_first_period_corner(event):
    return is_corner(event) and is_first_period(event)


class CornersFirstPeriodAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self, **kwargs):
        AttackDefenseFitter.__init__(self, _is_first_period_corner, **kwargs)


def _is_second_period_corner(event):
    return is_corner(event) and is_first_period(event)


class CornersSecondPeriodAttackDefenseFitter(AttackDefenseFitter):


    def __init__(self, **kwargs):
        AttackDefenseFitter.__init__(self, _is_second_period_corner, **kwargs)

