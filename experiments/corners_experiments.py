import datetime
from betrobot.util.common_util import populate, combine

from betrobot.betting.samplers.whole_sampler import WholeSampler

from betrobot.betting.fitters.corners_statistic_fitters import CornersStatisticFitter, CornersFirstPeriodStatisticFitter, CornersSecondPeriodStatisticFitter

from betrobot.betting.refitters.tournament_filter_statistic_transformer_refitter import TournamentFilterStatisticTransformerRefitter
from betrobot.betting.refitters.date_filter_statistic_transformer_refitters import MatchPastStatisticTransformerRefitter, MatchEveStatisticTransformerRefitter
from betrobot.betting.refitters.attack_defense_refitter import AttackDefenseRefitter

from betrobot.betting.predictors.corners_attack_defense_predictors import CornersResultProbabilitiesAttackDefensePredictor

from betrobot.betting.proposers.corners_proposers import CornersResults1Proposer, CornersResults1XProposer, CornersResultsX2Proposer, CornersResults2Proposer, CornersFirstPeriodResults1Proposer, CornersFirstPeriodResults1XProposer, CornersFirstPeriodResultsX2Proposer, CornersFirstPeriodResults2Proposer, CornersSecondPeriodResults1Proposer, CornersSecondPeriodResults1XProposer, CornersSecondPeriodResultsX2Proposer, CornersSecondPeriodResults2Proposer, CornersHandicapsHomeProposer, CornersHandicapsAwayProposer, CornersFirstPeriodHandicapsHomeProposer, CornersFirstPeriodHandicapsAwayProposer, CornersSecondPeriodHandicapsHomeProposer, CornersSecondPeriodHandicapsAwayProposer, CornersTotalsGreaterProposer, CornersTotalsLesserProposer, CornersFirstPeriodTotalsGreaterProposer, CornersFirstPeriodTotalsLesserProposer, CornersSecondPeriodTotalsGreaterProposer, CornersSecondPeriodTotalsLesserProposer, CornersIndividualTotalsHomeGreaterProposer, CornersIndividualTotalsHomeLesserProposer, CornersIndividualTotalsAwayGreaterProposer, CornersIndividualTotalsAwayLesserProposer, CornersFirstPeriodIndividualTotalsHomeGreaterProposer, CornersFirstPeriodIndividualTotalsHomeLesserProposer, CornersFirstPeriodIndividualTotalsAwayGreaterProposer, CornersFirstPeriodIndividualTotalsAwayLesserProposer, CornersSecondPeriodIndividualTotalsHomeGreaterProposer, CornersSecondPeriodIndividualTotalsHomeLesserProposer, CornersSecondPeriodIndividualTotalsAwayGreaterProposer, CornersSecondPeriodIndividualTotalsAwayLesserProposer

from betrobot.betting.experiment import Experiment

from betrobot.betting.presenters.table_investigation_presenter import TableInvestigationPresenter
from betrobot.betting.presenters.table_summary_presenter import TableSummaryPresenter


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
    (CornersIndividualTotalsAwayLesserProposer, (), {}),
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

presenter = TableSummaryPresenter(value_threshold=1.8, predicted_threshold=1.7, ratio_threshold=1.25)
# presenter1 = TableSummaryPresenter(value_threshold=1.0, predicted_threshold=99.0, ratio_threshold=0.0)
# presenter2 = TableInvestigationPresenter(deep=True)
presenters = [ presenter ]


corners_experiments_data = [ {} ]
corners_experiments_data = populate(corners_experiments_data, 'train_sampler', [ train_sampler ])
corners_experiments_data = populate(corners_experiments_data, 'fitter', [ (CornersStatisticFitter, (), {}) ])
refitters = combine([ (TournamentFilterStatisticTransformerRefitter, (), {}) ], [ (MatchEveStatisticTransformerRefitter, (), {}) ], [ (AttackDefenseRefitter, (), {}) ])
corners_experiments_data = populate(corners_experiments_data, 'refitters', refitters)
corners_experiments_data = populate(corners_experiments_data, 'predictor', [ (CornersResultProbabilitiesAttackDefensePredictor, (), {}) ])
corners_experiments_data = populate(corners_experiments_data, 'proposers', [ corners_proposers ])

corners_first_period_experiments_data = [ {} ]
corners_first_period_experiments_data = populate(corners_first_period_experiments_data, 'train_sampler', [ train_sampler ])
corners_first_period_experiments_data = populate(corners_first_period_experiments_data, 'fitter', [ (CornersFirstPeriodStatisticFitter, (), {}) ])
refitters = combine([ (TournamentFilterStatisticTransformerRefitter, (), {}) ], [ (MatchEveStatisticTransformerRefitter, (), {}) ], [ (AttackDefenseRefitter, (), {}) ])
corners_first_period_experiments_data = populate(corners_first_period_experiments_data, 'refitters', refitters)
corners_first_period_experiments_data = populate(corners_first_period_experiments_data, 'predictor', [ (CornersResultProbabilitiesAttackDefensePredictor, (), {}) ])
corners_first_period_experiments_data = populate(corners_first_period_experiments_data, 'proposers', [ corners_first_period_proposers ])

corners_second_period_experiments_data = [ {} ]
corners_second_period_experiments_data = populate(corners_second_period_experiments_data, 'train_sampler', [ train_sampler ])
corners_second_period_experiments_data = populate(corners_second_period_experiments_data, 'fitter', [ (CornersSecondPeriodStatisticFitter, (), {}) ])
refitters = combine([ (TournamentFilterStatisticTransformerRefitter, (), {}) ], [ (MatchEveStatisticTransformerRefitter, (), {}) ], [ (AttackDefenseRefitter, (), {}) ])
corners_second_period_experiments_data = populate(corners_second_period_experiments_data, 'refitters', refitters)
corners_second_period_experiments_data = populate(corners_second_period_experiments_data, 'predictor', [ (CornersResultProbabilitiesAttackDefensePredictor, (), {}) ])
corners_second_period_experiments_data = populate(corners_second_period_experiments_data, 'proposers', [ corners_second_period_proposers ])

experiments_data = corners_experiments_data # + corners_first_period_experiments_data + corners_second_period_experiments_data


experiment = Experiment(experiments_data, presenters, db_name=db_name, collection_name=collection_name, train_sample_condition=train_sample_condition, test_sample_condition=test_sample_condition)
experiment.test()

representation = experiment.get_representation()
print(representation)

experiment.clear()
experiment.save_providers()
