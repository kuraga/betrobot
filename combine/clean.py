import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./combine')

import os
import json
import glob2
from sport_util import is_goal, is_cross, is_corner


def clean_data(data):
  del data['whoscored'][0]['matchCentreEventType']
  del data['whoscored'][0]['formationIdNameMappings']
  del data['whoscored'][0]['matchCentreData']['commonEvents']
  del data['whoscored'][0]['matchCentreData']['home']['stats']
  del data['whoscored'][0]['matchCentreData']['home']['shotZones']
  del data['whoscored'][0]['matchCentreData']['home']['players']
  del data['whoscored'][0]['matchCentreData']['home']['formations']
  del data['whoscored'][0]['matchCentreData']['home']['incidentEvents']
  del data['whoscored'][0]['matchCentreData']['away']['stats']
  del data['whoscored'][0]['matchCentreData']['away']['shotZones']
  del data['whoscored'][0]['matchCentreData']['away']['players']
  del data['whoscored'][0]['matchCentreData']['away']['formations']
  del data['whoscored'][0]['matchCentreData']['away']['incidentEvents']
  data['whoscored'][0]['matchCentreData']['events'] = list(filter(
    lambda event: is_goal(event) or is_cross(event) or is_corner(event),
    data['whoscored'][0]['matchCentreData']['events']
  ))


glob_path = os.path.join('data', 'combined', 'matchesJson', '**', '*.json')
for file_path, (path, filename) in glob2.iglob(glob_path, with_matches=True):
  print(file_path)

  with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

  clean_data(data)

  out_dir_path = os.path.join('data', 'combined', 'matchesJson-cleaned', path)
  os.makedirs(out_dir_path, exist_ok=True)
  out_file_path = os.path.join(out_dir_path, '%s.json' % (filename,))
  with open(out_file_path, 'w', encoding='utf-8') as f_out:
    json.dump(data, f_out, ensure_ascii=False)
