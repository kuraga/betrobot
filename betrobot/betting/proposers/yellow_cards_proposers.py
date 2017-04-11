from betrobot.betting.proposer import Proposer
from betrobot.util.sport_util import is_betarch_match_yellow_card

from betrobot.betting.proposers.results_proposers import Results1Proposer, Results1XProposer, ResultsX2Proposer, Results2Proposer
from betrobot.betting.proposers.period_results_proposers import FirstPeriodResults1Proposer, FirstPeriodResults1XProposer, FirstPeriodResultsX2Proposer, FirstPeriodResults2Proposer, SecondPeriodResults1Proposer, SecondPeriodResults1XProposer, SecondPeriodResultsX2Proposer, SecondPeriodResults2Proposer
from betrobot.betting.proposers.handicaps_proposers import HandicapsHomeProposer, HandicapsAwayProposer
from betrobot.betting.proposers.period_handicaps_proposers import FirstPeriodHandicapsHomeProposer, FirstPeriodHandicapsAwayProposer, SecondPeriodHandicapsHomeProposer, SecondPeriodHandicapsAwayProposer
from betrobot.betting.proposers.totals_proposers import TotalsGreaterProposer, TotalsLesserProposer
from betrobot.betting.proposers.period_totals_proposers import FirstPeriodTotalsGreaterProposer, FirstPeriodTotalsLesserProposer, SecondPeriodTotalsGreaterProposer, SecondPeriodTotalsLesserProposer
from betrobot.betting.proposers.individual_totals_proposers import IndividualTotalsHomeGreaterProposer, IndividualTotalsHomeLesserProposer, IndividualTotalsAwayGreaterProposer, IndividualTotalsAwayLesserProposer
from betrobot.betting.proposers.period_individual_totals_proposers import FirstPeriodIndividualTotalsHomeGreaterProposer, FirstPeriodIndividualTotalsHomeLesserProposer, FirstPeriodIndividualTotalsAwayGreaterProposer, FirstPeriodIndividualTotalsAwayLesserProposer, SecondPeriodIndividualTotalsHomeGreaterProposer, SecondPeriodIndividualTotalsHomeLesserProposer, SecondPeriodIndividualTotalsAwayGreaterProposer, SecondPeriodIndividualTotalsAwayLesserProposer


class YellowCardsMatchProposer(object):

    def _handle(self, betcity_match, prediction, whoscored_match=None, **kwargs):
        if prediction is None:
            return

        if not is_betarch_match_yellow_card(betcity_match):
            return

        super()._handle(betcity_match, prediction, whoscored_match=whoscored_match, **kwargs)


class YellowCardsResults1Proposer(YellowCardsMatchProposer, Results1Proposer, Proposer):
    pass


class YellowCardsResults1XProposer(YellowCardsMatchProposer, Results1XProposer, Proposer):
    pass


class YellowCardsResultsX2Proposer(YellowCardsMatchProposer, ResultsX2Proposer, Proposer):
    pass


class YellowCardsResults2Proposer(YellowCardsMatchProposer, Results2Proposer, Proposer):
    pass


class YellowCardsFirstPeriodResults1Proposer(YellowCardsMatchProposer, FirstPeriodResults1Proposer, Proposer):
    pass


class YellowCardsFirstPeriodResults1XProposer(YellowCardsMatchProposer, FirstPeriodResults1XProposer, Proposer):
    pass


class YellowCardsFirstPeriodResultsX2Proposer(YellowCardsMatchProposer, FirstPeriodResultsX2Proposer, Proposer):
    pass


class YellowCardsFirstPeriodResults2Proposer(YellowCardsMatchProposer, FirstPeriodResults2Proposer, Proposer):
    pass


class YellowCardsSecondPeriodResults1Proposer(YellowCardsMatchProposer, SecondPeriodResults1Proposer, Proposer):
    pass


class YellowCardsSecondPeriodResults1XProposer(YellowCardsMatchProposer, SecondPeriodResults1XProposer, Proposer):
    pass


class YellowCardsSecondPeriodResultsX2Proposer(YellowCardsMatchProposer, SecondPeriodResultsX2Proposer, Proposer):
    pass


class YellowCardsSecondPeriodResults2Proposer(YellowCardsMatchProposer, SecondPeriodResults2Proposer, Proposer):
    pass


