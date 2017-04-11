import numpy as np
from betrobot.util.math_util import sum_submatrix


class TotalsGreaterProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Тотал', None, 'Бол', total)
            bet_pattern2 = ('*', 'Дополнительные тоталы', None, 'Бол', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
            predicted_probability = sum_submatrix(probabilities, correct_results)

            if predicted_probability > 0:
                self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class TotalsLesserProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Тотал', None, 'Мен', total)
            bet_pattern2 = ('*', 'Дополнительные тоталы', None, 'Мен', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
            predicted_probability = sum_submatrix(probabilities, correct_results)

            if predicted_probability > 0:
                self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
