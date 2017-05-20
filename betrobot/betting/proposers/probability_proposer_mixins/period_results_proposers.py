import numpy as np


class FirstPeriodResults1Proposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', None, '1', None)

        predicted_probability = np.tril(probabilities, k=-1).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class FirstPeriodResults1XProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', None, '1X', None)

        predicted_probability = np.tril(probabilities, k=0).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class FirstPeriodResultsX2Proposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', None, 'X2', None)

        predicted_probability = np.triu(probabilities, k=0).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class FirstPeriodResults2Proposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', None, '2', None)

        predicted_probability = np.triu(probabilities, k=1).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodResults1Proposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', None, '1', None)

        predicted_probability = np.tril(probabilities, k=-1).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodResults1XProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', None, '1X', None)

        predicted_probability = np.tril(probabilities, k=0).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodResultsX2Proposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', None, 'X2', None)

        predicted_probability = np.triu(probabilities, k=0).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodResults2Proposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', None, '2', None)

        predicted_probability = np.triu(probabilities, k=1).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
