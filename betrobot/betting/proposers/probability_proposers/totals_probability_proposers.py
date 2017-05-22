import numpy as np
from betrobot.betting.proposers.probability_proposers.probability_proposer import ProbabilityProposer
from betrobot.util.math_util import sum_submatrix


class TotalsGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class TotalsLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)
