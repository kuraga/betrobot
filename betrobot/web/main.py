import bottle
import pymongo
import bson
import datetime
import numpy as np
from betrobot.util.sport_util import bet_to_string


def print_bet(bet_data, show_panel=False):
    body = ''
    body += '<tr>'

    if bet_data.get('express', False):
        body += '<td>' + bet_data['date'].strftime('%Y-%m-%d') + '</td>'
        body += '<td>' + '[ %s ] & [ %s ]' % (bet_data['tournament'], bet_data['tournament_2']) + '</td>'
        body += '<td>' + bet_data['home'] + '</td>'
        body += '<td>' + bet_data['away'] + '</td>'
        body += '<td>' + '[ %s ] & [ %s ]' % (bet_to_string(bet_data['bet_pattern'], match_special_word=bet_data['match_special_word']), bet_to_string(bet_data['bet_2'], match_special_word=bet_data['match_special_word_2'])) + '</td>'
        body += '<td>' + str(np.round(bet_data['bet_value'] * bet_data['bet_value_2'], 2)) + '</td>'
        body += '<td>' + str(bet_data.get('data', None)) + '</td>'
    else:
        body += '<td>' + bet_data['date'].strftime('%Y-%m-%d') + '</td>'
        body += '<td>' + bet_data['tournament'] + '</td>'
        body += '<td>' + bet_data['home'] + '</td>'
        body += '<td>' + bet_data['away'] + '</td>'
        body += '<td>' + bet_to_string(bet_data['bet_pattern'], match_special_word=bet_data['match_special_word']) + '</td>'
        body += '<td>' + str(np.round(bet_data['bet_value'], 2)) + '</td>'
        body += '<td>' + str(bet_data.get('data', None)) + '</td>'

    body += '<td>'
    if show_panel:
        if not bet_data.get('approved', False):
            body += ' <a href="/approve/' + str(bet_data['_id']) + '">Поставлено</a>'
        if bet_data.get('ground_truth', None) is None:
            body += ' <a href="/green/' + str(bet_data['_id']) + '">Выиграла</a>'
            body += ' <a href="/red/' + str(bet_data['_id']) + '">Проиграла</a>'
        elif bet_data.get('ground_truth', None) is True:
            body += ' (выиграла)'
        elif bet_data.get('ground_truth', None) is False:
            body += ' (проиграла)'
    body += '</td>'

    body += '</tr>'

    return body


def print_bets(bet_datas, show_panel=False):
    body = ''
    body += '<table border="1" cellspacing="0" cellpadding="4">'

    body += '<thead><tr>'
    body += '<tr>'
    body += '<th>Дата</th>'
    body += '<th>Турнир</th>'
    body += '<th>Гости</th>'
    body += '<th>Хозяева</th>'
    body += '<th>Название ставки</th>'
    body += '<th>Значение ставки</th>'
    body += '<th>Доп. информация</th>'
    body += '<th>&nbsp;</th>'
    body += '</tr>'
    body += '</thead>'

    body += '<tbody>'
    for bet_data in bet_datas:
        body += print_bet(bet_data, show_panel=show_panel)
    body += '</tbody>'

    body += '</table>'

    return body


client = pymongo.MongoClient()
db = client['betrobot']
proposed_collection = db['proposed']


app = bottle.Bottle()


@app.route('/')
def index():
    current_date = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    order = [ ['date', 1], ['tournament', 1 ], ['home', 1], ['away', 1], ['bet_pattern', 1] ]

    bets_fresh = proposed_collection.find({ 'date': { '$gte': current_date }, 'approved': { '$ne': True } }).sort(order)
    bets_approved = proposed_collection.find({ 'date': { '$gte': current_date }, 'approved': True }).sort(order)
    bets_expired = proposed_collection.find({ 'date': { '$lt': current_date } }).sort(order)

    body = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"></head><body>"""

    body += '<h2>Для проставления</h2>'
    body += print_bets(bets_fresh, show_panel=True)

    body += '<h2>Поставленные</h2>'
    body += print_bets(bets_approved, show_panel=True)

    body += '<h2>Просроченные</h2>'
    body += print_bets(bets_expired, show_panel=True)

    body += """</body></html>"""

    return body


@app.route('/approve/<_id>')
def approve(_id):
    proposed_collection.update_one({ '_id': bson.objectid.ObjectId(_id) }, { '$set': { 'approved': True }})

    bottle.redirect('/')


@app.route('/green/<_id>')
def approve(_id):
    proposed_collection.update_one({ '_id': bson.objectid.ObjectId(_id) }, { '$set': { 'ground_truth': True }})

    bottle.redirect('/')


@app.route('/red/<_id>')
def approve(_id):
    proposed_collection.update_one({ '_id': bson.objectid.ObjectId(_id) }, { '$set': { 'ground_truth': False }})

    bottle.redirect('/')


bottle.run(app, host='0.0.0.0', port=8080)
