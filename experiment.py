import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')

import pymongo


client = pymongo.MongoClient()
db = client['betrobot']
matches_cleaned = db['matchesCleaned']


sample_condition = { 'tournamentId': 2 }
proposer = None
tresholds = None

exec(sys.argv[1])
if proposer is None:
    sys.exit()


sample = matches_cleaned.find(sample_condition)
matches_count = 0
for data in sample:
    whoscored_match = data['whoscored'][0]
    if whoscored_match is None:
        continue

    for betarch_match in data['betarch']:
        proposer.propose(betarch_match, whoscored_match, tresholds=tresholds)

    matches_count += 1


for betting_session in proposer.betting_sessions.values():
    betting_session.print_investigation(matches_count=matches_count)
    print()
    print()

if len(sys.argv) >= 3:
    proposer_file_path = sys.argv[2]
    proposer.save(proposer_file_path)
