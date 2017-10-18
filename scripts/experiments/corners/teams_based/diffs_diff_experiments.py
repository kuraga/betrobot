#!/usr/bin/env python3


import datetime
from betrobot.util.reproduce_util import cartesian_product_of_dict_item, cartesian_product, multiple_cartesian_product_of_dict_item, make_sets_of_object_templates

from betrobot.betting.fitters.match_headers_sampler_fitter import MatchHeadersSamplerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.attainable_matches_filter_statistic_transformer_fitter import AttainableMatchesFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.tournament_filter_statistic_transformer_fitter import TournamentFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.match_eve_filter_statistic_transformer_fitter import MatchEveFilterStatisticTransformerFitter

from betrobot.betting.fitters.statistic_extender_fitters.teams_based.corners_statistic_extender_fitters import CornersStatisticExtenderFitter, CornersFirstPeriodStatisticExtenderFitter, CornersSecondPeriodStatisticExtenderFitter
from betrobot.betting.fitters.statistic_extender_fitters.teams_based.crosses_statistic_extender_fitters import CrossesStatisticExtenderFitter, CrossesFirstPeriodStatisticExtenderFitter, CrossesSecondPeriodStatisticExtenderFitter
from betrobot.betting.fitters.statistic_extender_fitters.teams_based.shots_statistic_extender_fitters import ShotsStatisticExtenderFitter, ShotsFirstPeriodStatisticExtenderFitter, ShotsSecondPeriodStatisticExtenderFitter

from betrobot.betting.predictors.corners_diffs_diff_predictors import CornersDiffsDiffPredictor, CornersViaPassesDiffsDiffPredictor

from betrobot.betting.proposers.corners_diffs_diff_proposers import CornersResults1DiffsDiffProposer, CornersResults1XDiffsDiffProposer, CornersResultsX2DiffsDiffProposer, CornersResults2DiffsDiffProposer, CornersFirstPeriodResults1DiffsDiffProposer, CornersFirstPeriodResults1XDiffsDiffProposer, CornersFirstPeriodResultsX2DiffsDiffProposer, CornersFirstPeriodResults2DiffsDiffProposer, CornersSecondPeriodResults1DiffsDiffProposer, CornersSecondPeriodResults1XDiffsDiffProposer, CornersSecondPeriodResultsX2DiffsDiffProposer, CornersSecondPeriodResults2DiffsDiffProposer, CornersHandicapsHomeDiffsDiffProposer, CornersHandicapsAwayDiffsDiffProposer, CornersFirstPeriodHandicapsHomeDiffsDiffProposer, CornersFirstPeriodHandicapsAwayDiffsDiffProposer, CornersSecondPeriodHandicapsHomeDiffsDiffProposer, CornersSecondPeriodHandicapsAwayDiffsDiffProposer

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
        [ (MatchEveFilterStatisticTransformerFitter, (), {}) ]
    ]
    fitters_sets_base2 = [
    ]


    corners_diffs_diff_proposers = [
        (CornersResults1DiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.8 }),
        (CornersResults1XDiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.6 }),
        (CornersResultsX2DiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.6 }),
        (CornersResults2DiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.6 }),
        (CornersHandicapsHomeDiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.6 }),
        (CornersHandicapsAwayDiffsDiffProposer, (), { 'min_margin': 4, 'value_threshold': 2.0 })
    ]
    corners_first_period_diffs_diff_proposers = [
        (CornersFirstPeriodResults1DiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.6 }),
        (CornersFirstPeriodResults1XDiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.0 }),
        (CornersFirstPeriodResultsX2DiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.0 }),
        (CornersFirstPeriodResults2DiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.0 }),
        (CornersFirstPeriodHandicapsHomeDiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.6 }),
        (CornersFirstPeriodHandicapsAwayDiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.6 })
    ]
    corners_second_period_diffs_diff_proposers = [
        (CornersSecondPeriodResults1DiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.6 }),
        (CornersSecondPeriodResults1XDiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.0 }),
        (CornersSecondPeriodResultsX2DiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.0 }),
        (CornersSecondPeriodResults2DiffsDiffProposer, (), { 'min_margin': 2, 'value_threshold': 1.0 }),
        (CornersSecondPeriodHandicapsHomeDiffsDiffProposer, (), { 'min_margin': 3, 'value_threshold': 1.6 }),
        (CornersSecondPeriodHandicapsAwayDiffsDiffProposer, (), { 'min_margin': 4, 'value_threshold': 1.6 })
    ]


    corners_diffs_diff_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'fitters_sets': [
            cartesian_product([], *(fitters_sets_base1 + [ [ (CornersStatisticExtenderFitter, (), {}) ] ] + fitters_sets_base2))
        ],
        'predictor': [ (CornersDiffsDiffPredictor, (), {}) ],
        'proposers': [ corners_diffs_diff_proposers ]
    })

    corners_first_period_diffs_diff_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'fitters_sets': [
            cartesian_product([], *(fitters_sets_base1 + [ [ (CornersFirstPeriodStatisticExtenderFitter, (), {}) ] ] + fitters_sets_base2))
        ],
        'predictor': [ (CornersDiffsDiffPredictor, (), {}) ],
        'proposers': [ corners_first_period_diffs_diff_proposers ]
    })

    corners_second_period_diffs_diff_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'fitters_sets': [
            cartesian_product([], *(fitters_sets_base1 + [ [ (CornersSecondPeriodStatisticExtenderFitter, (), {}) ] ] + fitters_sets_base2))
        ],
        'predictor': [ (CornersDiffsDiffPredictor, (), {}) ],
        'proposers': [ corners_second_period_diffs_diff_proposers ]
    })


    presenter = TableSummaryPresenter()
    presenters = [ presenter ]


    experiments_data = \
        corners_diffs_diff_experiments_data + \
        corners_first_period_diffs_diff_experiments_data + \
        corners_second_period_diffs_diff_experiments_data

    experiment = Experiment(experiments_data, presenters, test_sample_condition=test_sample_condition)
    experiment.test()

    representation = experiment.get_representation()
    print(representation)
