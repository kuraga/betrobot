from betrobot.betting.proposer import Proposer
from betrobot.util.sport_util import is_betarch_match_main, is_betarch_match_corner


class MainMatchProposer(Proposer):

    def handle(self, betcity_match, prediction, whoscored_match=None):
        if prediction is None:
            return

        if not is_betarch_match_main(betcity_match):
            return

        return self._handle(betcity_match, prediction, whoscored_match=whoscored_match)


class CornersMatchProposer(Proposer):

    def handle(self, betcity_match, prediction, whoscored_match=None):
        if prediction is None:
            return

        if not is_betarch_match_corner(betcity_match):
            return

        return self._handle(betcity_match, prediction, whoscored_match=whoscored_match)
