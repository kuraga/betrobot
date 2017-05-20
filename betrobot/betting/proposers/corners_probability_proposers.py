from betrobot.betting.proposer import Proposer
from betrobot.util.sport_util import is_betarch_match_corner

from betrobot.betting.proposers.probability_proposer_mixins.results_proposers import Results1Proposer, Results1XProposer, ResultsX2Proposer, Results2Proposer
from betrobot.betting.proposers.probability_proposer_mixins.period_results_proposers import FirstPeriodResults1Proposer, FirstPeriodResults1XProposer, FirstPeriodResultsX2Proposer, FirstPeriodResults2Proposer, SecondPeriodResults1Proposer, SecondPeriodResults1XProposer, SecondPeriodResultsX2Proposer, SecondPeriodResults2Proposer
from betrobot.betting.proposers.probability_proposer_mixins.handicaps_proposers import HandicapsHomeProposer, HandicapsAwayProposer
from betrobot.betting.proposers.probability_proposer_mixins.period_handicaps_proposers import FirstPeriodHandicapsHomeProposer, FirstPeriodHandicapsAwayProposer, SecondPeriodHandicapsHomeProposer, SecondPeriodHandicapsAwayProposer
from betrobot.betting.proposers.probability_proposer_mixins.totals_proposers import TotalsGreaterProposer, TotalsLesserProposer
from betrobot.betting.proposers.probability_proposer_mixins.period_totals_proposers import FirstPeriodTotalsGreaterProposer, FirstPeriodTotalsLesserProposer, SecondPeriodTotalsGreaterProposer, SecondPeriodTotalsLesserProposer
from betrobot.betting.proposers.probability_proposer_mixins.individual_totals_proposers import IndividualTotalsHomeGreaterProposer, IndividualTotalsHomeLesserProposer, IndividualTotalsAwayGreaterProposer, IndividualTotalsAwayLesserProposer
from betrobot.betting.proposers.probability_proposer_mixins.period_individual_totals_proposers import FirstPeriodIndividualTotalsHomeGreaterProposer, FirstPeriodIndividualTotalsHomeLesserProposer, FirstPeriodIndividualTotalsAwayGreaterProposer, FirstPeriodIndividualTotalsAwayLesserProposer, SecondPeriodIndividualTotalsHomeGreaterProposer, SecondPeriodIndividualTotalsHomeLesserProposer, SecondPeriodIndividualTotalsAwayGreaterProposer, SecondPeriodIndividualTotalsAwayLesserProposer


class CornersMatchProposer(object):

    def _handle(self, betcity_match, prediction, whoscored_match=None, **kwargs):
        if prediction is None:
            return

        if not is_betarch_match_corner(betcity_match):
            return

        super()._handle(betcity_match, prediction, whoscored_match=whoscored_match, **kwargs)


class CornersResults1Proposer(CornersMatchProposer, Results1Proposer, Proposer):
    pass


class CornersResults1XProposer(CornersMatchProposer, Results1XProposer, Proposer):
    pass


class CornersResultsX2Proposer(CornersMatchProposer, ResultsX2Proposer, Proposer):
    pass


class CornersResults2Proposer(CornersMatchProposer, Results2Proposer, Proposer):
    pass


class CornersFirstPeriodResults1Proposer(CornersMatchProposer, FirstPeriodResults1Proposer, Proposer):
    pass


class CornersFirstPeriodResults1XProposer(CornersMatchProposer, FirstPeriodResults1XProposer, Proposer):
    pass


class CornersFirstPeriodResultsX2Proposer(CornersMatchProposer, FirstPeriodResultsX2Proposer, Proposer):
    pass


class CornersFirstPeriodResults2Proposer(CornersMatchProposer, FirstPeriodResults2Proposer, Proposer):
    pass


class CornersSecondPeriodResults1Proposer(CornersMatchProposer, SecondPeriodResults1Proposer, Proposer):
    pass


class CornersSecondPeriodResults1XProposer(CornersMatchProposer, SecondPeriodResults1XProposer, Proposer):
    pass


