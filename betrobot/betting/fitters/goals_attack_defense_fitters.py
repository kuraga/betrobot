from betrobot.betting.fitters.attack_defense_fitter import AttackDefenseFitter
from betrobot.util.sport_util import is_goal, is_first_period, is_second_period


class GoalsAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        super().__init__(is_goal)


class GoalsFirstPeriodAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        def _is_first_period_goal(event):
            return is_goal(event) and is_first_period(event)

        super().__init__(_is_first_period_goal)


class GoalsSecondPeriodAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        def _is_second_period_goal(event):
            return is_goal(event) and is_first_period(event)

        super().__init__(_is_second_period_goal)
