import numpy as np
from betrobot.betting.proposers.probability_proposers.probability_proposer import ProbabilityProposer
from betrobot.util.math_util import sum_submatrix


class FirstPeriodTotalsGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(period_total))-i+1,0), n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class FirstPeriodTotalsLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(period_total))-i,n))]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class SecondPeriodTotalsGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(period_total))-i+1,0), n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class SecondPeriodTotalsLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(period_total))-i,n))]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)
