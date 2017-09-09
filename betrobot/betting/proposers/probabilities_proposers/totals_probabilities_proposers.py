import numpy as np
from betrobot.betting.proposers.probabilities_proposers.probabilities_proposer import ProbabilityProposer
from betrobot.util.math_util import sum_submatrix


class TotalsGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        (m, n) = probabilities.shape
        total = bet[4]

        positive_result_indexes = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
        probability_prediction = sum_submatrix(probabilities_prediction, positive_result_indexes)

        self.propose(bet, match_header, **kwargs)


class TotalsLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        (m, n) = probabilities.shape
        total = bet[4]

        positive_result_indexes = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
        probability_prediction = sum_submatrix(probabilities_prediction, positive_result_indexes)

        self.propose(bet, match_header, **kwargs)
