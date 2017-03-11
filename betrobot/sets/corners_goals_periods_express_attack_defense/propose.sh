#!/bin/bash -xe

python3 propose.py "import sys; sys.path.append('./sets/corners_periods_attack_defense'); from corners_first_period_result_attack_defense_proposer import CornersFirstPeriodResultAttackDefenseProposer; proposer = CornersFirstPeriodResultAttackDefenseProposer()" tmp/corners_first_period_result_attack_defense_proposer.bin.tmp > /dev/null
python3 propose.py "import sys; sys.path.append('./sets/goals_periods_attack_defense'); from goals_second_period_result_attack_defense_proposer import GoalsSecondPeriodResultAttackDefenseProposer; proposer = GoalsSecondPeriodResultAttackDefenseProposer()" tmp/goals_second_period_result_attack_defense_proposer.bin.tmp > /dev/null
python3 propose_express.py "import sys; sys.path.append('./sets/corners_periods_attack_defense'); from corners_first_period_result_attack_defense_proposer import CornersFirstPeriodResultAttackDefenseProposer; corners_first_period_result_attack_defense_proposer = CornersFirstPeriodResultAttackDefenseProposer.load('tmp/corners_first_period_result_attack_defense_proposer.bin.tmp'); betting_session1 = corners_first_period_result_attack_defense_proposer.betting_sessions['1']; sys.path.append('./sets/goals_periods_attack_defense'); from goals_second_period_result_attack_defense_proposer import GoalsSecondPeriodResultAttackDefenseProposer; goals_second_period_result_attack_defense_proposer = GoalsSecondPeriodResultAttackDefenseProposer.load('tmp/goals_second_period_result_attack_defense_proposer.bin.tmp'); betting_session2 = goals_second_period_result_attack_defense_proposer.betting_sessions['X2'];"
rm tmp/corners_first_period_result_attack_defense_proposer.bin.tmp tmp/goals_second_period_result_attack_defense_proposer.bin.tmp