from betrobot.betting.sport_util import is_betarch_match_corner


class CornersMatchProposerMixin:

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        if not is_betarch_match_corner(betcity_match):
            return

        super()._handle_bet(bet, betcity_match, prediction, **kwargs)
