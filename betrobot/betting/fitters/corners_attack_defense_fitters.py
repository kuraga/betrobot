from betrobot.betting.fitters.attack_defense_fitter import AttackDefenseFitter
from betrobot.util.sport_util import is_corner, is_first_period, is_second_period


class CornersAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        super().__init__(is_corner)


class CornersFirstPeriodAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        def _is_first_period_corner(event):
            return is_corner(event) and is_first_period(event)

        super().__init__(_is_first_period_corner)


class CornersSecondPeriodAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        def _is_second_period_corner(event):
            return is_corner(event) and is_first_period(event)

        super().__init__(_is_second_period_corner)
