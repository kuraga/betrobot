import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./combine')

import os
import json


whoscored_teams = set()

whoscored_metadata_file_path = os.path.join('data', 'whoscored', 'matches_metadata.json')
with open(whoscored_metadata_file_path, 'r', encoding='utf-8') as f_whoscored_metadata:
  whoscored_metadata = json.load(f_whoscored_metadata)

for whoscored in whoscored_metadata:
  whoscored_teams.add(whoscored['home'])
  whoscored_teams.add(whoscored['away'])

print(whoscored_teams)


betarch_teams = set()

betarch_metadata_file_path = os.path.join('data', 'betarch', 'matches_metadata.json')
with open(betarch_metadata_file_path, 'r', encoding='utf-8') as f_betarch_metadata:
  betarch_metadata = json.load(f_betarch_metadata)

for betarch in betarch_metadata:
  betarch_teams.add(betarch['home'])
  betarch_teams.add(betarch['away'])

print(betarch_teams)
