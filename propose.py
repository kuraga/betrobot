import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')

import pymongo


client = pymongo.MongoClient()
db = client['betrobot']
matches_collection = db['bets']
proposed_collection = db['proposed']


sample_condition = { }
thresholds = 1.7

exec(sys.argv[1])
if provider is None:
    sys.exit()


sample = matches_collection.find(sample_condition)
for betcity_match in sample:
    provider.handle(betcity_match)


print(provider.to_string())
print()
print()

if len(sys.argv) >= 3:
    provider_file_path = sys.argv[2]
    provider.save(provider_file_path)
else:
    provider.flush(proposed_collection)
