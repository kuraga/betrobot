from abc import ABC
import numpy as np
from betrobot.betting.sport_util import get_bets


class IndividualTotalsHomeGreaterProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['home'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class IndividualTotalsHomeLesserProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['home'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class IndividualTotalsAwayGreaterProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['away'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class IndividualTotalsAwayLesserProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['away'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets
