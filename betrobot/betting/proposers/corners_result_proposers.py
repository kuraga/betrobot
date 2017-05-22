from betrobot.betting.proposers.match_proposer_mixins import CornersMatchProposerMixin

from betrobot.betting.proposers.bets_proposer_mixins.results_proposer_mixins import Results1ProposerMixin, Results1XProposerMixin, ResultsX2ProposerMixin, Results2ProposerMixin
from betrobot.betting.proposers.bets_proposer_mixins.handicaps_proposer_mixins import HandicapsHomeProposerMixin, HandicapsAwayProposerMixin

from betrobot.betting.proposers.result_proposers.results_result_proposers import Results1ResultProposer, Results1XResultProposer, ResultsX2ResultProposer, Results2ResultProposer
from betrobot.betting.proposers.result_proposers.handicaps_result_proposers import HandicapsHomeResultProposer, HandicapsAwayResultProposer


class CornersResults1ResultProposer(CornersMatchProposerMixin, Results1ProposerMixin, Results1ResultProposer):
    pass


class CornersResults1XResultProposer(CornersMatchProposerMixin, Results1XProposerMixin, Results1XResultProposer):
    pass


class CornersResultsX2ResultProposer(CornersMatchProposerMixin, ResultsX2ProposerMixin, ResultsX2ResultProposer):
    pass


class CornersResults2ResultProposer(CornersMatchProposerMixin, Results2ProposerMixin, Results2ResultProposer):
    pass


class CornersHandicapsHomeResultProposer(CornersMatchProposerMixin, HandicapsHomeProposerMixin, HandicapsHomeResultProposer):
    pass


class CornersHandicapsAwayResultProposer(CornersMatchProposerMixin, HandicapsAwayProposerMixin, HandicapsAwayResultProposer):
    pass
