#!/usr/bin/env python3


from betrobot.betting.fitters.match_headers_sampler_fitter import MatchHeadersSamplerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.attainable_matches_filter_statistic_transformer_fitter import AttainableMatchesFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.tournament_filter_statistic_transformer_fitter import TournamentFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.match_eve_filter_statistic_transformer_fitter import MatchEveFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.last_matches_filter_statistic_transformer_fitter import LastMatchesFilterStatisticTransformerFitter

from betrobot.betting.fitters.statistic_extender_fitters.players_based.corners_players_based_statistic_extender_fitters import CornersPlayersBasedStatisticExtenderFitter, CornersFirstPeriodPlayersBasedStatisticExtenderFitter, CornersSecondPeriodPlayersBasedStatisticExtenderFitter
from betrobot.betting.fitters.statistic_extender_fitters.players_based.crosses_players_based_statistic_extender_fitters import CrossesPlayersBasedStatisticExtenderFitter, CrossesFirstPeriodPlayersBasedStatisticExtenderFitter, CrossesSecondPeriodPlayersBasedStatisticExtenderFitter
from betrobot.betting.fitters.statistic_extender_fitters.players_based.shots_players_based_statistic_extender_fitters import ShotsPlayersBasedStatisticExtenderFitter, ShotsFirstPeriodPlayersBasedStatisticExtenderFitter, ShotsSecondPeriodPlayersBasedStatisticExtenderFitter

from betrobot.betting.predictors.corners_player_counts_result_predictors import CornersPlayerCountsResultPredictor, CornersViaPassesPlayerCountsResultPredictor

from betrobot.betting.proposers.corners_result_proposers import CornersResults1ResultProposer, CornersResults1XResultProposer, CornersResultsX2ResultProposer, CornersResults2ResultProposer, CornersFirstPeriodResults1ResultProposer, CornersFirstPeriodResults1XResultProposer, CornersFirstPeriodResultsX2ResultProposer, CornersFirstPeriodResults2ResultProposer, CornersSecondPeriodResults1ResultProposer, CornersSecondPeriodResults1XResultProposer, CornersSecondPeriodResultsX2ResultProposer, CornersSecondPeriodResults2ResultProposer, CornersHandicapsHomeResultProposer, CornersHandicapsAwayResultProposer, CornersFirstPeriodHandicapsHomeResultProposer, CornersFirstPeriodHandicapsAwayResultProposer, CornersSecondPeriodHandicapsHomeResultProposer, CornersSecondPeriodHandicapsAwayResultProposer, CornersTotalsGreaterResultProposer, CornersTotalsLesserResultProposer, CornersFirstPeriodTotalsGreaterResultProposer, CornersFirstPeriodTotalsLesserResultProposer, CornersSecondPeriodTotalsGreaterResultProposer, CornersSecondPeriodTotalsLesserResultProposer, CornersIndividualTotalsHomeGreaterResultProposer, CornersIndividualTotalsHomeLesserResultProposer, CornersIndividualTotalsAwayGreaterResultProposer, CornersIndividualTotalsAwayLesserResultProposer, CornersFirstPeriodIndividualTotalsHomeGreaterResultProposer, CornersFirstPeriodIndividualTotalsHomeLesserResultProposer, CornersFirstPeriodIndividualTotalsAwayGreaterResultProposer, CornersFirstPeriodIndividualTotalsAwayLesserResultProposer, CornersSecondPeriodIndividualTotalsHomeGreaterResultProposer, CornersSecondPeriodIndividualTotalsHomeLesserResultProposer, CornersSecondPeriodIndividualTotalsAwayGreaterResultProposer, CornersSecondPeriodIndividualTotalsAwayLesserResultProposer

from betrobot.betting.provider import Provider


if __name__ == '__main__':

    fitters_set_base1 = [
        (MatchHeadersSamplerFitter, (), {}),
        (AttainableMatchesFilterStatisticTransformerFitter, (), {}),
        (TournamentFilterStatisticTransformerFitter, (), {}),
        (MatchEveFilterStatisticTransformerFitter, (), {})
    ]

    fitters_set_base2 = [
    ]


    corners_result_proposers = [
        (CornersResults1ResultProposer, (), { 'min_margin': 1, 'value_threshold': 2.0 }),
        (CornersResults1XResultProposer, (), { 'min_margin': 1, 'value_threshold': 1.8 }),
        (CornersResultsX2ResultProposer, (), { 'min_margin': 1, 'value_threshold': 1.8 }),
        (CornersResults2ResultProposer, (), { 'min_margin': 1, 'value_threshold': 1.8 }),
        (CornersHandicapsHomeResultProposer, (), { 'min_margin': 1, 'value_threshold': 1.8 }),
        (CornersHandicapsAwayResultProposer, (), { 'min_margin': 2, 'value_threshold': 2.2 }),
        (CornersTotalsGreaterResultProposer, (), { 'min_margin': 2, 'value_threshold': 2.2 }),
        (CornersTotalsLesserResultProposer, (), { 'min_margin': 1, 'value_threshold': 2.0 }),
        (CornersIndividualTotalsHomeGreaterResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 }),
        (CornersIndividualTotalsAwayGreaterResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 })
    ]
    corners_first_period_result_proposers = [
        (CornersFirstPeriodResults1ResultProposer, (), { 'min_margin': 0, 'value_threshold': 2.0 }),
        (CornersFirstPeriodResults1XResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 }),
        (CornersFirstPeriodHandicapsAwayResultProposer, (), { 'min_margin': 1, 'value_threshold': 2.2 })
    ]
    corners_second_period_result_proposers = [
        (CornersSecondPeriodResults1ResultProposer, (), { 'min_margin': 0, 'value_threshold': 2.0 }),
        (CornersSecondPeriodResults1XResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 }),
        (CornersSecondPeriodHandicapsHomeResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 })
    ]


    match_provider = Provider(fitters_sets=[
                                  fitters_set_base1 + [ (CornersPlayersBasedStatisticExtenderFitter, (), {}) ] + fitters_set_base2
                              ],
                              predictor=CornersPlayerCountsResultPredictor(),
                              proposers=corners_result_proposers,
                              description='Угловые по средним угловых игроков, матч')
    match_provider.save()

    first_period_provider = Provider(fitters_sets=[
                                         fitters_set_base1 + [ (CornersFirstPeriodPlayersBasedStatisticExtenderFitter, (), {}) ] + fitters_set_base2
                                     ],
                                     predictor=CornersPlayerCountsResultPredictor(),
                                     proposers=corners_first_period_result_proposers,
                                     description='Угловые по средним угловых игроков, 1-й тайм')
    first_period_provider.save()

    second_time_provider = Provider(fitters_sets=[
                                        fitters_set_base1 + [ (CornersSecondPeriodPlayersBasedStatisticExtenderFitter, (), {}) ] + fitters_set_base2
                                    ],
                                    predictor=CornersPlayerCountsResultPredictor(),
                                    proposers=corners_second_period_result_proposers,
                                    description='Угловые по средним угловых игроков, 2-й тайм')
    second_time_provider.save()
