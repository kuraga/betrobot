#!/usr/bin/env python3


import bottle
import bson
import datetime
import re
import numpy as np
import pandas as pd
from betrobot.util.database_util import db
from betrobot.util.common_util import conjunct, eve_datetime, get_value
from betrobot.betting.sport_util import count_events_of_teams_by_match_uuid, count_events_of_players_by_match_uuid, is_corner, is_first_period, is_second_period, players_data
from betrobot.grabbing.intelbet.matching_names import intelbet_player_names_df, intelbet_player_names_match


# TODO: Разделить файл на части


_statistics_cache = {}


def _get_match_title(match_header):
    return match_header['date'].strftime('%Y-%m-%d') + ' - ' + match_header['home'] + ' vs ' + match_header['away']


def _get_match_headers(match_date):
    match_date_str = match_date.strftime('%Y-%m-%d')

    if match_date_str not in _statistics_cache:
        match_headers_collection = db['match_headers']
        sample = match_headers_collection.find({ 'date': { '$lte': eve_datetime(match_date) } })

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
        _statistics_cache[match_date_str] = pd.DataFrame(data, columns=['uuid', 'region_id', 'tournament_id', 'date', 'home', 'away']).set_index('uuid', drop=False)
        _statistics_cache[match_date_str].sort_values('date', ascending=False, inplace=True)

    return _statistics_cache[match_date_str].copy()


def _print_teams_statistic(match_header, is_home):
    team = match_header['home'] if is_home else match_header['away']

    statistic = _get_match_headers(match_header['date'])
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

    statistic = _get_match_headers(match_header['date'])
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
    content += '<tr><td>(%u игроков)</td></tr>' % (len(player_names),)
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


def _print_prediction(prediction_uuid):
    prediction_infos_collection = db['prediction_infos']
    proposed_collection = db['proposed']

    content = ''

    prediction_info = prediction_infos_collection.find_one({ 'uuid': prediction_uuid })

    content += '<tr>'
    content += '<td colspan="7">'
    content += '<pre>'
    # TODO: Либо экранировать, либо превратить в HTML
    content += prediction_info['info']
    content += '</pre>'
    content += '</td>'
    content += '</tr>'

    bets = proposed_collection.find({ 'data.prediction_uuid': prediction_uuid })
    content += _print_bets(bets)

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
    prediction_infos_collection = db['prediction_infos']

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


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--host', default='0.0.0.0')
    argument_parser.add_argument('--port', default=12345)
    args = argument_parser.parse_args()

    bottle.run(app, server='paste', host=args.host, port=args.port)
