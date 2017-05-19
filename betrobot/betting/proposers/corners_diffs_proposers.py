from betrobot.betting.proposer import Proposer
from betrobot.util.sport_util import is_betarch_match_corner

from betrobot.betting.proposers.diffs_proposer_mixins.results_diffs_proposer_mixins import Results1DiffsProposerMixin, Results1XDiffsProposerMixin, ResultsX2DiffsProposerMixin, Results2DiffsProposerMixin
from betrobot.betting.proposers.diffs_proposer_mixins.handicaps_diffs_proposer_mixins import HandicapsHomeDiffsProposerMixin, HandicapsAwayDiffsProposerMixin


class CornersMatchProposerMixin(object):

    def _handle(self, betcity_match, prediction, whoscored_match=None, **kwargs):
        if prediction is None:
            return

        if not is_betarch_match_corner(betcity_match):
            return

        super()._handle(betcity_match, prediction, whoscored_match=whoscored_match, **kwargs)


class CornersResults1DiffsProposer(CornersMatchProposerMixin, Results1DiffsProposerMixin, Proposer):
    pass


class CornersResults1XDiffsProposer(CornersMatchProposerMixin, Results1XDiffsProposerMixin, Proposer):
    pass


class CornersResultsX2DiffsProposer(CornersMatchProposerMixin, ResultsX2DiffsProposerMixin, Proposer):
    pass


class CornersResults2DiffsProposer(CornersMatchProposerMixin, Results2DiffsProposerMixin, Proposer):
    pass


class CornersHandicapsHomeDiffsProposer(CornersMatchProposerMixin, HandicapsHomeDiffsProposerMixin, Proposer):
    pass


class CornersHandicapsAwayDiffsProposer(CornersMatchProposerMixin, HandicapsAwayDiffsProposerMixin, Proposer):
    pass
