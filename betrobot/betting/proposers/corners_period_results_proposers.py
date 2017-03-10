import numpy as np
from betrobot.betting.proposers.match_proposers import CornersMatchProposer


class CornersFirstPeriodResults1Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=-1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '1', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersFirstPeriodResults1XProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '1X', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersFirstPeriodResultsX2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, 'X2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersFirstPeriodResults2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=-1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersSecondPeriodResults1Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=-1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '1', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersSecondPeriodResults1XProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '1X', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersSecondPeriodResultsX2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, 'X2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersSecondPeriodResults2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=-1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)
