import numpy as np
from betrobot.util.math_util import sum_submatrix


class IndividualTotalsHomeGreaterProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['home'], 'Бол', individual_total)

            correct_results = [(i,j) for i in range(int(np.ceil(individual_total)), m) for j in range(0, n)]
            predicted_probability = sum_submatrix(probabilities, correct_results)

            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class IndividualTotalsHomeLesserProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['home'], 'Мен', individual_total)

            correct_results = [(i,j) for i in range(0, int(np.floor(individual_total))) for j in range(0, n)]
            predicted_probability = sum_submatrix(probabilities, correct_results)

            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class IndividualTotalsAwayGreaterProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['away'], 'Бол', individual_total)

            correct_results = [(i,j) for i in range(0, m) for j in range(int(np.ceil(individual_total)), n)]
            predicted_probability = sum_submatrix(probabilities, correct_results)

            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class IndividualTotalsAwayLesserProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Индивидуальный тотал', betcity_match['away'], 'Мен', individual_total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, int(np.floor(individual_total)))]
            predicted_probability = sum_submatrix(probabilities, correct_results)

            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
