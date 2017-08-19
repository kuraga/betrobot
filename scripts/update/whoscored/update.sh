#!/bin/bash -xe


rm -rf tmp/update/whoscored
mkdir -p tmp/update/whoscored

./scripts/update/whoscored/stage1.py
./scripts/update/whoscored/stage2.py
./scripts/update/whoscored/stage3.py
./scripts/update/whoscored/incorporate.py
./scripts/update/whoscored/update_players_teams.py

rm -rf tmp/update/whoscored
