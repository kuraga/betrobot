import numpy as np
from betrobot.betting.proposers.match_proposers import MainMatchProposer


class GoalsResults1Proposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исход', None, '1', None)

        predicted_probability = np.tril(probabilities, k=-1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class GoalsResults1XProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исход', None, '1X', None)

        predicted_probability = np.tril(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class GoalsResultsX2Proposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исход', None, 'X2', None)

        predicted_probability = np.triu(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class GoalsResults2Proposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исход', None, '2', None)

        predicted_probability = np.triu(probabilities, k=1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
