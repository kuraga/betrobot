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

        if type(betting_sessions) is dict:
          self.betting_sessions = betting_sessions
        elif type(betting_sessions) is list:
          self.betting_sessions = { betting_session.name: betting_session for betting_session in betting_sessions }
        else:
          self.betting_sessions = { betting_sessions.name: betting_sessions }

    def _propose(self, bet, ground_truth, betcity_match, session_key='main', treshold=None):
        if bet is not None and (treshold is None or bet[5] >= treshold):
            self.betting_sessions[session_key].make_bet(betcity_match, bet, ground_truth)


    def _propose_express(self, bet1, ground_truth1, bet2, ground_truth2, betcity_match, session_key='main', treshold=None):
        if bet1 is not None and bet2 is not None and (treshold is None or bet1[5]*bet2[5] >= treshold):
            self.betting_sessions[session_key].make_express_bet(betcity_match, bet1, ground_truth1, bet2, ground_truth2)


    def save(self, file_path):
        with open(file_path, 'wb') as f_out:
            pickle.dump(self, f_out)


    def to_string(self):
        res = ''

        for betting_session in self.betting_sessions.values():
            res += betting_session.to_string() + '\n'

        print(res)
