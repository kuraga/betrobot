import re
import dirtyjson
import glob
import os
import datetime
import uuid
import json
import argparse
from betrobot.betting.sport_util import get_teams_tournaments_countries_value
from betrobot.util.common_util import safe_read_json


def _parse_whoscored_stage3():
  matches_metadata_file_path = os.path.join('data', 'whoscored', 'matches_metadata.json')
  matches_metadata = safe_read_json(matches_metadata_file_path, [])

  glob_path = os.path.join('tmp', 'update', 'whoscored', 'matchesHtml', '*.html')
  file_paths = glob.iglob(glob_path)

  for file_path in file_paths:
    print(file_path)

    with open(file_path, 'rt', encoding='utf-8') as f:
      match_html = f.read()

    m = re.search(r'var matchCentreData = (.+?);', match_html)
    if m is None:
      continue
    match_centre_data = dirtyjson.loads(m.group(1))
    if match_centre_data is None:
      continue

    m = re.search(r'var matchCentreEventTypeJson = (.+?);', match_html)
    if m is None:
      continue
    match_centre_event_type = dirtyjson.loads(m.group(1))

    m = re.search(r'var matchId = (\d+?);', match_html)
    if m is None:
      continue
    match_id = int(m.group(1))

    m = re.search(r'var formationIdNameMappings = (.+?);', match_html)
    if m is None:
      continue
    formation_id_name_mappings = dirtyjson.loads(m.group(1))

    m = re.search(r'<div id="breadcrumb-nav">.*?href="/Regions/(\d+)/Tournaments/(\d+)/Seasons/(\d+)(?:/Stages/(\d+))?(?:/[^"]+?)?"', match_html, re.MULTILINE | re.DOTALL)
    if m is None:
      continue
    region_id = int(m.group(1))
    tournament_id = int(m.group(2))
    season_id = int(m.group(3))
    stage_id = int(m.group(4)) if m.group(4) is not None else None

    match_date_str = datetime.datetime.strptime(match_centre_data['startDate'], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')
    match_uuid_str = str(uuid.uuid4())

    match_data = {
      'uuid': match_uuid_str,
      'date': match_date_str,
      'home': match_centre_data['home']['name'],
      'homeId': match_centre_data['home']['teamId'],
      'away': match_centre_data['away']['name'],
      'awayId': match_centre_data['away']['teamId'],
      'matchId': match_id,
      'regionId': region_id,
      'tournamentId': tournament_id,
      'seasonId': season_id,
      'stageId': stage_id,
      'matchCentreData': match_centre_data,
      'matchCentreEventType': match_centre_event_type,
      'formationIdNameMappings': formation_id_name_mappings
    }

    out_dir_path = os.path.join('tmp', 'update', 'whoscored', 'matchesJson', match_data['date'])
    os.makedirs(out_dir_path, exist_ok=True)
    out_file_path = os.path.join(out_dir_path, '%s.json' % (match_uuid_str,))
    with open(out_file_path, 'wt', encoding='utf-8') as f_out:
      json.dump(match_data, f_out, ensure_ascii=False)

    match_metadata = {
      'uuid': match_uuid_str,
      'date': match_data['date'],
      'home': match_data['home'],
      'away': match_data['away'],
      'country': get_teams_tournaments_countries_value('whoscoredName', match_data['home'], 'whoscoredCountryName'),
      'tournamentId': tournament_id,
      'seasonId': season_id,
      'stageId': stage_id
    }
    matches_metadata.append(match_metadata)

  matches_metadata_out_file_path = os.path.join('tmp', 'update', 'whoscored', 'matches_metadata.json')
  with open(matches_metadata_out_file_path, 'wt', encoding='utf-8') as matches_metadata_f_out:
    json.dump(matches_metadata, matches_metadata_f_out, ensure_ascii=False)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _parse_whoscored_stage3()
