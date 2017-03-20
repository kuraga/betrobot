import numpy as np
from betrobot.betting.proposers.match_proposers import CornersMatchProposer


class CornersResults1Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=-1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = ('УГЛ', 'Исход', None, '1', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersResults1XProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = ('УГЛ', 'Исход', None, '1X', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersResultsX2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = ('УГЛ', 'Исход', None, 'X2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersResults2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = ('УГЛ', 'Исход', None, '2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)
