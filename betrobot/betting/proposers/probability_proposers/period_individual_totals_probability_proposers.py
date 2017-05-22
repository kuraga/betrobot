import numpy as np
from betrobot.betting.proposers.probability_proposers.probability_proposer import ProbabilityProposer
from betrobot.util.math_util import sum_submatrix


class FirstPeriodIndividualTotalsHomeGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_individual_total = bet[4]

        correct_results = [(i,j) for i in range(int(np.ceil(period_individual_total)), m) for j in range(0, n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class FirstPeriodIndividualTotalsHomeLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape

        period_individual_total = bet[4]
        correct_results = [(i,j) for i in range(0, int(np.floor(period_individual_total))) for j in range(0, n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class FirstPeriodIndividualTotalsAwayGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_individual_total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(int(np.ceil(period_individual_total)), n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class FirstPeriodIndividualTotalsAwayLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_individual_total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(0, int(np.floor(period_individual_total)))]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class SecondPeriodIndividualTotalsHomeGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_individual_total = bet[4]

        correct_results = [(i,j) for i in range(int(np.ceil(period_individual_total)), m) for j in range(0, n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class SecondPeriodIndividualTotalsHomeLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_individual_total = bet[4]

        correct_results = [(i,j) for i in range(0, int(np.floor(period_individual_total))) for j in range(0, n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class SecondPeriodIndividualTotalsAwayGreaterProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_individual_total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(int(np.ceil(period_individual_total)), n)]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class SecondPeriodIndividualTotalsAwayLesserProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        (m, n) = probabilities.shape
        period_individual_total = bet[4]

        correct_results = [(i,j) for i in range(0, m) for j in range(0, int(np.floor(period_individual_total)))]
        predicted_probability = sum_submatrix(probabilities, correct_results)

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)
