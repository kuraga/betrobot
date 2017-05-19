import numpy as np
from betrobot.betting.proposers.diffs_proposer_mixins.diffs_proposer_mixin import DiffsProposerMixin


class Results1DiffsProposerMixin(DiffsProposerMixin):

    def _handle(self, betcity_match, prediction, whoscored_match=None):
        bet_pattern = ('*', 'Исход', None, '1', None)

        if prediction > self.min_diff:
            self.propose(bet_pattern, betcity_match, None, whoscored_match=whoscored_match)


class Results1XDiffsProposerMixin(DiffsProposerMixin):

    def _handle(self, betcity_match, prediction, whoscored_match=None):
        bet_pattern = ('*', 'Исход', None, '1X', None)

        if prediction >= self.min_diff:
            self.propose(bet_pattern, betcity_match, None, whoscored_match=whoscored_match)


class ResultsX2DiffsProposerMixin(DiffsProposerMixin):

    def _handle(self, betcity_match, prediction, whoscored_match=None):
        bet_pattern = ('*', 'Исход', None, 'X2', None)

        if prediction <= -self.min_diff:
            self.propose(bet_pattern, betcity_match, None, whoscored_match=whoscored_match)


class Results2DiffsProposerMixin(DiffsProposerMixin):

    def _handle(self, betcity_match, prediction, whoscored_match=None):
        bet_pattern = ('*', 'Исход', None, '2', None)

        if prediction < -self.min_diff:
            self.propose(bet_pattern, betcity_match, None, whoscored_match=whoscored_match)
