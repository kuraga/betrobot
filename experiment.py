import pymongo
import os
import pickle
from betting.provider import Provider
from betting.experimentor import Experimentor

from betting.samplers.historical_sampler import HistoricalSampler
from betting.samplers.eve_sampler import EveSampler
from betting.fitters.corners_attack_defense_fitter import CornersAttackDefenseFitter
from betting.predictors.corners_attack_defense_predictor import CornersAttackDefensePredictor
from betting.proposers.corners_results_attack_defense_proposer import CornersResults1AttackDefenseProposer, CornersResults1XAttackDefenseProposer, CornersResultsX2AttackDefenseProposer, CornersResults2AttackDefenseProposer
from util.common_util import safe_get


def make_experiment(provider, db_name, matches_collection_name, sample_condition):
    experimentor = Experimentor(provider, db_name, matches_collection_name, sample_condition)

    print('Training...')
    experimentor.train()
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
thresholds = 1.7


train_samplers = {
    # 'historical': HistoricalSampler(db_name, matches_collection_name),
    'eve': EveSampler(db_name, matches_collection_name)
}
corners_attack_defense_fitter = CornersAttackDefenseFitter()
corners_attack_defense_predictor = CornersAttackDefensePredictor()
# TODO: Перейти на ordereddict
corners_proposers_data = [{
    'name': '1',
    'proposer': CornersResults1AttackDefenseProposer(threshold=safe_get(thresholds, '1'))
}, {
    'name': '1X',
    'proposer': CornersResults1XAttackDefenseProposer(threshold=safe_get(thresholds, '1X'))
}, {
    'name': 'X2',
    'proposer': CornersResultsX2AttackDefenseProposer(threshold=safe_get(thresholds, 'X2'))
}, {
    'name': '2',
    'proposer': CornersResults2AttackDefenseProposer(threshold=safe_get(thresholds, '2'))
}]


for train_sampler_name, train_sampler in train_samplers.items():
    name = 'provider-corners_results-corners_corners_attack_defense-%s' % (train_sampler_name,)
    description = 'Исходы угловых, предсказание по атаке и обороне команд (угловые), исторические данные'
    provider = Provider(name, description, train_sampler, corners_attack_defense_fitter, corners_attack_defense_predictor, corners_proposers_data)
    make_experiment(provider, db_name, matches_collection_name, sample_condition)
