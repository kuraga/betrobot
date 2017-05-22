import numpy as np
from betrobot.util.sport_util import get_bets


class IndividualTotalsHomeGreaterProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['home'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class IndividualTotalsHomeLesserProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['home'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class IndividualTotalsAwayGreaterProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['away'], 'Бол', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets


class IndividualTotalsAwayLesserProposerMixin(object):

    def _get_bets(self, betcity_match):
        bets = []
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['away'], 'Мен', individual_total)
            bets += get_bets(bet_pattern, betcity_match)
        return bets
