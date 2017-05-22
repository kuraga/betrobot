from betrobot.betting.proposers.diffs_diff_proposer_mixins.diffs_diff_proposer_mixin import DiffsDiffProposerMixin
from betrobot.util.sport_util import get_bets


class HandicapsHomeDiffsDiffProposerMixin(DiffsDiffProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        handicap = bet[4]
        if prediction + handicap > self.min_diff:
            self.propose(bet, betcity_match, **kwargs)


class HandicapsAwayDiffsDiffProposerMixin(DiffsDiffProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        handicap = bet[4]
        if prediction + handicap < -self.min_diff:
            self.propose(bet, betcity_match, **kwargs)
