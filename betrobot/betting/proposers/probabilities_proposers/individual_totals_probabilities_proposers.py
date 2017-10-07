import numpy as np
from betrobot.betting.proposers.probabilities_proposers.probabilities_proposer import ProbabilityProposer
from betrobot.util.common_util import sum_submatrix


class IndividualTotalsHomeGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        (m, n) = probabilities_prediction.shape
        individual_total = bet[5]

        positive_result_indexes = [(i,j) for i in range(int(np.ceil(individual_total)), m) for j in range(0, n)]
        probability_prediction = sum_submatrix(probabilities_prediction, positive_result_indexes)

        self.propose(bet, match_header, **kwargs)


class IndividualTotalsHomeLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        (m, n) = probabilities_prediction.shape
        individual_total = bet[5]

        positive_result_indexes = [(i,j) for i in range(0, int(np.floor(individual_total))) for j in range(0, n)]
        probability_prediction = sum_submatrix(probabilities_prediction, positive_result_indexes)

        self.propose(bet, match_header, **kwargs)


class IndividualTotalsAwayGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        (m, n) = probabilities_prediction.shape
        individual_total = bet[5]

        positive_result_indexes = [(i,j) for i in range(0, m) for j in range(int(np.ceil(individual_total)), n)]
        probability_prediction = sum_submatrix(probabilities_prediction, positive_result_indexes)

        self.propose(bet, match_header, **kwargs)


class IndividualTotalsAwayLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        (m, n) = probabilities_prediction.shape
        individual_total = bet[5]

        positive_result_indexes = [(i,j) for i in range(0, m) for j in range(0, int(np.floor(individual_total)))]
        probability_prediction = sum_submatrix(probabilities_prediction, positive_result_indexes)

        self.propose(bet, match_header, **kwargs)
