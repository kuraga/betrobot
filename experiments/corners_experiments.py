import datetime
from betrobot.util.common_util import populate, combine

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

from betrobot.betting.predictors.corners_attack_defense_predictors import CornersResultProbabilitiesAttackDefensePredictor, CornersViaPassesResultProbabilitiesAttackDefensePredictor
from betrobot.betting.predictors.corners_results_result_predictors import CornersResultsResultPredictor, CornersViaPassesResultsResultPredictor
from betrobot.betting.predictors.corners_diffs_diff_predictors import CornersDiffsDiffPredictor, CornersViaPassesDiffsDiffPredictor

from betrobot.betting.proposers.corners_probability_proposers import CornersResults1Proposer, CornersResults1XProposer, CornersResultsX2Proposer, CornersResults2Proposer, CornersFirstPeriodResults1Proposer, CornersFirstPeriodResults1XProposer, CornersFirstPeriodResultsX2Proposer, CornersFirstPeriodResults2Proposer, CornersSecondPeriodResults1Proposer, CornersSecondPeriodResults1XProposer, CornersSecondPeriodResultsX2Proposer, CornersSecondPeriodResults2Proposer, CornersHandicapsHomeProposer, CornersHandicapsAwayProposer, CornersFirstPeriodHandicapsHomeProposer, CornersFirstPeriodHandicapsAwayProposer, CornersSecondPeriodHandicapsHomeProposer, CornersSecondPeriodHandicapsAwayProposer, CornersTotalsGreaterProposer, CornersTotalsLesserProposer, CornersFirstPeriodTotalsGreaterProposer, CornersFirstPeriodTotalsLesserProposer, CornersSecondPeriodTotalsGreaterProposer, CornersSecondPeriodTotalsLesserProposer, CornersIndividualTotalsHomeGreaterProposer, CornersIndividualTotalsHomeLesserProposer, CornersIndividualTotalsAwayGreaterProposer, CornersIndividualTotalsAwayLesserProposer, CornersFirstPeriodIndividualTotalsHomeGreaterProposer, CornersFirstPeriodIndividualTotalsHomeLesserProposer, CornersFirstPeriodIndividualTotalsAwayGreaterProposer, CornersFirstPeriodIndividualTotalsAwayLesserProposer, CornersSecondPeriodIndividualTotalsHomeGreaterProposer, CornersSecondPeriodIndividualTotalsHomeLesserProposer, CornersSecondPeriodIndividualTotalsAwayGreaterProposer, CornersSecondPeriodIndividualTotalsAwayLesserProposer
from betrobot.betting.proposers.corners_results_result_proposers import CornersResults1ResultsResultProposer, CornersResults1XResultsResultProposer, CornersResultsX2ResultsResultProposer, CornersResults2ResultsResultProposer, CornersHandicapsHomeResultsResultProposer, CornersHandicapsAwayResultsResultProposer
from betrobot.betting.proposers.corners_diffs_diff_proposers import CornersResults1DiffsDiffProposer, CornersResults1XDiffsDiffProposer, CornersResultsX2DiffsDiffProposer, CornersResults2DiffsDiffProposer, CornersHandicapsHomeDiffsDiffProposer, CornersHandicapsAwayDiffsDiffProposer

from betrobot.betting.experiment import Experiment

from betrobot.betting.presenters.table_investigation_presenter import TableInvestigationPresenter
from betrobot.betting.presenters.table_summary_presenter import TableSummaryPresenter
from betrobot.betting.presenters.thresholds_variation_presenter import ThresholdsVariationPresenter


db_name = 'betrobot'
collection_name = 'matchesCleaned'
train_sample_condition = { }
test_sample_condition = {
   'date': { '$gte': datetime.datetime(2017, 1, 1) }
}


train_sampler = WholeSampler(db_name, collection_name)

