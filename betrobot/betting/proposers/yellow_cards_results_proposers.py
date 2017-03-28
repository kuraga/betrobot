import numpy as np
from betrobot.betting.proposers.match_proposers import YellowCardsMatchProposer


class YellowCardsResults1Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=-1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = ('ЖК', 'Исход', None, '1', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class YellowCardsResults1XProposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.tril(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = ('ЖК', 'Исход', None, '1X', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class YellowCardsResultsX2Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=0).sum() / probabilities.sum() > confidence_level:
            bet_pattern = ('ЖК', 'Исход', None, 'X2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class YellowCardsResults2Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        if np.triu(probabilities, k=1).sum() / probabilities.sum() > confidence_level:
            bet_pattern = ('ЖК', 'Исход', None, '2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)
