#!/usr/bin/env python3


import bottle
import bson
import datetime
import numpy as np
from betrobot.util.database_util import db


def _print_bet(bet):
    body = ''
    body += '<tr>'

    match_headers_collection = db['match_headers']
    match_header = match_headers_collection.find_one({ 'uuid': bet['match_uuid'] })

    body += '<td>%s</td>' % (match_header['date'],)
    body += '<td>%s</td>' % (match_header['home'],)
    body += '<td>%s</td>' % (match_header['away'],)
    body += '<td>%s</td>' % (str(bet['pattern']),)
    body += '<td>%.2f</td>' % (bet['value'],)
    body += '<td>%s</td>' % (bet['data'].get('provider_description', ''),)
    body += '<td>%.2f : %.2f</td>' % tuple(bet['data'].get('result_prediction', [-1, -1]))

    body += '</tr>'

    return body


def print_bets(bets):
    body = ''
    body += '<table border="1" cellspacing="0" cellpadding="4">'

    body += '<thead><tr>'
    body += '<tr>'
    body += '<th>Дата</th>'
    body += '<th>Хозяева</th>'
    body += '<th>Гости</th>'
    body += '<th>Название ставки</th>'
    body += '<th>Значение ставки</th>'
    body += '<th>Алгоритм</th>'
    body += '<th>Предсказание</th>'
    body += '</tr>'
    body += '</thead>'

    body += '<tbody>'
    for bet in bets:
        body += _print_bet(bet)
    body += '</tbody>'

    body += '</table>'

    return body


app = bottle.Bottle()


@app.route('/')
def index():
    current_date = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    order = [ ['date', 1], ['tournament', 1 ], ['home', 1], ['away', 1], ['bet_pattern', 1] ]

    proposed_collection = db['proposed']
    bets = proposed_collection.find({}).sort(order)

    body = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"></head><body>"""

    body += print_bets(bets)

    body += """</body></html>"""

    return body

bottle.run(app, host='0.0.0.0', port=8080)
