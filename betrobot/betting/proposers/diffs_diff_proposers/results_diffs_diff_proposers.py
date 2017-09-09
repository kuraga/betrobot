from betrobot.betting.proposers.diffs_diff_proposers.diffs_diff_proposer import DiffsDiffProposer


class Results1DiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, diffs_diff_prediction, match_header, **kwargs):
        if diffs_diff_prediction > self.min_margin:
            self.propose(bet, match_header, **kwargs)


class Results1XDiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, diffs_diff_prediction, match_header, **kwargs):
        if diffs_diff_prediction >= self.min_margin:
            self.propose(bet, match_header, **kwargs)


class ResultsX2DiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, diffs_diff_prediction, match_header, **kwargs):
        if diffs_diff_prediction <= -self.min_margin:
            self.propose(bet, match_header, **kwargs)


class Results2DiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, diffs_diff_prediction, match_header, **kwargs):
        if diffs_diff_prediction < -self.min_margin:
            self.propose(bet, match_header, **kwargs)
