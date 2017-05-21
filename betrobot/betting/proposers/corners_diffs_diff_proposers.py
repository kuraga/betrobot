from betrobot.betting.proposer import Proposer
from betrobot.betting.proposers.match_proposer_mixins import CornersMatchProposerMixin

from betrobot.betting.proposers.results_proposer_mixins import Results1ProposerMixin, Results1XProposerMixin, ResultsX2ProposerMixin, Results2ProposerMixin
from betrobot.betting.proposers.handicaps_proposer_mixins import HandicapsHomeProposerMixin, HandicapsAwayProposerMixin

from betrobot.betting.proposers.diffs_diff_proposer_mixins.results_diffs_diff_proposer_mixins import Results1DiffsDiffProposerMixin, Results1XDiffsDiffProposerMixin, ResultsX2DiffsDiffProposerMixin, Results2DiffsDiffProposerMixin
from betrobot.betting.proposers.diffs_diff_proposer_mixins.handicaps_diffs_diff_proposer_mixins import HandicapsHomeDiffsDiffProposerMixin, HandicapsAwayDiffsDiffProposerMixin


class CornersResults1DiffsDiffProposer(CornersMatchProposerMixin, Results1ProposerMixin, Results1DiffsDiffProposerMixin, Proposer):
    pass


class CornersResults1XDiffsDiffProposer(CornersMatchProposerMixin, Results1XProposerMixin, Results1XDiffsDiffProposerMixin, Proposer):
    pass


class CornersResultsX2DiffsDiffProposer(CornersMatchProposerMixin, ResultsX2ProposerMixin, ResultsX2DiffsDiffProposerMixin, Proposer):
    pass


class CornersResults2DiffsDiffProposer(CornersMatchProposerMixin, Results2ProposerMixin, Results2DiffsDiffProposerMixin, Proposer):
    pass


class CornersHandicapsHomeDiffsDiffProposer(CornersMatchProposerMixin, HandicapsHomeProposerMixin, HandicapsHomeDiffsDiffProposerMixin, Proposer):
    pass


class CornersHandicapsAwayDiffsDiffProposer(CornersMatchProposerMixin, HandicapsAwayProposerMixin, HandicapsAwayDiffsDiffProposerMixin, Proposer):
    pass