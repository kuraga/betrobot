#!/bin/bash -x

python3 sets/goals_attack_defense/fit.py
./sets/goals_attack_defense/experiment.sh

python3 sets/corners_periods_attack_defense/fit.py
./sets/corners_periods_attack_defense/experiment.sh

python3 sets/corners_attack_defense/fit.py
./sets/corners_attack_defense/experiment.sh

python3 sets/goals_periods_attack_defense/fit.py
./sets/goals_periods_attack_defense/experiment.sh

./sets/corners_goals_periods_express_attack_defense/experiment.sh
