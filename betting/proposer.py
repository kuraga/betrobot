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


    def flush(self, collection, session_keys=None):
        if session_keys is None:
            session_keys = list(self.betting_sessions.keys())
        else:
            session_keys = list_wrap(session_keys)

        for session_key in session_keys:
            self.betting_sessions[session_key].flush_bets(collection)


    def to_string(self):
        res = ''

        for betting_session in self.betting_sessions.values():
            res += betting_session.to_string() + '\n'

        return res
