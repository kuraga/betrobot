import pymongo
import sys
import pickle
from betrobot.betting.provider import Provider

from betrobot.betting.samplers.historical_sampler import HistoricalSampler
from betrobot.betting.fitters.corners_attack_defense_fitter import CornersAttackDefenseFitter
from betrobot.betting.predictors.corners_attack_defense_results_predictor import CornersResultsAttackDefensePredictor
from betrobot.betting.proposers.corners_results_attack_defense_proposer import CornersResults1AttackDefenseProposer, CornersResults1XAttackDefenseProposer, CornersResultsX2AttackDefenseProposer, CornersResults2AttackDefenseProposer
from betrobot.util.common_util import safe_get


db_name = 'betrobot'
matches_collection_name = 'matchesCleaned'
betting_matches_collection_name = 'bets'
sample_condition = {}
thresholds = 1.7


print('Loading...')
client = pymongo.MongoClient()
db = client[db_name]

file_path = sys.argv[1]
with open(file_path, 'rb') as f:
    provider = pickle.load(f)


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



if len(sys.argv) >= 3 and sys.argv[2] != '-':
    print('Flushing...')
    proposed_collection_name = sys.argv[2]
    proposed_collection = db[proposed_collection_name]
    for proposer_data in provider.proposers_data:
        proposer_data['proposer'].flush(proposed_collection)

if len(sys.argv) >= 4 and sys.argv[3] != '-':
    print('Saving...')
    file_path = sys.argv[3]
    with open(file_path, 'wb') as f:
        pickle.dump(provider, f)
