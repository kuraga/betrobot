from betrobot.util.sport_util import is_betarch_match_corner


class CornersMatchProposerMixin(object):

    def _handle_bet(self, bet, prediction, betcity_match, whoscored_match=None):
        if not is_betarch_match_corner(betcity_match):
            return

        super()._handle_bet(bet, prediction, betcity_match, whoscored_match=whoscored_match)
