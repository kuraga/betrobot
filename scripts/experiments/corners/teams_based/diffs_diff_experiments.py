#!/usr/bin/env python3


import datetime
from betrobot.util.reproduce_util import cartesian_product_of_dict_item, cartesian_product, multiple_cartesian_product_of_dict_item, make_sets_of_object_templates

from betrobot.betting.samplers.whole_sampler import WholeSampler

from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.corners_statistic_fitters import CornersStatisticFitter, CornersFirstPeriodStatisticFitter, CornersSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.crosses_statistic_fitters import CrossesStatisticFitter, CrossesFirstPeriodStatisticFitter, CrossesSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.shots_statistic_fitters import ShotsStatisticFitter, ShotsFirstPeriodStatisticFitter, ShotsSecondPeriodStatisticFitter

from betrobot.betting.fitters.attainable_matches_filter_fitter_statistic_transformer_fitter import AttainableMatchesFilterStatisticTransformerFitter
from betrobot.betting.fitters.tournament_filter_statistic_transformer_fitter import TournamentFilterStatisticTransformerFitter
from betrobot.betting.fitters.match_eve_statistic_transformer_fitter import MatchEveStatisticTransformerFitter
from betrobot.betting.fitters.diffs_fitter import DiffsFitter

from betrobot.betting.predictors.corners_diffs_diff_predictors import CornersDiffsDiffPredictor, CornersViaPassesDiffsDiffPredictor
from betrobot.betting.predictors.corners_diffs_diff_predictors import CornersDiffsDiffPredictor, CornersViaPassesDiffsDiffPredictor

from betrobot.betting.proposers.corners_diffs_diff_proposers import CornersResults1DiffsDiffProposer, CornersResults1XDiffsDiffProposer, CornersResultsX2DiffsDiffProposer, CornersResults2DiffsDiffProposer, CornersFirstPeriodResults1DiffsDiffProposer, CornersFirstPeriodResults1XDiffsDiffProposer, CornersFirstPeriodResultsX2DiffsDiffProposer, CornersFirstPeriodResults2DiffsDiffProposer, CornersSecondPeriodResults1DiffsDiffProposer, CornersSecondPeriodResults1XDiffsDiffProposer, CornersSecondPeriodResultsX2DiffsDiffProposer, CornersSecondPeriodResults2DiffsDiffProposer, CornersHandicapsHomeDiffsDiffProposer, CornersHandicapsAwayDiffsDiffProposer, CornersFirstPeriodHandicapsHomeDiffsDiffProposer, CornersFirstPeriodHandicapsAwayDiffsDiffProposer, CornersSecondPeriodHandicapsHomeDiffsDiffProposer, CornersSecondPeriodHandicapsAwayDiffsDiffProposer
from betrobot.betting.proposers.corners_diffs_diff_proposers import CornersResults1DiffsDiffProposer, CornersResults1XDiffsDiffProposer, CornersResultsX2DiffsDiffProposer, CornersResults2DiffsDiffProposer, CornersFirstPeriodResults1DiffsDiffProposer, CornersFirstPeriodResults1XDiffsDiffProposer, CornersFirstPeriodResultsX2DiffsDiffProposer, CornersFirstPeriodResults2DiffsDiffProposer, CornersSecondPeriodResults1DiffsDiffProposer, CornersSecondPeriodResults1XDiffsDiffProposer, CornersSecondPeriodResultsX2DiffsDiffProposer, CornersSecondPeriodResults2DiffsDiffProposer, CornersHandicapsHomeDiffsDiffProposer, CornersHandicapsAwayDiffsDiffProposer, CornersFirstPeriodHandicapsHomeDiffsDiffProposer, CornersFirstPeriodHandicapsAwayDiffsDiffProposer, CornersSecondPeriodHandicapsHomeDiffsDiffProposer, CornersSecondPeriodHandicapsAwayDiffsDiffProposer

from betrobot.betting.experiment import Experiment

from betrobot.betting.presenters.table_summary_presenter import TableSummaryPresenter


