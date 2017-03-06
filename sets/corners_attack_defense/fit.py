import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./sets/attack_defense')
sys.path.append('./sets/corners_attack_defense')

import pymongo
from sport_util import tournaments, is_corner
from attack_defense_model import AttackDefenseModel


# Алгоритм:
# Предсказать индивидуальные тоталы угловых (используя силу атаки и обороны, а также распределение Пуассона, см. http://www.pinnacle.com/ru/betting-articles/soccer/how-to-calculate-poisson-distribution?webSyncID=091ca3c2-ce3c-365a-d749-87ceb6ba50ce&sessionGUID=19b35b37-c257-428c-02b5-818ac1b42350).
# Используется статистика противников, в данном чемпионате.


client = pymongo.MongoClient()
db = client['betrobot']
matches_cleaned = db['matchesCleaned']

for tournament_id in tournaments:
    tournament_id = int(tournament_id)
    print(tournament_id)
    sample_condition = { 'tournamentId': tournament_id, 'date': { '$regex': '^201(6-11|6-12|7-01|7-02)' } }

    sample = matches_cleaned.find(sample_condition)
    corners_attack_defense_tournament_model = AttackDefenseModel('corners-attack_defense-%d' % (sample_condition['tournamentId'],))
    corners_attack_defense_tournament_model.fit(sample, condition=is_corner)
    corners_attack_defense_tournament_model.save()