class YellowCardsHandicapsHomeProposer(YellowCardsMatchProposer, HandicapsHomeProposer, Proposer):
    pass


class YellowCardsHandicapsAwayProposer(YellowCardsMatchProposer, HandicapsAwayProposer, Proposer):
    pass


class YellowCardsFirstPeriodHandicapsHomeProposer(YellowCardsMatchProposer, FirstPeriodHandicapsHomeProposer, Proposer):
    pass


class YellowCardsFirstPeriodHandicapsAwayProposer(YellowCardsMatchProposer, FirstPeriodHandicapsAwayProposer, Proposer):
    pass


class YellowCardsSecondPeriodHandicapsHomeProposer(YellowCardsMatchProposer, SecondPeriodHandicapsHomeProposer, Proposer):
    pass


class YellowCardsSecondPeriodHandicapsAwayProposer(YellowCardsMatchProposer, SecondPeriodHandicapsAwayProposer, Proposer):
    pass


class YellowCardsTotalsGreaterProposer(YellowCardsMatchProposer, TotalsGreaterProposer, Proposer):
    pass


class YellowCardsTotalsLesserProposer(YellowCardsMatchProposer, TotalsLesserProposer, Proposer):
    pass


class YellowCardsFirstPeriodTotalsGreaterProposer(YellowCardsMatchProposer, FirstPeriodTotalsGreaterProposer, Proposer):
    pass


class YellowCardsFirstPeriodTotalsLesserProposer(YellowCardsMatchProposer, FirstPeriodTotalsLesserProposer, Proposer):
    pass


class YellowCardsSecondPeriodTotalsGreaterProposer(YellowCardsMatchProposer, SecondPeriodTotalsGreaterProposer, Proposer):
    pass


class YellowCardsSecondPeriodTotalsLesserProposer(YellowCardsMatchProposer, SecondPeriodTotalsLesserProposer, Proposer):
    pass


class YellowCardsIndividualTotalsHomeGreaterProposer(YellowCardsMatchProposer, IndividualTotalsHomeGreaterProposer, Proposer):
    pass


class YellowCardsIndividualTotalsHomeLesserProposer(YellowCardsMatchProposer, IndividualTotalsHomeLesserProposer, Proposer):
    pass


class YellowCardsIndividualTotalsAwayGreaterProposer(YellowCardsMatchProposer, IndividualTotalsAwayGreaterProposer, Proposer):
    pass


class YellowCardsIndividualTotalsAwayLesserProposer(YellowCardsMatchProposer, IndividualTotalsAwayLesserProposer, Proposer):
    pass


class YellowCardsFirstPeriodIndividualTotalsHomeGreaterProposer(YellowCardsMatchProposer, FirstPeriodIndividualTotalsHomeGreaterProposer, Proposer):
    pass


class YellowCardsFirstPeriodIndividualTotalsHomeLesserProposer(YellowCardsMatchProposer, FirstPeriodIndividualTotalsHomeLesserProposer, Proposer):
    pass


class YellowCardsFirstPeriodIndividualTotalsAwayGreaterProposer(YellowCardsMatchProposer, FirstPeriodIndividualTotalsAwayGreaterProposer, Proposer):
    pass


class YellowCardsFirstPeriodIndividualTotalsAwayLesserProposer(YellowCardsMatchProposer, FirstPeriodIndividualTotalsAwayLesserProposer, Proposer):
    pass


class YellowCardsSecondPeriodIndividualTotalsHomeGreaterProposer(YellowCardsMatchProposer, SecondPeriodIndividualTotalsHomeGreaterProposer, Proposer):
    pass


class YellowCardsSecondPeriodIndividualTotalsHomeLesserProposer(YellowCardsMatchProposer, SecondPeriodIndividualTotalsHomeLesserProposer, Proposer):
    pass


class YellowCardsSecondPeriodIndividualTotalsAwayGreaterProposer(YellowCardsMatchProposer, SecondPeriodIndividualTotalsAwayGreaterProposer, Proposer):
    pass


class YellowCardsSecondPeriodIndividualTotalsAwayLesserProposer(YellowCardsMatchProposer, SecondPeriodIndividualTotalsAwayLesserProposer, Proposer):
    pass
