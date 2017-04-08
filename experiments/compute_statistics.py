import pymongo
import os
import pickle
import pandas as pd
from betrobot.util.sport_util import count_events_of_teams, is_goal, is_corner


db_name = 'betrobot'
matches_collection_name = 'matchesCleaned'

client = pymongo.MongoClient()
db = client[db_name]
matches_collection = db[matches_collection_name]

sample = matches_collection.find()


statistics = pd.DataFrame(columns=['uuid', 'date', 'home', 'away', 'score_goals_home', 'score_goals_away', 'score_corners_home', 'score_corners_away']).set_index('uuid')
for data in sample:
    match_uuid = data['uuid']
    print(match_uuid)

    whoscored_match = data['whoscored'][0]

    (score_goals_home, score_goals_away) = count_events_of_teams(is_goal, whoscored_match)
    (score_corners_home, score_corners_away) = count_events_of_teams(is_corner, whoscored_match)

    statistics.loc[match_uuid] = {
        'date': whoscored_match['date'],
        'home': whoscored_match['home'],
        'away': whoscored_match['away'],
        'score_goals_home': score_goals_home,
        'score_goals_away': score_goals_away,
        'score_corners_home': score_corners_home,
        'score_corners_away': score_corners_away
    }


output_file_path = os.path.join('data', 'statistics.pkl')
with open(output_file_path, 'wb') as f_out:
    pickle.dump(statistics, f_out)
