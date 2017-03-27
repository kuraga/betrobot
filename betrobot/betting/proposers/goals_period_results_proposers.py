import numpy as np
from betrobot.betting.proposers.match_proposers import MainMatchProposer


class GoalsFirstPeriodResults1Proposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=-1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '1', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class GoalsFirstPeriodResults1XProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '1X', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class GoalsFirstPeriodResultsX2Proposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, 'X2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class GoalsFirstPeriodResults2Proposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class GoalsSecondPeriodResults1Proposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=-1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '1', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class GoalsSecondPeriodResults1XProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '1X', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class GoalsSecondPeriodResultsX2Proposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, 'X2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class GoalsSecondPeriodResults2Proposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)
