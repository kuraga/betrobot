import datetime
from betrobot.util.common_util import populate, combine

from betrobot.betting.samplers.whole_sampler import WholeSampler

from betrobot.betting.fitters.corners_statistic_fitters import CornersStatisticFitter, CornersFirstPeriodStatisticFitter, CornersSecondPeriodStatisticFitter
from betrobot.betting.fitters.crosses_statistic_fitters import CrossesStatisticFitter, CrossesFirstPeriodStatisticFitter, CrossesSecondPeriodStatisticFitter
from betrobot.betting.fitters.saved_shots_statistic_fitters import SavedShotsStatisticFitter, SavedShotsFirstPeriodStatisticFitter, SavedShotsSecondPeriodStatisticFitter

from betrobot.betting.refitters.tournament_filter_statistic_transformer_refitter import TournamentFilterStatisticTransformerRefitter
from betrobot.betting.refitters.date_filter_statistic_transformer_refitters import MatchPastStatisticTransformerRefitter, MatchEveStatisticTransformerRefitter
from betrobot.betting.refitters.attack_defense_refitter import AttackDefenseRefitter

from betrobot.betting.predictors.corners_attack_defense_predictors import CornersResultProbabilitiesAttackDefensePredictor, CornersViaPassesResultProbabilitiesAttackDefensePredictor

from betrobot.betting.proposers.corners_proposers import CornersResults1Proposer, CornersResults1XProposer, CornersResultsX2Proposer, CornersResults2Proposer, CornersFirstPeriodResults1Proposer, CornersFirstPeriodResults1XProposer, CornersFirstPeriodResultsX2Proposer, CornersFirstPeriodResults2Proposer, CornersSecondPeriodResults1Proposer, CornersSecondPeriodResults1XProposer, CornersSecondPeriodResultsX2Proposer, CornersSecondPeriodResults2Proposer, CornersHandicapsHomeProposer, CornersHandicapsAwayProposer, CornersFirstPeriodHandicapsHomeProposer, CornersFirstPeriodHandicapsAwayProposer, CornersSecondPeriodHandicapsHomeProposer, CornersSecondPeriodHandicapsAwayProposer, CornersTotalsGreaterProposer, CornersTotalsLesserProposer, CornersFirstPeriodTotalsGreaterProposer, CornersFirstPeriodTotalsLesserProposer, CornersSecondPeriodTotalsGreaterProposer, CornersSecondPeriodTotalsLesserProposer, CornersIndividualTotalsHomeGreaterProposer, CornersIndividualTotalsHomeLesserProposer, CornersIndividualTotalsAwayGreaterProposer, CornersIndividualTotalsAwayLesserProposer, CornersFirstPeriodIndividualTotalsHomeGreaterProposer, CornersFirstPeriodIndividualTotalsHomeLesserProposer, CornersFirstPeriodIndividualTotalsAwayGreaterProposer, CornersFirstPeriodIndividualTotalsAwayLesserProposer, CornersSecondPeriodIndividualTotalsHomeGreaterProposer, CornersSecondPeriodIndividualTotalsHomeLesserProposer, CornersSecondPeriodIndividualTotalsAwayGreaterProposer, CornersSecondPeriodIndividualTotalsAwayLesserProposer

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
    (CornersHandicapsHomeProposer, (), {}),
    (CornersHandicapsAwayProposer, (), {})
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

thresholds = [ {} ]
thresholds = populate(thresholds, 'value_threshold', 1.8)
thresholds = populate(thresholds, 'predicted_threshold', 1.6, 1.8, 2.0, 2.5, 3.0)
thresholds = populate(thresholds, 'ratio_threshold', 0.75, 1.0, 1.25, 1.5)
presenter = ThresholdsVariationPresenter(thresholds, filter_and_sort_investigation_kwargs={ 'min_bets': 50 })
# presenter2 = TableInvestigationPresenter(deep=True)
# presenter = TableSummaryPresenter(value_threshold=2.5, predicted_threshold=1.8, ratio_threshold=1.5, max_value=2.2)
presenters = [ presenter ]


