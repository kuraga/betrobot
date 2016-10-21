#!/bin/bash -xe

python3 propose.py "import sys; sys.path.append('./sets/corners_periods_attack_defense'); from corners_first_period_result_attack_defense_proposer import CornersFirstPeriodResultAttackDefenseProposer; proposer = CornersFirstPeriodResultAttackDefenseProposer()"
python3 propose.py "import sys; sys.path.append('./sets/corners_periods_attack_defense'); from corners_second_period_result_attack_defense_proposer import CornersSecondPeriodResultAttackDefenseProposer; proposer = CornersSecondPeriodResultAttackDefenseProposer()"
