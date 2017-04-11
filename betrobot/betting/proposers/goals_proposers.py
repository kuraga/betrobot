from betrobot.betting.proposer import Proposer
from betrobot.util.sport_util import is_betarch_match_main

from betrobot.betting.proposers.results_proposers import Results1Proposer, Results1XProposer, ResultsX2Proposer, Results2Proposer
from betrobot.betting.proposers.period_results_proposers import FirstPeriodResults1Proposer, FirstPeriodResults1XProposer, FirstPeriodResultsX2Proposer, FirstPeriodResults2Proposer, SecondPeriodResults1Proposer, SecondPeriodResults1XProposer, SecondPeriodResultsX2Proposer, SecondPeriodResults2Proposer
from betrobot.betting.proposers.handicaps_proposers import HandicapsHomeProposer, HandicapsAwayProposer
from betrobot.betting.proposers.period_handicaps_proposers import FirstPeriodHandicapsHomeProposer, FirstPeriodHandicapsAwayProposer, SecondPeriodHandicapsHomeProposer, SecondPeriodHandicapsAwayProposer
from betrobot.betting.proposers.totals_proposers import TotalsGreaterProposer, TotalsLesserProposer
from betrobot.betting.proposers.period_totals_proposers import FirstPeriodTotalsGreaterProposer, FirstPeriodTotalsLesserProposer, SecondPeriodTotalsGreaterProposer, SecondPeriodTotalsLesserProposer
from betrobot.betting.proposers.individual_totals_proposers import IndividualTotalsHomeGreaterProposer, IndividualTotalsHomeLesserProposer, IndividualTotalsAwayGreaterProposer, IndividualTotalsAwayLesserProposer
from betrobot.betting.proposers.period_individual_totals_proposers import FirstPeriodIndividualTotalsHomeGreaterProposer, FirstPeriodIndividualTotalsHomeLesserProposer, FirstPeriodIndividualTotalsAwayGreaterProposer, FirstPeriodIndividualTotalsAwayLesserProposer, SecondPeriodIndividualTotalsHomeGreaterProposer, SecondPeriodIndividualTotalsHomeLesserProposer, SecondPeriodIndividualTotalsAwayGreaterProposer, SecondPeriodIndividualTotalsAwayLesserProposer


class MainMatchProposer(object):

    def _handle(self, betcity_match, prediction, whoscored_match=None, **kwargs):
        if prediction is None:
            return

        if not is_betarch_match_main(betcity_match):
            return

        super()._handle(betcity_match, prediction, whoscored_match=whoscored_match, **kwargs)


class GoalsResults1Proposer(MainMatchProposer, Results1Proposer, Proposer):
    pass


class GoalsResults1XProposer(MainMatchProposer, Results1XProposer, Proposer):
    pass


class GoalsResultsX2Proposer(MainMatchProposer, ResultsX2Proposer, Proposer):
    pass


class GoalsResults2Proposer(MainMatchProposer, Results2Proposer, Proposer):
    pass


class GoalsFirstPeriodResults1Proposer(MainMatchProposer, FirstPeriodResults1Proposer, Proposer):
    pass


class GoalsFirstPeriodResults1XProposer(MainMatchProposer, FirstPeriodResults1XProposer, Proposer):
    pass


class GoalsFirstPeriodResultsX2Proposer(MainMatchProposer, FirstPeriodResultsX2Proposer, Proposer):
    pass


class GoalsFirstPeriodResults2Proposer(MainMatchProposer, FirstPeriodResults2Proposer, Proposer):
    pass


class GoalsSecondPeriodResults1Proposer(MainMatchProposer, SecondPeriodResults1Proposer, Proposer):
    pass


class GoalsSecondPeriodResults1XProposer(MainMatchProposer, SecondPeriodResults1XProposer, Proposer):
    pass


class GoalsSecondPeriodResultsX2Proposer(MainMatchProposer, SecondPeriodResultsX2Proposer, Proposer):
    pass


