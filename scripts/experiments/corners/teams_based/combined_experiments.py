#!/usr/bin/env python3


import datetime
from betrobot.util.reproduce_util import cartesian_product_of_dict_item, cartesian_product, multiple_cartesian_product_of_dict_item, make_sets_of_object_templates

from betrobot.betting.fitters.match_headers_sampler_fitter import MatchHeadersSamplerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.attainable_matches_filter_statistic_transformer_fitter import AttainableMatchesFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.tournament_filter_statistic_transformer_fitter import TournamentFilterStatisticTransformerFitter
from betrobot.betting.fitters.statistic_transformer_fitters.match_eve_filter_statistic_transformer_fitter import MatchEveFilterStatisticTransformerFitter

from betrobot.betting.fitters.statistic_extender_fitters.teams_based.crosses_statistic_extender_fitters import CrossesFirstPeriodStatisticExtenderFitter
from betrobot.betting.fitters.statistic_extender_fitters.teams_based.shots_statistic_extender_fitters import ShotsFirstPeriodStatisticExtenderFitter

from betrobot.betting.predictors.combined_result_predictor import CombinedResultPredictor

from betrobot.betting.proposers.combined_handicaps_proposers import CombinedHandicapsHomeProposer, CombinedHandicapsAwayProposer, CombinedFirstPeriodHandicapsHomeProposer, CombinedFirstPeriodHandicapsAwayProposer

from betrobot.betting.experiment import Experiment

from betrobot.betting.presenters.table_summary_presenter import TableSummaryPresenter


if __name__ == '__main__':

    test_sample_condition = {
       'date': { '$gte': datetime.datetime(2014, 1, 1), '$lt': datetime.datetime(2017, 6, 1) }
    }


    fitters_sets = [
        [ (MatchHeadersSamplerFitter, (), {}) ],
        [ (AttainableMatchesFilterStatisticTransformerFitter, (), {}) ],
        [ (TournamentFilterStatisticTransformerFitter, (), {}) ],
        [ (MatchEveFilterStatisticTransformerFitter, (), { 'days': 30 }) ],

        [ (CrossesFirstPeriodStatisticExtenderFitter, (), {}), (ShotsFirstPeriodStatisticExtenderFitter, (), {}) ]
    ]


    proposers = [
        (CombinedHandicapsHomeProposer, (), { 'value_threshold': 1.8 }),
        (CombinedHandicapsAwayProposer, (), { 'value_threshold': 1.8 }),
        (CombinedFirstPeriodHandicapsHomeProposer, (), { 'value_threshold': 1.8 }),
        (CombinedFirstPeriodHandicapsAwayProposer, (), { 'value_threshold': 1.8 })
    ]


    experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
        'fitters_sets': [
            cartesian_product([], *fitters_sets)
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
