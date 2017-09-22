#!/usr/bin/env python3


import datetime
from betrobot.util.reproduce_util import cartesian_product_of_dict_item, cartesian_product, multiple_cartesian_product_of_dict_item, make_sets_of_object_templates

from betrobot.betting.fitters.match_headers_sampler_fitter import MatchHeadersSamplerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.attainable_matches_filter_statistic_transformer_fitter import AttainableMatchesFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.tournament_filter_statistic_transformer_fitter import TournamentFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.match_eve_filter_statistic_transformer_fitter import MatchEveFilterStatisticTransformerFitter

from betrobot.betting.fitters.statistic_extender_fitters.teams_based.corners_statistic_extender_fitters import CornersStatisticExtenderFitter, CornersFirstPeriodStatisticExtenderFitter, CornersSecondPeriodStatisticExtenderFitter
from betrobot.betting.fitters.common_values_fitters.tournament_event_counts_means_fitter import TournamentEventCountsMeansFitter

from betrobot.betting.predictors.corners_attack_defense_results_result_predictors import CornersAttackDefenseResultsResultPredictor

from betrobot.betting.proposers.corners_result_proposers import CornersResults1ResultProposer, CornersResults1XResultProposer, CornersResultsX2ResultProposer, CornersResults2ResultProposer, CornersFirstPeriodResults1ResultProposer, CornersFirstPeriodResults1XResultProposer, CornersFirstPeriodResultsX2ResultProposer, CornersFirstPeriodResults2ResultProposer, CornersSecondPeriodResults1ResultProposer, CornersSecondPeriodResults1XResultProposer, CornersSecondPeriodResultsX2ResultProposer, CornersSecondPeriodResults2ResultProposer, CornersHandicapsHomeResultProposer, CornersHandicapsAwayResultProposer, CornersFirstPeriodHandicapsHomeResultProposer, CornersFirstPeriodHandicapsAwayResultProposer, CornersSecondPeriodHandicapsHomeResultProposer, CornersSecondPeriodHandicapsAwayResultProposer, CornersTotalsGreaterResultProposer, CornersTotalsLesserResultProposer, CornersFirstPeriodTotalsGreaterResultProposer, CornersFirstPeriodTotalsLesserResultProposer, CornersSecondPeriodTotalsGreaterResultProposer, CornersSecondPeriodTotalsLesserResultProposer, CornersIndividualTotalsHomeGreaterResultProposer, CornersIndividualTotalsHomeLesserResultProposer, CornersIndividualTotalsAwayGreaterResultProposer, CornersIndividualTotalsAwayLesserResultProposer, CornersFirstPeriodIndividualTotalsHomeGreaterResultProposer, CornersFirstPeriodIndividualTotalsHomeLesserResultProposer, CornersFirstPeriodIndividualTotalsAwayGreaterResultProposer, CornersFirstPeriodIndividualTotalsAwayLesserResultProposer, CornersSecondPeriodIndividualTotalsHomeGreaterResultProposer, CornersSecondPeriodIndividualTotalsHomeLesserResultProposer, CornersSecondPeriodIndividualTotalsAwayGreaterResultProposer, CornersSecondPeriodIndividualTotalsAwayLesserResultProposer

from betrobot.betting.experiment import Experiment

from betrobot.betting.presenters.table_summary_presenter import TableSummaryPresenter