class GoalsSecondPeriodResults2Proposer(MainMatchProposer, SecondPeriodResults2Proposer, Proposer):
    pass


class GoalsHandicapsHomeProposer(MainMatchProposer, HandicapsHomeProposer, Proposer):
    pass


class GoalsHandicapsAwayProposer(MainMatchProposer, HandicapsAwayProposer, Proposer):
    pass


class GoalsFirstPeriodHandicapsHomeProposer(MainMatchProposer, FirstPeriodHandicapsHomeProposer, Proposer):
    pass


class GoalsFirstPeriodHandicapsAwayProposer(MainMatchProposer, FirstPeriodHandicapsAwayProposer, Proposer):
    pass


class GoalsSecondPeriodHandicapsHomeProposer(MainMatchProposer, SecondPeriodHandicapsHomeProposer, Proposer):
    pass


class GoalsSecondPeriodHandicapsAwayProposer(MainMatchProposer, SecondPeriodHandicapsAwayProposer, Proposer):
    pass


class GoalsTotalsGreaterProposer(MainMatchProposer, TotalsGreaterProposer, Proposer):
    pass


class GoalsTotalsLesserProposer(MainMatchProposer, TotalsLesserProposer, Proposer):
    pass


class GoalsFirstPeriodTotalsGreaterProposer(MainMatchProposer, FirstPeriodTotalsGreaterProposer, Proposer):
    pass


class GoalsFirstPeriodTotalsLesserProposer(MainMatchProposer, FirstPeriodTotalsLesserProposer, Proposer):
    pass


class GoalsSecondPeriodTotalsGreaterProposer(MainMatchProposer, SecondPeriodTotalsGreaterProposer, Proposer):
    pass


class GoalsSecondPeriodTotalsLesserProposer(MainMatchProposer, SecondPeriodTotalsLesserProposer, Proposer):
    pass


class GoalsIndividualTotalsHomeGreaterProposer(MainMatchProposer, IndividualTotalsHomeGreaterProposer, Proposer):
    pass


class GoalsIndividualTotalsHomeLesserProposer(MainMatchProposer, IndividualTotalsHomeLesserProposer, Proposer):
    pass


class GoalsIndividualTotalsAwayGreaterProposer(MainMatchProposer, IndividualTotalsAwayGreaterProposer, Proposer):
    pass


class GoalsIndividualTotalsAwayLesserProposer(MainMatchProposer, IndividualTotalsAwayLesserProposer, Proposer):
    pass


class GoalsFirstPeriodIndividualTotalsHomeGreaterProposer(MainMatchProposer, FirstPeriodIndividualTotalsHomeGreaterProposer, Proposer):
    pass


class GoalsFirstPeriodIndividualTotalsHomeLesserProposer(MainMatchProposer, FirstPeriodIndividualTotalsHomeLesserProposer, Proposer):
    pass


class GoalsFirstPeriodIndividualTotalsAwayGreaterProposer(MainMatchProposer, FirstPeriodIndividualTotalsAwayGreaterProposer, Proposer):
    pass


class GoalsFirstPeriodIndividualTotalsAwayLesserProposer(MainMatchProposer, FirstPeriodIndividualTotalsAwayLesserProposer, Proposer):
    pass


class GoalsSecondPeriodIndividualTotalsHomeGreaterProposer(MainMatchProposer, SecondPeriodIndividualTotalsHomeGreaterProposer, Proposer):
    pass


class GoalsSecondPeriodIndividualTotalsHomeLesserProposer(MainMatchProposer, SecondPeriodIndividualTotalsHomeLesserProposer, Proposer):
    pass


class GoalsSecondPeriodIndividualTotalsAwayGreaterProposer(MainMatchProposer, SecondPeriodIndividualTotalsAwayGreaterProposer, Proposer):
    pass


class GoalsSecondPeriodIndividualTotalsAwayLesserProposer(MainMatchProposer, SecondPeriodIndividualTotalsAwayLesserProposer, Proposer):
    pass
