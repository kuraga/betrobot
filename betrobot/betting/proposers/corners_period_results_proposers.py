import numpy as np
from betrobot.betting.proposers.match_proposers import CornersMatchProposer


class CornersFirstPeriodResults1Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '1', None)

        predicted_probability = np.tril(probabilities, k=-1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersFirstPeriodResults1XProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '1X', None)

        predicted_probability = np.tril(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersFirstPeriodResultsX2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, 'X2', None)

        predicted_probability = np.triu(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersFirstPeriodResults2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '2', None)

        predicted_probability = np.triu(probabilities, k=1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersSecondPeriodResults1Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '1', None)

        predicted_probability = np.tril(probabilities, k=-1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersSecondPeriodResults1XProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '1X', None)

        predicted_probability = np.tril(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersSecondPeriodResultsX2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, 'X2', None)

        predicted_probability = np.triu(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersSecondPeriodResults2Proposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '2', None)

        predicted_probability = np.triu(probabilities, k=1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