if __name__ == '__main__':

    db_name = 'betrobot'
    collection_name = 'matches'
    train_sample_condition = { }
    test_sample_condition = {
       'date': { '$gte': datetime.datetime(2017, 1, 1) }
    }


    train_sampler = WholeSampler(db_name, collection_name)


    corners_diffs_diff_fitters_sets_variants = cartesian_product(
        [ (AttainableMatchesFilterStatisticTransformerFitter, (), {}) ],
        [ (TournamentFilterStatisticTransformerFitter, (), {}) ],
        [ (MatchEveStatisticTransformerFitter, (), {}) ],
        [ (DiffsFitter, (), {}) ]
    )
    corners_diffs_diff_fitters_sets = cartesian_product([], corners_diffs_diff_fitters_sets_variants)
    corners_via_passes_diffs_diff_fitters_sets = cartesian_product([], corners_diffs_diff_fitters_sets_variants, corners_diffs_diff_fitters_sets_variants)


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
        'train_sampler': [ train_sampler ],
        'fitters': [ [ (CornersStatisticFitter, (), {}) ] ] * len(corners_diffs_diff_fitters_sets),
        'fitters_sets': corners_diffs_diff_fitters_sets,
        'predictor': [ (CornersDiffsDiffPredictor, (), {}) ],
        'proposers': [ corners_diffs_diff_proposers ]
    })

    corners_first_period_diffs_diff_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'train_sampler': [ train_sampler ],
        'fitters': [ [ (CornersFirstPeriodStatisticFitter, (), {}) ] ] * len(corners_diffs_diff_fitters_sets),
        'fitters_sets': corners_diffs_diff_fitters_sets,
        'predictor': [ (CornersDiffsDiffPredictor, (), {}) ],
        'proposers': [ corners_first_period_diffs_diff_proposers ]
    })

    corners_second_period_diffs_diff_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'train_sampler': [ train_sampler ],
        'fitters': [ [ (CornersSecondPeriodStatisticFitter, (), {}) ] ] * len(corners_diffs_diff_fitters_sets),
        'fitters_sets': corners_diffs_diff_fitters_sets,
        'predictor': [ (CornersDiffsDiffPredictor, (), {}) ],
        'proposers': [ corners_second_period_diffs_diff_proposers ]
    })

    corners_via_passes_diffs_diff_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'train_sampler': [ train_sampler ],
        'fitters': [ [ (CrossesStatisticFitter, (), {}), (ShotsStatisticFitter, (), {}) ] ] * len(corners_via_passes_diffs_diff_fitters_sets),
        'fitters_sets': corners_via_passes_diffs_diff_fitters_sets,
        'predictor': [ (CornersViaPassesDiffsDiffPredictor, (), {}) ],
        'proposers': [ corners_diffs_diff_proposers ]
    })

    corners_via_passes_first_period_diffs_diff_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'train_sampler': [ train_sampler ],
        'fitters': [ [ (CrossesFirstPeriodStatisticFitter, (), {}), (ShotsFirstPeriodStatisticFitter, (), {}) ] ] * len(corners_via_passes_diffs_diff_fitters_sets),
        'fitters_sets': corners_via_passes_diffs_diff_fitters_sets,
        'predictor': [ (CornersViaPassesDiffsDiffPredictor, (), {}) ],
        'proposers': [ corners_first_period_diffs_diff_proposers ]
    })


    corners_via_passes_second_period_diffs_diff_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'train_sampler': [ train_sampler ],
        'fitters': [ [ (CrossesSecondPeriodStatisticFitter, (), {}), (ShotsSecondPeriodStatisticFitter, (), {}) ] ] * len(corners_via_passes_diffs_diff_fitters_sets),
        'fitters_sets': corners_via_passes_diffs_diff_fitters_sets,
        'predictor': [ (CornersViaPassesDiffsDiffPredictor, (), {}) ],
        'proposers': [ corners_second_period_diffs_diff_proposers ]
    })


    presenter = TableSummaryPresenter()
    presenters = [ presenter ]


    experiments_data = \
        corners_diffs_diff_experiments_data + \
        corners_via_passes_diffs_diff_experiments_data + \
        corners_first_period_diffs_diff_experiments_data + \
        corners_via_passes_first_period_diffs_diff_experiments_data + \
        corners_second_period_diffs_diff_experiments_data + \
        corners_via_passes_second_period_diffs_diff_experiments_data


    experiment = Experiment(experiments_data, presenters, db_name=db_name, collection_name=collection_name, train_sample_condition=train_sample_condition, test_sample_condition=test_sample_condition)
    experiment.test()

    representation = experiment.get_representation()
    print(representation)
