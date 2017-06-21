from abc import ABC
import numpy as np
from betrobot.betting.sport_util import get_bets


class TotalsGreaterProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Тотал', None, 'Бол', total)
            bet_pattern2 = ('*', 'Дополнительные тоталы', None, 'Бол', total)
            bets += get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
        return bets


class TotalsLesserProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Тотал', None, 'Мен', total)
            bet_pattern2 = ('*', 'Дополнительные тоталы', None, 'Мен', total)
            bets += get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
        return bets
