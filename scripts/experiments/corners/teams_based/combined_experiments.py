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

from betrobot.betting.predictors.combined_result_predictor import CombinedResultPredictor

from betrobot.betting.proposers.combined_handicaps_proposers import CombinedHandicapsHomeProposer, CombinedHandicapsAwayProposer

from betrobot.betting.experiment import Experiment

from betrobot.betting.presenters.table_summary_presenter import TableSummaryPresenter


if __name__ == '__main__':

    test_sample_condition = {
       'date': { '$gte': datetime.datetime(2016, 6, 1) }
    }


    fitters_sets_base1 = [
        [ (MatchHeadersSamplerFitter, (), {}) ],
        [ (AttainableMatchesFilterStatisticTransformerFitter, (), {}) ],
        [ (TournamentFilterStatisticTransformerFitter, (), {}) ],
        [ (MatchEveFilterStatisticTransformerFitter, (), { 'days': 30 }) ]
    ]
    fitters_sets_base2 = [
    ]


    proposers = [
        (CombinedHandicapsHomeProposer, (), { 'value_threshold': 1.8 }),
        (CombinedHandicapsAwayProposer, (), { 'value_threshold': 1.8 })
    ]


    experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'fitters_sets': [
            cartesian_product([], *(fitters_sets_base1 + [ [ (CrossesFirstPeriodStatisticExtenderFitter, (), {}), (ShotsFirstPeriodStatisticExtenderFitter, (), {}) ] ] + fitters_sets_base2))
        ],
        'predictor': [ (CombinedResultPredictor, (), {}) ],
        'proposers': [ proposers ]
    })

    presenter = TableSummaryPresenter()
    presenters = [ presenter ]

    experiment = Experiment(experiments_data, presenters, test_sample_condition=test_sample_condition)
    experiment.test()

    representation = experiment.get_representation()
    print(representation)
