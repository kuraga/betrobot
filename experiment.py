import pymongo
import sys
from betting.provider import Provider
from betting.experimentor import Experimentor

from betting.samplers.historical_sampler import HistoricalSampler
from betting.fitters.corners_attack_defense_fitter import CornersAttackDefenseFitter
from betting.predictors.corners_attack_defense_results_predictor import CornersResultsAttackDefensePredictor
from betting.proposers.corners_results_attack_defense_proposer import CornersResults1AttackDefenseProposer, CornersResults1XAttackDefenseProposer, CornersResultsX2AttackDefenseProposer, CornersResults2AttackDefenseProposer
from util.common_util import safe_get


db_name = 'betrobot'
matches_collection_name = 'matchesCleaned'
sample_condition = { 'date': { '$regex': '^2017' } }
thresholds = 1.7


client = pymongo.MongoClient()
db = client[db_name]


description = 'Супер эксперимент'
train_sampler = HistoricalSampler(db_name, matches_collection_name)
fitter = CornersAttackDefenseFitter()
predictor = CornersResultsAttackDefensePredictor()
proposers_data = [{
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


provider = Provider(description, train_sampler, fitter, predictor, proposers_data)

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
print()


if len(sys.argv) >= 2:
    file_path = sys.argv[1]
    provider.save_fitted_data(file_path)
