import numpy as np
from betrobot.betting.proposers.probabilities_proposers.probabilities_proposer import ProbabilityProposer
from betrobot.util.math_util import sum_submatrix


class FirstPeriodTotalsGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_total = bet[4]

        positive_result_indexes = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(period_total))-i+1,0), n)]
        probability_prediction = sum_submatrix(probabilities, positive_result_indexes)

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class FirstPeriodTotalsLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_total = bet[4]

        positive_result_indexes = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(period_total))-i,n))]
        probability_prediction = sum_submatrix(probabilities, positive_result_indexes)

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class SecondPeriodTotalsGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_total = bet[4]

        positive_result_indexes = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(period_total))-i+1,0), n)]
        probability_prediction = sum_submatrix(probabilities, positive_result_indexes)

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class SecondPeriodTotalsLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_total = bet[4]

        positive_result_indexes = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(period_total))-i,n))]
        probability_prediction = sum_submatrix(probabilities, positive_result_indexes)

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)
