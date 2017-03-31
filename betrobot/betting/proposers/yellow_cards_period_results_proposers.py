import numpy as np
from betrobot.betting.proposers.match_proposers import YellowCardsMatchProposer


class YellowCardsFirstPeriodResults1Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '1', None)

        predicted_probability = np.tril(probabilities, k=-1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class YellowCardsFirstPeriodResults1XProposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '1X', None)

        predicted_probability = np.tril(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class YellowCardsFirstPeriodResultsX2Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, 'X2', None)

        predicted_probability = np.triu(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class YellowCardsFirstPeriodResults2Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (1-й тайм)', None, '2', None)

        predicted_probability = np.triu(probabilities, k=1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class YellowCardsSecondPeriodResults1Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '1', None)

        predicted_probability = np.tril(probabilities, k=-1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class YellowCardsSecondPeriodResults1XProposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '1X', None)

        predicted_probability = np.tril(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class YellowCardsSecondPeriodResultsX2Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, 'X2', None)

        predicted_probability = np.triu(probabilities, k=0).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class YellowCardsSecondPeriodResults2Proposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = (None, 'Исходы по таймам (2-й тайм)', None, '2', None)

        predicted_probability = np.triu(probabilities, k=1).sum()

        self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