# corners_statistic_fitter_refitters_variants = combine(
#     [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
#     [ (MatchEveStatisticTransformerRefitter, (), {}) ],
#     [
#         (AttackDefenseRefitter, (), {}),
#         (AttackDefenseRefitter, (), { 'home_weights': [ 1/2, 1/2 ], 'away_weights': [ 1/2, 1/2 ] }),
#         (AttackDefenseRefitter, (), { 'home_weights': [ 3/4, 1/4 ], 'away_weights': [ 3/4, 1/4 ] }),
#         (AttackDefenseRefitter, (), { 'home_weights': [ 1/3, 1/3, 1/3 ], 'away_weights': [ 1/3, 1/3, 1/3 ] }),
#         (AttackDefenseRefitter, (), { 'home_weights': [ 3/6, 2/6, 1/6 ], 'away_weights': [ 3/6, 2/6, 1/6 ] }),
#         (AttackDefenseRefitter, (), { 'home_weights': [ 1/4, 1/4, 1/4, 1/4 ], 'away_weights': [ 1/4, 1/4, 1/4, 1/4 ] })
#     ]
# )
corners_statistic_fitter_refitters_variants = combine(
    [ (TournamentFilterStatisticTransformerRefitter, (), {}) ],
    [ (MatchEveStatisticTransformerRefitter, (), {}) ],
    [ (AttackDefenseRefitter, (), { 'home_weights': [ 0.6, 0.3, 0.1 ], 'away_weights': [ 0.6, 0.3, 0.1 ] }) ]
)
corners_refitters_sets_variants = combine([], corners_statistic_fitter_refitters_variants)
corners_via_passes_refitters_sets_variants = combine([], corners_statistic_fitter_refitters_variants, corners_statistic_fitter_refitters_variants)

corners_experiments_data = [ {} ]
corners_experiments_data = populate(corners_experiments_data, 'train_sampler', train_sampler)
corners_experiments_data = populate(corners_experiments_data, 'fitters', [ (CornersStatisticFitter, (), {}) ])
corners_experiments_data = populate(corners_experiments_data, 'refitters_sets', *corners_refitters_sets_variants)
corners_experiments_data = populate(corners_experiments_data, 'predictor', (CornersResultProbabilitiesAttackDefensePredictor, (), {}))
corners_experiments_data = populate(corners_experiments_data, 'proposers', corners_proposers)

corners_first_period_experiments_data = [ {} ]
corners_first_period_experiments_data = populate(corners_first_period_experiments_data, 'train_sampler', train_sampler)
corners_first_period_experiments_data = populate(corners_first_period_experiments_data, 'fitters', [ (CornersFirstPeriodStatisticFitter, (), {}) ])
corners_first_period_experiments_data = populate(corners_first_period_experiments_data, 'refitters_sets', *corners_refitters_sets_variants)
corners_first_period_experiments_data = populate(corners_first_period_experiments_data, 'predictor', (CornersResultProbabilitiesAttackDefensePredictor, (), {}))
corners_first_period_experiments_data = populate(corners_first_period_experiments_data, 'proposers', corners_first_period_proposers)

corners_second_period_experiments_data = [ {} ]
corners_second_period_experiments_data = populate(corners_second_period_experiments_data, 'train_sampler', train_sampler)
corners_second_period_experiments_data = populate(corners_second_period_experiments_data, 'fitters', [ (CornersSecondPeriodStatisticFitter, (), {}) ])
corners_second_period_experiments_data = populate(corners_second_period_experiments_data, 'refitters_sets', *corners_refitters_sets_variants)
corners_second_period_experiments_data = populate(corners_second_period_experiments_data, 'predictor', (CornersResultProbabilitiesAttackDefensePredictor, (), {}))
corners_second_period_experiments_data = populate(corners_second_period_experiments_data, 'proposers', corners_second_period_proposers)

experiments_data = corners_experiments_data  # + corners_first_period_experiments_data + corners_second_period_experiments_data


corners_via_passes_experiments_data = [ {} ]
corners_via_passes_experiments_data = populate(corners_via_passes_experiments_data, 'train_sampler', train_sampler)
corners_via_passes_experiments_data = populate(corners_via_passes_experiments_data, 'fitters', [ (CrossesStatisticFitter, (), {}), (SavedShotsStatisticFitter, (), {}) ])
corners_via_passes_experiments_data = populate(corners_via_passes_experiments_data, 'refitters_sets', *corners_via_passes_refitters_sets_variants)
corners_via_passes_experiments_data = populate(corners_via_passes_experiments_data, 'predictor', (CornersViaPassesResultProbabilitiesAttackDefensePredictor, (), {}))
corners_via_passes_experiments_data = populate(corners_via_passes_experiments_data, 'proposers', corners_proposers)


experiment = Experiment(corners_via_passes_experiments_data, presenters, db_name=db_name, collection_name=collection_name, train_sample_condition=train_sample_condition, test_sample_condition=test_sample_condition)
experiment.test()

representation = experiment.get_representation()
print(representation)

experiment.clear()
experiment.save_providers()