if __name__ == '__main__':

    test_sample_condition = {
       'date': { '$gte': datetime.datetime(2014, 1, 1), '$lt': datetime.datetime(2017, 6, 1) }
    }


    fitters_sets_base1 = [
        [ (MatchHeadersSamplerFitter, (), { 'do_prefit': True, 'do_fit': False }) ],
        [ (AttainableMatchesFilterStatisticTransformerFitter, (), {}) ],
        [ (TournamentFilterStatisticTransformerFitter, (), {}) ],
        [ (MatchEveFilterStatisticTransformerFitter, (), { 'days': 100 }) ]
    ]
    fitters_sets_base2 = [
    ]

    # WARNING: Здесь не корректное поведение: используются все матчи, а не только доступные.
    # Это сделано для ускорения. Считается допустимым ввиду малой дисперсии средних
    tournament_event_counts_means_fitters_sets_base1 = [
        [ (MatchHeadersSamplerFitter, (), { 'do_prefit': True, 'do_fit': False }) ]
    ]
    tournament_event_counts_means_fitters_sets_base2 = [
        [ (TournamentEventCountsMeansFitter, (), { 'do_prefit': True, 'do_fit': False }) ]
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
        (CornersIndividualTotalsHomeLesserResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 }),
        (CornersIndividualTotalsAwayGreaterResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 }),
        (CornersIndividualTotalsAwayLesserResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 })
    ]
    corners_first_period_result_proposers = [
        (CornersFirstPeriodResults1ResultProposer, (), { 'min_margin': 0, 'value_threshold': 2.0 }),
        (CornersFirstPeriodResults1XResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 }),
        (CornersFirstPeriodResultsX2ResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 }),
        (CornersFirstPeriodResults2ResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 }),
        (CornersFirstPeriodHandicapsHomeResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 }),
        (CornersFirstPeriodHandicapsAwayResultProposer, (), { 'min_margin': 1, 'value_threshold': 2.2 }),
        (CornersFirstPeriodTotalsGreaterResultProposer, (), { 'min_margin': 1, 'value_threshold': 2.2 }),
        (CornersFirstPeriodTotalsLesserResultProposer, (), { 'min_margin': 0, 'value_threshold': 2.0 }),
        (CornersFirstPeriodIndividualTotalsHomeGreaterResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 }),
        (CornersFirstPeriodIndividualTotalsHomeLesserResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 }),
        (CornersFirstPeriodIndividualTotalsAwayGreaterResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 }),
        (CornersFirstPeriodIndividualTotalsAwayLesserResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 })
    ]
    corners_second_period_result_proposers = [
        (CornersSecondPeriodResults1ResultProposer, (), { 'min_margin': 0, 'value_threshold': 2.0 }),
        (CornersSecondPeriodResults1XResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 }),
        (CornersSecondPeriodResultsX2ResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 }),
        (CornersSecondPeriodResults2ResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 }),
        (CornersSecondPeriodHandicapsHomeResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 }),
        (CornersSecondPeriodHandicapsAwayResultProposer, (), { 'min_margin': 1, 'value_threshold': 2.2 }),
        (CornersSecondPeriodTotalsGreaterResultProposer, (), { 'min_margin': 1, 'value_threshold': 2.2 }),
        (CornersSecondPeriodTotalsLesserResultProposer, (), { 'min_margin': 0, 'value_threshold': 2.0 }),
        (CornersSecondPeriodIndividualTotalsHomeGreaterResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 }),
        (CornersSecondPeriodIndividualTotalsHomeLesserResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 }),
        (CornersSecondPeriodIndividualTotalsAwayGreaterResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.6 }),
        (CornersSecondPeriodIndividualTotalsAwayLesserResultProposer, (), { 'min_margin': 0, 'value_threshold': 1.8 })
    ]


    corners_result_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'fitters_sets': cartesian_product([],
            cartesian_product(
                *(fitters_sets_base1 + [ [ (CornersStatisticExtenderFitter, (), {}) ] ] + fitters_sets_base2)
            ),
            cartesian_product(
                *(tournament_event_counts_means_fitters_sets_base1 + [ [ (CornersStatisticExtenderFitter, (), { 'do_prefit': True, 'do_fit': False }) ] ] + tournament_event_counts_means_fitters_sets_base2)
            )
        ),
        'predictor': [ (CornersAttackDefenseResultsResultPredictor, (), {}) ],
        'proposers': [ corners_result_proposers ]
    })


    corners_first_period_result_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'fitters_sets': cartesian_product([],
            cartesian_product(
                *(fitters_sets_base1 + [ [ (CornersFirstPeriodStatisticExtenderFitter, (), {}) ] ] + fitters_sets_base2)
            ),
            cartesian_product(
                *(tournament_event_counts_means_fitters_sets_base1 + [ [ (CornersFirstPeriodStatisticExtenderFitter, (), { 'do_prefit': True, 'do_fit': False }) ] ] + tournament_event_counts_means_fitters_sets_base2)
            )
        ),
        'predictor': [ (CornersAttackDefenseResultsResultPredictor, (), {}) ],
        'proposers': [ corners_first_period_result_proposers ]
    })


    corners_second_period_result_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'fitters_sets': cartesian_product([],
            cartesian_product(
                *(fitters_sets_base1 + [ [ (CornersSecondPeriodStatisticExtenderFitter, (), {}) ] ] + fitters_sets_base2)
            ),
            cartesian_product(
                *(tournament_event_counts_means_fitters_sets_base1 + [ [ (CornersFirstPeriodStatisticExtenderFitter, (), { 'do_prefit': True, 'do_fit': False }) ] ] + tournament_event_counts_means_fitters_sets_base2)
            )
        ),
        'predictor': [ (CornersAttackDefenseResultsResultPredictor, (), {}) ],
        'proposers': [ corners_second_period_result_proposers ]
    })


    presenter = TableSummaryPresenter()
    presenters = [ presenter ]


    experiments_data = \
        corners_result_experiments_data + \
        corners_first_period_result_experiments_data + \
        corners_second_period_result_experiments_data

    experiment = Experiment(experiments_data, presenters, test_sample_condition=test_sample_condition)
    experiment.test()

    representation = experiment.get_representation()
    print(representation)
