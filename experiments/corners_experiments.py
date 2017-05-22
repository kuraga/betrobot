import datetime
from betrobot.util.reproduce_util import cartesian_product_of_dict_item, cartesian_product, multiple_cartesian_product_of_dict_item, make_sets_of_object_templates

from betrobot.betting.samplers.whole_sampler import WholeSampler

from betrobot.betting.fitters.corners_statistic_fitters import CornersStatisticFitter, CornersFirstPeriodStatisticFitter, CornersSecondPeriodStatisticFitter
from betrobot.betting.fitters.crosses_statistic_fitters import CrossesStatisticFitter, CrossesFirstPeriodStatisticFitter, CrossesSecondPeriodStatisticFitter
from betrobot.betting.fitters.saved_shots_statistic_fitters import SavedShotsStatisticFitter, SavedShotsFirstPeriodStatisticFitter, SavedShotsSecondPeriodStatisticFitter

from betrobot.betting.refitters.tournament_filter_statistic_transformer_refitter import TournamentFilterStatisticTransformerRefitter
from betrobot.betting.refitters.date_filter_statistic_transformer_refitters import MatchPastStatisticTransformerRefitter, MatchEveStatisticTransformerRefitter
from betrobot.betting.refitters.last_matches_statistic_transformer_refitter import LastMatchesStatisticTransformerRefitter
from betrobot.betting.refitters.attack_defense_refitter import AttackDefenseRefitter
from betrobot.betting.refitters.diffs_refitter import DiffsRefitter
from betrobot.betting.refitters.results_refitter import ResultsRefitter

from betrobot.betting.predictors.corners_attack_defense_probabilities_predictors import CornersAttackDefenseProbabilitiesPredictor, CornersViaPassesAttackDefenseProbabilitiesPredictor
from betrobot.betting.predictors.corners_result_predictors import CornersResultPredictor, CornersViaPassesResultPredictor
from betrobot.betting.predictors.corners_diffs_diff_predictors import CornersDiffsDiffPredictor, CornersViaPassesDiffsDiffPredictor

from betrobot.betting.proposers.corners_probabilities_proposers import CornersResults1ProbabilityProposer, CornersResults1XProbabilityProposer, CornersResultsX2ProbabilityProposer, CornersResults2ProbabilityProposer, CornersFirstPeriodResults1ProbabilityProposer, CornersFirstPeriodResults1XProbabilityProposer, CornersFirstPeriodResultsX2ProbabilityProposer, CornersFirstPeriodResults2ProbabilityProposer, CornersSecondPeriodResults1ProbabilityProposer, CornersSecondPeriodResults1XProbabilityProposer, CornersSecondPeriodResultsX2ProbabilityProposer, CornersSecondPeriodResults2ProbabilityProposer, CornersHandicapsHomeProbabilityProposer, CornersHandicapsAwayProbabilityProposer, CornersFirstPeriodHandicapsHomeProbabilityProposer, CornersFirstPeriodHandicapsAwayProbabilityProposer, CornersSecondPeriodHandicapsHomeProbabilityProposer, CornersSecondPeriodHandicapsAwayProbabilityProposer, CornersTotalsGreaterProbabilityProposer, CornersTotalsLesserProbabilityProposer, CornersFirstPeriodTotalsGreaterProbabilityProposer, CornersFirstPeriodTotalsLesserProbabilityProposer, CornersSecondPeriodTotalsGreaterProbabilityProposer, CornersSecondPeriodTotalsLesserProbabilityProposer, CornersIndividualTotalsHomeGreaterProbabilityProposer, CornersIndividualTotalsHomeLesserProbabilityProposer, CornersIndividualTotalsAwayGreaterProbabilityProposer, CornersIndividualTotalsAwayLesserProbabilityProposer, CornersFirstPeriodIndividualTotalsHomeGreaterProbabilityProposer, CornersFirstPeriodIndividualTotalsHomeLesserProbabilityProposer, CornersFirstPeriodIndividualTotalsAwayGreaterProbabilityProposer, CornersFirstPeriodIndividualTotalsAwayLesserProbabilityProposer, CornersSecondPeriodIndividualTotalsHomeGreaterProbabilityProposer, CornersSecondPeriodIndividualTotalsHomeLesserProbabilityProposer, CornersSecondPeriodIndividualTotalsAwayGreaterProbabilityProposer, CornersSecondPeriodIndividualTotalsAwayLesserProbabilityProposer
from betrobot.betting.proposers.corners_result_proposers import CornersResults1ResultProposer, CornersResults1XResultProposer, CornersResultsX2ResultProposer, CornersResults2ResultProposer, CornersHandicapsHomeResultProposer, CornersHandicapsAwayResultProposer
from betrobot.betting.proposers.corners_diffs_diff_proposers import CornersResults1DiffsDiffProposer, CornersResults1XDiffsDiffProposer, CornersResultsX2DiffsDiffProposer, CornersResults2DiffsDiffProposer, CornersHandicapsHomeDiffsDiffProposer, CornersHandicapsAwayDiffsDiffProposer

