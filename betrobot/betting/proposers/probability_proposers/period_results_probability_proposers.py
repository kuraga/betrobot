import numpy as np
from betrobot.betting.proposers.probability_proposers.probability_proposer import ProbabilityProposer


class FirstPeriodResults1ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.tril(probabilities, k=-1).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class FirstPeriodResults1XProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.tril(probabilities, k=0).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class FirstPeriodResultsX2ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.triu(probabilities, k=0).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class FirstPeriodResults2ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.triu(probabilities, k=1).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class SecondPeriodResults1ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.tril(probabilities, k=-1).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class SecondPeriodResults1XProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.tril(probabilities, k=0).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class SecondPeriodResultsX2ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.triu(probabilities, k=0).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class SecondPeriodResults2ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.triu(probabilities, k=1).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)
