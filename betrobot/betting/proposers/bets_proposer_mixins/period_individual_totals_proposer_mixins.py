from abc import ABC
import numpy as np
from betrobot.betting.sport_util import get_bets


class FirstPeriodIndividualTotalsHomeGreaterProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class FirstPeriodIndividualTotalsHomeLesserProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class FirstPeriodIndividualTotalsAwayGreaterProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class FirstPeriodIndividualTotalsAwayLesserProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class SecondPeriodIndividualTotalsHomeGreaterProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class SecondPeriodIndividualTotalsHomeLesserProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class SecondPeriodIndividualTotalsAwayGreaterProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class SecondPeriodIndividualTotalsAwayLesserProposerMixin(ABC):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets
