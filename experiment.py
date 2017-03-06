import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting/providers')

import pymongo


client = pymongo.MongoClient()
db = client['betrobot']
matches_cleaned = db['matchesCleaned']


sample_condition = { 'date': { '$regex': '^2017' } }
thresholds = 1.7

exec(sys.argv[1])
if provider is None:
    sys.exit()


sample = matches_cleaned.find(sample_condition)
matches_count = 0
for data in sample:
    whoscored_match = data['whoscored'][0]
    if whoscored_match is None:
        continue

    for betarch_match in data['betarch']:
        provider.handle(betarch_match, whoscored_match=whoscored_match)

    matches_count += 1


print('Всего матчей обработано: %u' % matches_count)
for betting_session in provider.betting_sessions.values():
    betting_session.print_investigation(matches_count=matches_count)
    print()
    print()

if len(sys.argv) >= 3:
    provider_file_path = sys.argv[2]
    provider.save(provider_file_path)
