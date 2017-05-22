from betrobot.betting.proposers.diffs_diff_proposers.diffs_diff_proposer import DiffsDiffProposer
from betrobot.util.sport_util import get_bets


class HandicapsHomeDiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, betcity_match, diffs_diff_prediction, **kwargs):
        handicap = bet[4]

        if diffs_diff_prediction + handicap > self.min_diffs_diff_for_win:
            self.propose(bet, betcity_match, diffs_diff_prediction=diffs_diff_prediction, **kwargs)


class HandicapsAwayDiffsDiffProposer(DiffsDiffProposer):

    def _handle_bet(self, bet, betcity_match, diffs_diff_prediction, **kwargs):
        handicap = bet[4]

        if diffs_diff_prediction + handicap < -self.min_diffs_diff_for_win:
            self.propose(bet, betcity_match, diffs_diff_prediction=diffs_diff_prediction, **kwargs)
