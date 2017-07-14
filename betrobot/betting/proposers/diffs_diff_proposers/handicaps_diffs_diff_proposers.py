from betrobot.betting.proposers.diffs_diff_proposers.diffs_diff_proposer import DiffsDiffProposer


class HandicapsHomeDiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, diffs_diff_prediction, match_header, **kwargs):
        handicap = bet[4]

        if diffs_diff_prediction + handicap > self.min_margin:
            self.propose(bet, match_header, diffs_diff_prediction=diffs_diff_prediction, **kwargs)


class HandicapsAwayDiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, diffs_diff_prediction, match_header, **kwargs):
        handicap = bet[4]

        if diffs_diff_prediction + handicap < -self.min_margin:
            self.propose(bet, match_header, diffs_diff_prediction=diffs_diff_prediction, **kwargs)
