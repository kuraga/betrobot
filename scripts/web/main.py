#!/usr/bin/env python3


import bottle
import bson
import datetime
import re
import os
import json
import argparse
import numpy as np
import pandas as pd
from betrobot.util.database_util import db
from betrobot.util.common_util import conjunct, eve_datetime, get_value
from betrobot.betting.sport_util import get_match_headers, get_tournament_season_substatistic, count_events_of_teams_by_match_uuid, count_events_of_players_by_match_uuid, is_corner, is_first_period, is_second_period, tournaments_data, players_data
from betrobot.grabbing.intelbet.matching_names import intelbet_player_names_df, intelbet_player_names_match


# TODO: Разделить файл на части


def _get_match_title(match_header):
    return match_header['date'].strftime('%Y-%m-%d') + ' - ' + match_header['home'] + ' vs ' + match_header['away']


def _print_teams_statistic(match_header, is_home):
    content = ''

    team = match_header['home'] if is_home else match_header['away']

    whole_match_headers = get_match_headers()
    attainable_match_headers = whole_match_headers[ whole_match_headers['date'] <= eve_datetime(match_header['date']) ]
    attainable_team_match_headers = attainable_match_headers[ (attainable_match_headers['home'] == team) | (attainable_match_headers['away'] == team) ]
    last_match_headers = attainable_team_match_headers[:10]

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

    for (match_uuid, match_header) in last_match_headers.iterrows():
        corners_counts = count_events_of_teams_by_match_uuid(is_corner, match_uuid)
        if corners_counts is None:
            continue
        first_period_corners_counts = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_first_period), match_uuid)
        second_period_corners_counts = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_second_period), match_uuid)

        if (is_home and match_header['home'] == team) or (not is_home and match_header['away'] == team):
            content += '<tr class="active">'
        else:
            content += '<tr>'
        content += '<td>' + match_header['date'].strftime('%Y-%m-%d') + '</td>'
        content += '<td>' + match_header['home'] + '</td>'
        content += '<td>' + match_header['away'] + '</td>'
        content += '<td>%u : %u</td>' % corners_counts
        content += '<td>%u : %u</td>' % first_period_corners_counts
        content += '<td>%u : %u</td>' % second_period_corners_counts
        content += '</tr>'

    content += '</tbody>'
    content += '</table>'

    return content


