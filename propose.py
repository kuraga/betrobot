import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')

import pymongo


client = pymongo.MongoClient()
db = client['betrobot']
bets_collection = db['bets']
proposed_collection = db['proposed']


sample_condition = { }
proposer = None
tresholds = 1.6

exec(sys.argv[1])
if proposer is None:
    sys.exit()


sample = bets_collection.find(sample_condition)
for betcity_match in sample:
    proposer.propose(betcity_match, tresholds=tresholds)


print(proposer.to_string())
print()
print()

if len(sys.argv) >= 3:
    proposer_file_path = sys.argv[2]
    proposer.save(proposer_file_path)

proposer.flush_bets(proposed_collection)
