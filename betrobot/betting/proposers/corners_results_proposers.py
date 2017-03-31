import numpy as np
from betrobot.betting.proposers.match_proposers import CornersMatchProposer


class CornersResults1Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('УГЛ', 'Исход', None, '1', None)

        predicted_probability = np.tril(probabilities, k=-1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersResults1XProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('УГЛ', 'Исход', None, '1X', None)

        predicted_probability = np.tril(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersResultsX2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('УГЛ', 'Исход', None, 'X2', None)

        predicted_probability = np.triu(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersResults2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('УГЛ', 'Исход', None, '2', None)

        predicted_probability = np.triu(probabilities, k=1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
