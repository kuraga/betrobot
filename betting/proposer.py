import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')

import pickle
from common_util import list_wrap
from sport_util import get_bet
from betting_session import BettingSession


class Proposer(object):

    @classmethod
    def load(cls, file_path):
        with open(file_path, 'rb') as f_in:
            return pickle.load(f_in)


    def __init__(self, betting_sessions):
        if betting_sessions is None:
            betting_sessions = BettingSession('main')

        if isinstance(betting_sessions, dict):
            self.betting_sessions = betting_sessions
        elif isinstance(betting_sessions, list):
            self.betting_sessions = { betting_session.name: betting_session for betting_session in betting_sessions }
        else:
            self.betting_sessions = { betting_sessions.name: betting_sessions }


    def _propose(self, bet, ground_truth, betcity_match, session_key='main', treshold=None):
        if bet is not None and (treshold is None or bet[5] >= treshold):
            self.betting_sessions[session_key].make_bet(betcity_match, bet, ground_truth)


    def save(self, file_path):
        with open(file_path, 'wb') as f_out:
            pickle.dump(self, f_out)


    def flush_bets(self, collection, session_keys=None):
        if session_key is None:
            session_keys = list(betting_sessions.keys())
        else:
            session_keys = list_wrap(session_keys)

        for session_key in session_keys:
            self._flush_bets(self, collection, session_key)


    def _flush_bets(self, collection, session_key):
        betting_session = self.betting_sessions[session_key]
        bets = betting_session.bets

        for (i, bet) in bets.iterrows():
            bet1 = bet.to_dict()
            bet1['date'] = datetime.datetime.strptime(bet['date'], '%Y-%m-%d')
            del bet1['match_uuid']

            bet2 = bet.to_dict()
            bet2['date'] = datetime.datetime.strptime(bet['date'], '%Y-%m-%d')

            collection.update_one(bet1, { '$set': bet2 }, upsert=True)


    def to_string(self):
        res = ''

        for betting_session in self.betting_sessions.values():
            res += betting_session.to_string() + '\n'

        print(res)
