#!/usr/bin/env python3


import bottle
import bson
import datetime
import numpy as np
import pandas as pd
from betrobot.util.database_util import db
from betrobot.util.common_util import conjunct
from betrobot.betting.sport_util import count_events_of_teams_by_match_uuid, count_events_of_players_by_match_uuid, is_corner, is_first_period, is_second_period


_statistic_cache = None


def _get_match_title(match_header):
    return match_header['date'].strftime('%Y-%m-%d') + ' - ' + match_header['home'] + ' vs ' + match_header['away']


def _get_statistic():
    global _statistic_cache

    if _statistic_cache is None:
        match_headers_collection = db['match_headers']
        sample = match_headers_collection.find()

        data = []
        for match_header in sample:
            data.append({
                'uuid': match_header['uuid'],
                'region_id': match_header['regionId'],
                'tournament_id': match_header['tournamentId'],
                'date': match_header['date'],
                'home': match_header['home'],
                'away': match_header['away']
            })
        _statistic_cache = pd.DataFrame(data, columns=['uuid', 'region_id', 'tournament_id', 'date', 'home', 'away']).set_index('uuid', drop=False)
        _statistic_cache.sort_values('date', ascending=False, inplace=True)

    return _statistic_cache


def _print_teams_statistic(match_header, is_home):
    team = match_header['home'] if is_home else match_header['away']

    statistic = _get_statistic()
    statistic = statistic[ (statistic['home'] == team) | (statistic['away'] == team) ]
    statistic = statistic[:10]

    content = ''
    content += '<table>'
    content += '<thead>'
    content += '<tr>'
    content += '<th>Дата</th>'
    content += '<th>Хозяева</th>'
    content += '<th>Гости</th>'
    content += '<th>Угловые (матч)</th>'
    content += '<th>Угловые (1-й тайм)</th>'
    content += '<th>Угловые (2-й тайм)</th>'
    content += '</tr>'
    content += '</thead>'
    content += '<tbody>'
    for (i, row) in statistic.iterrows():
        try:
            (home_corners_count, away_corners_count) = count_events_of_teams_by_match_uuid(is_corner, row['uuid'])
            (first_period_home_corners_count, first_period_away_corners_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_first_period), row['uuid'])
            (second_period_home_corners_count, second_period_away_corners_count) = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_second_period), row['uuid'])
        except TypeError:
            continue

        if (is_home and row['home'] == team) or (not is_home and row['away'] == team):
            content += '<tr class="active">'
        else:
            content += '<tr>'
        content += '<td>' + row['date'].strftime('%Y-%m-%d') + '</td>'
        content += '<td>' + row['home'] + '</td>'
        content += '<td>' + row['away'] + '</td>'
        content += '<td>%u : %u</td>' % (home_corners_count, away_corners_count)
        content += '<td>%u : %u</td>' % (first_period_home_corners_count, first_period_away_corners_count)
        content += '<td>%u : %u</td>' % (second_period_home_corners_count, second_period_away_corners_count)
        content += '</tr>'
    content += '</tbody>'
    content += '</table>'

    return content


def _print_players_statistic(match_header, is_home):
    team = match_header['home'] if is_home else match_header['away']
    k = 'homePlayers' if is_home else 'awayPlayers'

    additional_info_collection = db['additional_info']
    additional_info = additional_info_collection.find_one({ 'match_uuid': match_header['uuid'] })
    if k not in additional_info:
        return ''

    player_names = [ player['playerName'] for player in additional_info[k] if player['isFirstEleven'] ]
    data = { player_name: {} for player_name in player_names }
    first_period_data = { player_name: {} for player_name in player_names }
    second_period_data = { player_name: {} for player_name in player_names }

    statistic = _get_statistic()
    statistic = statistic[ (statistic['home'] == team) | (statistic['away'] == team) ]
    statistic = statistic[:10]

    for (i, row) in statistic.iterrows():
        player_counts = count_events_of_players_by_match_uuid(is_corner, row['uuid'])
        if player_counts is None:
            continue
        first_period_player_counts = count_events_of_players_by_match_uuid(conjunct(is_corner, is_first_period), row['uuid'])
        second_period_player_counts = count_events_of_players_by_match_uuid(conjunct(is_corner, is_second_period), row['uuid'])

        for player_name in player_counts:
            if player_name in data:
                data[player_name][row['uuid']] = player_counts[player_name]
                first_period_data[player_name][row['uuid']] = first_period_player_counts[player_name]
                second_period_data[player_name][row['uuid']] = second_period_player_counts[player_name]

    content = ''

    content += '<table>'
    content += '<thead>'
    content += '<tr>'
    content += '<th>Имя</th>'
    for (i, row) in statistic.iterrows():
        content += '<th>' + _get_match_title(row) + '</th>'
    content += '</tr>'
    content += '</thead>'
    content += '<tbody>'
    for player_name in player_names:
        content += '<tr>'
        content += '<td>' + player_name + '</td>'
        for (i, row) in statistic.iterrows():
            if row['uuid'] in data[player_name]:
                content += '<td>%u (%u + %u)</td>' % (data[player_name][row['uuid']], first_period_data[player_name][row['uuid']], second_period_data[player_name][row['uuid']])
            else:
                content += '<td></td>'
        content += '</tr>'
    content += '</tbody>'
    content += '</table>'

    return content

