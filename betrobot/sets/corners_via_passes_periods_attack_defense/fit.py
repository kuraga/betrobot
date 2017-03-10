import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./sets/attack_defense')

import pymongo
from sport_util import tournaments, is_cross, is_saved_shot, is_first_period, is_second_period
from attack_defense_model import AttackDefenseModel


# Алгоритм:
# Предсказать индивидуальные тоталы кроссов и ударов в каждом тайме (используя силу атаки и обороны, а также распределение Пуассона, см. http://www.pinnacle.com/ru/betting-articles/soccer/how-to-calculate-poisson-distribution?webSyncID=091ca3c2-ce3c-365a-d749-87ceb6ba50ce&sessionGUID=19b35b37-c257-428c-02b5-818ac1b42350).
# Затем предсказать индивидуальные тоталы угловых в каждом тайме (использую средние отношений полученных выше данных к угловым).
# Используется статистика противников, в данном чемпионате.


client = pymongo.MongoClient()
db = client['betrobot']
matches_cleaned = db['matchesCleaned']

for tournament_id in tournaments:
    tournament_id = int(tournament_id)
    print(tournament_id)
    sample_condition = { 'tournamentId': tournament_id }

    sample = matches_cleaned.find(sample_condition)
    crosses_first_period_attack_defense_tournament_model = AttackDefenseModel('crosses_first_period-attack_defense-%d' % (sample_condition['tournamentId'],))
    crosses_first_period_attack_defense_tournament_model.fit(sample, condition=lambda event: is_cross(event) and is_first_period(event))
    crosses_first_period_attack_defense_tournament_model.save()

    sample = matches_cleaned.find(sample_condition)
    saved_shots_first_period_attack_defense_tournament_model = AttackDefenseModel('saved_shots_first_period-attack_defense-%d' % (sample_condition['tournamentId'],))
    saved_shots_first_period_attack_defense_tournament_model.fit(sample, condition=lambda event: is_saved_shot(event) and is_first_period(event))
    saved_shots_first_period_attack_defense_tournament_model.save()

    sample = matches_cleaned.find(sample_condition)
    crosses_second_period_attack_defense_tournament_model = AttackDefenseModel('crosses_second_period-attack_defense-%d' % (sample_condition['tournamentId'],))
    crosses_second_period_attack_defense_tournament_model.fit(sample, condition=lambda event: is_cross(event) and is_second_period(event))
    crosses_second_period_attack_defense_tournament_model.save()

    sample = matches_cleaned.find(sample_condition)
    saved_shots_second_period_attack_defense_tournament_model = AttackDefenseModel('saved_shots_second_period-attack_defense-%d' % (sample_condition['tournamentId'],))
    saved_shots_second_period_attack_defense_tournament_model.fit(sample, condition=lambda event: is_saved_shot(event) and is_second_period(event))
    saved_shots_second_period_attack_defense_tournament_model.save()
