import pymongo
import os
import pickle
from betting.provider import Provider
from betting.experimentor import Experimentor
from util.common_util import safe_get

from betting.samplers.date_based_samplers import HistoricalSampler, EveSampler
from betting.fitters.corners_attack_defense_fitters import CornersAttackDefenseFitter, CornersFirstPeriodAttackDefenseFitter, CornersSecondPeriodAttackDefenseFitter
from betting.predictors.corners_attack_defense_predictors import CornersResultProbabilitiesAttackDefensePredictor
from betting.proposers.corners_results_proposers import CornersResults1Proposer, CornersResults1XProposer, CornersResultsX2Proposer, CornersResults2Proposer
from betting.proposers.corners_totals_proposers import CornersTotalsGreaterProposer, CornersTotalsLesserProposer
from betting.proposers.corners_period_results_proposers import CornersFirstPeriodResults1Proposer, CornersFirstPeriodResults1XProposer, CornersFirstPeriodResultsX2Proposer, CornersFirstPeriodResults2Proposer, CornersSecondPeriodResults1Proposer, CornersSecondPeriodResults1XProposer, CornersSecondPeriodResultsX2Proposer, CornersSecondPeriodResults2Proposer


def make_experiment(provider, db_name, matches_collection_name, sample_condition, fitter_fitted_data=None):
    experimentor = Experimentor(provider, db_name, matches_collection_name, sample_condition)

    print('Training...')
    experimentor.train(fitter_fitted_data)
    print()

    print('Testing...')
    experimentor.test()
    print()

    print('Results')
    print(experimentor.get_investigation())
    print()

    print('Saving...')
    file_name = '%s.pkl' % (provider.name,)
    file_path = os.path.join('data', 'providers', file_name)
    with open(file_path, 'wb') as f:
        pickle.dump(provider, f)

    return experimentor


db_name = 'betrobot'
matches_collection_name = 'matchesCleaned'
sample_condition = { 'date': { '$regex': '^2017' } }
threshold = 1.7


train_samplers = {
    # 'historical': HistoricalSampler(db_name, matches_collection_name),
    'eve': EveSampler(db_name, matches_collection_name)
}

corners_attack_defense_fitter = CornersAttackDefenseFitter()
corners_first_period_attack_defense_fitter = CornersFirstPeriodAttackDefenseFitter()
corners_second_period_attack_defense_fitter = CornersSecondPeriodAttackDefenseFitter()

corners_result_probabilities_attack_defense_predictor = CornersResultProbabilitiesAttackDefensePredictor()

corners_results_proposers_data = [{
    'name': 'corners_results-1',
    'proposer': CornersResults1Proposer(threshold=threshold)
}, {
    'name': 'corners_results-1X',
    'proposer': CornersResults1XProposer(threshold=threshold)
}, {
    'name': 'corners_results-X2',
    'proposer': CornersResultsX2Proposer(threshold=threshold)
}, {
    'name': 'corners_results-2',
    'proposer': CornersResults2Proposer(threshold=threshold)
}]
corners_first_period_results_proposers_data = [{
    'name': 'corners_period_results-first_period-1',
    'proposer': CornersFirstPeriodResults1Proposer(threshold=threshold)
}, {
    'name': 'corners_period_results-first_period-1X',
    'proposer': CornersFirstPeriodResults1XProposer(threshold=threshold)
}, {
    'name': 'corners_period_results-first_period-X2',
    'proposer': CornersFirstPeriodResultsX2Proposer(threshold=threshold)
}, {
    'name': 'corners_period_results-first_period-2',
    'proposer': CornersFirstPeriodResults2Proposer(threshold=threshold)
}]
corners_second_period_results_proposers_data = [{
    'name': 'corners_period_results-second_period-1',
    'proposer': CornersSecondPeriodResults1Proposer(threshold=threshold)
}, {
    'name': 'corners_period_results-second_period-1X',
    'proposer': CornersSecondPeriodResults1XProposer(threshold=threshold)
}, {
    'name': 'corners_period_results-second_period-X2',
    'proposer': CornersSecondPeriodResultsX2Proposer(threshold=threshold)
}, {
    'name': 'corners_period_results-second_period-2',
    'proposer': CornersSecondPeriodResults2Proposer(threshold=threshold)
}]
corners_totals_proposers_data = [{
    'name': 'corners_totals-greater',
    'proposer': CornersTotalsGreaterProposer(threshold=threshold)
}, {
    'name': 'corners_totals-lesser',
    'proposer': CornersTotalsLesserProposer(threshold=threshold)
}]


# В данном цикле используем `corners_attack_defense_fitter`
for train_sampler_name, train_sampler in train_samplers.items():
    name = 'provider-corners_results-corners_attack_defense-%s' % (train_sampler_name,)
    description = 'Исходы угловых, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов), недавние данные'
    provider1 = Provider(name, description, train_sampler, corners_attack_defense_fitter, corners_result_probabilities_attack_defense_predictor, corners_results_proposers_data)
    make_experiment(provider1, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_totals-corners_attack_defense-%s' % (train_sampler_name,)
    description = 'Тоталы угловых, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов), недавние данные'
    provider2 = Provider(name, description, train_sampler, corners_attack_defense_fitter, corners_result_probabilities_attack_defense_predictor, corners_totals_proposers_data)
    make_experiment(provider2, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_period_results-corners_periods_attack_defense-%s' % (train_sampler_name,)
    description = 'Исходы угловых 1-го тайма, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов), недавние данные'
    provider3 = Provider(name, description, train_sampler, corners_first_period_attack_defense_fitter, corners_result_probabilities_attack_defense_predictor, corners_first_period_results_proposers_data)
    make_experiment(provider3, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_period_results-corners_periods_attack_defense-%s' % (train_sampler_name,)
    description = 'Исходы угловых 2-го тайма, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов), недавние данные'
    provider4 = Provider(name, description, train_sampler, corners_second_period_attack_defense_fitter, corners_result_probabilities_attack_defense_predictor, corners_second_period_results_proposers_data)
    make_experiment(provider4, db_name, matches_collection_name, sample_condition)
