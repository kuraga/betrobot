#!/bin/bash -xe

python3 propose.py "import sys; sys.path.append('./sets/goals_periods_attack_defense'); from goals_first_period_result_attack_defense_proposer import GoalsFirstPeriodResultAttackDefenseProposer; proposer = GoalsFirstPeriodResultAttackDefenseProposer()"
python3 propose.py "import sys; sys.path.append('./sets/goals_periods_attack_defense'); from goals_second_period_result_attack_defense_proposer import GoalsSecondPeriodResultAttackDefenseProposer; proposer = GoalsSecondPeriodResultAttackDefenseProposer()"
