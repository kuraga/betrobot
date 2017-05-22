import numpy as np
from betrobot.betting.proposers.probability_proposers.probability_proposer import ProbabilityProposer
from betrobot.util.math_util import sum_submatrix


class IndividualTotalsHomeGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        individual_total = bet[4]

        correct_results = [(i,j) for i in range(int(np.ceil(individual_total)), m) for j in range(0, n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class IndividualTotalsHomeLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        individual_total = bet[4]

        correct_results = [(i,j) for i in range(0, int(np.floor(individual_total))) for j in range(0, n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class IndividualTotalsAwayGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        individual_total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(int(np.ceil(individual_total)), n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class IndividualTotalsAwayLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        individual_total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(0, int(np.floor(individual_total)))]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)
