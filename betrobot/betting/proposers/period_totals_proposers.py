import numpy as np
from betrobot.util.sport_util import get_bets
from betrobot.util.math_util import sum_submatrix


class FirstPeriodTotalsGreaterProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for period_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', '', 'Бол', period_total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(period_total))-i+1,0), n)]
            predicted_probability = sum_submatrix(probabilities, correct_results)

            if predicted_probability > 0:
                self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class FirstPeriodTotalsLesserProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for period_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', '', 'Мен', period_total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(period_total))-i,n))]
            predicted_probability = sum_submatrix(probabilities, correct_results)

            if predicted_probability > 0:
                self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodTotalsGreaterProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for period_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', '', 'Бол', period_total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(period_total))-i+1,0), n)]
            predicted_probability = sum_submatrix(probabilities, correct_results)

            if predicted_probability > 0:
                self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodTotalsLesserProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for period_total in np.arange(0, 20.5, 0.5):
            bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', '', 'Мен', period_total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(period_total))-i,n))]
            predicted_probability = sum_submatrix(probabilities, correct_results)

            if predicted_probability > 0:
                self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
