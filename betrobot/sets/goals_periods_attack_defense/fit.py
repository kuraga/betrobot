import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./sets/attack_defense')
sys.path.append('./sets/goals_periods_attack_defense')

import pymongo
from sport_util import tournaments, is_goal, is_first_period, is_second_period
from attack_defense_model import AttackDefenseModel


# Алгоритм:
# Предсказать индивидуальные тоталы голов в каждом тайме (используя силу атаки и обороны, а также распределение Пуассона, см. http://www.pinnacle.com/ru/betting-articles/soccer/how-to-calculate-poisson-distribution?webSyncID=091ca3c2-ce3c-365a-d749-87ceb6ba50ce&sessionGUID=19b35b37-c257-428c-02b5-818ac1b42350).
# Используется статистика противников, в данном чемпионате.


client = pymongo.MongoClient()
db = client['betrobot']
matches_cleaned = db['matchesCleaned']

for tournament_id in tournaments:
    tournament_id = int(tournament_id)
    print(tournament_id)
    sample_condition = { 'tournamentId': tournament_id }

    sample = matches_cleaned.find(sample_condition)
    goals_first_period_attack_defense_tournament_model = AttackDefenseModel('goals_first_period-attack_defense-%d' % (sample_condition['tournamentId'],))
    goals_first_period_attack_defense_tournament_model.fit(sample, condition=lambda event: is_goal(event) and is_first_period(event))
    goals_first_period_attack_defense_tournament_model.save()

    sample = matches_cleaned.find(sample_condition)
    goals_second_period_attack_defense_tournament_model = AttackDefenseModel('goals_second_period-attack_defense-%d' % (sample_condition['tournamentId'],))
    goals_second_period_attack_defense_tournament_model.fit(sample, condition=lambda event: is_goal(event) and is_second_period(event))
    goals_second_period_attack_defense_tournament_model.save()
