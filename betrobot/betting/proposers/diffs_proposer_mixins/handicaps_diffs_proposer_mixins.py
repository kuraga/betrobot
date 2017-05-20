import numpy as np
from betrobot.betting.proposers.diffs_proposer_mixins.diffs_proposer_mixin import DiffsProposerMixin
from betrobot.util.sport_util import get_bets


class HandicapsHomeDiffsProposerMixin(DiffsProposerMixin):

    def _handle(self, betcity_match, prediction, whoscored_match=None):
        bet_pattern1 = ('*', 'Фора', betcity_match['home'], None, '*')
        bet_pattern2 = ('*', 'Дополнительные форы', betcity_match['home'], None, '*')

        bets = get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
        for bet in bets:
            handicap = bet[4]
            if prediction + handicap > self.min_diff:
                self.propose(bet, betcity_match, None, whoscored_match=whoscored_match)


class HandicapsAwayDiffsProposerMixin(DiffsProposerMixin):

    def _handle(self, betcity_match, prediction, whoscored_match=None):
        bet_pattern1 = ('*', 'Фора', betcity_match['away'], None, '*')
        bet_pattern2 = ('*', 'Дополнительные форы', betcity_match['away'], None, '*')

        bets = get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
        for bet in bets:
            handicap = bet[4]
            if prediction + handicap < -self.min_diff:
                self.propose(bet, betcity_match, None, whoscored_match=whoscored_match)
