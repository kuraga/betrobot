import pymongo
import os
import pickle
from betting.provider import Provider
from betting.experimentor import Experimentor

from betting.samplers.date_based_samplers import HistoricalSampler, EveSampler
from betting.fitters.corners_attack_defense_fitters import CornersAttackDefenseFitter
from betting.predictors.corners_attack_defense_predictors import CornersAttackDefensePredictor
from betting.proposers.corners_results_proposers import CornersResults1Proposer, CornersResults1XProposer, CornersResultsX2Proposer, CornersResults2Proposer
from util.common_util import safe_get


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
corners_attack_defense_predictor = CornersAttackDefensePredictor()
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


# В данном цикле используем `corners_attack_defense_fitter`
for train_sampler_name, train_sampler in train_samplers.items():
    name = 'provider-corners_results-corners_attack_defense-%s' % (train_sampler_name,)
    description = 'Исходы угловых, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов), недавние данные'
    provider = Provider(name, description, train_sampler, corners_attack_defense_fitter, corners_attack_defense_predictor, corners_results_proposers_data)
    make_experiment(provider, db_name, matches_collection_name, sample_condition)
