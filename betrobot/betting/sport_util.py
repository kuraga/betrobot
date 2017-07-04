import os
import numpy as np
import pandas as pd
import json
from betrobot.util.common_util import count, get_first, conjunction


def _get_teams_tournaments_countries_data():
    with open(os.path.join('data', 'teams.csv'), 'rt', encoding='utf-8') as f:
        teams = pd.read_csv(f)

    with open(os.path.join('data', 'tournaments.csv'), 'rt', encoding='utf-8') as f:
        tournaments = pd.read_csv(f)

    with open(os.path.join('data', 'countries.csv'), 'rt', encoding='utf-8') as f:
        countries = pd.read_csv(f)

    teams_data = teams.copy()
    teams_data = teams_data.merge(tournaments, on='whoscoredTournamentId')
    teams_data = teams_data.merge(countries, on='whoscoredCountryId')
    teams_data.set_index('whoscoredId', drop=False, inplace=True)

    return teams_data


teams_tournaments_countries_data = _get_teams_tournaments_countries_data()


def get_teams_tournaments_countries_value(by, value, which, default=None):
    s = teams_tournaments_countries_data.loc[ teams_tournaments_countries_data[by] == value ]

    if s.shape[0] == 1:
        return s.iloc[0][which]
    elif s.shape[0] == 0:
        return default
    else:
      raise RuntimeError('Multiple items found by condition %s == %s' % (by, str(value)))


def is_home_or_away_by_betcity_team_name(betcity_team_name, whoscored_match):
    if betcity_team_name == '1':
        return 'H'
    if betcity_team_name == '2':
        return 'A'

    team_whoscored_name = get_teams_tournaments_countries_value('betcityName', betcity_team_name, 'whoscoredName')
    if team_whoscored_name is None:
        return None

    if team_whoscored_name == whoscored_match['home']:
        return 'H'
    if team_whoscored_name == whoscored_match['away']:
        return 'A'

    return None


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


def is_betarch_match_main(betarch_match):
    return betarch_match['specialWord'] is None


def get_betarch_main_match(betarch_data):
    return get_first(is_betarch_match_main, betarch_data)


def is_betarch_match_corner(betarch_match):
    return betarch_match['specialWord'] == 'УГЛ'


def get_betarch_corner_match(betarch_data):
    return get_first(is_betarch_match_corner, betarch_data)


def is_betarch_match_yellow_card(betarch_match):
    return betarch_match['specialWord'] == 'ЖК'


def get_betarch_yellow_card_match(betarch_data):
    return get_first(is_betarch_match_yellow_card, betarch_data)


def count_events(function, whoscored_match):
    return count(function, whoscored_match['matchCentreData']['events'], whoscored_match=whoscored_match)


def count_events_of_teams(function, whoscored_match):
    events_home_count = count_events(conjunction(function, is_home), whoscored_match)
    events_away_count = count_events(conjunction(function, is_away), whoscored_match)

    return (events_home_count, events_away_count)


# TODO: Внедрить регулярные выражения?
def bet_satisfy(condition, bet_or_pattern):
    for i in range(len(condition)):
        # FIXME: Исправлять такие ситуации на этапе парсинга
        if condition[i] != '*' and condition[i] != bet_or_pattern[i] and \
          not ((condition[i] is None and bet_or_pattern[i] == '') or (condition[i] == '' and bet_or_pattern[i] is None)):
            return False

    return True


def get_bet(condition, betarch_match):
    bet = get_first(lambda bet: bet_satisfy(condition, bet), betarch_match['bets'])
    if bet is None or bet[5] is None:
        return None

    return bet


def get_bets(condition, betarch_match):
    bets = [ bet for bet in betarch_match['bets'] if bet[5] is not None and bet_satisfy(condition, bet) ]
    return bets


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
    roi = bets_successful['bet_value'].sum() / bets_count - 1
    profit = bets_successful['bet_value'].sum() - bets_count

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
