from betrobot.betting.fitters.attack_defense_fitter import AttackDefenseFitter
from betrobot.util.sport_util import is_corner, is_first_period, is_second_period


class CornersAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        corners_condition = is_corner
        AttackDefenseFitter.__init__(self, corners_condition)


class CornersFirstPeriodAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        def _is_first_period_corner(event):
            return is_corner(event) and is_first_period(event)

        AttackDefenseFitter.__init__(self, _is_first_period_corner)


class CornersSecondPeriodAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        def _is_second_period_corner(event):
            return is_corner(event) and is_first_period(event)

        AttackDefenseFitter.__init__(self, _is_second_period_corner)