from betrobot.betting.experiment import Experiment

from betrobot.betting.presenters.table_investigation_presenter import TableInvestigationPresenter
from betrobot.betting.presenters.table_summary_presenter import TableSummaryPresenter
from betrobot.betting.presenters.thresholds_variation_presenter import ThresholdsVariationPresenter


db_name = 'betrobot'
collection_name = 'matchesCleaned'
train_sample_condition = { }
test_sample_condition = {
   'date': { '$gte': datetime.datetime(2017, 5, 1) }
}


train_sampler = WholeSampler(db_name, collection_name)

corners_probabilities_proposers = make_sets_of_object_templates(
    (), {}, [
        CornersResults1ProbabilityProposer,
        CornersResults1XProbabilityProposer,
        CornersResultsX2ProbabilityProposer,
        CornersResults2ProbabilityProposer,
        CornersHandicapsHomeProbabilityProposer,
        CornersHandicapsAwayProbabilityProposer,
        CornersTotalsGreaterProbabilityProposer,
        CornersTotalsLesserProbabilityProposer,
        CornersIndividualTotalsHomeGreaterProbabilityProposer,
        CornersIndividualTotalsHomeLesserProbabilityProposer,
        CornersIndividualTotalsAwayGreaterProbabilityProposer,
        CornersIndividualTotalsAwayLesserProbabilityProposer
    ]
)
corners_first_period_probabilities_proposers = make_sets_of_object_templates(
    (), {}, [
        CornersFirstPeriodResults1ProbabilityProposer,
        CornersFirstPeriodResults1XProbabilityProposer,
        CornersFirstPeriodResultsX2ProbabilityProposer,
        CornersFirstPeriodResults2ProbabilityProposer,
        CornersFirstPeriodHandicapsHomeProbabilityProposer,
        CornersFirstPeriodHandicapsAwayProbabilityProposer,
        CornersFirstPeriodTotalsGreaterProbabilityProposer,
        CornersFirstPeriodTotalsLesserProbabilityProposer,
        CornersFirstPeriodIndividualTotalsHomeGreaterProbabilityProposer,
        CornersFirstPeriodIndividualTotalsHomeLesserProbabilityProposer,
        CornersFirstPeriodIndividualTotalsAwayGreaterProbabilityProposer,
        CornersFirstPeriodIndividualTotalsAwayLesserProbabilityProposer
    ]
)
corners_second_period_probabilities_proposers = make_sets_of_object_templates(
    (), {}, [
        CornersSecondPeriodResults1ProbabilityProposer,
        CornersSecondPeriodResults1XProbabilityProposer,
        CornersSecondPeriodResultsX2ProbabilityProposer,
        CornersSecondPeriodResults2ProbabilityProposer,
        CornersSecondPeriodHandicapsHomeProbabilityProposer,
        CornersSecondPeriodHandicapsAwayProbabilityProposer,
        CornersSecondPeriodTotalsGreaterProbabilityProposer,
        CornersSecondPeriodTotalsLesserProbabilityProposer,
        CornersSecondPeriodIndividualTotalsHomeGreaterProbabilityProposer,
        CornersSecondPeriodIndividualTotalsHomeLesserProbabilityProposer,
        CornersSecondPeriodIndividualTotalsAwayGreaterProbabilityProposer,
        CornersSecondPeriodIndividualTotalsAwayLesserProbabilityProposer
    ]
)

corners_result_proposers = make_sets_of_object_templates(
    (), {}, [
        CornersResults1ResultProposer,
        CornersResults1XResultProposer,
        CornersResultsX2ResultProposer,
        CornersResults2ResultProposer,
        CornersHandicapsHomeResultProposer,
        CornersHandicapsAwayResultProposer
    ]
)

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


# thresholds_sets = multiple_cartesian_product_of_dict_item([ {} ], {
#     'value_threshold': [ 1.8 ]
#     'predicted_threshold': [ 1.6, 1.8, 2.0, 2.5, 3.0 ],
#     'ratio_threshold': [ 0.75, 1.0, 1.25, 1.5 ]
# presenter = ThresholdsVariationPresenter(thresholds_sets, filter_and_sort_investigation_kwargs={ 'min_bets': 50 })
# presenter2 = TableInvestigationPresenter(deep=True)
presenter = TableSummaryPresenter(value_threshold=1.8, predicted_threshold=2.0, ratio_threshold=1.25)
presenters = [ presenter ]


# corners_attack_defense_refitters_sets_variants = cartesian_product(
#     [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
#     [
#         (MatchEveStatisticTransformerRefitter, (), { 'days': 30 }),
#         (MatchEveStatisticTransformerRefitter, (), { 'days': 60 }),
#         (MatchEveStatisticTransformerRefitter, (), { 'days': 90 }),
#         (MatchEveStatisticTransformerRefitter, (), { 'days': 180 }),
#         (LastMatchesStatisticTransformerRefitter, (), { 'n': 1 }),
#         (LastMatchesStatisticTransformerRefitter, (), { 'n': 2 }),
#         (LastMatchesStatisticTransformerRefitter, (), { 'n': 3 }),
#         (LastMatchesStatisticTransformerRefitter, (), { 'n': 4 }),
#     ],
#     [
#         (AttackDefenseRefitter, (), {}),
#         (AttackDefenseRefitter, (), { 'home_weights': [ 1/2, 1/2 ], 'away_weights': [ 1/2, 1/2 ] }),
#         (AttackDefenseRefitter, (), { 'home_weights': [ 3/4, 1/4 ], 'away_weights': [ 3/4, 1/4 ] }),
#         (AttackDefenseRefitter, (), { 'home_weights': [ 1/3, 1/3, 1/3 ], 'away_weights': [ 1/3, 1/3, 1/3 ] }),
#         (AttackDefenseRefitter, (), { 'home_weights': [ 3/6, 2/6, 1/6 ], 'away_weights': [ 3/6, 2/6, 1/6 ] }),
#         (AttackDefenseRefitter, (), { 'home_weights': [ 1/4, 1/4, 1/4, 1/4 ], 'away_weights': [ 1/4, 1/4, 1/4, 1/4 ] }),
#         (AttackDefenseRefitter, (), { 'home_weights': [ 0.6, 0.3, 0.1 ], 'away_weights': [ 0.6, 0.3, 0.1 ] })
#     ]
# )
corners_attack_defense_refitters_sets_variants = cartesian_product(
    [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
    [ (MatchEveStatisticTransformerRefitter, (), {}) ],
    [ (AttackDefenseRefitter, (), {}) ]
)
corners_attack_defense_refitters_sets = cartesian_product(corners_attack_defense_refitters_sets_variants)
corners_via_passes_attack_defense_refitters_sets = cartesian_product(corners_attack_defense_refitters_sets_variants, corners_attack_defense_refitters_sets_variants)

corners_result_refitters_sets_variants = cartesian_product(
    [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
    [ (LastMatchesStatisticTransformerRefitter, (), { 'n': 1 }) ],
    [ (ResultsRefitter, (), {}) ]
)
corners_result_refitters_sets = cartesian_product(corners_result_refitters_sets_variants)
corners_via_passes_result_refitters_sets = cartesian_product(corners_result_refitters_sets_variants, corners_result_refitters_sets_variants)

corners_diffs_diff_refitters_sets_variants = cartesian_product(
    [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
    [ (LastMatchesStatisticTransformerRefitter, (), { 'n': 1 }) ],
    [ (DiffsRefitter, (), {}) ]
)
corners_diffs_diff_refitters_sets = cartesian_product(corners_diffs_diff_refitters_sets_variants)
corners_via_passes_diffs_diff_refitters_sets = cartesian_product(corners_diffs_diff_refitters_sets_variants, corners_diffs_diff_refitters_sets_variants)


corners_attack_defense_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CornersStatisticFitter, (), {}) ] ],
    'refitters_sets': corners_attack_defense_refitters_sets,
    'predictor': [ (CornersAttackDefenseProbabilitiesPredictor, (), {}) ],
    'proposers': [ corners_probabilities_proposers ]
})

corners_first_period_attack_defense_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CornersFirstPeriodStatisticFitter, (), {}) ] ],
    'refitters_sets': corners_attack_defense_refitters_sets,
    'predictor': [ (CornersAttackDefenseProbabilitiesPredictor, (), {}) ],
    'proposers': [ corners_first_period_probabilities_proposers ]
})

corners_second_period_attack_defense_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CornersSecondPeriodStatisticFitter, (), {}) ] ],
    'refitters_sets': corners_attack_defense_refitters_sets,
    'predictor': [ (CornersAttackDefenseProbabilitiesPredictor, (), {}) ],
    'proposers': [ corners_second_period_probabilities_proposers ]
})

corners_via_passes_attack_defense_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CrossesStatisticFitter, (), {}), (SavedShotsStatisticFitter, (), {}) ] ],
    'refitters_sets': corners_via_passes_attack_defense_refitters_sets,
    'predictor': [ (CornersViaPassesAttackDefenseProbabilitiesPredictor, (), {}) ],
    'proposers': [ corners_probabilities_proposers ]
})

corners_results_results_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CornersStatisticFitter, (), {}) ] ],
    'refitters_sets': corners_result_refitters_sets,
    'predictor': [ (CornersResultPredictor, (), {}) ],
    'proposers': [ corners_result_proposers ]
})

corners_via_passes_results_results_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CrossesStatisticFitter, (), {}), (SavedShotsStatisticFitter, (), {}) ] ],
    'refitters_sets': corners_via_passes_result_refitters_sets,
    'predictor': [ (CornersViaPassesResultPredictor, (), {}) ],
    'proposers': [ corners_result_proposers ]
})

corners_diffs_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CornersStatisticFitter, (), {}) ] ],
    'refitters_sets': corners_diffs_diff_refitters_sets,
    'predictor': [ (CornersDiffsDiffPredictor, (), {}) ],
    'proposers': [ corners_diffs_diff_proposers ]
})

corners_via_passes_diffs_experiments_data = multiple_cartesian_product_of_dict_item([ {} ], {
    'train_sampler': [ train_sampler ],
    'fitters': [ [ (CrossesStatisticFitter, (), {}), (SavedShotsStatisticFitter, (), {}) ] ],
    'refitters_sets': corners_via_passes_diffs_diff_refitters_sets,
    'predictor': [ (CornersViaPassesDiffsDiffPredictor, (), {}) ],
    'proposers': [ corners_diffs_diff_proposers ]
})


# experiments_data = corners_attack_defense_experiments_data + corners_first_period_attack_defense_experiments_data + corners_second_period_attack_defense_experiments_data + corners_via_passes_attack_defense_experiments_data + corners_results_results_experiments_data + corners_via_passes_results_results_experiments_data + corners_diffs_experiments_data + corners_via_passes_diffs_experiments_data
experiments_data = corners_via_passes_diffs_experiments_data
experiment = Experiment(experiments_data, presenters, db_name=db_name, collection_name=collection_name, train_sample_condition=train_sample_condition, test_sample_condition=test_sample_condition)
experiment.test()

representation = experiment.get_representation()
print(representation)

experiment.clear()
experiment.save_providers()