class CornersSecondPeriodResultsX2Proposer(CornersMatchProposer, SecondPeriodResultsX2Proposer, Proposer):
    pass


class CornersSecondPeriodResults2Proposer(CornersMatchProposer, SecondPeriodResults2Proposer, Proposer):
    pass


class CornersHandicapsHomeProposer(CornersMatchProposer, HandicapsHomeProposer, Proposer):
    pass


class CornersHandicapsAwayProposer(CornersMatchProposer, HandicapsAwayProposer, Proposer):
    pass


class CornersFirstPeriodHandicapsHomeProposer(CornersMatchProposer, FirstPeriodHandicapsHomeProposer, Proposer):
    pass


class CornersFirstPeriodHandicapsAwayProposer(CornersMatchProposer, FirstPeriodHandicapsAwayProposer, Proposer):
    pass


class CornersSecondPeriodHandicapsHomeProposer(CornersMatchProposer, SecondPeriodHandicapsHomeProposer, Proposer):
    pass


class CornersSecondPeriodHandicapsAwayProposer(CornersMatchProposer, SecondPeriodHandicapsAwayProposer, Proposer):
    pass


class CornersTotalsGreaterProposer(CornersMatchProposer, TotalsGreaterProposer, Proposer):
    pass


class CornersTotalsLesserProposer(CornersMatchProposer, TotalsLesserProposer, Proposer):
    pass


class CornersFirstPeriodTotalsGreaterProposer(CornersMatchProposer, FirstPeriodTotalsGreaterProposer, Proposer):
    pass


class CornersFirstPeriodTotalsLesserProposer(CornersMatchProposer, FirstPeriodTotalsLesserProposer, Proposer):
    pass


class CornersSecondPeriodTotalsGreaterProposer(CornersMatchProposer, SecondPeriodTotalsGreaterProposer, Proposer):
    pass


class CornersSecondPeriodTotalsLesserProposer(CornersMatchProposer, SecondPeriodTotalsLesserProposer, Proposer):
    pass


class CornersIndividualTotalsHomeGreaterProposer(CornersMatchProposer, IndividualTotalsHomeGreaterProposer, Proposer):
    pass


class CornersIndividualTotalsHomeLesserProposer(CornersMatchProposer, IndividualTotalsHomeLesserProposer, Proposer):
    pass


class CornersIndividualTotalsAwayGreaterProposer(CornersMatchProposer, IndividualTotalsAwayGreaterProposer, Proposer):
    pass


class CornersIndividualTotalsAwayLesserProposer(CornersMatchProposer, IndividualTotalsAwayLesserProposer, Proposer):
    pass


class CornersFirstPeriodIndividualTotalsHomeGreaterProposer(CornersMatchProposer, FirstPeriodIndividualTotalsHomeGreaterProposer, Proposer):
    pass


class CornersFirstPeriodIndividualTotalsHomeLesserProposer(CornersMatchProposer, FirstPeriodIndividualTotalsHomeLesserProposer, Proposer):
    pass


class CornersFirstPeriodIndividualTotalsAwayGreaterProposer(CornersMatchProposer, FirstPeriodIndividualTotalsAwayGreaterProposer, Proposer):
    pass


class CornersFirstPeriodIndividualTotalsAwayLesserProposer(CornersMatchProposer, FirstPeriodIndividualTotalsAwayLesserProposer, Proposer):
    pass


class CornersSecondPeriodIndividualTotalsHomeGreaterProposer(CornersMatchProposer, SecondPeriodIndividualTotalsHomeGreaterProposer, Proposer):
    pass


class CornersSecondPeriodIndividualTotalsHomeLesserProposer(CornersMatchProposer, SecondPeriodIndividualTotalsHomeLesserProposer, Proposer):
    pass


class CornersSecondPeriodIndividualTotalsAwayGreaterProposer(CornersMatchProposer, SecondPeriodIndividualTotalsAwayGreaterProposer, Proposer):
    pass


class CornersSecondPeriodIndividualTotalsAwayLesserProposer(CornersMatchProposer, SecondPeriodIndividualTotalsAwayLesserProposer, Proposer):
    pass
