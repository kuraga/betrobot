import numpy as np
from betrobot.betting.proposers.diffs_diff_proposer_mixins.diffs_diff_proposer_mixin import DiffsDiffProposerMixin


class Results1DiffsDiffProposerMixin(DiffsDiffProposerMixin):

    def _handle_bet(self, bet, prediction, betcity_match, whoscored_match=None):
        if prediction > self.min_diff:
            self.propose(bet, betcity_match, None, whoscored_match=whoscored_match)


class Results1XDiffsDiffProposerMixin(DiffsDiffProposerMixin):

    def _handle_bet(self, bet, prediction, betcity_match, whoscored_match=None):
        if prediction >= self.min_diff:
            self.propose(bet, betcity_match, None, whoscored_match=whoscored_match)


class ResultsX2DiffsDiffProposerMixin(DiffsDiffProposerMixin):

    def _handle_bet(self, bet, prediction, betcity_match, whoscored_match=None):
        if prediction <= -self.min_diff:
            self.propose(bet, betcity_match, None, whoscored_match=whoscored_match)


class Results2DiffsDiffProposerMixin(DiffsDiffProposerMixin):

    def _handle_bet(self, bet, prediction, betcity_match, whoscored_match=None):
        if prediction < -self.min_diff:
            self.propose(bet, betcity_match, None, whoscored_match=whoscored_match)