corners_proposers = [
    (CornersResults1Proposer, (), {}),
    (CornersResults1XProposer, (), {}),
    (CornersResultsX2Proposer, (), {}),
    (CornersResults2Proposer, (), {}),
    (CornersHandicapsHomeProposer, (), {}),
    (CornersHandicapsAwayProposer, (), {}),
    (CornersTotalsGreaterProposer, (), {}),
    (CornersTotalsLesserProposer, (), {}),
    (CornersIndividualTotalsHomeGreaterProposer, (), {}),
    (CornersIndividualTotalsHomeLesserProposer, (), {}),
    (CornersIndividualTotalsAwayGreaterProposer, (), {}),
    (CornersIndividualTotalsAwayLesserProposer, (), {})
]
corners_first_period_proposers = [
    (CornersFirstPeriodResults1Proposer, (), {}),
    (CornersFirstPeriodResults1XProposer, (), {}),
    (CornersFirstPeriodResultsX2Proposer, (), {}),
    (CornersFirstPeriodResults2Proposer, (), {}),
    (CornersFirstPeriodHandicapsHomeProposer, (), {}),
    (CornersFirstPeriodHandicapsAwayProposer, (), {}),
    (CornersFirstPeriodTotalsGreaterProposer, (), {}),
    (CornersFirstPeriodTotalsLesserProposer, (), {}),
    (CornersFirstPeriodIndividualTotalsHomeGreaterProposer, (), {}),
    (CornersFirstPeriodIndividualTotalsHomeLesserProposer, (), {}),
    (CornersFirstPeriodIndividualTotalsAwayGreaterProposer, (), {}),
    (CornersFirstPeriodIndividualTotalsAwayLesserProposer, (), {})
]
corners_second_period_proposers = [
    (CornersSecondPeriodResults1Proposer, (), {}),
    (CornersSecondPeriodResults1XProposer, (), {}),
    (CornersSecondPeriodResultsX2Proposer, (), {}),
    (CornersSecondPeriodResults2Proposer, (), {}),
    (CornersSecondPeriodHandicapsHomeProposer, (), {}),
    (CornersSecondPeriodHandicapsAwayProposer, (), {}),
    (CornersSecondPeriodTotalsGreaterProposer, (), {}),
    (CornersSecondPeriodTotalsLesserProposer, (), {}),
    (CornersSecondPeriodIndividualTotalsHomeGreaterProposer, (), {}),
    (CornersSecondPeriodIndividualTotalsHomeLesserProposer, (), {}),
    (CornersSecondPeriodIndividualTotalsAwayGreaterProposer, (), {}),
    (CornersSecondPeriodIndividualTotalsAwayLesserProposer, (), {})
]

corners_results_results_proposers = [
    (CornersResults1ResultsResultProposer, (), {}),
    (CornersResults1XResultsResultProposer, (), {}),
    (CornersResultsX2ResultsResultProposer, (), {}),
    (CornersResults2ResultsResultProposer, (), {}),
    (CornersHandicapsHomeResultsResultProposer, (), {}),
    (CornersHandicapsAwayResultsResultProposer, (), {})
]

corners_diffs_proposers = [
    (CornersResults1DiffsDiffProposer, (), {}),
    (CornersResults1XDiffsDiffProposer, (), {}),
    (CornersResultsX2DiffsDiffProposer, (), {}),
    (CornersResults2DiffsDiffProposer, (), {}),
    (CornersHandicapsHomeDiffsDiffProposer, (), {}),
    (CornersHandicapsAwayDiffsDiffProposer, (), {})
]


# thresholds = [ {} ]
# thresholds = populate(thresholds, 'value_threshold', 1.8)
# thresholds = populate(thresholds, 'predicted_threshold', 1.6, 1.8, 2.0, 2.5, 3.0)
# thresholds = populate(thresholds, 'ratio_threshold', 0.75, 1.0, 1.25, 1.5)
# presenter = ThresholdsVariationPresenter(thresholds, filter_and_sort_investigation_kwargs={ 'min_bets': 50 })
# presenter2 = TableInvestigationPresenter(deep=True)
presenter = TableSummaryPresenter(value_threshold=1.8, predicted_threshold=2.0, ratio_threshold=1.25)
presenters = [ presenter ]


