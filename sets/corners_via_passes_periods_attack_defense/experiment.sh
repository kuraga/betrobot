#!/bin/bash -xe

python3 experiment.py "import sys; sys.path.append('./sets/corners_via_passes_periods_attack_defense'); from corners_via_passes_first_period_result_attack_defense_proposer import CornersViaPassesFirstPeriodResultAttackDefenseProposer; proposer = CornersViaPassesFirstPeriodResultAttackDefenseProposer()"
python3 experiment.py "import sys; sys.path.append('./sets/corners_via_passes_periods_attack_defense'); from corners_via_passes_second_period_result_attack_defense_proposer import CornersViaPassesSecondPeriodResultAttackDefenseProposer; proposer = CornersViaPassesSecondPeriodResultAttackDefenseProposer()"
