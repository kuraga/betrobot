from betrobot.betting.proposer import Proposer
from betrobot.util.sport_util import is_betarch_match_corner

from betrobot.betting.proposers.results_proposers import Results1Proposer, Results1XProposer, ResultsX2Proposer, Results2Proposer
from betrobot.betting.proposers.period_results_proposers import FirstPeriodResults1Proposer, FirstPeriodResults1XProposer, FirstPeriodResultsX2Proposer, FirstPeriodResults2Proposer, SecondPeriodResults1Proposer, SecondPeriodResults1XProposer, SecondPeriodResultsX2Proposer, SecondPeriodResults2Proposer
from betrobot.betting.proposers.handicaps_proposers import HandicapsHomeProposer, HandicapsAwayProposer
from betrobot.betting.proposers.period_handicaps_proposers import FirstPeriodHandicapsHomeProposer, FirstPeriodHandicapsAwayProposer, SecondPeriodHandicapsHomeProposer, SecondPeriodHandicapsAwayProposer
from betrobot.betting.proposers.totals_proposers import TotalsGreaterProposer, TotalsLesserProposer
from betrobot.betting.proposers.period_totals_proposers import FirstPeriodTotalsGreaterProposer, FirstPeriodTotalsLesserProposer, SecondPeriodTotalsGreaterProposer, SecondPeriodTotalsLesserProposer
from betrobot.betting.proposers.individual_totals_proposers import IndividualTotalsHomeGreaterProposer, IndividualTotalsHomeLesserProposer, IndividualTotalsAwayGreaterProposer, IndividualTotalsAwayLesserProposer
from betrobot.betting.proposers.period_individual_totals_proposers import FirstPeriodIndividualTotalsHomeGreaterProposer, FirstPeriodIndividualTotalsHomeLesserProposer, FirstPeriodIndividualTotalsAwayGreaterProposer, FirstPeriodIndividualTotalsAwayLesserProposer, SecondPeriodIndividualTotalsHomeGreaterProposer, SecondPeriodIndividualTotalsHomeLesserProposer, SecondPeriodIndividualTotalsAwayGreaterProposer, SecondPeriodIndividualTotalsAwayLesserProposer


class CornersMatchProposer(object):

    def _handle(self, betcity_match, prediction, whoscored_match=None, **kwargs):
        if prediction is None:
            return

        if not is_betarch_match_corner(betcity_match):
            return

        super()._handle(betcity_match, prediction, whoscored_match=whoscored_match, **kwargs)


class CornersResults1Proposer(Proposer, CornersMatchProposer, Results1Proposer):
    pass


class CornersResults1XProposer(Proposer, CornersMatchProposer, Results1XProposer):
    pass


class CornersResultsX2Proposer(Proposer, CornersMatchProposer, ResultsX2Proposer):
    pass


class CornersResults2Proposer(Proposer, CornersMatchProposer, Results2Proposer):
    pass


class CornersFirstPeriodResults1Proposer(Proposer, CornersMatchProposer, FirstPeriodResults1Proposer):
    pass


class CornersFirstPeriodResults1XProposer(Proposer, CornersMatchProposer, FirstPeriodResults1XProposer):
    pass


class CornersFirstPeriodResultsX2Proposer(Proposer, CornersMatchProposer, FirstPeriodResultsX2Proposer):
    pass


class CornersFirstPeriodResults2Proposer(Proposer, CornersMatchProposer, FirstPeriodResults2Proposer):
    pass


class CornersSecondPeriodResults1Proposer(Proposer, CornersMatchProposer, SecondPeriodResults1Proposer):
    pass


class CornersSecondPeriodResults1XProposer(Proposer, CornersMatchProposer, SecondPeriodResults1XProposer):
    pass


class CornersSecondPeriodResultsX2Proposer(Proposer, CornersMatchProposer, SecondPeriodResultsX2Proposer):
    pass


