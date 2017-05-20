from betrobot.betting.proposer import Proposer
from betrobot.betting.proposers.match_proposer_mixins import CornersMatchProposerMixin

from betrobot.betting.proposers.results_proposer_mixins import Results1ProposerMixin, Results1XProposerMixin, ResultsX2ProposerMixin, Results2ProposerMixin
from betrobot.betting.proposers.handicaps_proposer_mixins import HandicapsHomeProposerMixin, HandicapsAwayProposerMixin

from betrobot.betting.proposers.diffs_proposer_mixins.results_diffs_proposer_mixins import Results1DiffsProposerMixin, Results1XDiffsProposerMixin, ResultsX2DiffsProposerMixin, Results2DiffsProposerMixin
from betrobot.betting.proposers.diffs_proposer_mixins.handicaps_diffs_proposer_mixins import HandicapsHomeDiffsProposerMixin, HandicapsAwayDiffsProposerMixin


class CornersResults1DiffsProposer(CornersMatchProposerMixin, Results1ProposerMixin, Results1DiffsProposerMixin, Proposer):
    pass


class CornersResults1XDiffsProposer(CornersMatchProposerMixin, Results1XProposerMixin, Results1XDiffsProposerMixin, Proposer):
    pass


class CornersResultsX2DiffsProposer(CornersMatchProposerMixin, ResultsX2ProposerMixin, ResultsX2DiffsProposerMixin, Proposer):
    pass


class CornersResults2DiffsProposer(CornersMatchProposerMixin, Results2ProposerMixin, Results2DiffsProposerMixin, Proposer):
    pass


class CornersHandicapsHomeDiffsProposer(CornersMatchProposerMixin, HandicapsHomeProposerMixin, HandicapsHomeDiffsProposerMixin, Proposer):
    pass


class CornersHandicapsAwayDiffsProposer(CornersMatchProposerMixin, HandicapsAwayProposerMixin, HandicapsAwayDiffsProposerMixin, Proposer):
    pass
