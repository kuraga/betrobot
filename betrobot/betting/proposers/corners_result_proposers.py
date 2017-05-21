from betrobot.betting.proposer import Proposer
from betrobot.betting.proposers.match_proposer_mixins import CornersMatchProposerMixin

from betrobot.betting.proposers.bets_proposer_mixins.results_proposer_mixins import Results1ProposerMixin, Results1XProposerMixin, ResultsX2ProposerMixin, Results2ProposerMixin
from betrobot.betting.proposers.bets_proposer_mixins.handicaps_proposer_mixins import HandicapsHomeProposerMixin, HandicapsAwayProposerMixin

from betrobot.betting.proposers.result_proposer_mixins.results_result_proposer_mixins import Results1ResultProposerMixin, Results1XResultProposerMixin, ResultsX2ResultProposerMixin, Results2ResultProposerMixin
from betrobot.betting.proposers.result_proposer_mixins.handicaps_result_proposer_mixins import HandicapsHomeResultProposerMixin, HandicapsAwayResultProposerMixin


class CornersResults1ResultProposer(CornersMatchProposerMixin, Results1ProposerMixin, Results1ResultProposerMixin, Proposer):
    pass


class CornersResults1XResultProposer(CornersMatchProposerMixin, Results1XProposerMixin, Results1XResultProposerMixin, Proposer):
    pass


class CornersResultsX2ResultProposer(CornersMatchProposerMixin, ResultsX2ProposerMixin, ResultsX2ResultProposerMixin, Proposer):
    pass


class CornersResults2ResultProposer(CornersMatchProposerMixin, Results2ProposerMixin, Results2ResultProposerMixin, Proposer):
    pass


class CornersHandicapsHomeResultProposer(CornersMatchProposerMixin, HandicapsHomeProposerMixin, HandicapsHomeResultProposerMixin, Proposer):
    pass


class CornersHandicapsAwayResultProposer(CornersMatchProposerMixin, HandicapsAwayProposerMixin, HandicapsAwayResultProposerMixin, Proposer):
    pass