def _print_unmatched_player_names(match_header, is_home):
    content = ''

    if is_home:
        intelbet_player_names = list(intelbet_player_names_df.loc[ intelbet_player_names_df['whoscoredName'] == match_header['home'], 'intelbetPlayerName' ].values)
        unmatched_whoscored_names = list(players_data.loc[ (players_data['whoscoredName'] == match_header['home']) & (players_data['intelbetPlayerName'].isnull()), 'whoscoredPlayerName' ].values)
        team_players_data = players_data[ players_data['whoscoredName'] == match_header['home'] ]
    else:
        intelbet_player_names = list(intelbet_player_names_df.loc[ intelbet_player_names_df['whoscoredName'] == match_header['away'], 'intelbetPlayerName' ].values)
        unmatched_whoscored_names = list(players_data.loc[ (players_data['whoscoredName'] == match_header['away']) & (players_data['intelbetPlayerName'].isnull()), 'whoscoredPlayerName' ].values)
        team_players_data = players_data[ players_data['whoscoredName'] == match_header['away'] ]
    if len(intelbet_player_names) > 0:
        content += '<form action="/match_player_names" method="post">'

        for intelbet_player_name in sorted(intelbet_player_names):
            whoscored_player_name = get_value(team_players_data, 'intelbetPlayerName', intelbet_player_name, 'whoscoredPlayerName')
            if whoscored_player_name is not None and whoscored_player_name != '':
                continue

            content += intelbet_player_name
            content += ' '

            content += '<select name="player_%s">' % (intelbet_player_name,)
            content += '<option value="" selected="selected"></option>'
            for unmatched_whoscored_name in unmatched_whoscored_names:
                escaped_unmatched_whoscored_name = re.sub('"', '\\"', unmatched_whoscored_name)
                content += '<option value="%s">%s</option>' % (escaped_unmatched_whoscored_name, unmatched_whoscored_name)
            content += '</select>'

            content += '<br>'

        content += '<input type="submit" value="Задать соответствия">'
        content += '</form>'

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

    whole_match_headers = get_match_headers()
    attainable_match_headers = whole_match_headers[ whole_match_headers['date'] <= eve_datetime(match_header['date']) ]
    attainable_team_match_headers = attainable_match_headers[ (attainable_match_headers['home'] == team) | (attainable_match_headers['away'] == team) ]
    last_match_headers = attainable_team_match_headers[:10]

    for (match_uuid_, match_header_) in last_match_headers.iterrows():
        player_counts = count_events_of_players_by_match_uuid(is_corner, match_uuid_)
        if player_counts is None:
            continue
        first_period_player_counts = count_events_of_players_by_match_uuid(conjunct(is_corner, is_first_period), match_uuid_)
        second_period_player_counts = count_events_of_players_by_match_uuid(conjunct(is_corner, is_second_period), match_uuid_)

        for player_name in player_counts:
            if player_name in data:
                data[player_name][match_uuid_] = player_counts[player_name]
                first_period_data[player_name][match_uuid_] = first_period_player_counts[player_name]
                second_period_data[player_name][match_uuid_] = second_period_player_counts[player_name]

    content = ''

    content += '<table>'
    content += '<tbody>'

    content += '<tr>'
    content += '<th></th>'
    for (match_uuid, match_header) in last_match_headers.iterrows():
        content += '<th>' + _get_match_title(match_header) + '</th>'
    content += '</tr>'

    for player_name in player_names:
        content += '<tr>'
        content += '<th>' + player_name + '</th>'
        for (match_uuid, match_header) in last_match_headers.iterrows():
            if match_uuid in data[player_name]:
                content += '<td>%u (%u / %u)</td>' % (data[player_name][match_uuid], first_period_data[player_name][match_uuid], second_period_data[player_name][match_uuid])
            else:
                content += '<td></td>'
        content += '</tr>'

    content += '<tr><td>(%u игроков)</td></tr>' % (len(player_names),)

    content += '</tbody>'
    content += '</table>'

    content += _print_unmatched_player_names(match_header, is_home)

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

    for bet in bets:
        content += _print_bet(bet)

    return content


def _print_match_bets(match_uuid):
    content = ''

    prediction_infos_collection = db['prediction_infos']

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

    prediction_infos = prediction_infos_collection.find({ 'match_uuid': match_uuid })
    for prediction_info in prediction_infos:
        content += _print_prediction(prediction_info['uuid'])

    content += '</tbody>'

    content += '</table>'

    return content


def _print_prediction(prediction_uuid):
    prediction_infos_collection = db['prediction_infos']
    proposed_collection = db['proposed']

    content = ''

    bets = proposed_collection.find({ 'data.prediction_uuid': prediction_uuid })

    prediction_info = prediction_infos_collection.find_one({ 'uuid': prediction_uuid })

    content += '<tr>'
    content += '<td colspan="7">'
    content += '<pre>'
    # TODO: Либо экранировать, либо превратить в HTML
    content += prediction_info['info']
    content += '</pre>'
    content += '</td>'
    content += '</tr>'

    content += _print_bets(bets)

    return content


