#!/usr/bin/env python3


from betrobot.betting.fitters.match_headers_sampler_fitter import MatchHeadersSamplerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.attainable_matches_filter_statistic_transformer_fitter import AttainableMatchesFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.tournament_filter_statistic_transformer_fitter import TournamentFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.match_eve_filter_statistic_transformer_fitter import MatchEveFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.last_matches_filter_statistic_transformer_fitter import LastMatchesFilterStatisticTransformerFitter

from betrobot.betting.fitters.statistic_extender_fitters.teams_based.corners_statistic_extender_fitters import CornersStatisticExtenderFitter, CornersFirstPeriodStatisticExtenderFitter, CornersSecondPeriodStatisticExtenderFitter
from betrobot.betting.fitters.statistic_extender_fitters.teams_based.crosses_statistic_extender_fitters import CrossesStatisticExtenderFitter, CrossesFirstPeriodStatisticExtenderFitter, CrossesSecondPeriodStatisticExtenderFitter
from betrobot.betting.fitters.statistic_extender_fitters.teams_based.shots_statistic_extender_fitters import ShotsStatisticExtenderFitter, ShotsFirstPeriodStatisticExtenderFitter, ShotsSecondPeriodStatisticExtenderFitter

from betrobot.betting.predictors.corners_results_result_predictors import CornersResultsResultPredictor, CornersViaPassesResultsResultPredictor

from betrobot.betting.proposers.corners_result_proposers import CornersResults1ResultProposer, CornersResults1XResultProposer, CornersResultsX2ResultProposer, CornersResults2ResultProposer, CornersFirstPeriodResults1ResultProposer, CornersFirstPeriodResults1XResultProposer, CornersFirstPeriodResultsX2ResultProposer, CornersFirstPeriodResults2ResultProposer, CornersSecondPeriodResults1ResultProposer, CornersSecondPeriodResults1XResultProposer, CornersSecondPeriodResultsX2ResultProposer, CornersSecondPeriodResults2ResultProposer, CornersHandicapsHomeResultProposer, CornersHandicapsAwayResultProposer, CornersFirstPeriodHandicapsHomeResultProposer, CornersFirstPeriodHandicapsAwayResultProposer, CornersSecondPeriodHandicapsHomeResultProposer, CornersSecondPeriodHandicapsAwayResultProposer, CornersTotalsGreaterResultProposer, CornersTotalsLesserResultProposer, CornersFirstPeriodTotalsGreaterResultProposer, CornersFirstPeriodTotalsLesserResultProposer, CornersSecondPeriodTotalsGreaterResultProposer, CornersSecondPeriodTotalsLesserResultProposer, CornersIndividualTotalsHomeGreaterResultProposer, CornersIndividualTotalsHomeLesserResultProposer, CornersIndividualTotalsAwayGreaterResultProposer, CornersIndividualTotalsAwayLesserResultProposer, CornersFirstPeriodIndividualTotalsHomeGreaterResultProposer, CornersFirstPeriodIndividualTotalsHomeLesserResultProposer, CornersFirstPeriodIndividualTotalsAwayGreaterResultProposer, CornersFirstPeriodIndividualTotalsAwayLesserResultProposer, CornersSecondPeriodIndividualTotalsHomeGreaterResultProposer, CornersSecondPeriodIndividualTotalsHomeLesserResultProposer, CornersSecondPeriodIndividualTotalsAwayGreaterResultProposer, CornersSecondPeriodIndividualTotalsAwayLesserResultProposer

from betrobot.betting.provider import Provider


if __name__ == '__main__':

    fitters_set_base1 = [
        (MatchHeadersSamplerFitter, (), {}),
        (AttainableMatchesFilterStatisticTransformerFitter, (), {}),
        (TournamentFilterStatisticTransformerFitter, (), {}),
        (MatchEveFilterStatisticTransformerFitter, (), {}),
    ]

    fitters_set_base2 = [
    ]


    corners_result_proposers = [
        (CornersResultsX2ResultProposer, (), { 'min_margin': 1, 'value_threshold': 1.8 }),
        (CornersResults2ResultProposer, (), { 'min_margin': 1, 'value_threshold': 1.8 }),
        (CornersIndividualTotalsHomeGreaterResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 }),
        (CornersIndividualTotalsAwayGreaterResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 }),
        (CornersIndividualTotalsAwayLesserResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 })
    ]
    corners_first_period_result_proposers = [
        (CornersFirstPeriodHandicapsAwayResultProposer, (), { 'min_margin': 1, 'value_threshold': 2.2 })
    ]
    corners_second_period_result_proposers = [
        (CornersSecondPeriodResults1ResultProposer, (), { 'min_margin': 0, 'value_threshold': 2.0 }),
        (CornersSecondPeriodResults1XResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 })
    ]


    match_provider = Provider(fitters_sets=[
                                  fitters_set_base1 + [ (CornersStatisticExtenderFitter, (), {}) ] + fitters_set_base2
                              ],
                              predictor=CornersResultsResultPredictor(),
                              proposers=corners_result_proposers,
                              description='Угловые по средним угловых команд, матч')
    match_provider.save()

    first_period_provider = Provider(fitters_sets=[
                                         fitters_set_base1 + [ (CornersFirstPeriodStatisticExtenderFitter, (), {}) ] + fitters_set_base2
                                     ],
                                     predictor=CornersResultsResultPredictor(),
                                     proposers=corners_first_period_result_proposers,
                                     description='Угловые по средним угловых команд, 1-й тайм')
    first_period_provider.save()

    second_time_provider = Provider(fitters_sets=[
                                        fitters_set_base1 + [ (CornersSecondPeriodStatisticExtenderFitter, (), {}) ] + fitters_set_base2
                                    ],
                                    predictor=CornersResultsResultPredictor(),
                                    proposers=corners_second_period_result_proposers,
                                    description='Угловые по средним угловых команд, 2-й тайм')
    second_time_provider.save()
