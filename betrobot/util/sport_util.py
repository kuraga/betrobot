import os
import pandas as pd
import json
from betrobot.util.common_util import count, get_first


def _get_countries():
    with open(os.path.join('data', 'whoscored_countries.json'), 'r', encoding='utf-8') as f:
        countries = json.load(f)

    return countries

countries = _get_countries()


def _get_tournaments():
    with open(os.path.join('data', 'whoscored_tournaments.json'), 'r', encoding='utf-8') as f:
        tournaments = json.load(f)

    return tournaments

tournaments = _get_tournaments()


def _get_teams():
  with open(os.path.join('data', 'teams.csv'), 'r', encoding='utf-8') as f:
    teams = pd.read_csv(f)

  return teams

teams = _get_teams()


def get_country_name(country_id):
    return countries.get(country_id, country_id)


def get_team_info_by(column, value, default=None):
    s = teams.loc[ teams[column] == value ]
    if s.shape[0] > 0:
      return s.iloc[0]
    else:
      return default


def get_whoscored_team_ids_of_betcity_match(betcity_match):
    home_whoscored_id = None
    away_whoscored_id = None

    home_info = get_team_info_by('betcityName', betcity_match['home'])
    if home_info is not None:
        home_whoscored_id = home_info['whoscoredId']
    away_info = get_team_info_by('betcityName', betcity_match['away'])
    if away_info is not None:
        away_whoscored_id = away_info['whoscoredId']

    return (home_whoscored_id, away_whoscored_id)


def get_betcity_teams_of_whoscored_match(whoscored_match):
    home_betcity = None
    away_betcity = None

    home_info = get_team_info_by('whoscoredName', whoscored_match['home'])
    if home_info is not None:
        home_betcity = home_info['betcityName']
    away_info = get_team_info_by('whoscoredName', whoscored_match['away'])
    if away_info is not None:
        away_betcity = away_info['betcityName']

    return (home_betcity, away_betcity)


def get_whoscored_tournament_id_of_betcity_match(betcity_match):
    (home, away) = get_whoscored_team_ids_of_betcity_match(betcity_match)
    if home is None or away is None:
        return None

    home_info = get_team_info_by('whoscoredId', home)
    if home_info is None:
        return None

    tournament_id = home_info['whoscoredTournamentId']

    return tournament_id


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


def is_event_successful(event):
    return event['outcomeType']['displayName'] == 'Successful'


def is_goal(event):
    return is_event_successful(event) and event.get('isGoal') == True and event['type']['displayName'] == 'Goal'


def is_pass(event):
    return event['type']['displayName'] == 'Pass'


def is_corner(event):
    return is_pass(event) and 'CornerTaken' in get_types(event)


def is_cross(event):
    return is_pass(event) and 'Cross' in get_types(event)


def is_shot(event):
    return event.get('isShot') == True


def is_saved_shot(event):
    return is_shot(event) and 'SavedShot' in get_types(event)


def is_missed_shot(event):
    return is_shot(event) and 'MissedShots' in get_types(event)


def is_first_period(event):
    return event['period']['displayName'] == 'FirstHalf'


def is_second_period(event):
    return event['period']['displayName'] == 'SecondHalf'


def is_betarch_match_main(betarch_match):
    return betarch_match['specialWord'] is None


def get_betarch_main_match(betarch_data):
    return get_first(is_betarch_match_main, betarch_data)


def is_betarch_match_corner(betarch_match):
    return betarch_match['specialWord'] == 'УГЛ'


def get_betarch_corner_match(betarch_data):
    return get_first(is_betarch_match_corner, betarch_data)


def get_whoscored_teams(whoscored_match):
    whoscored_home = whoscored_match['matchCentreData']['home']['teamId']
    whoscored_away = whoscored_match['matchCentreData']['away']['teamId']

    return (whoscored_home, whoscored_away)


def get_betarch_teams(betarch_match):
    return (betarch_match['home'], betarch_match['away'])


def count_events(function, whoscored_match):
    return count(function, whoscored_match['matchCentreData']['events'])


def count_events_of_teams(function, whoscored_match):
    (whoscored_home, whoscored_away) = get_whoscored_teams(whoscored_match)

    events_home_count = count_events(
        lambda event: function(event) and event['teamId'] == whoscored_home,
        whoscored_match
    )
    events_away_count = count_events(
        lambda event: function(event) and event['teamId'] == whoscored_away,
        whoscored_match
    )

    return (events_home_count, events_away_count)


def bet_satisfy(condition, bet_or_pattern):
    for i in range(len(condition)):
        # FIXME: Исправлять такие ситуации на этапе парсинга
        if condition[i] != '*' and condition[i] != bet_or_pattern[i] and \
          not ((condition[i] is None and bet_or_pattern[i] == '') or (condition[i] == '' and bet_or_pattern[i] is None)):
            return False

    return True


def get_bet(condition, betarch_match):
    bet = get_first(lambda bet: bet_satisfy(condition, bet), betarch_match['bets'])
    # FIXME: Отфильтровывать такие ситуации на этапе парсинга
    return bet if bet is None or bet[5] is not None else None


def collect_events_data(function, sample):
    events_data = pd.DataFrame(columns=['match_uuid', 'home', 'away', 'events_home_count', 'events_away_count']).set_index('match_uuid')

    for data in sample:
          match_uuid = data['uuid']
          whoscored_match = data['whoscored'][0]

          (whoscored_home, whoscored_away) = get_whoscored_teams(whoscored_match)
          (events_home_count, events_away_count) = count_events_of_teams(function, whoscored_match)

          events_data = events_data.append({
             'match_uuid': match_uuid,
             'home': whoscored_home,
             'away': whoscored_away,
             'events_home_count': events_home_count,
             'events_away_count': events_away_count
          }, ignore_index=True)

    return events_data


def bet_to_string(bet, match_special_word=None):
    if len(bet) == 6:
        (special_word, type_, prefix, name, handicap, bet_value) = bet
    else:
        (special_word, type_, prefix, name, handicap) = bet
        bet_value = None

    bet_str = ''
    if match_special_word is not None:
        bet_str += '(%s) ' % (match_special_word,)
    if type_ is not None and type_ != '':
        bet_str += '%s: ' % (type_,)
    if special_word is not None and special_word != '':
        bet_str += '%s' % (special_word,)
    if prefix is not None and prefix != '':
        bet_str += ' %s' % (prefix,)
    if name is not None and name != '':
        bet_str += ' %s' % (name,)
    if handicap is not None:
        bet_str += ' (%.1f)' % (handicap,)
    if bet_value is not None:
        bet_str += ' (%.2f)' % (bet_value,)

    return bet_str
