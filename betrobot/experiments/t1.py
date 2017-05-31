import datetime
from betrobot.util.reproduce_util import cartesian_product_of_dict_item, cartesian_product, multiple_cartesian_product_of_dict_item, make_sets_of_object_templates

from betrobot.betting.samplers.whole_sampler import WholeSampler

from betrobot.betting.fitters.corners_statistic_fitters import CornersStatisticFitter, CornersFirstPeriodStatisticFitter, CornersSecondPeriodStatisticFitter

from betrobot.betting.refitters.invalid_matches_filter_refitter_statistic_transformer_refitter import IvalidMatchesFilterStatisticTransformerRefitter
from betrobot.betting.refitters.tournament_filter_statistic_transformer_refitter import TournamentFilterStatisticTransformerRefitter
from betrobot.betting.refitters.date_filter_statistic_transformer_refitters import MatchEveStatisticTransformerRefitter
from betrobot.betting.refitters.diffs_refitter import DiffsRefitter

from betrobot.betting.predictors.corners_diffs_diff_predictors import CornersDiffsDiffPredictor
from betrobot.betting.predictors.corners_diffs_diff2_predictors import CornersDiffsDiff2Predictor

from betrobot.betting.proposers.corners_diffs_diff_proposers import CornersResults1DiffsDiffProposer, CornersResults1XDiffsDiffProposer, CornersResultsX2DiffsDiffProposer, CornersResults2DiffsDiffProposer, CornersFirstPeriodResults1DiffsDiffProposer, CornersFirstPeriodResults1XDiffsDiffProposer, CornersFirstPeriodResultsX2DiffsDiffProposer, CornersFirstPeriodResults2DiffsDiffProposer, CornersSecondPeriodResults1DiffsDiffProposer, CornersSecondPeriodResults1XDiffsDiffProposer, CornersSecondPeriodResultsX2DiffsDiffProposer, CornersSecondPeriodResults2DiffsDiffProposer, CornersHandicapsHomeDiffsDiffProposer, CornersHandicapsAwayDiffsDiffProposer, CornersFirstPeriodHandicapsHomeDiffsDiffProposer, CornersFirstPeriodHandicapsAwayDiffsDiffProposer, CornersSecondPeriodHandicapsHomeDiffsDiffProposer, CornersSecondPeriodHandicapsAwayDiffsDiffProposer
from betrobot.betting.proposers.corners_diffs_diff_proposers import CornersResults1DiffsDiffProposer, CornersResults1XDiffsDiffProposer, CornersResultsX2DiffsDiffProposer, CornersResults2DiffsDiffProposer, CornersFirstPeriodResults1DiffsDiffProposer, CornersFirstPeriodResults1XDiffsDiffProposer, CornersFirstPeriodResultsX2DiffsDiffProposer, CornersFirstPeriodResults2DiffsDiffProposer, CornersSecondPeriodResults1DiffsDiffProposer, CornersSecondPeriodResults1XDiffsDiffProposer, CornersSecondPeriodResultsX2DiffsDiffProposer, CornersSecondPeriodResults2DiffsDiffProposer, CornersHandicapsHomeDiffsDiffProposer, CornersHandicapsAwayDiffsDiffProposer, CornersFirstPeriodHandicapsHomeDiffsDiffProposer, CornersFirstPeriodHandicapsAwayDiffsDiffProposer, CornersSecondPeriodHandicapsHomeDiffsDiffProposer, CornersSecondPeriodHandicapsAwayDiffsDiffProposer

from betrobot.betting.experiment import Experiment

from betrobot.betting.presenters.table_summary_presenter import TableSummaryPresenter


db_name = 'betrobot'
collection_name = 'matchesCleaned'
train_sample_condition = { }
test_sample_condition = {
   'date': { '$gte': datetime.datetime(2017, 1, 1) }
}


train_sampler = WholeSampler(db_name, collection_name)


corners_diffs_diff_refitters_sets_variants = cartesian_product(
    [ (IvalidMatchesFilterStatisticTransformerRefitter, (), {}) ],
    [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
    [ (MatchEveStatisticTransformerRefitter, (), {}) ],
    [ (DiffsRefitter, (), {}) ]
)
corners_diffs_diff_refitters_sets = cartesian_product([], corners_diffs_diff_refitters_sets_variants)

corners_diffs_diff2_refitters_sets_variants = cartesian_product(
    [ (IvalidMatchesFilterStatisticTransformerRefitter, (), {}) ],
    [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
    [ (MatchEveStatisticTransformerRefitter, (), {}) ]
)
corners_diffs_diff2_refitters_sets = cartesian_product([], corners_diffs_diff2_refitters_sets_variants)


corners_diffs_diff_proposers = make_sets_of_object_templates(
    (), {}, [
        CornersResults1DiffsDiffProposer,
        CornersResults1XDiffsDiffProposer,
        CornersResultsX2DiffsDiffProposer,
        CornersResults2DiffsDiffProposer,
        CornersHandicapsHomeDiffsDiffProposer,
        CornersHandicapsAwayDiffsDiffProposer
    ]
)


corners_diffs_diff_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CornersStatisticFitter, (), {}) ] ] * len(corners_diffs_diff_refitters_sets),
    'refitters_sets': corners_diffs_diff_refitters_sets,
    'predictor': [ (CornersDiffsDiffPredictor, (), {}) ],
    'proposers': [ corners_diffs_diff_proposers ]
})


corners_diffs_diff2_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CornersStatisticFitter, (), {}) ] ] * len(corners_diffs_diff2_refitters_sets),
    'refitters_sets': corners_diffs_diff2_refitters_sets,
    'predictor': [ (CornersDiffsDiff2Predictor, (), {}) ],
    'proposers': [ corners_diffs_diff_proposers ]
})


presenter = TableSummaryPresenter(value_threshold=1.8, predicted_threshold=2.0, ratio_threshold=1.25)
presenters = [ presenter ]


experiments_data = \
    corners_diffs_diff_experiments_data + \
    corners_diffs_diff2_experiments_data


experiment = Experiment(experiments_data, presenters, db_name=db_name, collection_name=collection_name, train_sample_condition=train_sample_condition, test_sample_condition=test_sample_condition)
experiment.test()

representation = experiment.get_representation()
print(representation)

experiment.clear()
experiment.save_providers()
