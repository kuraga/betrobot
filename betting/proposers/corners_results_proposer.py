from betting.proposer import Proposer
from util.sport_util import is_betarch_match_corner


class CornersResultsProposer(Proposer):

    def handle(self, betcity_match, prediction, whoscored_match=None):
        if prediction is None:
            return

        if not is_betarch_match_corner(betcity_match):
            return

        (corners_predicted_home, corners_predicted_away) = prediction

        return self._handle(betcity_match, corners_predicted_home, corners_predicted_away, whoscored_match=whoscored_match)
