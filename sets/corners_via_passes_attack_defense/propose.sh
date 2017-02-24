#!/bin/bash -xe

python3 propose.py "import sys; sys.path.append('./sets/corners_via_passes_attack_defense'); from corners_via_passes_result_attack_defense_proposer import CornersViaPassesResultAttackDefenseProposer; proposer = CornersViaPassesResultAttackDefenseProposer()"
python3 propose.py "import sys; sys.path.append('./sets/corners_via_passes_attack_defense'); from corners_via_passes_totals_attack_defense_proposer import CornersViaPassesTotalsAttackDefenseProposer; proposer = CornersViaPassesTotalsAttackDefenseProposer()"
