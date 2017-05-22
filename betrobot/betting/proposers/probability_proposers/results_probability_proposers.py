import numpy as np
from betrobot.betting.proposers.probability_proposers.probability_proposer import ProbabilityProposer


class Results1ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.tril(probabilities, k=-1).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class Results1XProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.tril(probabilities, k=0).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class ResultsX2ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.triu(probabilities, k=0).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)


class Results2ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        probability_prediction = np.triu(probabilities, k=1).sum()

        self.propose(bet, betcity_match, probability_prediction=probability_prediction, **kwargs)
