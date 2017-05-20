import numpy as np


class Results1Proposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исход', None, '1', None)

        predicted_probability = np.tril(probabilities, k=-1).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class Results1XProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исход', None, '1X', None)

        predicted_probability = np.tril(probabilities, k=0).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class ResultsX2Proposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исход', None, 'X2', None)

        predicted_probability = np.triu(probabilities, k=0).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class Results2Proposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исход', None, '2', None)

        predicted_probability = np.triu(probabilities, k=1).sum()

        if predicted_probability > 0:
            self.propose(bet_pattern, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
