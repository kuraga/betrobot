from betrobot.betting.proposers.diffs_diff_proposer_mixins.diffs_diff_proposer_mixin import DiffsDiffProposerMixin


class Results1DiffsDiffProposerMixin(DiffsDiffProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        if prediction > self.min_diff:
            self.propose(bet, betcity_match, **kwargs)


class Results1XDiffsDiffProposerMixin(DiffsDiffProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        if prediction >= self.min_diff:
            self.propose(bet, betcity_match, **kwargs)


class ResultsX2DiffsDiffProposerMixin(DiffsDiffProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        if prediction <= -self.min_diff:
            self.propose(bet, betcity_match, **kwargs)


class Results2DiffsDiffProposerMixin(DiffsDiffProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        if prediction < -self.min_diff:
            self.propose(bet, betcity_match, **kwargs)
