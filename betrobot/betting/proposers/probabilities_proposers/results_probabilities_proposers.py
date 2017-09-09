import numpy as np
from betrobot.betting.proposers.probabilities_proposers.probabilities_proposer import ProbabilityProposer


class Results1ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        probability_prediction = np.tril(probabilities_prediction, k=-1).sum()

        self.propose(bet, match_header, **kwargs)


class Results1XProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        probability_prediction = np.tril(probabilities_prediction, k=0).sum()

        self.propose(bet, match_header, **kwargs)


class ResultsX2ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        probability_prediction = np.triu(probabilities_prediction, k=0).sum()

        self.propose(bet, match_header, **kwargs)


class Results2ProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        probability_prediction = np.triu(probabilities_prediction, k=1).sum()

        self.propose(bet, match_header, **kwargs)
