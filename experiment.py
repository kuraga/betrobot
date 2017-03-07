import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting/providers')


import pymongo
from research_util import get_investigation_representation, print_investigation_representation


client = pymongo.MongoClient()
db = client['betrobot']
matches_collection = db['matchesCleaned']


sample_condition = { 'date': { '$regex': '^2017' } }
thresholds = 1.7

exec(sys.argv[1])
if provider is None:
    sys.exit()


sample = matches_collection.find(sample_condition)
matches_count = sample.count()
for data in sample:
    whoscored_match = data['whoscored'][0]
    if whoscored_match is None:
        continue

    for betarch_match in data['betarch']:
        provider.handle(betarch_match, whoscored_match=whoscored_match)


print()
print('Всего матчей обработано: %u' % matches_count)
print()

for proposer_data in provider.proposers_data:
    print_investigation_representation(proposer_data, matches_count=matches_count)
    print()
    print()


if len(sys.argv) >= 3:
    # TODO: Реализовать сохранение в файл
    raise NotImplementedError()