def _print_bet(bet):
    match_headers_collection = db['match_headers']
    match_header = match_headers_collection.find_one({ 'uuid': bet['match_uuid'] })

    content = ''
    content += '<tr>'

    content += '<td>' + match_header['date'].strftime('%Y-%m-%d') + '</td>'
    content += '<td>' + match_header['home'] + '</td>'
    content += '<td>' + match_header['away'] + '</td>'
    content += '<td>' + str(bet['pattern']) + '</td>'
    content += '<td>%.2f</td>' % (bet['value'],)
    content += '<td>' + bet['data'].get('provider_description', '') + '</td>'
    content += '<td>%.2f : %.2f</td>' % tuple(bet['data'].get('result_prediction', [-1, -1]))

    content += '</tr>'

    return content


def _print_bets(bets):
    content = ''
    content += '<table>'

    content += '<thead>'
    content += '<tr>'
    content += '<th>Дата</th>'
    content += '<th>Хозяева</th>'
    content += '<th>Гости</th>'
    content += '<th>Название ставки</th>'
    content += '<th>Значение ставки</th>'
    content += '<th>Алгоритм</th>'
    content += '<th>Предсказание</th>'
    content += '</tr>'
    content += '</thead>'

    content += '<tbody>'
    for bet in bets:
        content += _print_bet(bet)
    content += '</tbody>'

    content += '</table>'

    return content


app = bottle.Bottle()


@app.route('/')
@bottle.view('main')
def index():
    match_headers_collection = db['match_headers']

    today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    match_uuids = match_headers_collection.distinct('uuid', { 'date': today })
    match_headers = match_headers_collection.find({ 'uuid': { '$in': match_uuids } })

    content = ''
    content += '<table>'
    content += '<tbody>'
    content += '<h2>Матчи сегодня</h2>'

    for match_header in match_headers:
        content += '<tr>'
        content += '<td>' + match_header['date'].strftime('%Y-%m-%d') + '</td>'
        content += '<td><a href="/matches/' + match_header['uuid'] + '">' + match_header['uuid'] + '</a></td>'
        content += '<td><a href="/matches/' + match_header['uuid'] + '">' + match_header['home'] + '</a></td>'
        content += '<td><a href="/matches/' + match_header['uuid'] + '">' + match_header['away'] + '</a></td>'
        content += '</tr>'

    content += '</tbody>'
    content += '</table>'

    return { 'content': content }


@app.route('/matches/<match_uuid>')
@bottle.view('main')
def match(match_uuid):
    proposed_collection = db['proposed']
    match_headers_collection = db['match_headers']

    match_header = match_headers_collection.find_one({ 'uuid': match_uuid })

    content = ''
    content += '<h2>Матч ' + _get_match_title(match_header) + '</h2>'

    content += '<h3>Хозяева: ' + match_header['home'] + '</h3>'
    content += _print_teams_statistic(match_header, True)
    content += _print_players_statistic(match_header, True)

    content += '<h3>Гости: ' + match_header['away'] + '</h3>'
    content += _print_teams_statistic(match_header, False)
    content += _print_players_statistic(match_header, False)

    content += '<h3>Ставки на матч</h3>'
    bets = proposed_collection.find({ 'match_uuid': match_uuid })
    content += _print_bets(bets)

    return { 'content': content }


bottle.run(app, host='0.0.0.0',
    port=12345,
    server='paste')
