import os
import numpy as np
import pandas as pd
import datetime
from collections import Counter
from betrobot.util.database_util import db
from betrobot.util.cache_util import memoize
from betrobot.util.common_util import get_value


# TODO: Разделить файл на части




with open(os.path.join('data', 'teams.csv'), 'rt', encoding='utf-8') as f:
    teams_data = pd.read_csv(f)

with open(os.path.join('data', 'tournaments.csv'), 'rt', encoding='utf-8') as f:
    tournaments_data = pd.read_csv(f)

with open(os.path.join('data', 'countries.csv'), 'rt', encoding='utf-8') as f:
    countries_data = pd.read_csv(f)

with open(os.path.join('data', 'players.csv'), 'rt', encoding='utf-8') as f:
    players_data = pd.read_csv(f)




def dateize(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d')




def get_types(event):
    types = set()

    types.add(event['type']['displayName'])

    # types.add(event['outcomeType']['displayName'])

    if event.get('isGoal'):
        types.add('Goal')
    if event.get('isTouch'):
        types.add('Touch')
    if event.get('isShot'):
        types.add('Shot')

    types.update( qualifier['type']['displayName'] for qualifier in event['qualifiers'] if 'value' not in qualifier )

    return types


def is_event_successful(event, whoscored_match=None):
    return event['outcomeType']['displayName'] == 'Successful'


def is_event_unsuccessful(event, whoscored_match=None):
    return event['outcomeType']['displayName'] == 'Unsuccessful'


def is_goal(event, whoscored_match=None):
    return event.get('isGoal') == True and event['type']['displayName'] == 'Goal'


def is_pass(event, whoscored_match=None):
    return event['type']['displayName'] == 'Pass'


def is_corner(event, whoscored_match=None):
    return is_pass(event) and 'CornerTaken' in get_types(event)


def is_yellow_card(event, whoscored_match=None):
    return event['type']['displayName'] == 'Card' and event['cardType']['displayName'] == 'Yellow'


def is_red_card(event, whoscored_match=None):
    return event['type']['displayName'] == 'Card' and event['cardType']['displayName'] == 'Red'


def is_cross(event, whoscored_match=None):
    return is_pass(event) and 'Cross' in get_types(event)


def is_shot(event, whoscored_match=None):
    return event.get('isShot') == True


def is_foul(event, whoscored_match=None):
    return 'Foul' in get_types(event) and event['type']['displayName'] == 'Foul'


def is_first_period(event, whoscored_match=None):
    return event['period']['displayName'] == 'FirstHalf'


def is_second_period(event, whoscored_match=None):
    return event['period']['displayName'] == 'SecondHalf'


def is_home(event, whoscored_match):
    return event['teamId'] == whoscored_match['homeId']


def is_away(event, whoscored_match):
    return event['teamId'] == whoscored_match['awayId']


def is_player(event, player_name, whoscored_match):
    if 'playerId' not in event or event['playerId'] is None:
        return False

    event_player_id_str = str(event['playerId'])
    if event_player_id_str not in whoscored_match['matchCentreData']['playerIdNameDictionary']:
        return False

    event_player_name = whoscored_match['matchCentreData']['playerIdNameDictionary'][event_player_id_str]

    return player_name == event_player_name




def match_exists(match_uuid):
    match_headers_collection = db['match_headers']

    return match_headers_collection.count({ 'uuid': match_uuid }) > 0


def get_match_header(match_uuid):
    match_headers_collection = db['match_headers']

    return match_headers_collection.find_one({ 'uuid': match_uuid })


def get_match_header_by_date_and_teams(date_, home, away):
    match_headers_collection = db['match_headers']

    match_header = match_headers_collection.find_one({ 'date': date_, 'home': home, 'away': away })
    if match_header is None:
        return None

    return match_header['uuid']


def get_additional_info(match_uuid):
    additional_info_collection = db['additional_info']
    return additional_info_collection.find_one({ 'match_uuid': match_uuid })


def get_extended_info(match_uuid):
    matches_collection = db['matches']
    return matches_collection.find_one({ 'match_uuid': match_uuid })


def get_bets_match(match_uuid):
    bets_collection = db['bets']
    return bets_collection.find_one({ 'match_uuid': match_uuid })


def get_match_uuid_by_whoscored_match(whoscored_match):
    date_ = dateize(whoscored_match['date'])
    home = whoscored_match['home']
    away = whoscored_match['away']

    return get_match_header_by_date_and_teams(date_, home, away)


def get_match_uuid_by_betarch_match(betarch_match):
    date_ = dateize(betarch_match['date'])
    home = get_value(teams_data, 'betarchName', betarch_match['home'], 'whoscoredName')
    away = get_value(teams_data, 'betarchName', betarch_match['away'], 'whoscoredName')
    if home is None or away is None:
        return None

    return get_match_header_by_date_and_teams(date_, home, away)


def get_match_uuid_by_betcity_match(betcity_match):
    date_ = dateize(betcity_match['date'])
    home = get_value(teams_data, 'betcityName', betcity_match['home'], 'whoscoredName')
    away = get_value(teams_data, 'betcityName', betcity_match['away'], 'whoscoredName')
    if home is None or away is None:
        return None

    return get_match_header_by_date_and_teams(date_, home, away)


def get_match_uuid_by_intelbet_match(intelbet_match):
    date_ = dateize(intelbet_match['date'])
    home = get_value(teams_data, 'intelbetName', intelbet_match['home'], 'whoscoredName')
    away = get_value(teams_data, 'intelbetName', intelbet_match['away'], 'whoscoredName')
    if home is None or away is None:
        return None

    return get_match_header_by_date_and_teams(date_, home, away)


def count_events(function, whoscored_match):
    if 'matchCentreData' not in whoscored_match:
        return None

    result = 0

    for event in whoscored_match['matchCentreData']['events']:
        if function(event, whoscored_match=whoscored_match):
            result += 1

    return result


@memoize(lambda functions, match_uuid: match_uuid)
def count_events_by_match_uuid(function, match_uuid):
    if not match_exists(match_uuid):
        return None

    whoscored_match = get_extended_info(match_uuid)['whoscored']

    return count_events(function, whoscored_match)


def count_events_multiple(functions, whoscored_match):
    if 'matchCentreData' not in whoscored_match:
        return None

    results = [ 0 ] * len(functions)

    for event in whoscored_match['matchCentreData']['events']:
        for i in range(len(functions)):
            if functions[i](event, whoscored_match=whoscored_match):
                results[i] += 1

    return tuple(results)


@memoize(lambda functions, match_uuid: match_uuid)
def count_events_multiple_by_match_uuid(functions, match_uuid):
    if not match_exists(match_uuid):
        return None

    whoscored_match = get_extended_info(match_uuid)['whoscored']

    return count_events(functions, whoscored_match)


def count_events_of_teams(function, whoscored_match):
    if 'matchCentreData' not in whoscored_match:
        return None

    t = whoscored_match['matchCentreData']['playerIdNameDictionary']

    event_team_ids = [ event.get('teamId', "Not-a-Team's") for event in whoscored_match['matchCentreData']['events'] if function(event, whoscored_match=whoscored_match) ]
    event_team_id_freqs = Counter(event_team_ids)

    home_id = whoscored_match['homeId']
    home_count = event_team_id_freqs[home_id]
    away_id = whoscored_match['awayId']
    away_count = event_team_id_freqs[away_id]

    return (home_count, away_count)


@memoize(lambda functions, match_uuid: match_uuid)
def count_events_of_teams_by_match_uuid(function, match_uuid):
    if not match_exists(match_uuid):
        return None

    whoscored_match = get_extended_info(match_uuid)['whoscored']

    return count_events_of_teams(function, whoscored_match)


def count_events_of_players(function, whoscored_match):
    if 'matchCentreData' not in whoscored_match:
        return None

    t = whoscored_match['matchCentreData']['playerIdNameDictionary']

    event_player_ids = [ event.get('playerId', "Not-a-Player's") for event in whoscored_match['matchCentreData']['events'] if function(event, whoscored_match=whoscored_match) ]
    event_player_id_freqs = Counter(event_player_ids)
    counts = { t[player_id]: event_player_id_freqs[int(player_id)] for player_id in t }

    return counts


@memoize(lambda functions, match_uuid: match_uuid)
def count_events_of_players_by_match_uuid(function, match_uuid):
    if not match_exists(match_uuid):
        return None

    whoscored_match = get_extended_info(match_uuid)['whoscored']

    return count_events_of_players(function, whoscored_match)




# TODO: Внедрить регулярные выражения?
def bet_satisfy(condition, bet):
    for i in range(len(condition)):
        if condition[i] != '*' and condition[i] != bet['pattern'][i]:
            return False

    return True


def filter_bets(bet_pattern, bets_match):
    bets = [ bet for bet in bets_match['bets'] if bet_satisfy(bet_pattern, bet) ]

    return bets




def get_substatistic(statistic, notnull=None, by=None, value=None, n=None, min_n=None, sort_by=None, ascending=True, which=None):
    substatistic = statistic

    if by is not None:
        substatistic = substatistic[ substatistic[by] == value ]

    if notnull is not None:
        substatistic = substatistic[ substatistic[notnull].notnull() ]

    if min_n is not None:
        if substatistic.shape[0] < min_n:
            return None

    if sort_by is not None:
        substatistic = substatistic.sort_values(sort_by, ascending=ascending)

    if n is not None:
        substatistic = substatistic[:n]

    if which is not None:
        return substatistic[which].values
    else:
        return substatistic.copy()


# TODO: Выводить дисперсию ROI
def get_standard_investigation(bets_data, matches_count=None):
    known_ground_truth_bets_data = bets_data.copy()

    known_ground_truth_bets_data = known_ground_truth_bets_data[ known_ground_truth_bets_data['ground_truth'].notnull() ]

    bets_count = known_ground_truth_bets_data.shape[0]
    if bets_count == 0:
        return None

    used_matches_count = known_ground_truth_bets_data['match_uuid'].nunique()
    matches_frequency = used_matches_count / matches_count if matches_count is not None else np.nan
    bets_successful = known_ground_truth_bets_data[ known_ground_truth_bets_data['ground_truth'] ]
    bets_successful_count = bets_successful.shape[0]
    accuracy = bets_successful_count / bets_count
    roi = bets_successful['value'].sum() / bets_count - 1
    profit = bets_successful['value'].sum() - bets_count

    standard_investigation_line_dict = {
       'matches': matches_count,
       'matches_frequency': matches_frequency,
       'bets': bets_count,
       'win': bets_successful_count,
       'accuracy': accuracy,
       'roi': roi,
       'profit': profit
    }

    return standard_investigation_line_dict


def filter_and_sort_investigation(investigation, min_bets=50, min_matches_frequency=0.00, min_accuracy=None, min_roi=None, sort_by=['roi', 'matches'], sort_ascending=[False, False]):
    result = investigation.copy()

    if min_bets is not None:
        result = result[ result['bets'] >= min_bets ]
    if min_matches_frequency is not None:
        result = result[ result['matches_frequency'] >= min_matches_frequency ]
    if min_accuracy is not None:
        result = result[ result['accuracy'] >= min_accuracy ]
    if min_roi is not None:
        result = result[ result['roi'] >= min_roi ]

    if sort_by is not None:
        result.sort_values(by=sort_by, ascending=sort_ascending, inplace=True)

    return result