class CornersSecondPeriodResults2Proposer(Proposer, CornersMatchProposer, SecondPeriodResults2Proposer):
    pass


class CornersHandicapsHomeProposer(Proposer, CornersMatchProposer, HandicapsHomeProposer):
    pass


class CornersHandicapsAwayProposer(Proposer, CornersMatchProposer, HandicapsAwayProposer):
    pass


class CornersFirstPeriodHandicapsHomeProposer(Proposer, CornersMatchProposer, FirstPeriodHandicapsHomeProposer):
    pass


class CornersFirstPeriodHandicapsAwayProposer(Proposer, CornersMatchProposer, FirstPeriodHandicapsAwayProposer):
    pass


class CornersSecondPeriodHandicapsHomeProposer(Proposer, CornersMatchProposer, SecondPeriodHandicapsHomeProposer):
    pass


class CornersSecondPeriodHandicapsAwayProposer(Proposer, CornersMatchProposer, SecondPeriodHandicapsAwayProposer):
    pass


class CornersTotalsGreaterProposer(Proposer, CornersMatchProposer, TotalsGreaterProposer):
    pass


class CornersTotalsLesserProposer(Proposer, CornersMatchProposer, TotalsLesserProposer):
    pass


class CornersFirstPeriodTotalsGreaterProposer(Proposer, CornersMatchProposer, FirstPeriodTotalsGreaterProposer):
    pass


class CornersFirstPeriodTotalsLesserProposer(Proposer, CornersMatchProposer, FirstPeriodTotalsLesserProposer):
    pass


class CornersSecondPeriodTotalsGreaterProposer(Proposer, CornersMatchProposer, SecondPeriodTotalsGreaterProposer):
    pass


class CornersSecondPeriodTotalsLesserProposer(Proposer, CornersMatchProposer, SecondPeriodTotalsLesserProposer):
    pass


class CornersIndividualTotalsHomeGreaterProposer(Proposer, CornersMatchProposer, IndividualTotalsHomeGreaterProposer):
    pass


class CornersIndividualTotalsHomeLesserProposer(Proposer, CornersMatchProposer, IndividualTotalsHomeLesserProposer):
    pass


class CornersIndividualTotalsAwayGreaterProposer(Proposer, CornersMatchProposer, IndividualTotalsAwayGreaterProposer):
    pass


class CornersIndividualTotalsAwayLesserProposer(Proposer, CornersMatchProposer, IndividualTotalsAwayLesserProposer):
    pass


class CornersFirstPeriodIndividualTotalsHomeGreaterProposer(Proposer, CornersMatchProposer, FirstPeriodIndividualTotalsHomeGreaterProposer):
    pass


class CornersFirstPeriodIndividualTotalsHomeLesserProposer(Proposer, CornersMatchProposer, FirstPeriodIndividualTotalsHomeLesserProposer):
    pass


class CornersFirstPeriodIndividualTotalsAwayGreaterProposer(Proposer, CornersMatchProposer, FirstPeriodIndividualTotalsAwayGreaterProposer):
    pass


class CornersFirstPeriodIndividualTotalsAwayLesserProposer(Proposer, CornersMatchProposer, FirstPeriodIndividualTotalsAwayLesserProposer):
    pass


class CornersSecondPeriodIndividualTotalsHomeGreaterProposer(Proposer, CornersMatchProposer, SecondPeriodIndividualTotalsHomeGreaterProposer):
    pass


class CornersSecondPeriodIndividualTotalsHomeLesserProposer(Proposer, CornersMatchProposer, SecondPeriodIndividualTotalsHomeLesserProposer):
    pass


class CornersSecondPeriodIndividualTotalsAwayGreaterProposer(Proposer, CornersMatchProposer, SecondPeriodIndividualTotalsAwayGreaterProposer):
    pass


class CornersSecondPeriodIndividualTotalsAwayLesserProposer(Proposer, CornersMatchProposer, SecondPeriodIndividualTotalsAwayLesserProposer):
    pass
