import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./combine')

import os
import json
import uuid
from sport_util import get_team_info_by


def whoscored_to_universal(metadata):
  res = {}

  for match_metadata in metadata:
    team_info = get_team_info_by('whoscoredName', match_metadata['home'])
    if team_info is None:
      continue

    match_home = team_info['whoscoredName']
    match_date = match_metadata['date']
    match_uuid = match_metadata['uuid']

    res[match_home] = res.get(match_home, {})
    res[match_home][match_date] = res[match_home].get(match_date, [])
    res[match_home][match_date].append(match_uuid)

  return res


def betarch_to_universal(metadata):
  res = {}

  for match_metadata in metadata:
    team_info = get_team_info_by('betarchName', match_metadata['home'])
    if team_info is None:
      continue

    match_home = team_info['whoscoredName']
    match_date = match_metadata['date']
    match_uuid = match_metadata['uuid']

    res[match_home] = res.get(match_home, {})
    res[match_home][match_date] = res[match_home].get(match_date, [])
    res[match_home][match_date].append(match_uuid)

  return res


def betcity_to_universal(metadata):
  res = {}

  for match_metadata in metadata:
    team_info = get_team_info_by('betcityName', match_metadata['home'])
    if team_info is None:
      continue

    match_home = team_info['whoscoredName']
    match_date = match_metadata['date']
    match_uuid = match_metadata['uuid']

    res[match_home] = res.get(match_home, {})
    res[match_home][match_date] = res[match_home].get(match_date, [])
    res[match_home][match_date].append(match_uuid)

  return res


def get_whoscored_matches(match_date, match_uuids):
  matches = []

  for match_uuid in match_uuids:
    file_path = os.path.join('data', 'whoscored', 'matchesJson', match_date, '%s.json' % (match_uuid,))
    with open(file_path, 'r', encoding='utf-8') as f:
      match = json.load(f)
    matches.append(match)

  return matches


def get_betarch_matches(match_date, match_uuids):
  matches = []

  for match_uuid in match_uuids:
    file_path = os.path.join('data', 'betarch', 'matchesJson', match_date, '%s.json' % (match_uuid,))
    with open(file_path, 'r', encoding='utf-8') as f:
      match = json.load(f)
    matches.append(match)

  return matches


def get_betcity_matches(match_date, match_uuids):
  matches = []

  for match_uuid in match_uuids:
    file_path = os.path.join('data', 'betcity', 'matchesJson', match_date, '%s.json' % (match_uuid,))
    with open(file_path, 'r', encoding='utf-8') as f:
      match = json.load(f)
    matches.append(match)

  return matches


whoscored_metadata_file_path = os.path.join('data', 'whoscored', 'matches_metadata.json')
with open(whoscored_metadata_file_path, 'r', encoding='utf-8') as f_whoscored_metadata:
  whoscored_metadata = json.load(f_whoscored_metadata)
whoscored_metadata_grouped = whoscored_to_universal(whoscored_metadata)

betarch_metadata_file_path = os.path.join('data', 'betarch', 'matches_metadata.json')
with open(betarch_metadata_file_path, 'r', encoding='utf-8') as f_betarch_metadata:
  betarch_metadata = json.load(f_betarch_metadata)
betarch_metadata_grouped = betarch_to_universal(betarch_metadata)

betcity_metadata_file_path = os.path.join('data', 'betcity', 'matches_metadata.json')
with open(betcity_metadata_file_path, 'r', encoding='utf-8') as f_betcity_metadata:
  betcity_metadata = json.load(f_betcity_metadata)
betcity_metadata_grouped = betcity_to_universal(betcity_metadata)

handled_whoscored_uuids = set()
for team in whoscored_metadata_grouped:
  for date_str in whoscored_metadata_grouped[team]:
    whoscored_uuids = whoscored_metadata_grouped[team][date_str]
    if whoscored_uuids[0] in handled_whoscored_uuids:
      continue

    print('%s - %s' % (team, date_str))
    whoscored_data = get_whoscored_matches(date_str, whoscored_uuids)

    betting_data = []
    if team in betarch_metadata_grouped and date_str in betarch_metadata_grouped[team]:
      betarch_uuids = betarch_metadata_grouped[team][date_str]
      betting_data += get_betarch_matches(date_str, betarch_uuids)
    if team in betcity_metadata_grouped and date_str in betcity_metadata_grouped[team]:
      betcity_uuids = betcity_metadata_grouped[team][date_str]
      betting_data += get_betcity_matches(date_str, betcity_uuids)

    match_uuid_str = str(uuid.uuid4())
    match_data = {
      'uuid': match_uuid_str,
      'date': date_str,
      'home': whoscored_data[0]['home'],
      'away': whoscored_data[0]['away'],
      'regionId': whoscored_data[0]['regionId'],
      'tournamentId': whoscored_data[0]['tournamentId'],
      'seasonId': whoscored_data[0]['seasonId'],
      'stageId': whoscored_data[0]['stageId'],
      'whoscored': whoscored_data,
      'betarch': betting_data
    }
    match_name = '%s - %s vs %s' % (match_data['date'], match_data['home'], match_data['away'])

    out_dir_path = os.path.join('data', 'combined', 'matchesJson', match_data['date'])
    os.makedirs(out_dir_path, exist_ok=True)
    out_file_path = os.path.join(out_dir_path, '%s.json' % (match_name,))
    with open(out_file_path, 'w', encoding='utf-8') as f_out:
      json.dump(match_data, f_out, ensure_ascii=False)

    handled_whoscored_uuids.update(whoscored_uuids)
