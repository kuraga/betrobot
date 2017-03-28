from betrobot.betting.fitters.attack_defense_fitter import AttackDefenseFitter
from betrobot.util.sport_util import is_yellow_card, is_first_period, is_second_period


class YellowCardsAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        yellow_cards_condition = is_yellow_card
        AttackDefenseFitter.__init__(self, yellow_cards_condition)


class YellowCardsFirstPeriodAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        def _is_first_period_yellow_card(event):
            return is_yellow_card(event) and is_first_period(event)

        AttackDefenseFitter.__init__(self, _is_first_period_yellow_card)


class YellowCardsSecondPeriodAttackDefenseFitter(AttackDefenseFitter):

    def __init__(self):
        def _is_second_period_yellow_card(event):
            return is_yellow_card(event) and is_first_period(event)

        AttackDefenseFitter.__init__(self, _is_second_period_yellow_card)