def _print_tournament_data(match_date, tournament_id):
    content = ''

    whole_match_headers = get_match_headers()
    attainable_match_headers = whole_match_headers[ whole_match_headers['date'] <= eve_datetime(match_date) ]

    first_year = match_date.year if match_date.month >= 6 else match_date.year - 1
    tournament_season_match_headers = get_tournament_season_substatistic(attainable_match_headers, tournament_id, first_year)
    sorted_tournament_season_match_headers = tournament_season_match_headers.sort_values('date', ascending=True)

    home_teams = frozenset(tournament_season_match_headers['home'].values)
    away_teams = frozenset(tournament_season_match_headers['away'].values)
    teams = home_teams | away_teams

    data = { home: { away: None for away in teams } for home in teams }
    for (match_uuid, match_header) in sorted_tournament_season_match_headers.iterrows():
        events_counts = count_events_of_teams_by_match_uuid(is_corner, match_uuid)
        if events_counts is None:
            continue
        first_period_events_counts = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_first_period), match_uuid)
        second_period_events_counts = count_events_of_teams_by_match_uuid(conjunct(is_corner, is_second_period), match_uuid)

        data[ match_header['home'] ][ match_header['away'] ] = (events_counts[0], events_counts[1], first_period_events_counts[0], first_period_events_counts[1], second_period_events_counts[0], second_period_events_counts[1])

    content += '<table>'
    content += '<tbody>'

    content += '<tr>'
    content += '<th></th>'
    for team in sorted(teams):
        content += '<th>' + team + '</th>'
    content += '</tr>'

    for home in sorted(teams):
        content += '<tr>'
        content += '<th>' + home + '</th>'
        for away in sorted(teams):
            match_data = data[home][away]
            if match_data is not None:
                content += '<td>%u : %u (%u : %u / %u : %u)</td>' % match_data
            else:
                content += '<td></td>'
        content += '</tr>'

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

    content += '<h3>Статистика чемпионата</h3>'
    content += _print_tournament_data(match_header['date'], match_header['tournamentId'])

    content += '<h3>Ставки на матч</h3>'
    content += _print_match_bets(match_uuid)

    return { 'content': content }


@app.route('/match_player_names', method='POST')
@bottle.view('main')
def match_player_names_action():
    content = ''

    content += '<p>Были заданы следующие соответствия:</p>'
    content += '<ul>'
    for k, v in bottle.request.forms.decode().items():
        if len(v) == 0:
            continue

        m = re.search(r'^player_(.+)$', k)
        if m is None:
            continue

        intelbet_player_name = m.group(1)
        whoscored_player_name = v

        intelbet_player_names_match(intelbet_player_name, whoscored_player_name)

        content += '<li>' + intelbet_player_name + ' &mdash; ' + whoscored_player_name + '</li>'
    content += '</ul>'
    content += '<p>В скором времени составы команд, прогнозы и предложенные ставки обновятся.</p>'

    return { 'content': content }


@app.route('/update_headers', method='GET')
@bottle.view('main')
def update_headers():
    content = ''

    content += '<form action="/update_headers", method="post">'
    content += 'Домен: <input type="text" name="domain">'
    content += '<br>'
    content += 'Заголовки: <textarea name="headers" rows="10" cols="100"></textarea>'
    content += '<br>'
    content += '<input type="submit" value="Обновить заголовки!">'
    content += '</form>'

    return { 'content': content }


@app.route('/update_headers', method='POST')
@bottle.view('main')
def update_headers_action():
    content = ''

    domain = bottle.request.forms.getunicode('domain')
    headers_text = bottle.request.forms.getunicode('headers')

    headers = {}
    for header_line in headers_text.splitlines():
        (header_name, header_value) = re.split(': ?', header_line, maxsplit=1)
        header_name = header_name.lower()
        headers[header_name] = header_value

    headers_file_path = os.path.join('tmp', 'update', 'headers', '%s.json' % (domain,))
    with open(headers_file_path, 'wt', encoding='utf-8') as f_out:
        json.dump(headers, f_out)

    content += '<p>Заголовки для домена ' + domain + ' записаны.</p>'

    return { 'content': content }


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--host', default='0.0.0.0')
    argument_parser.add_argument('--port', type=int, default=12345)
    args = argument_parser.parse_args()

    bottle.run(app, server='paste', host=args.host, port=args.port)
