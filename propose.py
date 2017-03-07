import pymongo
from util.research_util import print_bets_data


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
matches_count = sample.count()
for betcity_match in sample:
    provider.handle(betcity_match)


print()
print('Всего матчей обработано: %u' % matches_count)
print()

for proposer_data in provider.proposers_data:
    print_bets_data(proposer_data)
    print()
    print()


if len(sys.argv) >= 3:
    # TODO: Реализовать сохранение в файл
    raise NotImplementedError()
else:
    for proposer_data in provider.proposers_data:
        proposer_data['proposer'].flush(proposed_collection)
