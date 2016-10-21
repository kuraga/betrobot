#!/bin/bash -xe

python3 experiment.py "import sys; sys.path.append('./sets/corners_attack_defense'); from corners_result_attack_defense_proposer import CornersResultAttackDefenseProposer; proposer = CornersResultAttackDefenseProposer()"
python3 experiment.py "import sys; sys.path.append('./sets/corners_attack_defense'); from corners_totals_attack_defense_proposer import CornersTotalsAttackDefenseProposer; proposer = CornersTotalsAttackDefenseProposer()"
