from betrobot.betting.proposers.diffs_diff_proposers.diffs_diff_proposer import DiffsDiffProposer


class Results1DiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, betcity_match, diffs_diff_prediction, **kwargs):
        if diffs_diff_prediction > self.min_margin:
            self.propose(bet, betcity_match, diffs_diff_prediction=diffs_diff_prediction, **kwargs)


class Results1XDiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, betcity_match, diffs_diff_prediction, **kwargs):
        if diffs_diff_prediction >= self.min_margin:
            self.propose(bet, betcity_match, diffs_diff_prediction=diffs_diff_prediction, **kwargs)


class ResultsX2DiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, betcity_match, diffs_diff_prediction, **kwargs):
        if diffs_diff_prediction <= -self.min_margin:
            self.propose(bet, betcity_match, diffs_diff_prediction=diffs_diff_prediction, **kwargs)


class Results2DiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, betcity_match, diffs_diff_prediction, **kwargs):
        if diffs_diff_prediction < -self.min_margin:
            self.propose(bet, betcity_match, diffs_diff_prediction=diffs_diff_prediction, **kwargs)
