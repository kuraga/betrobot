import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./sets/attack_defense')

import pymongo
from sport_util import tournaments, is_cross, is_saved_shot
from attack_defense_model import AttackDefenseModel


# Алгоритм:
# Предсказать индивидуальные тоталы кроссов и ударов (используя силу атаки и обороны, а также распределение Пуассона, см. http://www.pinnacle.com/ru/betting-articles/soccer/how-to-calculate-poisson-distribution?webSyncID=091ca3c2-ce3c-365a-d749-87ceb6ba50ce&sessionGUID=19b35b37-c257-428c-02b5-818ac1b42350).
# Затем предсказать индивидуальные тоталы угловых (использую средние отношений полученных выше данных к угловым).
# Используется статистика противников, в данном чемпионате.


client = pymongo.MongoClient()
db = client['betrobot']
matches_cleaned = db['matchesCleaned']

for tournament_id in tournaments:
    tournament_id = int(tournament_id)
    print(tournament_id)
    sample_condition = { 'tournamentId': tournament_id }

    sample = matches_cleaned.find(sample_condition)
    crosses_attack_defense_tournament_model = AttackDefenseModel('crosses-attack_defense-%d' % (sample_condition['tournamentId'],))
    crosses_attack_defense_tournament_model.fit(sample, condition=is_cross)
    crosses_attack_defense_tournament_model.save()

    sample = matches_cleaned.find(sample_condition)
    saved_shots_attack_defense_tournament_model = AttackDefenseModel('saved_shots-attack_defense-%d' % (sample_condition['tournamentId'],))
    saved_shots_attack_defense_tournament_model.fit(sample, condition=is_saved_shot)
    saved_shots_attack_defense_tournament_model.save()
