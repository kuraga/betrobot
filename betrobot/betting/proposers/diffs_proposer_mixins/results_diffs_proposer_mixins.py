import numpy as np
from betrobot.betting.proposers.diffs_proposer_mixins.diffs_proposer_mixin import DiffsProposerMixin


class Results1DiffsProposerMixin(DiffsProposerMixin):

    def _handle_bet(self, bet, prediction, betcity_match, whoscored_match=None):
        if prediction > self.min_diff:
            self.propose(bet, betcity_match, None, whoscored_match=whoscored_match)


class Results1XDiffsProposerMixin(DiffsProposerMixin):

    def _handle_bet(self, bet, prediction, betcity_match, whoscored_match=None):
        if prediction >= self.min_diff:
            self.propose(bet, betcity_match, None, whoscored_match=whoscored_match)


class ResultsX2DiffsProposerMixin(DiffsProposerMixin):

    def _handle_bet(self, bet, prediction, betcity_match, whoscored_match=None):
        if prediction <= -self.min_diff:
            self.propose(bet, betcity_match, None, whoscored_match=whoscored_match)


class Results2DiffsProposerMixin(DiffsProposerMixin):

    def _handle_bet(self, bet, prediction, betcity_match, whoscored_match=None):
        if prediction < -self.min_diff:
            self.propose(bet, betcity_match, None, whoscored_match=whoscored_match)
