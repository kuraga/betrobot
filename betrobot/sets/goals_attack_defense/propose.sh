#!/bin/bash -xe

python3 propose.py "import sys; sys.path.append('./sets/goals_attack_defense'); from goals_result_attack_defense_proposer import GoalsResultAttackDefenseProposer; proposer = GoalsResultAttackDefenseProposer()"
python3 propose.py "import sys; sys.path.append('./sets/goals_attack_defense'); from goals_totals_attack_defense_proposer import GoalsTotalsAttackDefenseProposer; proposer = GoalsTotalsAttackDefenseProposer()"
