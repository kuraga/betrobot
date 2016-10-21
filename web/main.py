import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./web')

import bottle
import pymongo
import bson
import datetime
from sport_util import bet_to_string


def print_bet(bet, show_panel=False):
    body = ''
    body += '<tr>'

    body += '<td>' + bet['date'].strftime('%Y-%m-%d') + '</td>'
    body += '<td>' + str(bet['tournament']) + '</td>'
    body += '<td>' + str(bet['home']) + '</td>'
    body += '<td>' + str(bet['away']) + '</td>'
    body += '<td>' + bet_to_string(bet['bet'], match_special_word=bet['match_special_word']) + '</td>'
    body += '<td>' + str(bet['bet_value']) + '</td>'

    body += '<td>'
    if show_panel:
        if not bet.get('approved', False):
            body += ' <a href="/approve/' + str(bet['_id']) + '">Поставлено</a>'
        else:
            if bet.get('result', None) is None:
                body += ' <a href="/green/' + str(bet['_id']) + '">Выиграла</a>'
                body += ' <a href="/red/' + str(bet['_id']) + '">Проиграла</a>'
            elif bet.get('result', None) is True:
                body += ' (выиграла)'
            elif bet.get('result', None) is False:
                body += ' (проиграла)'
    body += '</td>'

    body += '</tr>'

    return body


def print_bets(bets, show_panel=False):
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
    body += '<th>&nbsp;</th>'
    body += '</tr>'
    body += '</thead>'

    body += '<tbody>'
    for bet in bets:
        body += print_bet(bet, show_panel=show_panel)
    body += '</tbody>'

    body += '</table>'

    return body


client = pymongo.MongoClient()
db = client['betrobot']
bets = db['bets']
proposed = db['proposed']


app = bottle.Bottle()


@app.route('/')
def index():
    current_date = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    order = [ ['date', 1], ['tournament', 1 ], ['home', 1], ['away', 1], ['bet', 1] ]

    bets_fresh = proposed.find({ 'date': { '$gte': current_date }, 'approved': { '$ne': True } }).sort(order)
    bets_approved = proposed.find({ 'date': { '$gte': current_date }, 'approved': True }).sort(order)
    bets_expired = proposed.find({ 'date': { '$lt': current_date } }).sort(order)

    body = ''

    body += '<p>Всего ставок обработано при последнем проходе: %d</p>' % (bets.count(),)

    body += '<h2>Для проставления</h2>'
    body += print_bets(bets_fresh, show_panel=True)

    body += '<h2>Поставленные</h2>'
    body += print_bets(bets_approved, show_panel=True)

    body += '<h2>Просроченные</h2>'
    body += print_bets(bets_expired, show_panel=True)

    return body


@app.route('/approve/<_id>')
def approve(_id):
    proposed.update_one({ '_id': bson.objectid.ObjectId(_id) }, { '$set': { 'approved': True }})

    bottle.redirect('/')


@app.route('/green/<_id>')
def approve(_id):
    proposed.update_one({ '_id': bson.objectid.ObjectId(_id) }, { '$set': { 'result': True }})

    bottle.redirect('/')


@app.route('/red/<_id>')
def approve(_id):
    proposed.update_one({ '_id': bson.objectid.ObjectId(_id) }, { '$set': { 'result': False }})

    bottle.redirect('/')


bottle.run(app, host='0.0.0.0', port=8080)
