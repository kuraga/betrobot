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

    def _propose(self, betcity_match, bet, ground_truth, session_key='main', treshold=None):
        if bet is not None and (treshold is None or bet[5] >= treshold):
            self.betting_sessions[session_key].make_bet(betcity_match, bet, ground_truth)


    def _propose_pattern(self, bet_pattern, betcity_match, ground_truth, session_key='main', treshold=None):
        bet = get_bet(bet_pattern, betcity_match)
        self._propose(betcity_match, bet, ground_truth, session_key=session_key, treshold=treshold)


    def _propose_express(self, betcity_match, bet1, ground_truth1, bet2, ground_truth2, session_key='main', treshold=None):
        if bet1 is not None and bet2 is not None and (treshold is None or bet1[5]*bet2[5] >= treshold):
            self.betting_sessions[session_key].make_express_bet(betcity_match, bet1, ground_truth1, bet2, ground_truth2)


    def _propose_express_pattern(self, bet_pattern1, betcity_match1, ground_truth1, bet_pattern2, betcity_match2, ground_truth2, session_key='main', treshold=None):
        bet1 = get_bet(bet_pattern1, betcity_match1)
        bet2 = get_bet(bet_pattern2, betcity_match2)
        self._propose_express(betcity_match1, bet1, ground_truth1, bet2, ground_truth2, session_key=session_key, treshold=treshold)


    def save(self, file_path):
        with open(file_path, 'wb') as f_out:
            pickle.dump(self, f_out)


    def to_string(self):
        res = ''

        for betting_session in self.betting_sessions.values():
            res += betting_session.to_string() + '\n'

        print(res)