# corners_attack_defense_statistic_fitter_refitters_variants = combine(
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
corners_attack_defense_statistic_fitter_refitters_variants = combine(
    [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
    [ (MatchEveStatisticTransformerRefitter, (), {}) ],
    [ (AttackDefenseRefitter, (), {}) ]
)
corners_attack_defense_refitters_sets_variants = combine([], corners_attack_defense_statistic_fitter_refitters_variants)
corners_via_passes_attack_defense_refitters_sets_variants = combine([], corners_attack_defense_statistic_fitter_refitters_variants, corners_attack_defense_statistic_fitter_refitters_variants)

corners_results_results_statistic_fitter_refitters_variants = combine(
    [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
    [ (LastMatchesStatisticTransformerRefitter, (), { 'n': 1 }) ],
    [ (ResultsRefitter, (), {}) ]
)
corners_results_results_refitters_sets_variants = combine([], corners_results_results_statistic_fitter_refitters_variants)
corners_via_passes_results_results_refitters_sets_variants = combine([], corners_results_results_statistic_fitter_refitters_variants, corners_results_results_statistic_fitter_refitters_variants)

corners_diffs_statistic_fitter_refitters_variants = combine(
    [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
    [ (LastMatchesStatisticTransformerRefitter, (), { 'n': 1 }) ],
    [ (DiffsRefitter, (), {}) ]
)
corners_diffs_refitters_sets_variants = combine([], corners_diffs_statistic_fitter_refitters_variants)
corners_via_passes_diffs_refitters_sets_variants = combine([], corners_diffs_statistic_fitter_refitters_variants, corners_diffs_statistic_fitter_refitters_variants)


corners_attack_defense_experiments_data = [ {} ]
corners_attack_defense_experiments_data = populate(corners_attack_defense_experiments_data, 'train_sampler', train_sampler)
corners_attack_defense_experiments_data = populate(corners_attack_defense_experiments_data, 'fitters', [ (CornersStatisticFitter, (), {}) ])
corners_attack_defense_experiments_data = populate(corners_attack_defense_experiments_data, 'refitters_sets', *corners_attack_defense_refitters_sets_variants)
corners_attack_defense_experiments_data = populate(corners_attack_defense_experiments_data, 'predictor', (CornersResultProbabilitiesAttackDefensePredictor, (), {}))
corners_attack_defense_experiments_data = populate(corners_attack_defense_experiments_data, 'proposers', corners_proposers)

corners_first_period_attack_defense_experiments_data = [ {} ]
corners_first_period_attack_defense_experiments_data = populate(corners_first_period_attack_defense_experiments_data, 'train_sampler', train_sampler)
corners_first_period_attack_defense_experiments_data = populate(corners_first_period_attack_defense_experiments_data, 'fitters', [ (CornersFirstPeriodStatisticFitter, (), {}) ])
corners_first_period_attack_defense_experiments_data = populate(corners_first_period_attack_defense_experiments_data, 'refitters_sets', *corners_attack_defense_refitters_sets_variants)
corners_first_period_attack_defense_experiments_data = populate(corners_first_period_attack_defense_experiments_data, 'predictor', (CornersResultProbabilitiesAttackDefensePredictor, (), {}))
corners_first_period_attack_defense_experiments_data = populate(corners_first_period_attack_defense_experiments_data, 'proposers', corners_first_period_proposers)

corners_second_period_attack_defense_experiments_data = [ {} ]
corners_second_period_attack_defense_experiments_data = populate(corners_second_period_attack_defense_experiments_data, 'train_sampler', train_sampler)
corners_second_period_attack_defense_experiments_data = populate(corners_second_period_attack_defense_experiments_data, 'fitters', [ (CornersSecondPeriodStatisticFitter, (), {}) ])
corners_second_period_attack_defense_experiments_data = populate(corners_second_period_attack_defense_experiments_data, 'refitters_sets', *corners_attack_defense_refitters_sets_variants)
corners_second_period_attack_defense_experiments_data = populate(corners_second_period_attack_defense_experiments_data, 'predictor', (CornersResultProbabilitiesAttackDefensePredictor, (), {}))
corners_second_period_attack_defense_experiments_data = populate(corners_second_period_attack_defense_experiments_data, 'proposers', corners_second_period_proposers)

corners_via_passes_attack_defense_experiments_data = [ {} ]
corners_via_passes_attack_defense_experiments_data = populate(corners_via_passes_attack_defense_experiments_data, 'train_sampler', train_sampler)
corners_via_passes_attack_defense_experiments_data = populate(corners_via_passes_attack_defense_experiments_data, 'fitters', [ (CrossesStatisticFitter, (), {}), (SavedShotsStatisticFitter, (), {}) ])
corners_via_passes_attack_defense_experiments_data = populate(corners_via_passes_attack_defense_experiments_data, 'refitters_sets', *corners_via_passes_attack_defense_refitters_sets_variants)
corners_via_passes_attack_defense_experiments_data = populate(corners_via_passes_attack_defense_experiments_data, 'predictor', (CornersViaPassesResultProbabilitiesAttackDefensePredictor, (), {}))
corners_via_passes_attack_defense_experiments_data = populate(corners_via_passes_attack_defense_experiments_data, 'proposers', corners_proposers)

corners_results_results_experiments_data = [ {} ]
corners_results_results_experiments_data = populate(corners_results_results_experiments_data, 'train_sampler', train_sampler)
corners_results_results_experiments_data = populate(corners_results_results_experiments_data, 'fitters', [ (CornersStatisticFitter, (), {}) ])
corners_results_results_experiments_data = populate(corners_results_results_experiments_data, 'refitters_sets', *corners_results_results_refitters_sets_variants)
corners_results_results_experiments_data = populate(corners_results_results_experiments_data, 'predictor', (CornersResultsResultPredictor, (), {}))
corners_results_results_experiments_data = populate(corners_results_results_experiments_data, 'proposers', corners_results_results_proposers)

corners_via_passes_results_results_experiments_data = [ {} ]
corners_via_passes_results_results_experiments_data = populate(corners_via_passes_results_results_experiments_data, 'train_sampler', train_sampler)
corners_via_passes_results_results_experiments_data = populate(corners_via_passes_results_results_experiments_data, 'fitters', [ (CrossesStatisticFitter, (), {}), (SavedShotsStatisticFitter, (), {}) ])
corners_via_passes_results_results_experiments_data = populate(corners_via_passes_results_results_experiments_data, 'refitters_sets', *corners_via_passes_results_results_refitters_sets_variants)
corners_via_passes_results_results_experiments_data = populate(corners_via_passes_results_results_experiments_data, 'predictor', (CornersViaPassesResultsResultPredictor, (), {}))
corners_via_passes_results_results_experiments_data = populate(corners_via_passes_results_results_experiments_data, 'proposers', corners_results_results_proposers)

corners_diffs_experiments_data = [ {} ]
corners_diffs_experiments_data = populate(corners_diffs_experiments_data, 'train_sampler', train_sampler)
corners_diffs_experiments_data = populate(corners_diffs_experiments_data, 'fitters', [ (CornersStatisticFitter, (), {}) ])
corners_diffs_experiments_data = populate(corners_diffs_experiments_data, 'refitters_sets', *corners_diffs_refitters_sets_variants)
corners_diffs_experiments_data = populate(corners_diffs_experiments_data, 'predictor', (CornersDiffsDiffPredictor, (), {}))
corners_diffs_experiments_data = populate(corners_diffs_experiments_data, 'proposers', corners_diffs_proposers)

corners_via_passes_diffs_experiments_data = [ {} ]
corners_via_passes_diffs_experiments_data = populate(corners_via_passes_diffs_experiments_data, 'train_sampler', train_sampler)
corners_via_passes_diffs_experiments_data = populate(corners_via_passes_diffs_experiments_data, 'fitters', [ (CrossesStatisticFitter, (), {}), (SavedShotsStatisticFitter, (), {}) ])
corners_via_passes_diffs_experiments_data = populate(corners_via_passes_diffs_experiments_data, 'refitters_sets', *corners_diffs_refitters_sets_variants)
corners_via_passes_diffs_experiments_data = populate(corners_via_passes_diffs_experiments_data, 'predictor', (CornersViaPassesDiffsDiffPredictor, (), {}))
corners_via_passes_diffs_experiments_data = populate(corners_via_passes_diffs_experiments_data, 'proposers', corners_diffs_proposers)


# experiments_data = corners_attack_defense_experiments_data + corners_first_period_attack_defense_experiments_data + corners_second_period_attack_defense_experiments_data + corners_via_passes_attack_defense_experiments_data + corners_results_results_experiments_data + corners_via_passes_results_results_experiments_data + corners_diffs_experiments_data + corners_via_passes_diffs_experiments_data
experiments_data = corners_via_passes_results_results_experiments_data
experiment = Experiment(experiments_data, presenters, db_name=db_name, collection_name=collection_name, train_sample_condition=train_sample_condition, test_sample_condition=test_sample_condition)
experiment.test()

representation = experiment.get_representation()
print(representation)

experiment.clear()
experiment.save_providers()
