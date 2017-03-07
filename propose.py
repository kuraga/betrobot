import pymongo
import sys
from betting.provider import Provider

from betting.samplers.historical_sampler import HistoricalSampler
from betting.fitters.corners_attack_defense_fitter import CornersAttackDefenseFitter
from betting.predictors.corners_attack_defense_results_predictor import CornersResultsAttackDefensePredictor
from betting.proposers.corners_results_attack_defense_proposer import CornersResults1AttackDefenseProposer, CornersResults1XAttackDefenseProposer, CornersResultsX2AttackDefenseProposer, CornersResults2AttackDefenseProposer
from util.common_util import safe_get


db_name = 'betrobot'
matches_collection_name = 'matchesCleaned'
betting_matches_collection_name = 'bets'
proposed_collection_name = 'proposed'
sample_condition = {}
thresholds = 1.7


client = pymongo.MongoClient()
db = client[db_name]


description = 'Супер ставки'
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

print('Training...')
provider.fit()
print()


print('Betting...')
bets_collection = db[betting_matches_collection_name]
sample = bets_collection.find(sample_condition)
matches_count = sample.count()
for betcity_match in sample:
    provider.handle(betcity_match)

print('==================================================')
print('%s: %s' % (provider.uuid, provider.description))
print()
for proposer_data in provider.proposers_data:
    bets_data = proposer_data['proposer'].get_bets_data().to_string(index=False)

    print(proposer_data['name'])
    print(bets_data)
    print()
print('==================================================')
print()
print()


if len(sys.argv) >= 2:
    # TODO: Реализовать сохранение в файл
    raise NotImplementedError()
else:
    proposed_collection = db[proposed_collection_name]
    for proposer_data in provider.proposers_data:
        proposer_data['proposer'].flush(proposed_collection)
