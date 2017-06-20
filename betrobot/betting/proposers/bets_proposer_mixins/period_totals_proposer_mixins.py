import numpy as np
from betrobot.betting.sport_util import get_bets


class FirstPeriodTotalsGreaterProposerMixin:

    def _get_bets(self, betcity_match):
        bets = []
        for period_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', None, 'Бол', period_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class FirstPeriodTotalsLesserProposerMixin:

    def _get_bets(self, betcity_match):
        bets = []
        for period_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', None, 'Мен', period_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class SecondPeriodTotalsGreaterProposerMixin:

    def _get_bets(self, betcity_match):
        bets = []
        for period_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', None, 'Бол', period_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class SecondPeriodTotalsLesserProposerMixin:

    def _get_bets(self, betcity_match):
        bets = []
        for period_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', None, 'Мен', period_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets
