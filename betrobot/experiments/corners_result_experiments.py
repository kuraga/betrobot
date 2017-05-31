import datetime
from betrobot.util.reproduce_util import cartesian_product_of_dict_item, cartesian_product, multiple_cartesian_product_of_dict_item, make_sets_of_object_templates

from betrobot.betting.samplers.whole_sampler import WholeSampler

from betrobot.betting.fitters.corners_statistic_fitters import CornersStatisticFitter, CornersFirstPeriodStatisticFitter, CornersSecondPeriodStatisticFitter
from betrobot.betting.fitters.crosses_statistic_fitters import CrossesStatisticFitter, CrossesFirstPeriodStatisticFitter, CrossesSecondPeriodStatisticFitter
from betrobot.betting.fitters.saved_shots_statistic_fitters import SavedShotsStatisticFitter, SavedShotsFirstPeriodStatisticFitter, SavedShotsSecondPeriodStatisticFitter

from betrobot.betting.refitters.invalid_matches_filter_refitter_statistic_transformer_refitter import IvalidMatchesFilterStatisticTransformerRefitter
from betrobot.betting.refitters.tournament_filter_statistic_transformer_refitter import TournamentFilterStatisticTransformerRefitter
from betrobot.betting.refitters.date_filter_statistic_transformer_refitters import MatchEveStatisticTransformerRefitter
from betrobot.betting.refitters.results_refitter import ResultsRefitter

from betrobot.betting.predictors.corners_result_predictors import CornersResultPredictor, CornersViaPassesResultPredictor
from betrobot.betting.predictors.corners_result_predictors import CornersResultPredictor, CornersViaPassesResultPredictor

from betrobot.betting.proposers.corners_result_proposers import CornersResults1ResultProposer, CornersResults1XResultProposer, CornersResultsX2ResultProposer, CornersResults2ResultProposer, CornersFirstPeriodResults1ResultProposer, CornersFirstPeriodResults1XResultProposer, CornersFirstPeriodResultsX2ResultProposer, CornersFirstPeriodResults2ResultProposer, CornersSecondPeriodResults1ResultProposer, CornersSecondPeriodResults1XResultProposer, CornersSecondPeriodResultsX2ResultProposer, CornersSecondPeriodResults2ResultProposer, CornersHandicapsHomeResultProposer, CornersHandicapsAwayResultProposer, CornersFirstPeriodHandicapsHomeResultProposer, CornersFirstPeriodHandicapsAwayResultProposer, CornersSecondPeriodHandicapsHomeResultProposer, CornersSecondPeriodHandicapsAwayResultProposer, CornersTotalsGreaterResultProposer, CornersTotalsLesserResultProposer, CornersFirstPeriodTotalsGreaterResultProposer, CornersFirstPeriodTotalsLesserResultProposer, CornersSecondPeriodTotalsGreaterResultProposer, CornersSecondPeriodTotalsLesserResultProposer, CornersIndividualTotalsHomeGreaterResultProposer, CornersIndividualTotalsHomeLesserResultProposer, CornersIndividualTotalsAwayGreaterResultProposer, CornersIndividualTotalsAwayLesserResultProposer, CornersFirstPeriodIndividualTotalsHomeGreaterResultProposer, CornersFirstPeriodIndividualTotalsHomeLesserResultProposer, CornersFirstPeriodIndividualTotalsAwayGreaterResultProposer, CornersFirstPeriodIndividualTotalsAwayLesserResultProposer, CornersSecondPeriodIndividualTotalsHomeGreaterResultProposer, CornersSecondPeriodIndividualTotalsHomeLesserResultProposer, CornersSecondPeriodIndividualTotalsAwayGreaterResultProposer, CornersSecondPeriodIndividualTotalsAwayLesserResultProposer

from betrobot.betting.experiment import Experiment

from betrobot.betting.presenters.table_summary_presenter import TableSummaryPresenter


db_name = 'betrobot'
collection_name = 'matchesCleaned'
train_sample_condition = { }
test_sample_condition = {
   'date': { '$gte': datetime.datetime(2017, 1, 1) }
}


train_sampler = WholeSampler(db_name, collection_name)


corners_result_refitters_sets_variants = cartesian_product(
    [ (IvalidMatchesFilterStatisticTransformerRefitter, (), {}) ],
    [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
    [ (MatchEveStatisticTransformerRefitter, (), {}) ],
    [ (ResultsRefitter, (), {}) ]
)
corners_result_refitters_sets = cartesian_product([], corners_result_refitters_sets_variants)
corners_via_passes_result_refitters_sets = cartesian_product([], corners_result_refitters_sets_variants, corners_result_refitters_sets_variants)


corners_result_proposers = make_sets_of_object_templates(
    (), {}, [
        CornersResults1ResultProposer,
        CornersResults1XResultProposer,
        CornersResultsX2ResultProposer,
        CornersResults2ResultProposer,
        CornersHandicapsHomeResultProposer,
        CornersHandicapsAwayResultProposer,
        CornersTotalsGreaterResultProposer,
        CornersTotalsLesserResultProposer,
        CornersIndividualTotalsHomeGreaterResultProposer,
        CornersIndividualTotalsHomeLesserResultProposer,
        CornersIndividualTotalsAwayGreaterResultProposer,
        CornersIndividualTotalsAwayLesserResultProposer
    ]
)
corners_first_period_result_proposers = make_sets_of_object_templates(
    (), {}, [
        CornersFirstPeriodResults1ResultProposer,
        CornersFirstPeriodResults1XResultProposer,
        CornersFirstPeriodResultsX2ResultProposer,
        CornersFirstPeriodResults2ResultProposer,
        CornersFirstPeriodHandicapsHomeResultProposer,
        CornersFirstPeriodHandicapsAwayResultProposer,
        CornersFirstPeriodTotalsGreaterResultProposer,
        CornersFirstPeriodTotalsLesserResultProposer,
        CornersFirstPeriodIndividualTotalsHomeGreaterResultProposer,
        CornersFirstPeriodIndividualTotalsHomeLesserResultProposer,
        CornersFirstPeriodIndividualTotalsAwayGreaterResultProposer,
        CornersFirstPeriodIndividualTotalsAwayLesserResultProposer
    ]
)
corners_second_period_result_proposers = make_sets_of_object_templates(
    (), {}, [
        CornersSecondPeriodResults1ResultProposer,
        CornersSecondPeriodResults1XResultProposer,
        CornersSecondPeriodResultsX2ResultProposer,
        CornersSecondPeriodResults2ResultProposer,
        CornersSecondPeriodHandicapsHomeResultProposer,
        CornersSecondPeriodHandicapsAwayResultProposer,
        CornersSecondPeriodTotalsGreaterResultProposer,
        CornersSecondPeriodTotalsLesserResultProposer,
        CornersSecondPeriodIndividualTotalsHomeGreaterResultProposer,
        CornersSecondPeriodIndividualTotalsHomeLesserResultProposer,
        CornersSecondPeriodIndividualTotalsAwayGreaterResultProposer,
        CornersSecondPeriodIndividualTotalsAwayLesserResultProposer
    ]
)


corners_result_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CornersStatisticFitter, (), {}) ] ] * len(corners_result_refitters_sets),
    'refitters_sets': corners_result_refitters_sets,
    'predictor': [ (CornersResultPredictor, (), {}) ],
    'proposers': [ corners_result_proposers ]
})

corners_first_period_result_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CornersFirstPeriodStatisticFitter, (), {}) ] ] * len(corners_result_refitters_sets),
    'refitters_sets': corners_result_refitters_sets,
    'predictor': [ (CornersResultPredictor, (), {}) ],
    'proposers': [ corners_first_period_result_proposers ]
})

corners_second_period_result_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CornersSecondPeriodStatisticFitter, (), {}) ] ] * len(corners_result_refitters_sets),
    'refitters_sets': corners_result_refitters_sets,
    'predictor': [ (CornersResultPredictor, (), {}) ],
    'proposers': [ corners_second_period_result_proposers ]
})

corners_via_passes_result_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CrossesStatisticFitter, (), {}), (SavedShotsStatisticFitter, (), {}) ] ] * len(corners_result_refitters_sets),
    'refitters_sets': corners_via_passes_result_refitters_sets,
    'predictor': [ (CornersViaPassesResultPredictor, (), {}) ],
    'proposers': [ corners_result_proposers ]
})

corners_via_passes_first_period_result_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CrossesFirstPeriodStatisticFitter, (), {}), (SavedShotsFirstPeriodStatisticFitter, (), {}) ] ] * len(corners_result_refitters_sets),
    'refitters_sets': corners_via_passes_result_refitters_sets,
    'predictor': [ (CornersViaPassesResultPredictor, (), {}) ],
    'proposers': [ corners_first_period_result_proposers ]
})

corners_via_passes_second_period_result_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CrossesSecondPeriodStatisticFitter, (), {}), (SavedShotsSecondPeriodStatisticFitter, (), {}) ] ] * len(corners_result_refitters_sets),
    'refitters_sets': corners_via_passes_result_refitters_sets,
    'predictor': [ (CornersViaPassesResultPredictor, (), {}) ],
    'proposers': [ corners_second_period_result_proposers ]
})


presenter = TableSummaryPresenter(value_threshold=1.8, predicted_threshold=2.0, ratio_threshold=1.25)
presenters = [ presenter ]


experiments_data = \
    corners_result_experiments_data + \
    corners_via_passes_result_experiments_data + \
    corners_first_period_result_experiments_data + \
    corners_via_passes_first_period_result_experiments_data + \
    corners_second_period_result_experiments_data + \
    corners_via_passes_second_period_result_experiments_data


experiment = Experiment(experiments_data, presenters, db_name=db_name, collection_name=collection_name, train_sample_condition=train_sample_condition, test_sample_condition=test_sample_condition)
experiment.test()

representation = experiment.get_representation()
print(representation)

experiment.clear()
experiment.save_providers()
