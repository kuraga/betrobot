import numpy as np
from betrobot.betting.proposers.match_proposers import YellowCardsMatchProposer


class YellowCardsResults1Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('ЖК', 'Исход', None, '1', None)

        predicted_probability = np.tril(probabilities, k=-1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class YellowCardsResults1XProposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('ЖК', 'Исход', None, '1X', None)

        predicted_probability = np.tril(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class YellowCardsResultsX2Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('ЖК', 'Исход', None, 'X2', None)

        predicted_probability = np.triu(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class YellowCardsResults2Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('ЖК', 'Исход', None, '2', None)

        predicted_probability = np.triu(probabilities, k=1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
