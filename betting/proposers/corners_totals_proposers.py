import numpy as np
from betting.proposers.match_proposers import CornersMatchProposer


class CornersTotalsGreaterProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=1.0):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            correct_results = [(i,j) for i in range(m) for j in range(max(int(total)+1-i+1,0), n)]
            correct_results_probabilities = probabilities[tuple(zip(*correct_results))]
            correct_total_probability = np.sum(correct_results_probabilities)
            predicted_bet_value = 1 / correct_total_probability

            bet_pattern = ('УГЛ', 'Тотал', None, 'Бол', total)
            self.propose_confident(bet_pattern, betcity_match, predicted_bet_value, whoscored_match=whoscored_match, confidence_level=confidence_level)

            bet_pattern = ('УГЛ', 'Дополнительные тоталы', None, 'Бол', total)
            self.propose_confident(bet_pattern, betcity_match, predicted_bet_value, whoscored_match=whoscored_match, confidence_level=confidence_level)


class CornersTotalsLesserProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=1.0):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            correct_results = [(i,j) for i in range(m) for j in range(0, min(int(total)-i,n))]
            correct_results_probabilities = probabilities[tuple(zip(*correct_results))]
            correct_total_probability = np.sum(correct_results_probabilities)
            predicted_bet_value = 1 / correct_total_probability

            bet_pattern = ('УГЛ', 'Тотал', None, 'Мен', total)
            self.propose_confident(bet_pattern, betcity_match, predicted_bet_value, whoscored_match=whoscored_match, confidence_level=confidence_level)

            bet_pattern = ('УГЛ', 'Дополнительные тоталы', None, 'Мен', total)
            self.propose_confident(bet_pattern, betcity_match, predicted_bet_value, whoscored_match=whoscored_match, confidence_level=confidence_level)
