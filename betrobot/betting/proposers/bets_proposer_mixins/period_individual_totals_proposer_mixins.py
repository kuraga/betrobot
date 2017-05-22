import numpy as np
from betrobot.util.sport_util import get_bets


class FirstPeriodIndividualTotalsHomeGreaterProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class FirstPeriodIndividualTotalsHomeLesserProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class FirstPeriodIndividualTotalsAwayGreaterProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class FirstPeriodIndividualTotalsAwayLesserProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class SecondPeriodIndividualTotalsHomeGreaterProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class SecondPeriodIndividualTotalsHomeLesserProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class SecondPeriodIndividualTotalsAwayGreaterProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class SecondPeriodIndividualTotalsAwayLesserProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets
